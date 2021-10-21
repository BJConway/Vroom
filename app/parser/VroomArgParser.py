import argparse
import importlib
import os
import pkgutil

from types import ModuleType
from typing import Any, Dict, List

from app.registry.VroomRegistry import VroomRegistry


class VroomArgParser():

    modules_path = [os.path.join(os.path.dirname(__file__), 'parser_configs')]

    def __init__(self):
        self.parse_modules = self.load_parser_modules()
        self.parser = self.init_argparser()
        self.args = self.parser.parse_args()

    def load_parser_modules(self) -> List[ModuleType]:
        mods = pkgutil.iter_modules(self.modules_path)
        return [importlib.import_module(f'app.parser.parser_configs.{m.name}') for m in mods]

    def run_handler(self, reg: VroomRegistry):
        self.args.handler(self.args, reg)

    def add_arguments(self, parser: argparse.ArgumentParser, arg_conf: Dict[str, Dict[str, Any]]) -> None:
        for name, conf in arg_conf.items():
            parser.add_argument(name, **conf)

    def add_subparser(self, subparsers: argparse._SubParsersAction, p_conf: Dict[str, Any]) -> None:
        p = subparsers.add_parser(p_conf['name'])
        self.add_arguments(p, p_conf['args'])
        p.set_defaults(handler=p_conf['handler'])

    def init_argparser(self) -> argparse.ArgumentParser:

        main_parser = argparse.ArgumentParser()
        subparsers = main_parser.add_subparsers()

        for module in self.parse_modules:
            self.add_subparser(subparsers, module.conf)

        return main_parser
