S = 'W'
P = 'python'

# ord() returns the unicode of any char
print(ord('O'))

# You can also do math - e.g. ord() + int
print(f"{ord(S) + 10}")

print(f"Unicode a + Unicode b = {ord('a') + ord('b')}")

# Looping through a string to return each binary digits
def main():
    global P
    stk = []
    for i in P:
        if i:
            stk.append(ord(i))
        if i == 'n':
            print(stk)

if __name__ == '__main__':
    main()
