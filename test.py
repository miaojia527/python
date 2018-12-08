#!/usr/bin/python
#coding:utf8

print([i for i in 'Hello'])

def decorator_func_args(func):
    def handle_args(*args, **kwargs): #处理传入函数的参数
        print("begin")
        func(*args, **kwargs)   #函数调用
        print("end")
    return handle_args
 
 
@decorator_func_args
def foo2(a, b=2):
    print(a, b)
 
foo2(1)
