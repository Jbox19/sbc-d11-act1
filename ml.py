                                    #*---Bubble Sort---*
def bs(letters):
    print(letters)
    l = len(letters)
    for i in range(l):
        for j in range(l-i-1):
            if letters[j] > letters[j+1]:
                letters[j], letters[j+1] = letters[j+1], letters[j]
                print(letters)

letters = ["Q", "S", "A", "M", "Z", "R"]
bs(letters)
