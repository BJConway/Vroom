#!/usr/bin/env python3

import sys
sys.dont_write_bytecode = 1

from app.parser.VroomArgParser import VroomArgParser
from app.registry.VroomRegistry import VroomRegistry
from app.helpers import print_banner


def main() -> None:

    print_banner()

    vreg = VroomRegistry()
    varg = VroomArgParser()

    if len(sys.argv) == 1:
        sys.exit(varg.parser.print_help())
    else:
        varg.run_handler(vreg)


if __name__ == '__main__':
    main()
