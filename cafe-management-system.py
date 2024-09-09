print('Welcome to Ashok Restaurant')

menu = {
    "coffee": 100,
    "pizza": 150,
    "cold coffee": 80,
    "sandwich": 50,
    "tea": 20,
    "dabeli": 70,
    "momos": 70,
    "salad": 50,
    "cold drink": 70,
    "burger": 100,
}
while True:
 total_order = 0  # Initialize total_order outside the loop

 while True:
    print("coffee: Rs100\npizza: Rs150\ncold coffee: Rs80\nsandwich: Rs50\ntea: Rs20\ndabeli: Rs70\nmomos: Rs70\nsalad: Rs50\ncold drink: Rs70\nburger: Rs100")
    dish_1 = input("Enter the dish you want to order = ").strip().lower()
    
    if dish_1 in menu:
        total_order += menu[dish_1]
        print(f"Your dish {dish_1} has been added to your order")
    else:
        print(f"Ordered dish {dish_1} is not available at this moment")
    
    another_order = input("Do you want to add another dish? (Yes/No): ").strip().lower()
    
    if another_order == "yes":
        dish_2 = input(f"Enter the next dish you want to order = ").strip().lower()
        
        if dish_2 in menu:
            total_order += menu[dish_2]
            print(f"Your ordered dish {dish_2} has been added to your order")
        else:
            print(f"Ordered dish {dish_2} is not available at this moment")
    elif another_order == "no":
        break
    else:
        print("Invalid input. Please respond with 'Yes' or 'No'.")

 print(f"The total amount of your order is Rs{total_order}")
 print("Thank you for visiting Ashok Restaurant. Have a great day!")
 restart = input("\nDo you want to start a new order? (Yes/No): ").strip().lower()
 if restart == "no":
    print("Thank you for visiting Ashok Restaurant. Have a great day!")
    break  # This break statement correctly exits the outer loop
 elif restart != "yes":
    print("Invalid input. Please respond with 'Yes' or 'No'.")
