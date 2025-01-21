try:
    result = 10 + 10
except:
    print("Error...something went wrong")
finally:
    print(result)

try:
    f = open("testfile.txt", "r")
    f.write("Write a test line.")
except TypeError:
    print("There is a type error")
except OSError:
    print("There is an OS Error")
except:
    print("Whatever other errors will go here.")
finally:
    print("This will run no matter what.")


def ask_for_int():
    while True:
        try:
            result = int(input("Enter a number here: "))
        except ValueError as ve:
            print(ve)
            print("Invalid number. Please try again.")
        else:
            print("Good Job!")
            return result


ask_for_int()
