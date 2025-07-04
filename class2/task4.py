#task:  print numbers from 1 to 100
#for 3,6,9,12,15 (for every 3rd) add foo
#for 5,10,15,20 (for every 5th) add bar
#for 10,20,30,40 (for every 10th) abb hello

for i in range(1,101):
    x=str(i)
    if i % 3 == 0:
        x += " foo"       
    if i % 5 == 0:
        x += " bar"
    if i % 10 == 0:
        x +=" hello"
    print (x)