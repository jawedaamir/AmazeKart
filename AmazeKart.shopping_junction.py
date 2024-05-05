#!/usr/bin/env python
# coding: utf-8

# In[1]:


def register ():
    global username
    print("___________________________________________________________________________________________")
    username = input("Create username : ")
    password = input("Create password : ")
    password1 = input("Confirm password : ")
    if password != password1:
        print("******Password don't match, Restart***********")
        register()
    else:
        if len(password)<=6:
            print("********Password too short, Restart************")
            register
        else:
            print("Congratulation Succesfully Register.")
register()
def product_list():
    print("**************Welcome to AmazeKart ",username.title(),"******************")
    print("                                                                      ")
    print("                     **ITEM LIST**                                    ")
    print("s.no          Item")
    print("1             Shoes")
    print("2              Belt")
    print("______________________________________________________________________")
    print("--------------------------------")
    print("SHOES WITH BRAND NAMES AND PRICE")
    print("--------------------------------")
    print("<<<<<<<<<<<<< List of Adidas Shoes >>>>>>>>>>>")
    print("Code Number      Price              shoes Name")
    print("1           10,999.00              Niteball Shoes")
    print("2           12,999.00              Busenitz Shoes")
    print("3           9,999.00               Adifom Superstar Shoes")
    print("<<<<<<<<<<<<< List of Nike Shoes >>>>>>>>>>>>>>")
    print("Code Number      Price              shoes Name")
    print("4           17,999.00               Air Dunk Shoes")
    print("5           19,999.00               Nike Air Force Shoes")
    print("6           24,999.00               Dunk Low Retro Shoes")
    print("7           45,999.00               Nike Dior x Air Jordan 1 High")
    print("--------------------------------")
    print("BELTS WITH BRANDS NAME AND PRICE")
    print("--------------------------------")
    print("<<<<<<<<<<<<<< List of Gucci Belts >>>>>>>>>>>")
    print("8            8,999.00               GG MARMONT WIDE BELT")
    print("9            12,999.00              GG MARMONT BELT")
    print("10           15,999.00              GG MARMONT DOUBLE BUCKLE")
    print("<<<<<<<<<<<<<< List of Levi's Belts >>>>>>>>>>")
    print("11           4,999.00                Levi's Men Belt Brown")
    print("12           3,999.00                Levi's Men Belt Metal")
    print("13           2,999.00                Levi's Men Belt Black")
product_list()
print("____________________________________________________________________________________")
print("------------------------Shoes and Belts item code with price------------------------")
code = {"1": 10999.00,
       "2": 12999.00,
       "3": 9999.00,
       "4": 17999.00,
       "5": 19999.00,
       "6": 24999.00,
       "7": 45999.00,
       "8": 8999.00,
       "9": 12999.00,
       "10": 15999.00,
       "11": 4999.00,
       "12": 3999.00,
       "13": 2999.00,}
cart = []
Total = 0
for key, values in code.items():
    print(f"{key}:{values}")
    print()
print("-----------------------------------------------------------------")
while True:
    product = input("Select an item(q to quit): ")
    if product.lower() =="q":
        break
    elif code.get(product)is not None:
        cart.append (product)
print("_________________________Product Code List_______________________")
for product in cart:
    Total += code.get(product)
    print("Product Code Number",product)
    
    
def after_discount():
    print("_____________________________________________________________")
    Payment_method = int(input("""1 for UPI(20% off upto 2000)
2 for Net Banking(15% off upto 2000)
3 for Credit Crad (10% off upto 2000)
4 for Cash on Delivery
Payment Method:    """))
    if Payment_method == 1 and Total >=2000:
        print("-------------------------------------------")
        print("TOTAL AMOUNT")
        print("Total amount",Total)
        print("Discount  :  ",Total*20/100)
        print("Total amount after Discount  :  ",Total-Total*20/100)
        print("---------------------------------------")
    elif Payment_method == 2 and Total>=2000:
        print("-------------------------------------------")
        print("TOTAL AMOUNT")
        print("Total amount",Total)
        print("Discount  :  ",Total*20/100)
        print("Total amount after Discount  :  ",Total-Total*20/100)
        print("---------------------------------------")
    elif Payment_method == 3 and Total >=2000:
        print("-------------------------------------------")
        print("TOTAL AMOUNT")
        print("Total amount",Total)
        print("Discount  :  ",Total*20/100)
        print("Total amount after Discount  :  ",Total-Total*20/100)
        print("---------------------------------------")
    elif Payment_method == 4 and Total >=2000:
        print("-------------------------------------------")
        print("TOTAL AMOUNT")
        print("Total amount",Total)
        print("Discount  :  ",Total*20/100)
        print("Total amount after Discount  :  ",Total-Total*20/100)
        print("---------------------------------------")
    elif Payment_method == 5:
        print("-------------------------------------------")
        print("TOTAL AMOUNT")
        print("Total amount ", Total)
        print("---------------------------------------")
    else:
        after_discount()
after_discount()
print("***************************Congratulations you will get 5% off on your next shopping*************************")

        


# In[ ]:




