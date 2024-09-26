while True:
    answer = input("Ready to continue? y/n: ").lower()
    if answer == "y":
        temp_in_f = int(input("Enter Temperature in F: "))
        temp_in_с = (temp_in_f - 32) * 5 / 9
        print(f"Temperature in C: {round(temp_in_с, 1)}")
    elif answer == "n":
        print("Thank you for using me")
        break

