import minecraft as M

active = False
on = True
output = ""

def materials():
    print(M.Back.BLACK + "Wood: " + str(M.count_wood))
    print(M.Back.BLACK + "Stone: " + str(M.count_stone))

def ActualizeView():
    M.ClearConsole()
    M.DrawWorldEmpty()
    M.DrawWorld()
    M.DrawPlayer()
    M.endWorld()
    materials()
    print("Output: ")
    print(outputs)

def Interaction():

    entry = input("Command>> ")
    comms= entry.split(" ")

    global active
    global on
    global outputs
    
    for com in comms:
        if com == "top" or com == "down" or com == "left" or com == "right":
            output = M.MovePlayer(com)
            outputs = outputs + ("    *" + output + "\n")

        elif com == "extract":
            output = "Extract block"
            M.CollectBlocks()
            outputs = outputs + ("    *" + output + "\n")

        elif com == "destroy":
            output = "Destroy block"
            M.DestroyBlocks()
            outputs = outputs + ("    *" + output + "\n")
        elif com == "materials":
            materials()
        elif com == "exit":
            output = "Thanks for playing!"
            outputs = outputs + ("    " + output + "\n")
            active = False
            on = False
        elif com == "help":
            print("move: Moves the player")
            print("break: Breaks a block")
            print("place: Places a block")
            print("materials: Shows the materials")
            print("exit: Exits the game")
            print("help: Shows this message")
        elif com == "init":
            active = True
        else:
            output = "Unknown command" + com
            outputs = outputs + ("    *" + output + "\n")

M.ClearConsole()
while on:
    if active:
        ActualizeView()
    outputs = ""
    Interaction()