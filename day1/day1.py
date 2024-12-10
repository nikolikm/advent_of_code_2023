sum = 0
words = {"one": "1", "two": "2", "three": "3", "four": "4",
         "five": "5", "six": "6", "seven": "7", "eight" : "8",
         "nine": "9"}

for l in open("./day1.txt", "r"):
    best_first_index = len(l) 
    best_last_index = -1
    number = "  "

    for word, num in words.items():
        # Find words
        index = l.find(word)
        if (-1 < index < best_first_index): 
            best_first_index = index
            number = num + number[1]

        index = l.rfind(word)
        if (-1 < index > best_last_index): 
            best_last_index = index
            number = number[0] + num

        index = l.find(num)
        if (-1 < index < best_first_index): 
            best_first_index = index
            number = num + number[1]

        index = l.rfind(num)
        if (-1 < index > best_last_index): 
            best_last_index = index
            number = number[0] + num

    sum += int(number)
print(sum)





