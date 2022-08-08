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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources["Money"] = 0


def check_user():
    user_choice = input("What would you like?(espresso/latte/cappuccino):").lower()
    return user_choice


def insert_coin():
    """让用户输入各种硬币各几枚，计算收到的总金额"""
    print("Please insert coins.")
    inserted_quarters = int(input("How many quarters?"))
    inserted_dimes = int(input("How many dimes?"))
    inserted_nickles = int(input("How many nickles?"))
    inserted_pennies = int(input("How many pennies?"))
    received_money = 0.25 * inserted_quarters + 0.1 * inserted_dimes + 0.05 * inserted_nickles + 0.01 * inserted_pennies
    return received_money


def check_resource(user_choice):
    """查看是否有足够的资源，如果有，返回true，如果没有，返回false"""
    # 问题是，如果同时几种ingredients都缺少，for语句是否要遇到首次不够的ingredients就退出，还是全部ingredients都查找一遍.目前的语句，就算碰到了一个不够的ingredients，仍然要检查所有单独ingredients
    # 修改过后，如果同时几种ingredients都缺少，就把所有缺少的ingredients在for语句中陆续加到一个list里。在for语句结束后，把list转化成string，并以字符and隔开，然后打印所有缺少的ingredients
    # if_enough = True
    not_enough_ingredients = []
    for i in MENU[user_choice]["ingredients"]:
        if resources[i] < MENU[user_choice]["ingredients"][i]:
            not_enough_ingredients.append(i)
    if not_enough_ingredients:
        print(f"Sorry there is not enough {' and '.join(not_enough_ingredients)}")
        return False
    return True

    #       print (f"Sorry there is not enough {i} ")
    #       if_enough = False
    # return(if_enough)


def report_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${resources['Money']}")


def check_money(user_choice):
    received_money = insert_coin()
    if received_money < MENU[user_choice]["cost"]:
        print(f"Sorry that's not enough money. Money refunded")
    else:  # 如果钱足够，那就把钱收下，多余的钱退回，resources更新
        if received_money > MENU[user_choice]["cost"]:
            refund = round(received_money - MENU[user_choice]["cost"], 2)
            print(f"Here is ${refund} in change")
        for i in MENU[user_choice]["ingredients"]:  # 挨个check resource里各元素的值，money增加，ingredients扣掉用掉的量
            resources[i] -= MENU[user_choice]["ingredients"][i]
        resources["Money"] += MENU[user_choice]["cost"]
        print(f"Here is your {user_choice}. Enjoy!")


if_continue = True
# choice=check_user()

# if check_resource(choice):
#   check_money(choice)

while if_continue:
    choice = check_user()
    if choice == "off":
        if_continue = False
    elif choice == "report":  # 这里需要用elif，满足off时，就不执行后面的语句，满足report时，就不执行后面的语句，否则执行check_resource时会报错
        report_resources()
    else:
        if check_resource(choice):
            check_money(choice)
        # if resources["water"] < MENU[user_choice]["water"] and resources["coffee"] < MENU[choice]["coffee"]:
        #     print(f"Sorry there is not enough water and coffee")
        # elif resources["water"] < MENU[user_choice]["water"]:
        #     print(f"Sorry there is not enough water ")
        # elif resources["coffee"] < MENU[user_choice]["coffee"]:
        #     print(f"Sorry there is not enough coffee ")