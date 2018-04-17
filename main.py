#!/usr/bin python3
import sys
sys.path.append('./app')
import gen

if(__name__ == "__main__"):
    n = input("Length of the password:")
    l = input("Your word list:")
    # TODO : 
        '''
            Traceback (most recent call last):
            File "main.py", line 8, in <module>
                l = input("Your word list:")
            File "<string>", line 1, in <module>
        '''
    
    print(gen.userList(n,l))