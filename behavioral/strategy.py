#!/usr/bin/python
#coding:utf8
"""
策略

在大多数其他语言中，策略模式是通过创建一些基本的策略接口/抽象类和来实现的

使用一些具体的策略对其进行子类化(如http://en.wikipedia.org/wiki/Strategy_pattern所示)，

然而Python支持高阶函数，并且允许我们只有一个类并将函数注入其中

实例，如本例所示。

"""
import types
 
 
class StrategyExample:
    def __init__(self, func=None):
        self.name= 'Strategy Example 0'
        if func is not None:
            self.execute= types.MethodType(func,self)
 
    def execute(self):        
        print(self.name)  
 
def execute_replacement1(self):
    print(self.name+ ' from execute 1')  
 
def execute_replacement2(self):
    print(self.name+ ' from execute 2') 
 
if __name__ =='__main__':
    strat0= StrategyExample()    
 
    strat1= StrategyExample(execute_replacement1)
    strat1.name= 'Strategy Example 1'    
 
    strat2= StrategyExample(execute_replacement2)
    strat2.name= 'Strategy Example 2'
 
    strat0.execute()
    strat1.execute()    
    strat2.execute()
