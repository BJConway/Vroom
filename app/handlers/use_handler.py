from argparse import Namespace
from typing import List
from app.registry import VroomRegistry
import app.helpers as hlp
import sys
import shutil
import subprocess


def use_handler(args: Namespace, reg: VroomRegistry.VroomRegistry) -> None:

    shell, ip, port, type, listen, out = args.shell, args.ip, args.port, args.type, args.listen, args.out
    errors: List[str] = []

    if shell not in reg.get_shell_names():
        errors.append(f'Invalid shell type: {shell}')
    else:
        if not reg.is_valid_template(shell, int(type)):
            errors.append(f'Invalid subtype for shell {shell} : {type}')

    if not hlp.is_valid_ip(ip):
        errors.append(f'Invalid IP address : {ip}')

    if not hlp.is_valid_port(port):
        errors.append(f'Invalid port: {port}')

    if errors:
        for e in errors:
            hlp.report_stderr(e)
        sys.exit(1)

    shell = hlp.format_template(reg.get_subtype(shell, int(type)), ip, port)

    if out:
        try:
            with open(out, 'w') as f:
                f.write(shell)
                hlp.report_stdout(f'Writing to {out} ...')
        except PermissionError:
            hlp.report_stderr(f'Cannot write to "{out}" - permission denied', exit=True)
        except FileNotFoundError:
            hlp.report_stderr(f'Cannot write to "{out}" - invalid location or filename', exit=True)
        except IsADirectoryError:
            hlp.report_stderr(f'Cannot write to "{out}" - location is a directory', exit=True)
    else:
        hlp.report_stdout(shell)

    if listen:
        if nc := shutil.which('nc'):
            hlp.report_stdout('Initiating nc listener...')
            try:
                subprocess.run(args=[nc, '-lnvp', str(port)])
            except KeyboardInterrupt:
                hlp.report_stdout('Exiting vroom...')
                sys.exit(0)
        else:
            hlp.report_stderr('No nc binary found! Cannot start listener.')
