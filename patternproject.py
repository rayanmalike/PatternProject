def is_positive_integer(input_str):
    try:
        num = int(input_str)
        return num > 0
    except ValueError:
        return False #This ensures the numbers that are being inputted are positive

def get_valid_dimension(prompt): 
    while True:
        dimension = input(prompt)
        if is_positive_integer(dimension):
            return int(dimension)
        else:
            print("Invalid input. Please enter a valid positive integer.") #This block stops the code if integer in invalid

def print_rectangle(height, width):
    for i in range(height):
        for j in range(width):
            print('*', end = '')
        print() #for the rectangle, you input the height and width and add an end function in order for the asterisks to go sideways
def hollow_rectangle(height, width):
    for i in range(height):
        for j in range (width):
            if i == 0 or j == 0 or i == height - 1 or j == width - 1:
                print('*', end = '')
            else:
                print(' ', end = '')
        print()

def print_pyramid(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1)) #For a pyramid, you need to add and subtract numbers in order for the asterisks to gradually go up 

def print_diamond(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
    for i in range(height - 2, -1, -1):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

while True:
    print("Welcome to Pattern Print Shop. Please select from the following menu:")
    print("A- To print a rectangle")
    print("B- To print Pyramid pattern")
    print("C- To print Diamond Pattern")
    print("Q- To quit") #If the functions on top are true, code will ask user to select which shape they want to pattern

    choice = input("Enter your choice: ").upper()

    if choice == 'A':#If user chooses choice A, they have to enter a certain number for the rectangle to match that number
        print('Enter which dimension of Rectangle: ')
        print('A - Solid Rectangle')
        print('B - Hollow Rectangle')
        print('C - Back to Main Menu')
        choice = input('Enter a choice: ')  
        if choice == 'A':
            height = get_valid_dimension("Enter the height of the rectangle: ")
            width = get_valid_dimension("Enter the width of the rectangle: ")
            print_rectangle(height, width)
            print('Thank you for your business')
        elif choice == 'B': 
            height = get_valid_dimension("Enter the height of the rectangle: ")
            width = get_valid_dimension("Enter the width of the rectangle: ")
            hollow_rectangle(height, width)
            print('Thank you for your business')
        elif choice == 'C':
            break
            
            
    elif choice == 'B': #Same here, if user picks B, they must pick a number in order for the shape to match the number.
        height = get_valid_dimension("Enter the height of the pyramid: ")
        print_pyramid(height)
        print('Thank you for your business')
    elif choice == 'C': #Same with C here
        height = get_valid_dimension("Enter the height of the diamond: ")
        if height % 2 == 0: 
            print("Diamond height must be an odd number.") #Stops the code from drawing a shape if the number input is an even number.
        else:
            print_diamond(height)
            print('Thank you for your business')
    elif choice == 'Q': #this breaks and/or puts the code in a loop until user inputs a valid number
        break
    else:
        print("Invalid choice. Please select a valid option.")


