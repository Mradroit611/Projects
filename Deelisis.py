# LOGIN_______________________________________________________________________________________________________________________
def login():
    print("_______DEELISIS Login Page_______")
    import csv

    def main():
        with open("users.txt", "r") as file:
            file_reader = csv.reader(file)
            user_find(file_reader)
            file.close()

    def user_find(file):
        user = input("Enter your username: ")
        for row in file:
            if row[0] == user:
                print("username found", user)
                user_found = [row[0], row[1]]
                pass_check(user_found)
                break
        else:
            print("Username not found")

    def pass_check(user_found):
        user = input("enter your password: ")
        if user_found[1] == user:
            print("password match")
            print("\n_____User Logged in successfully_____")
            afterlog()
        else:
            print("password not match")
            user_find(file_reader)

    main()


# Mob number_______________________________________________________________________________________________________________
def mob():
    m = int(input("Enter your mobile number: "))
    if m<10000000000 and m>6999999999:
        return m
    else:
        print("Please enter valid number__ ")
        b = int(input("Enter 1 to re-enter the mobile number or 2 to go back: "))
        if b == 1:
            m = int(input("Enter your mobile number: "))
            if m < 10000000000 and m > 6999999999:
                return m
        elif b == 2:
            signup()
        else:
            print("Invalid choice try again__")
            mob()

# SIGNUP_______________________________________________________________________________________________________________________
def signup():
    print("\n-------DEELISIS Signup page-------")
    b = input("Enter your name: ")
    k = str(mob())
    c = k
    d = input("Enter your address: ")
    e = input("Enter your pincode: ")
    u = input("Create your username: ")
    p = input("Create your password: ")
    print("_____You have successfully signed up in DEELISIS_____")

    f = open("users.txt", "a") #User ID and password
    f.write(u)
    f.write(",")
    f.write(p)
    f.write("\n")
    f.close()
    f = open("profile.txt","a")  #User Data File
    f.write(b)
    f.write(", ")
    f.write(c)
    f.write(", ")
    f.write(d)
    f.write(", ")
    f.write(e)
    f.write("\n")
    f.close()

    print("\n\n")
    print("__________Welcome to DEELISIS__________")
    print("1.Login\n2.Exit")
    a = int(input("Please enter your choice: "))
    if a == 1:
        login()

    elif a == 2:
        exit()

    else:
        print("Error")


# OTHER___________________________________________________________________________________________________________________
def other():
    print("_______________________ [OTHER OPTIONS] ______________________")
    print("1.Main menu\n2.Logout\n3.Exit\n4.Go back")
    c = int(input("Enter your choice :"))
    if c == 1:
        afterlog()
    elif c == 2:
        login()
    elif c == 3:
        exit()
    elif c == 4:
        home()
    else:
        print("Invalid choice try again__")
        other()

# BILL___________________________________________________________________________________________________________________
def bill():
    b = int(input("Enter 1 to place order and 2 to go back: "))
    if b == 1:
        print("\n_____________ Payment Ways _______________ \n1.Card payment\n2.UPI payment")
        c = int(input("Choose the payment way: "))
        if c == 1:
            print("Enter your card details___ ")
            a = int(input("Enter Card number: "))
            if a<10000000000000000 and a>999999999999999:
                j = int(input("Enter CVV number: "))
                if j>99 and j<1000:
                    l = int(input("Enter 1 to pay and 2 to go back: "))
                    if l == 1:
                        print("\n________________Your order is successfully placed___________________")
                    elif l == 2:
                        bill()
                    else:
                        print("Invalid choice")
                        bill()
                else:
                    print("Invalid card number try again__")
                    bill()
            else:
                print("Invalid card number try again__")
                bill()
        elif c == 2:
            print("Enter your UPI Details____")
            z = input("Enter UPI ID: ")
            y = int(input("Check your message box and select 12, 13, 14, 15 and same as enter their which u have choose : "))
            if y == 12 or y == 13 or y == 14 or y == 15:
                x = int(input("Enter 1 to pay and 2 to go back: "))
                if x == 1:
                    print("\n________________Your order is successfully placed___________________")
                elif x == 2:
                    bill()
                else:
                    print("Invalid choice try again__")
                    bill()
            else:
                print("Invalid Number try again__")
                bill()

    elif b == 2:
        pizza()
    else:
        print("Invalid choice try again__ ")
        pizza()


