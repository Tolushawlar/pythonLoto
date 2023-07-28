import random
# get the number of users to play
userInput = int(input("Enter How many players"))
# list to store money and user numbers
playerMoney = []
playerNumber = []
winningNumber = []
usernames = {}
userWinCount = {}
# generate the machine number
machineNo = []
for i in range(3):
    macNo = random.randint(0, 10)
    machineNo.append(macNo)


def lotteryFuction(players):
    # to display instructions
    print("####### WELCOME TO HIGHTSLOTO ########")
    print("%d Players Registered to Play" % (players))
    userReponse = int(
        input("To Start Game PRESS 1 to Read Instruction PRESS 2"))
    if userReponse == 1:

        # looping according to the users to create gameplay
        for i in range(0, players):
            # making uplayer enter their number and stake
            stake = input("Player %d Enter Stake Amount" % (i + 1))
            for j in range(3):
                playerNo = input(
                    "Player %d Enter your lucky number %d" % (i + 1, j + 1))
                playerNumber.append(int(playerNo))
            playerMoney.append(stake)

        # divide the user numbers
        def splitPlayerNumbers(numberList, chunkSize):
            if chunkSize <= 0:
                raise ValueError("Chunk size must be greater than 0")
            return [numberList[i:i + chunkSize] for i in range(0, len(numberList), chunkSize)]
        singleUsersNumber = splitPlayerNumbers(playerNumber, 3)
        for userNumber in range(len(singleUsersNumber)):
            username = f"user_{userNumber}"
            singleStake = singleUsersNumber[userNumber]
            usernames[username] = singleStake

        # check if stake number is in machine generated numbers
        def machineNoCheck(list1, list2):
            count = 0
            for item in list1:
                if item in list2:
                    count += 1
                    winningNumber.append(item)
            return count
        machineNoCheckResult = machineNoCheck(playerNumber, machineNo)

        # generate the count wins of each user
        for key, value in usernames.items():
            for i in range(len(usernames)):
                userWin = 0
                winUsername = f"win_{key}"
                for item in value:
                    if item in winningNumber:
                        userWin += 1
                userWinCount[winUsername] = userWin

        # displaying who wins
        userWinCountWinner = max(userWinCount.values())
        for key, value in userWinCount.items():
            if value == userWinCountWinner:
                print(str(key) + " wins, has " + str(value) + " correct numbers")

    elif userReponse == 2:
        print("This is a lottory game that any defined number of users can play Each User must enter their stake amount at the start\nafter then the user can enter three lucky numbers, which at the end the system will match to its own")
        lotteryFuction(players)


lotteryFuction(userInput)
