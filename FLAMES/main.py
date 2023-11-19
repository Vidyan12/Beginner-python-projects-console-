# Define a function to eliminate common characters between two lists
def eliminateCommonChars(listOne, listTwo):
    # Iterate through elements in the first list
    for i in range(len(listOne)):
        # Iterate through elements in the second list
        for j in range(len(listTwo)):
            # Check if the current elements in both lists are the same
            if listOne[i] == listTwo[j]:
                # Store the common character
                c = listOne[i]
                # Remove the common character from both lists
                listOne.remove(c)
                listTwo.remove(c)
                # Create a new list combining the modified lists with a '*' separator
                listThree = listOne + ["*"] + listTwo
                # Return the new list and True to indicate removal occurred
                return [listThree, True]

    # If no common characters were found, create a new list without modifications and return False
    listThree = listOne + ["*"] + listTwo
    return [listThree, False]

# Driver code
if __name__ == "__main__":
    # Get input for the first player's name, convert to lowercase, and create a list of characters
    playerOne = input(" Name of the boy: ")
    playerOne = playerOne.lower()
    playerOne.replace(" ", "")  # This line has no effect, as it does not modify 'playerOne'
    playerOneList = list(playerOne)

    # Get input for the second player's name, convert to lowercase, and create a list of characters
    playerTwo = input(" Name of the girl : ")
    playerTwo = playerTwo.lower()
    playerTwo.replace(" ", "")  # This line has no effect, as it does not modify 'playerTwo'
    playerTwoList = list(playerTwo)

    # Initialize a variable to control the while loop
    proceed = True

    # Continue eliminating common characters until there are none left
    while proceed:
        # Call the eliminateCommonChars function and store the result
        retList = eliminateCommonChars(playerOneList, playerTwoList)
        conList = retList[0]
        proceed = retList[1]
        starIndex = conList.index("*")

        # Update playerOneList and playerTwoList based on the modified list
        playerOneList = conList[: starIndex]
        playerTwoList = conList[starIndex + 1:]

    # Calculate the total count of characters in both player lists
    theCount = len(playerOneList) + len(playerTwoList)

    # Define a list of FLAMES acronym
    res = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]

    # Continue reducing the list until only one element is left
    while len(res) > 1:
        splitIndex = (theCount % len(res) - 1)
        if splitIndex >= 0:
            right = res[splitIndex + 1:]
            left = res[: splitIndex]
            res = right + left
        else:
            # Remove the last element if splitIndex is negative
            res = res[: len(res) - 1]

    # Print the final relationship status
    print("Relationship Status :", res[0])



