list_str = []
while True:
    string = input("Enter string: ")
    list_str.append(string)
    set_=set(list_str)

    if string == "quit":

        if len(set_) == len(list_str):
            print("There were no duplicates")
        else:
            print("There were duplicates")
        break
