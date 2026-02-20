digits = [1,2,3,4,5]
s = ""
new = []
for i in range(len(digits)):
    s += str(digits[i])
s = int(s)
s += 1
s = str(s)
for i in range(len(s)):
    new.append(int(s[i]))

return new
