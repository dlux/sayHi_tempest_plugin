'''
Simple say hi class
The intention is to grow from here


@author: luzC
'''
import random
import sys


class SayHiClass(object):
    '''
    Say hi class documentation
    '''

    def __init__(self):
        '''
        Class constructor

        '''
        pass

    def hi(self, name='Stranger'):
        hi = ("Bonjour","Hello", "Hi", "Hola", "Ni hao")
        
        print "{0} {1}".format(random.choice(hi), name)

    def a_sum(self, values):
        try:
            values = map(int, values)
        except:
            print "Skiping due to invalid entry {0}".format(values)
            sys.exit(2)

        result = 0
        for num_ in values:
            result = result + num_
        print "Sum is = {0}".format(result)


def main():
    args = sys.argv[1:]
    dlux = SayHiClass()

    if not args:
        dlux.hi() 
    elif args[0] == "a_sum":
        dlux.a_sum(args[1:])
    else:
        dlux.hi(''.join(args)) 


if __name__ == '__main__':
    main()
    #dlux = sayHiClass()
    #dlux.hi()
    #dlux.a_sum([1,2,3,4])
