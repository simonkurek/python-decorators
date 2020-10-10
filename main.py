# define decorator
def logging(func):
    def before():
        print('Start func')
        func()

    def after():
        func()
        print('End func')

    return before,after

# use decorator

@logging.before
def my_function():
    print('Hello World!')

my_function()