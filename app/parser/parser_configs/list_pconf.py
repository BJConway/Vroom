from app.handlers.list_handler import list_handler

conf = {
    "name": "list",
    "args": {
        "-t": {
            "dest": "type",
            "help": 'shell type (run "vroom list" for a list of available shell types)',
        }
    },
    "handler": list_handler
}
