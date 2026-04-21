# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nKade Demaagd And Cohen Smith")
print("Program Name: Hoop Competition ")
print("Date: 4.20.2026 ")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff', 5)  


        # Commit Message: First Hoop - Stable
        # Don't Forget to take video of this portion of the comp
        # Make sure I put the video in out Repository
        # Comit Message: First Hoop Video in Repository
        # Write code below

        sendmsg('up 20')
        sendmsg('forward 260')
    



        # Commit Message: Second Hoop - Stable
        # SDK GO command
        # Don't Forget to take video of this portion of the comp
        # Make sure I put the video in out Repository
        # Comit Message: Second Hoop Video in Repository
        # Write code below





        # Commit Message: Third Hoop - Stable
        # SDK Curve command
        # Don't Forget to take video of this portion of the comp
        # Make sure I put the video in out Repository
        # Comit Message: Third Hoop Video in Repository
        # Write code below





        # Commit Message: Fourth Hoop - Stable
        # SDK GO command
        # Don't Forget to take video of this portion of the comp
        # Make sure I put the video in out Repository
        # Comit Message: Fourth Hoop Video in Repository
        # Write code below




        # Video of entire Hoop Competition
        # Commit Message: Video of entire Hoop Competition in Repository


        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
