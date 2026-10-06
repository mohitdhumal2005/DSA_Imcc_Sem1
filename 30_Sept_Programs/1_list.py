#find smallest, second smallest, largest and second largest element in the list

a = [10,86,4,33,39,25,29,7]
max=min=a[0]
smin=smax=a[0]

for num in a:
    if num>max:
        smax=max
        max=num
    elif (num>smax and num!=max):
        smax=num

    if num<min:
        smin=min
        min=num

    elif (num>smin and num!=min):
        smin=num

print("maximum: ",max)
print("second maximum: ",smax)
print("minimum: ",min)
print("second minimum: ",smin)