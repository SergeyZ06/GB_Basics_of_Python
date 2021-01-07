print(f'Hello World!')

a = 5
b = 6
print(f'There you can see a = {a} and b = {b}, so a + b = {a + b}')

a = input(f'Now can I ask your name please? ')
print(f'Look! I use the same variable "a" to contain your name, a = "{a}", great! Isnt it?')

a, b = b, a
print(f'Now I wanna interchange values of my variables "a" and "b", so a = "{a}" and b = "{b}", cool!')

b = input(f'Say something please: ')
print(f'As well its possible for variable "b" to contain something whatever you said before, look, b = "{b}"')

a = 5.45
print(f'I also can use my variable "a" to save some float values, for instance a = "{a}"')
print(f'Now its a float type, I can multiply it: a * 2 = {a * 2}')
a = str(a)
print(f'Currently "a" has became str type because of function str(), very useful! We are able to see it: {a}')

print(f'Thats all for now. Thank you for your attention!')
