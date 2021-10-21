import app.helpers as hlp

from argparse import Namespace
from app.registry import VroomRegistry


def list_handler(args: Namespace, reg: VroomRegistry) -> None:

    shell = args.type

    if not shell:
        shell_names = reg.get_shell_names()
        numbered_shell_names = [f'[{i}]  {s}' for i, s in enumerate(shell_names)]
        count = len(shell_names)
        hlp.report_stdout(f'{count} available shell {hlp.pluralise("type", count)} :', underline=True)
        hlp.print_list(numbered_shell_names)
        return

    try:
        templates = reg.get_shell_templates(shell)
    except ValueError:
        hlp.report_stderr(f'Unrecognised shell type "{shell}"', exit=True)
    else:
        count = len(templates)
        numbered_templates = [f'[{i}]  {s}' for i, s in enumerate(templates)]
        hlp.report_stdout(f'{count} available {hlp.pluralise("template", count)} for {shell} :', underline=True)
        hlp.print_list(numbered_templates)
