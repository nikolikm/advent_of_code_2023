class Token:
    def __init__(self):
        self.string = ""
        self.index = 0
        self.summed = False
        self.adj_nums = []

last_symbols = []
last_numbers = []
sum = 0
ratio_sum = 0

for line in open("day3.txt", "r"):
    symbols: list[Token] = []
    numbers: list[Token] = []

    # Scan through the current line and add tokens
    token = Token()
    curr_type = -1      # 0 = ., 1 = number, 2 = symbol

    # Lazy workaround - pad to the line
    line += "."

    for i in range(0, len(line)):
        need_push = (curr_type != -1) and (
            (line[i] == "." and curr_type != 0) or
            (line[i].isnumeric() and curr_type != 1) or
            (not line[i].isalnum() and curr_type != 2))

        # Check if a token needs to be pushed
        if (need_push):
            if (curr_type == 1):
                numbers.append(token)
            elif (curr_type == 2):
                symbols.append(token)
            token = Token()

        # Check if the index should be initialized
        if (curr_type == -1 or need_push):
            token.index = i

        # Add to the current token
        token.string += line[i]
        
        # Set the type correctly
        if (line[i] == "."): curr_type = 0
        elif (line[i].isnumeric()): curr_type = 1
        else: curr_type = 2

    # Lazy workaround 2: remove blank extra items
    if (numbers[len(numbers)-1].string == "\n"): numbers.pop()
    if (symbols[len(symbols)-1].string == "\n"): symbols.pop()
    
    # Add numbers from this line
    for number in numbers: # Horizontal & top adjacencies
        for symbol in (symbols + last_symbols):
            if (number.index - 1 <= symbol.index <= number.index + len(number.string)):
                symbol.adj_nums.append(int(number.string))
                if (not number.summed):
                    sum += int(number.string)
                    number.summed = True

    # Add remaining numbers from the prev. line that may now be summed
    for number in last_numbers: # Bottom adjacencies
        for symbol in symbols:
            if (number.index - 1 <= symbol.index <= number.index + len(number.string)):
                symbol.adj_nums.append(int(number.string))
                if (not number.summed):
                    sum += int(number.string)
                    number.summed = True

    # Only the last set of gear ratios has been finalized now
    for symbol in last_symbols:
        if (symbol.string == "*" and len(symbol.adj_nums) == 2):
            ratio_sum += symbol.adj_nums[0] * symbol.adj_nums[1]


    # Update the last lists for the next run
    last_symbols = symbols
    last_numbers = numbers

# Need to sum up the last finalized set of gear ratios as well
for symbol in (last_symbols):
     if (symbol.string == "*" and len(symbol.adj_nums) == 2):
        ratio_sum += symbol.adj_nums[0] * symbol.adj_nums[1]

print(sum)
print(ratio_sum)