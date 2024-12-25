# Stuctural Pattern Matching
# switch statement ==
# or
# lang = input("你需要學甚麼程式語言?")

# match lang:
#     case "JavaScript":
#         print("你會成為網頁前端開發人員!")
#     case "PHP" | "Java":
#         print("你會成為網頁後端開發人員!")
#     case "Python":
#         print("你會成為資料科學家！")
#     case "Kotlin":
#         print("你會成為 Android 應用程式開發人員！")
#     case "Swift":
#         print("你會成為 iOS 應用程式開發人員！")
#     case _:
#         print("你會成為其他開發人員！")

command = input("Where do you wanna go? ")
print(command.split(" "))
# Where do you wanna go? I wanna go home
# ['I', 'wanna', 'go', 'home']

match command.split(" "):
    case ["Go", "home"]:
        print("You wanna go home.")
    case _:
        print("The system cannot determine where you wanna go.")

# if elif => switch ==, >, <, >=, <=
# 不一定要使用 switch
