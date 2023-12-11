list_a = [['','','','',''],
          ['','','','',''],
          ['','','','',''],
          ['','','','',''],
          ['','','','','']]

def printBoard(list_val):
    print("--------------------")
    for row in range(len(list_val)):
        print(list_val[row])

def task1(list_val):
    for i in range(len(list_val)):
        for j in range(len(list_val[i])):
            list_val[i][j] = j
    return list_val

def task2(list_val):
    for i in range(len(list_val)):
        for j in range(len(list_val[i])):
            list_val[i][j] = i
    return list_val

def task3(list_val):
    val = "X"
    for i in range(len(list_val)):
        for j in range(len(list_val[i])):
            if val == "X":
                list_val[i][j] = val
                val = "O"
            else:
                list_val[i][j] = val
                val = "X"
    return list_val

def task4(list_val):
    count = 1
    for i in range(len(list_val)):
        for j in range(len(list_val[i])):
            list_val[i][j] = count
            count += 1
    return list_val

def task5(list_val):
    count = 1
    for i in range(len(list_val)):
        for j in range(len(list_val[i])):
            list_val[i][len(list_val[i])-1-j] = count
            count += 1
    return list_val

def task6(list_val):
    count = 1
    for i in range(len(list_val)):
        for j in range(len(list_val[i])):
            list_val[len(list_val)-1-i][j] = count
            count += 1
    return list_val


printBoard(task1(list_a))
printBoard(task2(list_a))
printBoard(task3(list_a))
printBoard(task4(list_a))
printBoard(task5(list_a))
printBoard(task6(list_a))

