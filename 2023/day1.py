def convWords2Digits(lines: [str]):
    digitWords = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ret = []
    for line in lines:
        i = 0
        temp = ""
        while i < len(line):
            if line[i].isnumeric():
                temp += line[i]
                break
            found = False
            for j in range(len(digitWords)):
                if line.startswith(digitWords[j], i):
                    temp += str(j)
                    found = True
            if found:
                break
            i += 1

        i = len(line) - 1
        while i > -1:
            if line[i].isnumeric():
                temp += line[i]
                break
            found = False
            for j in range(len(digitWords)):
                if line.startswith(digitWords[j], i):
                    temp += str(j)
                    found = True
            if found:
                break
            i -= 1
        ret.append(float(temp))

    return ret




f = open("input.txt")
text = f.read()
lines = text.splitlines()

digits = [[c for c in line if c.isdigit()] for line in lines]
calib = [float(c[0] + c[-1]) for c in digits]
print(sum(calib))

newLines = convWords2Digits(lines)
print(sum(newLines))


print(lines[-1], digits[-1], newLines[-1])