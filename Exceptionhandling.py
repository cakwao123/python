try:
    x = 5
    print(x)
except:
    print("An error occured")
finally:
    print("success")

    num1 = 67
    num2 = 0
    try:
        print(num1 / num2)
    except:
        print("zerodivision error occured")
    finally:
        print("success")