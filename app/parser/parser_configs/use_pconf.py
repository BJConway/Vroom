from app.handlers.use_handler import use_handler

conf = {
    "name": "use",
    "args": {
        "shell": {
            "help": "shell type (run \"vroom list\" for a list of available shell types)"
        },
        "ip": {
            "type": str,
            "help": "valid IPv4 address"
        },
        "-p": {
            "dest": "port",
            "type": int,
            "help": "valid port (1-65535, , defaults to 4242)",
            "default": 4242,
        },
        "-t": {
            "dest": "type",
            "type": int,
            "help": "valid shell template (run \"vroom list -t TYPE\" for a list of available templates for a shell type)",
            "default": 0
        },
        "-o": {
            "dest": "out",
            "help": "location to write shell to file",
        },
        "-l": {
            "dest": "listen",
            "help": "Initiate nc listener",
            "action": "store_true"
        }
    },
    "handler": use_handler
}