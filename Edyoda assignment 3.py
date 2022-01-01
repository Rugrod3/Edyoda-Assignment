Q1.
def summ(x):
    suum=0
    for i in x:
        suum+=i
    print(suum)


Q2.
def reverse_string(str):  
    str1 = ""  
    for i in str:  
        str1 = i + str1  
    return str1


Q3.
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
