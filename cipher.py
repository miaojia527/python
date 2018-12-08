#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def  translationCipher(msg,key):
   result = [""]*key
   for i in range(key):#把每一列元素按照顺序相加组成新的字符序列
    pointer = i
    while i<len(msg):
     result[pointer]+=msg[i]
     i+=key
   return ''.join(result)
 
def  main():
  print translationCipher("hello,world",4)#以4个字母为一行进行换位加密
if  __name__=="__main__":
  main()
