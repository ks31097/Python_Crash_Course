guests = int(input("How many guests will there be? "))

if guests > 0:
    if guests < 8:
        print(f"Your table is ready. {guests}")
    else:
        print(f"Please wait for a while! {guests}")
else:
    print("Sorry!")