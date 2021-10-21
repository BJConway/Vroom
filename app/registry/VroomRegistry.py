import importlib
import os
import pkgutil

import app.helpers as hlp

from types import ModuleType
from typing import Dict, List, Union


class VroomRegistry():

    conf_dir_paths = [os.path.join(os.path.dirname(__file__), 'conf')]
    conf_prefix = 'conf_'

    def __init__(self, ):
        self.modules = self.init_module_list()

    def init_module_list(self) -> Dict[str, ModuleType]:

        module_handles = [mh for mh in pkgutil.iter_modules(self.conf_dir_paths) if mh.name.startswith(self.conf_prefix)]
        modules: Dict[str, ModuleType] = dict()

        if not len(module_handles):
            hlp.report_stderr(f'No configuration files found at {"".join(self.conf_dir_paths)}', exit=True)

        for mh in module_handles:

            module = importlib.import_module(f'app.registry.conf.{mh.name}')

            try:
                conf = module.conf
            except AttributeError:
                hlp.report_stderr(f'Skipping misconfigured module {mh.name} (missing conf attribute)')
                continue

            if conf_errors := self.get_conf_errors(conf):
                hlp.report_stderr(f'Skipping misconfigured config in module {mh.name} ({", ".join(conf_errors)})')
                continue

            shell_name: str = conf['name']

            if shell_name not in modules:
                modules[shell_name] = conf
            else:
                hlp.report_stderr(f'Skipping duplicate shell name "{shell_name}" found in module "{mh.name}".')

        return modules

    def get_conf_errors(self, conf: Dict[str, Union[str, List[str]]]) -> List[str]:

        errors: List[str] = []

        if ('name' not in conf):
            errors.append('missing "name" key')
        else:
            if not isinstance(conf['name'], str):
                errors.append('"name" not a string')

        if ('templates' not in conf):
            errors.append('missing "templates" key')
        else:
            tmp = conf['templates']
            if not isinstance(tmp, list):
                errors.append('"templates" is not a list')
            else:
                if not len(tmp):
                    errors.append('"templates" has no members')
                else:
                    if not all([isinstance(t, str) for t in tmp]):
                        errors.append('"templates" has invalid members')

        return errors

    def get_shell_templates(self, shell_name: str) -> List[str]:
        if shell_name not in self.get_shell_names():
            raise ValueError
        return self.modules[shell_name]["templates"]

    def get_shell_names(self) -> List[str]:
        return list(self.modules.keys())

    def get_subtype(self, shell_name: str, subtype_index: int) -> str:
        if not self.is_valid_template(shell_name, subtype_index):
            raise ValueError
        return self.get_shell_templates(shell_name)[subtype_index]

    def is_valid_template(self, shell_name: str, subtype_index: int) -> bool:
        return 0 <= subtype_index < len(self.get_shell_templates(shell_name))
