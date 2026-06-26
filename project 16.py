def shutdown():
    choice = input("Do you want to shut down the computer? (yes/no): ")

    if choice.lower() == "yes":
        print("Shutting down...")
    elif choice.lower() == "no":
        print("Abort shutdown.")
    else:
        print("Sorry, invalid input.")
shutdown()