# INVOICE__________________________________________________________________________________________________________________
def invoice(j):
    a = j
    print("\n[DEELISIS]")
    print("____________________________________________________________________")
    print("____________________________Receipt 001_____________________________")
    print("Ordered Item : ")
    print(" \tFood Name           \tPrice\tTotal_Bill")
    if a == 120:
        print("1\tVeg Loadded Pizza   \t₹110 \t₹120")
    elif a == 110:
        print("1\tCheesy Pizza        \t₹100 \t₹110")
    elif a == 130:
        print("1\tPaneer & Onion Pizza\t₹120 \t₹130")
    elif a == 100:
        print("1\tCapsicum             \t₹90 \t₹100")
    elif a == 101:
        print("1\tVeg Meal             \t₹90 \t₹101")
    elif a == 150:
        print("1\tNon-Veg Meal         \t₹140 \t₹150")
    elif a == 55:
        print("1\tLemonade             \t₹40 \t₹35")
    elif a == 35:
        print("1\tWater                \t₹20 \t₹35")
    elif a == 200:
        print("1\tCarrot Cake          \t₹200 \t₹200")
    elif a == 90:
        print("1\tIce Cream            \t₹80 \t₹90")
    print("\n______________________________________________________________________")
    print("1.Exit\n2.Food Manual\n3.Home\n4.Logout")
    q = int(input("Enter your choice: "))
    if q == 1:
        exit()
    elif q == 2:
        foodmanual()
    elif q == 3:
        home()
    elif q == 4:
        login()
    else:
        print("invalid choice")
        invoice()




# DESSERT_________________________________________________________________________________________________________________
def des():
    print("\n____ [DESSERTS] ___________________________________")
    print("1.Carrot Cake\n2.Ice Cream\n3.Go back")
    a = int(input("Choose your order: "))
    match a:
        case 1:
            print("\n__ Carrot cake __")
            print("-----------------------------")
            print("Subtotal       : ₹200")
            print("Discount       : ₹20")
            print("Tax and charges: ₹20")
            print("________________________")
            print("Grand Total    : ₹200")
            bill()
            print("1.Order Bill\n2.Food manual\n3.Home\n4.Logout")
            v = int(input("Enter your choice: "))
            if v == 1:
                invoice(200)
            elif v == 2:
                foodmanual()
            elif v == 3:
                home()
            elif v == 4:
                login()
            else:
                print("Invalid choice")
                des()

        case 2:
            print("\n__ Ice Cream __")
            print("-----------------------------")
            print("Subtotal       : ₹80")
            print("Discount       : ₹10")
            print("Tax and charges: ₹20")
            print("________________________")
            print("Grand Total    : ₹90")
            bill()
            print("1.Order Bill\n2.Food manual\n3.Home\n4.Logout")
            b = int(input("Enter your choice: "))
            if b == 1:
                invoice(90)
            elif b == 2:
                foodmanual()
            elif b == 3:
                home()
            elif b == 4:
                login()
            else:
                print("Invalid choice")
                des()

        case 3:
            foodmanual()

        case default:
            print("Invalid choice try again__")
            des()

# BEVERAGES_______________________________________________________________________________________________________________
def bev():
    print("\n____ [BEVERAGES] ___________________________________")
    print("1.Lemonade\n2.Water\n3.Go back")
    a = int(input("Choose your order: "))
    match a:
        case 1:
            print("\n__ Lemonade __")
            print("-----------------------------")
            print("Subtotal       : ₹40")
            print("Discount       : ₹5")
            print("Tax and charges: ₹20")
            print("________________________")
            print("Grand Total    : ₹55")
            bill()
            print("1.Order Bill\n2.Food manual\n3.Home\n4.Logout")
            v = int(input("Enter your choice: "))
            if v == 1:
                invoice(55)
            elif v == 2:
                foodmanual()
            elif v == 3:
                home()
            elif v == 4:
                login()
            else:
                print("Invalid choice")
                bev()

        case 2:
            print("\n__ Water __")
            print("-----------------------------")
            print("Subtotal       : ₹20")
            print("Discount       : ₹5")
            print("Tax and charges: ₹20")
            print("________________________")
            print("Grand Total    : ₹35")
            bill()
            print("1.Order Bill\n2.Food manual\n3.Home\n4.Logout")
            b = int(input("Enter your choice: "))
            if b == 1:
                invoice(35)
            elif b == 2:
                foodmanual()
            elif b == 3:
                home()
            elif b == 4:
                login()
            else:
                print("Invalid choice")
                bev()

        case 3:
            foodmanual()

        case default:
            print("Invalid choice try again__")
            bev()

