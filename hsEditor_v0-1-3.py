import os, time

def clear(): os.system('cls') if os.name == 'nt' else os.system('clear')

def qwerty():
    global value
    value = input('Select actions:\n1. Clear all scores\n2. Edit highscore value\n3. clean up scores\n4. Exit script\n\n>> ')
    return value

while True:
    time.sleep(1)
    qwerty()
    if value == '1':
        clear()
        time.sleep(1)
        os.remove('.highscore.txt')
        print('Removing local scores...')
        time.sleep(3)
        print('Your local scores have been cleared successfully.\n--End of session, please wait--')
        time.sleep(5)
        clear()
    elif value == '2':
        clear()
        time.sleep(1)
        ed = input('Enter highscore to be appended.\n\n>> ')
        clear()
        print('Loading file...')
        f = open('.highscore.txt', 'a+')
        f.write(f'{ed}\n')
        f.close()
        time.sleep(3)
        print('Your local highscore has been edited successfully.\n--End of session, please wait--')
        time.sleep(5)
        clear()
    elif value == '3':
        clear()
        time.sleep(1)
        print('Cleaning up zeros...')
        with open('.highscore.txt', 'r+') as fb:
            lines = fb.readlines()
            fb.seek(0)
            fb.truncate()
            for i in lines:
                if i.strip('\n') != "0": fb.write(i)
        time.sleep(3)
        print('Your scores have been cleaned up successfully.\n--End of session, please wait--')
        time.sleep(5)
        clear()
    elif value == '4':
        clear()
        print('Script will exit soon...')
        time.sleep(3)
        exit()
    else: print('Invalid action. Please try again and enter a correct action. (1/2/3)')
