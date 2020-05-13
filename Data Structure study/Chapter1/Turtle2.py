# This imports the turtle graphics module.
import turtle

# The main function is where the main code of the program is written.
def main():
    # This line reads a line of input from the user.
    filename = input("Please enter drawing filename: ")
    
    # Create a Turtle Graphics window to draw in.
    t = turtle.Turtle()
    # The screen is used at the end of the program.
    screen = t.getscreen()
    
    # The next line opens the file for "r" or reading. "w" would open it for
    # writing, and "a" would open the file to append it (i.e. add to the
    # end). In this program we are only interested in reading the file.
    file = open(filename, "r")
    
    
    # Here we have the half a loop to get things started. Reading our first
    # graphics command here lets us determind if the file is empty or not.
    command = file.readline().strip()
    
    # If the command is empty, then there are no more commands left in the file.
    while command != "":
        
        # Now we must read the rest of the record and then process it. Because
        # records are variable length, we'll use an if-elif to determine which
        # tytpe of record it is and then we'll read and process the record.
        
        if command == "goto":
            # Writing float(commandList[1]) makes a float object out of the
            # string found in commandList[1]. You can do similar conversion
            # between types for int objects.
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)
        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = file.readline().strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file: ", command)
    
    
        # This is still inside the while loop. We must (attempt to) read
        # the next command from the file. If the read succeeds, then command
        # will not be the empty string and the loop will be repeated. If
        # command is empty it is because there were no more commands in the
        # file and the while loop will terminate.
        command = file.readline().strip()
        
    #close the file
    file.close()
    
    # hide the turtle that we used to draw the picture.
    t.ht()
    
    # This causes the program to hold the turtle graphics window open
    # until the mouse is clicked.
    screen.exitonclick()
    print("Program Execution Completed")
    
# This code calls the main function to get everything started.
if __name__ == "__main__":
    main()
            