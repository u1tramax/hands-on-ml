from colorama import Fore, Style, init
import numpy as np

init(autoreset=True)

z = np.column_stack((
    np.arange(15, 6, -1),
    np.arange(1, 18, 2)
))

[print(
    Fore.GREEN + ' ' * i + '*' * j + Style.RESET_ALL
) for i, j in z]
[print(
    Fore.RED + ' ' * 13 + '||' + Style.RESET_ALL
) for _ in range(3)]
print(
    Fore.BLUE + ' ' * 11 + r'\======/' + Style.RESET_ALL
)   
print()
print(Fore.YELLOW + 'Merry Christmas & Happy New Year!')