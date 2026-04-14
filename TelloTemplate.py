import time

sock = None

try:
    ready = input("Ready? (yes/no): ")

    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 1)
        sendmsg('takeoff')

<<<<<<< Updated upstream
        # Review the (SDK) Software Development Kit resource for Drone Commands
        # Delete these comments before writing your program
=======
        time.sleep(3)  # allow drone to stabilize

        sendmsg('flip f')  # forward flip

        time.sleep(3)  # stabilize after flip

        sendmsg('forward 100')
>>>>>>> Stashed changes

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')

except KeyboardInterrupt:
    try:
        sendmsg('emergency')
    except:
        pass

except Exception as e:
    print("Error occurred:", e)