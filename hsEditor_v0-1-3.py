value = input('highscore value to be edited to: ')

f = open('.highscore.txt', 'a+')
f.write(value)
f.close()

print('Your highscore has been edited successfully.')