# PIZZA ___________________________________________________________________________________________________________________
def pizza():
    print("\n____ [PIZZA MANIA] ___________________________________")
    print("1.Veg Loaded\n2.Cheesy\n3.Paneer and Onion\n4.Capsicum\n5.Go back")
    a = int(input("Choose your order: "))
    match a:
        case 1:
            print("\n__Veg Loaded Pizza__")
            print("-----------------------------")
            print("Subtotal       : ₹110")
            print("Discount       : ₹10")
            print("Tax and charges: ₹20")
            print("________________________")
            print("Grand Total    : ₹120")
            bill()
            print("1.Order Bill\n2.Food manual\n3.Home\n4.Logout")
            v = int(input("Enter your choice: "))
            if v == 1:
                invoice(120)
            elif v == 2:
                foodmanual()
            elif v == 3:
                home()
            elif v == 4:
                login()
            else:
                print("Invalid choice")
                pizza()

        case 2:
            print("\n__Cheesy Pizza__")
            print("-----------------------------")
            print("Subtotal       : ₹100")
            print("Discount       : ₹10")
            print("Tax and charges: ₹20")
            print("________________________")
            print("Grand Total    : ₹110")
            bill()
            print("1.Order Bill\n2.Food manual\n3.Home\n4.Logout")
            b = int(input("Enter your choice: "))
            if b == 1:
                invoice(110)
            elif b == 2:
                foodmanual()
            elif b == 3:
                home()
            elif b == 4:
                login()
            else:
                print("Invalid choice")
                pizza()
        case 3:
             print("\n__Paneer and Onion Pizza__")
             print("-----------------------------")
             print("Subtotal       : ₹120")
             print("Discount       : ₹10")
             print("Tax and charges: ₹20")
             print("________________________")
             print("Grand Total    : ₹130")
             bill()
             print("1.Order Bill\n2.Food manual\n3.Home\n4.Logout")
             b = int(input("Enter your choice: "))
             if b == 1:
                 invoice(130)
             elif b == 2:
                 foodmanual()
             elif b == 3:
                 home()
             elif b == 4:
                 login()
             else:
                 print("Invalid choice")
                 pizza()
        case 4:
              print("\n__Capsicum Pizza__")
              print("-----------------------------")
              print("Subtotal       : ₹90")
              print("Discount       : ₹10")
              print("Tax and charges: ₹20")
              print("________________________")
              print("Grand Total    : ₹100")
              bill()
              print("1.Order Bill\n2.Food manual\n3.Home\n4.Logout")
              b = int(input("Enter your choice: "))
              if b == 1:
                  invoice(100)
              elif b == 2:
                  foodmanual()
              elif b == 3:
                  home()
              elif b == 4:
                  login()
              else:
                  print("Invalid choice")
                  pizza()

        case 5:
            foodmanual()

        case default:
            print("Invalid choice try again__")
            pizza()


# MEALS __________________________________________________________________________________________________________________
def meal():
    print("\n____ [MEALS AND COMBOS] ___________________________________")
    print("1.Veg Meals\n2.Non-Veg Meals\n3.Go back")
    a = int(input("Choose your order: "))
    match a:
        case 1:
            print("\n__ Veg meals (Cheese Burger + Fries + Cold_drink) __")
            print("-----------------------------")
            print("Subtotal       : ₹90")
            print("Discount       : ₹9")
            print("Tax and charges: ₹20")
            print("________________________")
            print("Grand Total    : ₹101")
            bill()
            print("1.Order Bill\n2.Food manual\n3.Home\n4.Logout")
            v = int(input("Enter your choice: "))
            if v == 1:
                invoice(101)
            elif v == 2:
                foodmanual()
            elif v == 3:
                home()
            elif v == 4:
                login()
            else:
                print("Invalid choice")
                meal()

        case 2:
            print("\n__ Non-Veg Meals (Chicken Burger + Fries + Cold_drink) __")
            print("-----------------------------")
            print("Subtotal       : ₹140")
            print("Discount       : ₹10")
            print("Tax and charges: ₹20")
            print("________________________")
            print("Grand Total    : ₹150")
            bill()
            print("1.Order Bill\n2.Food manual\n3.Home\n4.Logout")
            b = int(input("Enter your choice: "))
            if b == 1:
                invoice(150)
            elif b == 2:
                foodmanual()
            elif b == 3:
                home()
            elif b == 4:
                login()
            else:
                print("Invalid choice")
                meal()

        case 3:
            foodmanual()

        case default:
            print("Invalid choice try again__")
            meal()


