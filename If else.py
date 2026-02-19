vge=str(input())
kg=int(input())
if(vge=='tomato'):
    a=kg*3.5
    x=f"{a:.2f}"
    y=f"{kg:.1f}"
    print("total price of", y, "for amount : $", x)
elif(vge=='potato'):
    a=kg*2.5
    x=f"{a:.2f}"
    y=f"{kg:.1f}"
    print("total price of", y, "for amount : $", x)
elif(vge=='onion'):
    a=kg*1.5
    x=f"{a:.2f}"
    y=f"{kg:.1f}"
    print("total price of", y, "for amount : $ ", x)
else:
    print("you enter veg not in list .")
