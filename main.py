inputString = input("Enter the string you want to compress: ")
outputString = ""
lastLetter = inputString[0]
count = 0
for i in range(len(inputString)):
    if lastLetter == inputString[i]:
        count += 1 # increment letter count by 1
    else:
        outputString += str(count) + lastLetter + " "
        count = 1
        lastLetter = inputString[i]
outputString += str(count) + lastLetter
print(outputString)