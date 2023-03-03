   

with open("input.txt", "r") as f:

    # total number of records
    n = int(f.readline().strip())

    # initialize
    allValid = True
    errorCodes = []

    # loop through each record
    for i in range(n):
        record = f.readline().strip().split()
        # check if record is valid
        if record[1] == "false":
            allValid = False
            errorCodes.append(record[2])

    if allValid:
        print("Yes")
    else:
        print("No")
        print(" ".join(errorCodes))
