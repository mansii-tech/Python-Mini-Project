
#Define the menu of restaurant.
menu = {
    'Pizza':150,
    'Burger':100,
    'Coffe':120,
    'Chai':40,
    'Dosa':50
}

#Greet
print("Welcome To Mahi's Cafe")
print("Pizza: Rs.150 \n Burger: Rs.100 \n Coffe: Rs.120 \n Chai: Rs.40 \n Dosa: Rs.50" )

#Creating order_total variable.
order_total = 0

#Now, we’ll use a while loop to order multiple items.
while True:

#Input
    item_1 = input("Enter the name of your item you want to order = ").upper()

#Now, we’ll use a conditional statement to check if the item exists on the menu.
    if item_1 in menu:
        order_total += menu[item_1]    #0 + pizza(150) = total 150
        print(f"Your item {item_1} has been added to your order")

#If the user enters an item that is not on our menu.
    else:
        print(f"Ordered item {item_1} is not available yet")

#Now, we are creating a variable named another_order to ask the customer if they want to order anything else.
    another_order = input("Do you want to add another item? (Yes/NO):")

#Now, I’ll use a condition to check whether the customer wants to order another item.
    if another_order.upper() != "YES":
        break

#Finally, display the total amount.
print(f"The total amount of items to pay {order_total}")
