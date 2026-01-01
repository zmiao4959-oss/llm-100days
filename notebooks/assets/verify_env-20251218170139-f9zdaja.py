def verify_env():
    models = ['dotenv','requests','numpy','pandas', 'matplotlib', 'rich']
    for model in models:
        try:
            model = __import__(model)
        except ImportError:
            print('{}导入失败，{}'.format(model, ImportError))

        try:
            print("{}导入成功！\n版本号：{}".format(model.__name__,model.__version__))
        except :
            print("{}导入成功！".format(model.__name__))

if __name__ == '__main__':
    verify_env()