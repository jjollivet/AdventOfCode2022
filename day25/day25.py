def to_dec(value):
    dec_value = 0
    for i in range(len(value)):
        x = value[i]
        exponent = len(value) - i - 1

        if x == '-':
            dec_value -= 5 ** exponent
        elif x == "=":
            dec_value -= 2 * 5 ** exponent
        else:
            dec_value += int(x) * 5 ** exponent

    return dec_value

def to_snafu(value):
    snafu = []
    oncemore = True
    # Run this loop once more than the condition of a quotient of 0
    while oncemore:
        if (value // 5) == 0:
            oncemore = False

        remainder = value % 5
        if remainder == 4:
            snafu.insert(0,'-')
            value += 5
            if not(oncemore):
                snafu.insert(0,'1')
        elif remainder == 3:
            snafu.insert(0,'=')
            value += 5
            if not(oncemore):
                snafu.insert(0,'1')
        else:
            snafu.insert(0,str(remainder))

        value = value // 5

    return ''.join(snafu)

#Import intput file
with open("input.txt") as my_file:
    data = my_file.read().split("\n")
data = list(filter(None, data))

total = 0

for num in data:
    total += to_dec(num)

print(f'Part 1 sum is {total}. Convert to SNAFU:{to_snafu(total)}')
