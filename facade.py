#!/usr/bin/python
#coding:utf8

#
#by panda
#外观模式（Facade）
 
 
def printInfo(info):
    print unicode(info, 'utf-8').encode('gbk')
    
class Stock1():
    name = '股票1'
    def buy(self):
        printInfo('买 '+self.name)
    
    def sell(self):
        printInfo('卖 '+self.name)
        
class Stock2():
    name = '股票2'
    def buy(self):
        printInfo('买 '+self.name)
    
    def sell(self):
        printInfo('卖 '+self.name)
 
class NationDebt1():
    name = '国债1'
    def buy(self):
        printInfo('买 '+self.name)
    
    def sell(self):
        printInfo('卖 '+self.name)
 
class Realty1():
    name = '房地产1'
    def buy(self):
        printInfo('买 '+self.name)
    
    def sell(self):
        printInfo('卖 '+self.name)
 
#基金
class Fund():
    gu1 = None
    gu2 = None
    nd1 = None
    rt1 = None
    def __init__(self):
        self.gu1 = Stock1()
        self.gu2 = Stock2()
        self.nd1 = NationDebt1()
        self.rt1 = Realty1()
        
    def buyFund(self):
        self.gu1.buy()
        self.gu2.buy()
        self.nd1.buy()
        self.rt1.buy()
    
    def sellFund(self):
        self.gu1.sell()
        self.gu2.sell()
        self.nd1.sell()
        self.rt1.sell()
    
def clientUI():
    myFund = Fund()
    myFund.buyFund()
    myFund.sellFund()
    return
 
 
if __name__ == '__main__':
    clientUI();
