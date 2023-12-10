words = ["SEND", "MORE"]
result = "MONEY"

all_words = words + [result]
rows = len(all_words)  # rows represents the number of input words plus 1 (result)
print(all_words)

char_mapping = {}
n = -1  # n represents the length of longest word in all_words
for word in all_words:
    n = max(n, len(word))


used = [0] * 10  # flag that tells which number is used


def dfs(row, col, val):
    if col == n:
        return val == 0  # base case
    elif row == rows:
        return val % 10 == 0 and dfs(0, col + 1, val // 10)
    else:
        word = all_words[row]
        if col >= len(word):
            return dfs(row + 1, col, val)
        c = word[~col]
        if c in char_mapping:
            if col and col + 1 == len(word) and char_mapping[c] == 0:
                return False  # check leading's 0
            elif row + 1 == rows:
                return dfs(row + 1, col, val - char_mapping[c])
            else:
                return dfs(row + 1, col, val + char_mapping[c])
        else:
            # blind search
            for digit, flag in enumerate(used):
                if not flag and (digit or col == 0 or col + 1 < len(word)):
                    char_mapping[c] = digit
                    used[digit] = 1  # flag that digit as used
                    if row + 1 == rows and dfs(row + 1, col, val - digit):
                        return True
                    if row + 1 < rows and dfs(row + 1, col, val + digit):
                        return True
                    used[digit] = 0  # flag that digit as unused
                    char_mapping.pop(c)


found = dfs(0, 0, 0)
if found:
    print("We got the answer", char_mapping)
else:
    print("There is no answer for this question!")
