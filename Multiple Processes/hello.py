from multiprocessing import *

def HelloWorld(name):
    print( "Hello %s, from %d"%(name,current_process().pid ))

def main():
    name = input("Name: ")
    p = Process(target=HelloWorld, args=(name,))
    p.start()
main()