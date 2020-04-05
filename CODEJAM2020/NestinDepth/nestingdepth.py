from sys import stdin,stdout

x = int(stdin.readline().strip())
#no.of cases
results=[]
for i in range(x):
    string = stdin.readline().strip()
    
    lstring = list(string)
    
    nd = 0
    
    new_l = []
    #depth determination
    
    for c in lstring:
        if c == '1':
            new_l.append('(')
            new_l.append(c)
            new_l.append(')')
            continue
        elif c == '2':
            for i in range(2):
                new_l.append('(')
            new_l.append(c)
            for i in range (2):
                new_l.append(')')
            continue
        elif c == '3':
            for i in range(3):
                new_l.append('(')
            new_l.append(c)
            for i in range (3):
                new_l.append(')')
            continue
        elif c == '4':
            for i in range(4):
                new_l.append('(')
            new_l.append(c)
            for i in range (4):
                new_l.append(')')
            continue
        elif c == '5':
            for i in range(5):
                new_l.append('(')
            new_l.append(c)
            for i in range (5):
                new_l.append(')')
            continue
        elif c == '6':
            for i in range(6):
                new_l.append('(')
            new_l.append(c)
            for i in range (6):
                new_l.append(')')
            continue
        elif c == '7':
            for i in range(7):
                new_l.append('(')
            new_l.append(c)
            for i in range (7):
                new_l.append(')')
            continue
        elif c == '8':
            for i in range(8):
                new_l.append('(')
            new_l.append(c)
            for i in range (8):
                new_l.append(')')
            continue
        elif c == '9':
            for i in range(9):
                new_l.append('(')
            new_l.append(c)
            for i in range (9):
                new_l.append(')')
            continue
        
        new_l.append(c)
        
    strnew_l=''.join(new_l)
    while')('in strnew_l:
        listnew_l= strnew_l.split(')(')
        strnew_l=''.join(listnew_l)
        
    results.append(strnew_l)
    
for index in range(len(results)):
    print("Case #{}: {}".format(index+1,results[index])) 