try:
    age=int(input("please enter your age for sign up "))
    if age>18 and age<50: 
        print("yes you are qualifyed ")
    elif age>50:
        d=age%2
        if d==0:
            print("your age is qualifyed ")
    elif age<18:
        c=age%2
        if c==0:
            print("your age is qualifyed ")
    else:
        print("sorry age {} is not allowed for sign up".format(age))
except ValueError as ex:
    print("error you commited a ",ex)