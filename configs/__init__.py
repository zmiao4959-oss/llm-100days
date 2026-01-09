"""Configuration management for LLM Bootstrapping."""

import logging
import os
from pathlib import Path
from typing import Any, Dict, Optional

import yaml
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


class ConfigManager:
    """Manage application configuration from multiple sources."""

    def __init__(self, config_path: Optional[str] = None):
        """Initialize configuration manager.

        Args:
            config_path: Path to config file. If None, uses default location.
        """
        self.config_path = config_path or self._get_default_config_path()
        self.config: Dict[str, Any] = {}
        self.env_loaded = False

        # Load configuration
        self._load_env()
        self._load_yaml_config()
        self._apply_env_overrides()

        # Validate configuration
        self._validate_config()

    def _get_default_config_path(self) -> Path:
        """Get default configuration path."""
        # Try current directory first, then project root
        possible_paths = [
            Path("configs/config.yaml"),
            Path(__file__).parent.parent.parent / "configs" / "config.yaml",
            Path.cwd() / "configs" / "config.yaml",
        ]

        for path in possible_paths:
            if path.exists():
                logger.debug(f"Found config file at: {path}")
                return path

        # Return default path (will create if not exists)
        default_path = Path.cwd() / "configs" / "config.yaml"
        default_path.parent.mkdir(exist_ok=True)
        return default_path

    def _load_env(self) -> None:
        """Load environment variables from .env file."""
        # Try multiple .env file locations
        possible_env_files = [
            Path(".env"),
            Path(__file__).parent.parent.parent / ".env",
            Path.cwd() / ".env",
        ]

        for env_file in possible_env_files:
            if env_file.exists():
                load_dotenv(env_file)
                self.env_loaded = True
                logger.info(f"Loaded environment variables from: {env_file}")
                break

        if not self.env_loaded:
            logger.warning("No .env file found. Using default environment variables.")

    def _load_yaml_config(self) -> None:
        """Load YAML configuration file."""
        try:
            if self.config_path.exists():
                with open(self.config_path, "r", encoding="utf-8") as f:
                    self.config = yaml.safe_load(f) or {}
                logger.info(f"Loaded configuration from: {self.config_path}")
            else:
                self.config = self._get_default_config()
                self._save_default_config()
                logger.warning(
                    f"Config file not found. Created default at: {self.config_path}"
                )
        except yaml.YAMLError as e:
            logger.error(f"Error parsing YAML config: {e}")
            self.config = self._get_default_config()
        except Exception as e:
            logger.error(f"Error loading config file: {e}")
            self.config = self._get_default_config()

    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration."""
        return {
            "app": {
                "name": "LLM Bootstrapping Tool",
                "version": "0.1.0",
                "description": "A tool for bootstrapping LLM projects with CLI interface",
                "defaults": {
                    "greeting_name": "LLM Developer",
                    "greeting_times": 2,
                    "log_level": "INFO",
                    "max_times": 10,
                },
            },
            "logging": {
                "level": "INFO",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "date_format": "%Y-%m-%d %H:%M:%S",
                "file": {
                    "enabled": False,
                    "path": "logs/llm_bootstrap.log",
                    "max_size_mb": 10,
                    "backup_count": 5,
                },
                "console": {"enabled": True, "use_colors": True},
            },
            "greeting": {
                "templates": {
                    "default": "Hello, {name}!",
                    "formal": "Good day, {name}.",
                    "casual": "Hey {name}!",
                    "excited": "HELLO {name}!!!",
                },
                "behavior": {
                    "allow_empty_name": False,
                    "max_name_length": 50,
                    "min_times": 1,
                    "max_times": 10,
                },
            },
        }

    def _save_default_config(self) -> None:
        """Save default configuration to file."""
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, "w", encoding="utf-8") as f:
                yaml.dump(self.config, f, default_flow_style=False, sort_keys=False)
            logger.info(f"Saved default configuration to: {self.config_path}")
        except Exception as e:
            logger.error(f"Error saving default config: {e}")

    def _apply_env_overrides(self) -> None:
        """Override configuration with environment variables."""
        # Override log level
        env_log_level = os.getenv("LOG_LEVEL")
        if env_log_level and "logging" in self.config:
            self.config["logging"]["level"] = env_log_level
            logger.debug(f"Overridden log level from env: {env_log_level}")

        # Override default name
        env_default_name = os.getenv("DEFAULT_NAME")
        if (
            env_default_name
            and "app" in self.config
            and "defaults" in self.config["app"]
        ):
            self.config["app"]["defaults"]["greeting_name"] = env_default_name

        # Override default times
        env_default_times = os.getenv("DEFAULT_TIMES")
        if (
            env_default_times
            and "app" in self.config
            and "defaults" in self.config["app"]
        ):
            try:
                self.config["app"]["defaults"]["greeting_times"] = int(
                    env_default_times
                )
            except ValueError:
                logger.warning(f"Invalid DEFAULT_TIMES value: {env_default_times}")

        # Override greeting template
        env_template = os.getenv("GREETING_TEMPLATE")
        if (
            env_template
            and "greeting" in self.config
            and "templates" in self.config["greeting"]
        ):
            if env_template in self.config["greeting"]["templates"]:
                # Move the env template to be the default
                template = self.config["greeting"]["templates"][env_template]
                self.config["greeting"]["templates"]["default"] = template

    def _validate_config(self) -> None:
        """Validate configuration values."""
        try:
            # Validate logging level
            valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
            log_level = self.get("logging.level", "INFO")
            if log_level not in valid_log_levels:
                logger.warning(f"Invalid log level: {log_level}. Using INFO.")
                self.set("logging.level", "INFO")

            # Validate greeting times
            min_times = self.get("greeting.behavior.min_times", 1)
            max_times = self.get("greeting.behavior.max_times", 10)
            if min_times > max_times:
                logger.error(
                    f"min_times ({min_times}) > max_times ({max_times}). Swapping values."
                )
                self.set("greeting.behavior.min_times", max_times)
                self.set("greeting.behavior.max_times", min_times)

            logger.debug("Configuration validation completed")

        except Exception as e:
            logger.error(f"Configuration validation error: {e}")

    def get(self, key_path: str, default: Any = None) -> Any:
        """Get configuration value using dot notation.

        Args:
            key_path: Path to configuration key using dot notation (e.g., "app.name")
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        try:
            keys = key_path.split(".")
            value = self.config

            for key in keys:
                if isinstance(value, dict) and key in value:
                    value = value[key]
                else:
                    return default

            return value
        except (AttributeError, KeyError, TypeError):
            return default

    def set(self, key_path: str, value: Any) -> None:
        """Set configuration value using dot notation.

        Args:
            key_path: Path to configuration key using dot notation
            value: Value to set
        """
        keys = key_path.split(".")
        config = self.config

        for i, key in enumerate(keys[:-1]):
            if key not in config:
                config[key] = {}
            config = config[key]

        config[keys[-1]] = value
        logger.debug(f"Set config {key_path} = {value}")

    def save(self) -> None:
        """Save current configuration to file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                yaml.dump(self.config, f, default_flow_style=False, sort_keys=False)
            logger.info(f"Configuration saved to: {self.config_path}")
        except Exception as e:
            logger.error(f"Error saving configuration: {e}")

    def reload(self) -> None:
        """Reload configuration from file."""
        self._load_env()
        self._load_yaml_config()
        self._apply_env_overrides()
        self._validate_config()
        logger.info("Configuration reloaded")

    def get_all(self) -> Dict[str, Any]:
        """Get all configuration as dictionary."""
        return self.config.copy()


# Global configuration instance
_config_manager: Optional[ConfigManager] = None


def get_config_manager(config_path: Optional[str] = None) -> ConfigManager:
    """Get or create global configuration manager instance.

    Args:
        config_path: Path to config file

    Returns:
        ConfigManager instance
    """
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager(config_path)
    return _config_manager


def get_config(key_path: str, default: Any = None) -> Any:
    """Get configuration value from global config manager.

    Args:
        key_path: Path to configuration key using dot notation
        default: Default value if key not found

    Returns:
        Configuration value or default
    """
    return get_config_manager().get(key_path, default)
