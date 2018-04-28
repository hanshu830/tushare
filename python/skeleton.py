
def file_test():
    f = open('workfile', 'w+')
    f.write(str(sys.argv))
    f.seek(0)
    data = f.read() 
    print "Dump:"+ str(data)
    f.close()


def usage(s):
    print s

if __name__ == "__main__":
    import sys
    usage(sys.argv)
    file_test()