# FOODMANUAL______________________________________________________________________________________________________________
def foodmanual():
    print("___________________________[FOOD MANUAL] ____________________________")
    print("1.Pizza Mania\n2.Meals and Combos\n3.Beverages\n4.Dessert")
    a = int(input("Enter your choice: "))
    if a == 1:
        pizza()
    elif a == 2:
        meal()
    elif a == 3:
        bev()
    elif a == 4:
        des()
    else:
        print("Invalid choice try again__")
        foodmanual()

# Home____________________________________________________________________________________________________________________
def home():
    print("___________________________ [HOME PAGE] _______________________________")
    print("1.User Profile\n2.Food Manual\n3.Invoices\n4.Feedback\n5.Other options")
    a = int(input("Enter your choice: "))

    if a == 1:
        print("To Check User profile first verify by giving some details____ ")
        x = input("Your Name: ")
        y = int(input("Contact number: "))
        z = input("State: ")
        print("\n__________________________ [USER PROFILE] ____________________________")
        print("User Name: ",x)
        print("User Mobile Number: ",y)
        print("Address: India, ",z)
        print("________________________________________________________________________\n\n")
        q = int(input("Enter 1 to go back and 2 for logout: "))
        if q == 1:
            home()
        elif q == 2:
            login()
        else:
            print("Invalid enter try again__")
            home()
    elif a == 2:
        foodmanual()
    elif a == 3:
        k = int(input("Please Enter your last Bill price: "))
        invoice(k)
    elif a == 4:
        print("___________________________ [FEEDBACK] ___________________________")
        print("Feedback: \n")
        fd = input()
        d = int(input("Enter 1 to submit the feedback and 2 to go back: "))
        if d == 1:
            f = open("feedback.txt", "a")
            f.write(fd)
            f.write("\n\n")
            f.close()
            print("Feeedback submitted")
            print("__________Thanks for your feedback________\n\n")
            home()
        elif d == 2:
            home()
        else:
            print("Invalid choice try again__")
            home()

    elif a == 5:
        other()
    else:
        print("Invalid choice try again__")
        home()

# Afterlog_________________________________________________________________________________________________________________
def afterlog():
    print("1.Home\n2.About\n3.logout")
    a = int(input("Enter your choice: "))
    match a:
        case 1:
            home()
        case 2:
            print("____________________________________ ABOUT  [DEELISIS] _____________________________________")
            print("DEELISIS is an Indian multinational restaurant aggregator and food delivery company founded ")
            print("by Sanjay Verma in 2023. DEELISIS provides information, menus and ")
            print("user-reviews of restaurants and the best facilities than other restaurants. \n")
            print("Founders: Sanjay Verma")
            print("Founded: January 2023")
            print("Number of employees: 5,000+")
            print("Headquarters: Delhi")
            print("Subsidiaries: Techadroit")
            print("____________________________________________________________________________________________\n")
            print("1.Go back\n2.Logout\n3.Exit")
            b = int(input("Enter your choice: "))
            if b == 1:
                print("\n_________________________________________________________________________________________\n")
                afterlog()
            elif b == 2:
                print("\n_________________________________________________________________________________________\n")
                login()
            elif b == 3:
                exit()
            else:
                print("Error")
        case 3:
            login()

            # insert goto statement

        case default:
            print("Invalid choice try again")
            afterlog()

#Main Body of program***************************************************************************************************

print("__________Welcome to DEELISIS__________")
print("1.Login\n2.Signup\n3.Exit")
a = int(input("Please enter your choice: "))
if a == 1:
    login()

elif a == 2:
    signup()

#insert goto statement

else:
    exit()