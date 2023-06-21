# initialize a list to hold the numbers
numbers = []

# initialize a variable to hold the total
total = 0

# initialize a variable to hold the count of numbers entered
count = 0

# loop until the user enters -1
while True:
    # ask the user to enter a number
    num = input("Enter a number (or -1 to stop): ")
    
    # check if the user wants to stop
    if num == "-1":
        break
    
    # convert the input to a float and add it to the list of numbers
    # chose a float rather an int to allow for decimals 
    num = float(num)
    numbers.append(num)
    
    # add the number to the total and increment the count
    total += num
    count += 1

# check if any numbers were entered
if count == 0:
    print("No numbers were entered.")
else:
    # calculate the average and print the result
    average = total / count
    print("The average of the", count, "numbers entered is:", average)