#WAP to generate electricity bill
units=int(input("Enter the amount of units consumed: "))

if units>0 and units<=100:
    bill=units*10
    print("The amount need to pay is ",bill)
elif units>100 and units<=200:
    bill=1000+(units-100)*15
    print("The amount need to pay is ",bill)
elif units>200 and units<=300:
    bill=1000+1500+(units-200)*20
    print("The amount need to pay is ",bill)
else:
    bill=1000+1500+2000+(units-300)*25
    print("The amount need to pay is ",bill)
    
