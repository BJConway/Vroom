import ipaddress
import sys
from typing import List

BANNER  = \
''' _    ______  ____  ____  __  ___
| |  / / __ \/ __ \/ __ \/  |/  /
| | / / /_/ / / / / / / / /|_/ / 
| |/ / _, _/ /_/ / /_/ / /  / /  
|___/_/ |_|\____/\____/_/  /_/

'''


def format_template(template: str, ip: str, port: int) -> str:
    return template.replace('%IP%', ip).replace('%PORT%', str(port))


def print_banner(main: str = '31m', detail: str = '37m') -> None:
    for i, line in enumerate(BANNER.splitlines()):
        print(f'\033[{detail if i in [2, 3] else main}{line}\033[0m')


def report_stderr(m: str, exit: bool = False) -> None:
    print(f"[!]  {m}", file=sys.stderr)
    if exit:
        sys.exit(1)


def report_stdout(m: str, underline: bool = False):
    report = f"[+]  {m}"
    if underline:
        report += f'\n{"-" * len(report)}'
    print(report)


def pluralise(m: str, c: int) -> str:
    return f'{m}{"s" if c != 1 else ""}'


def print_list(lst: List[str], prefix: str = '') -> None:
    if prefix:
        lst = [f'{prefix}{m}' for m in lst]
    print(*lst, sep='\n')


def is_valid_port(port: int) -> bool:
    return 0 < port <= 65535


def is_valid_ip(ip: str) -> bool:
    try:
        ipaddress.IPv4Network(ip)
        return True
    except ValueError:
        return False
