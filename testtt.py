def a(*args):
    print(args)
    
# a({"1":2},a=2)
# *args指的是所有沒有指定名稱的參數，而**kwargs指的是指定名稱的參數


from functools import wraps

def decorate(f):
    print(f.__name__)
    def wrapper(*args,**kwargs):
        print(f'do something before calling function {f.__name__}')
        f(*args,**kwargs)
        print(f'do something after calling function {f.__name__}')
    return wrapper

@decorate
def hello(*args,**kwargs):
    print(args,kwargs)
    return 2


#上面的 return的wrapper最後會變成我們之後call的hello，所以其實後來傳入hello的參數，最後都會傳入wrapper
print(hello(1,2))
# decorate=decorate(hello)
# print(decorate())