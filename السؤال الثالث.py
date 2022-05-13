import json
def function():
    name=["ayoub"]
    degrees=[]
    for i in range(1):
        degree=0
        name_student=input("enter student name:"+str(name[i]))
        qes1=input("what is your name?")
        qes2=input("how old are you?")
        qes3=input("what is your favourit sport?")
        qes4=input("what is your favourit food?")
        if qes1=="ayoub":
            degree=degree+5
        else:
            degree=degree+0
        if qes2=="25":
            degree=degree+5
        else:
            degree=degree+0
        if qes3=="football":
            degree=degree+5
        else:
            degree=degree+0
        if qes4=="fish":
            degree=degree+5
        else:
            degree=degree+0
        print("your degree is: " +str (degree))
        degrees.append (degree)
    d={}
    for i in range (1):
        N=name[i]
        M=degrees[i]
        d[N]={"name":N,"degree":M}
        i+=1
    folder=json.dumps(d)
    with open ("ayoub.json","w") as x:
        x.write(folder)
    with open ("ayoub.json","r") as x:
        result=json.loads(x.read())
    print (result)
    
