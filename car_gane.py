#command = ""
status = ""

while True:
    command = input("> ").lower()
    if command == "start":
        if status == "started":
            print("car already started")
        else:
            print('Car started...Ready to go!')
        status = "started"
    elif command == "stop":
        if status == "stopped":
            print("car aleready stopped")
        else:
            print('Car stopped')
        status = "stopped"
    elif command == "help":
        print("""
        start - to start the car 
        stop  - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")
else:
    print("process stoped with exit code 0")