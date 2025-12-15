# Index value pairs vs dictionaries
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j']

print("INDEX | KEY | VALUE")
for i, value in zip(range(len(x)), zip(x, y)):
    # i = index
    # value = value in index
    print(i, value)

print('=' * 11)

dict_tst = {
    ['name']: ['Goofy', 'Faba', 'Naruto', 'Rock', 'Obito'],
    'age': [18, 19, 22, 15, 32]
}

for i, value in zip(dict_tst['name'], dict_tst['age'], ):
    # i  = key
    # value = value in key 
    print(i, value)