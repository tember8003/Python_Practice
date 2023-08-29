MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    """재료가 충분하지 않을 경우 False 아니면 True 반환"""
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough=False
    return is_enough

def process_coins():
    """총액 계산해서 반환하기."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    """비용이 충분하면 True 아니면 False 반환"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += change
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    """가진 재료에서 커피 만드는데 필요한 재료 빼기."""
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"Here is your {drink_name} ☕. ENJOY!!")

def resource_add():
    """재료 추가하기(파일 저장 형태가 아니라서 현재로선 의미없는 함수긴 함.)"""
    water = int(input("How much water will you put in??"))
    resources['water'] += water
    print(f"put in {water}ml and now, We have {resources['water']}")
    milk= int(input("How much milk will you put in??"))
    resources['milk'] += milk
    print(f"put in {milk}ml and now, We have {resources['milk']}")
    coffee = int(input("How much coffee will you put in??"))
    resources['coffee'] +=coffee
    print(f"put in {coffee}ml and now, We have {resources['coffee']}")



is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    elif choice =="add":
        resource_add()
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])


