storage = {
    "cap": 18, 
    # 5m
    "trourserse": 80, 
    # 30m
    "shirt": 65 
    # 15m
}

balance = 200

while True:
    person = input("Write what you want to buy >>> ").lower()

    match(person):
        case "cap":
            count = int(input("Write how much you want cap >>> "))
            a = count * 5
            if a > storage["cap"]:
                print("sorry you not have enough")
            else:
                storage["cap"] = storage["cap"] - count
                balance -= a
                print(f"You have in balance {balance} and {count} caps")
                break
            
        case "trourserse":
            count = int(input("Write how much you want trourserse >>> "))
            a = count * 30
            if a > storage["trourserse"]:
                print("sorry you not have enough")
            else:
                storage["trourserse"] = storage["trourserse"] - count
                balance -= a
                print(f"You have in balance {balance} and {count} trourserse")
                break

        case "shirt":
            count = int(input("Write how much you want shirt >>> "))
            a = count * 30
            if a > storage["shirt"]:
                print("sorry you not have enough")
            else:
                storage["shirt"] = storage["shirt"] - count
                balance -= a
                print(f"You have in balance {balance} and {count} shirt")
                break

        case _:
            print("We have shirt, trourserse, cap")