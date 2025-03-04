# Coding: UTF-8
# Author: Sarthak2143
# Source Code: github.com/Sarthak2143/shin

import shin
import time
from colorama import Fore, Style                        
print("Shin Lang v0.2 | Author: Shinero")

try:
    while True:
        text = input(Fore.GREEN + 'shin' + Fore.RED  + ' >>> ' + Style.RESET_ALL)
        if text.strip() == "": continue
        result, error = shin.run('<stdin>', text)
        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))

except KeyboardInterrupt:
    print('\nExiting...')
    time.sleep(1)
