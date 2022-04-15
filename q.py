def ff():
    f=open("first.ch","r")
    a=f.readlines()
    print(a[1],'hello')
    f.close()
    return a[1]