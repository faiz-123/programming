import re

folder =['main.py','main2.py','main3.py','main4.py','main5.py']
function = [r'mul',r'add',r'sub',r'div',r'faiz']

for i in range(5):
    file1 = open(folder[i],'r')
    a=file1.read()

    result = re.search(function[i],a)
    start = result.start()

    s=a[start-4:start+25]
    print(s)
    
    
    