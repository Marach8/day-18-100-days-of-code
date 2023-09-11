print('\033[32mMY FIRST GUESSING GAME\033[0m')
print()

x = 0 
y = 5600
while True:
  print()
  ask = int(input('Guess the secret number: '))
  if 0 < ask < y:
    print()
    print('\033[31mYour guess is too low! try again.\033[0m')
    x += 1
    continue
  elif ask > y:
    print()
    print('\033[31mYour guess is too high! try again.\033[0m')
    x += 1
    continue
  elif ask < 0:
    exit()
  elif ask == y:
    print()
    print('\033[32mYou got it correct! Welldone.\033[0m')
    break
print()
print(f'You got the answer correct after {x+1} attempts!!')