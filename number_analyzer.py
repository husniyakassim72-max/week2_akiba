even=0
odd=0
total=0
for i in range(10):
    num= int(input("enter number: "))
    if i==0:
        largest=num
        smallest=num
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
    total=total+num
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
ave =total/10 
print("largest:",largest)
print("smalles:",smallest)
print("sum:",total)
print("average:",ave)
print("even number",even)
print("odd number:",odd)                    