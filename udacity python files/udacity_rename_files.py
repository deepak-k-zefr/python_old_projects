# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 00:02:15 2016

@author: p2admin
"""
import os
def rename_files():
# list everything in a durectory    
    file_list=os.listdir(r"C:\Users\p2admin\Downloads\prank")
    print(file_list)   
    print(os.getcwd())
    os.chdir(r"C:\Users\p2admin\Downloads\prank")
# rename everyfile
    for file_name in file_list:         
      os.rename(file_name, file_name.lstrip("0123456789"))

         
rename_files()