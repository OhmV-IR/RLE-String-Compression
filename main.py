# Get a string from the user to compress
inputString = input("Enter the string you want to compress: ")
# Initialize the output string variable
outputString = ""
# Initialize the lastLetter to the first character in the string
lastLetter = inputString[0]
# Initialize the counter variable
count = 0
# Loop over every character in the string, i is the current character
for i in inputString:
    # If the letter is still the same,
    if lastLetter == i:
        # Increment the counter by 1
        count += 1
    # If the letter is different,
    else:
        # Add the count of how many letters were the same and the letter along with a blank space(so that this can be continued) to the output string
        outputString += str(count) + lastLetter + " "
        count = 1
        lastLetter = i
# Add the count of the number of letters that were the same and the letter with no blank space(because this is the end of the output string) to the output string
outputString += str(count) + lastLetter
# Print the output string to the console
print(outputString)