#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Amit
#
# Created:     07-08-2019
# Copyright:   (c) Amit 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    sample = {1: {2:3,4:{5:{1:2,4:5}}},2: {2:3,4:1}}
    #starting tab count after def
    tabs = 1
    for key, value in sample.items():
        ifelse(key, value,tabs)

def ifelse(key, value,tabs):
    '''
    Recurcive function which will print if else statement as per key values
    '''
    print( "\t"*tabs+"if %s:"%key)
    tabs=tabs+1
    if type(value) == dict:
        for key1,value1 in value.items():
            ifelse(key1,value1,tabs)
    else:
        tabs=tabs-1
        print("\t"*(tabs+1) + str(value))


if __name__ == '__main__':
    main()
