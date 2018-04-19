#!/usr/bin/python
import socket
import sys
 
if len(sys.argv) != 5:
    print "X-code HTTP Fuzzer v0.1" 
    print "Oleh Kurniawan. trainingxcode@gmail.com. xcode.or.id."
    print "Cara penggunaan : ./fuzzerhttp.py <ip target> <port> <karakter> <jumlah karakter> "
    sys.exit(1)
 
ipaddress = sys.argv[1]
port = int(sys.argv[2])
karakter = sys.argv[3]
paket = int(sys.argv[4])
buffer = (karakter) * (paket)
header1 = "GET / %s HTTP/1.1\r\nHost:(str(ipaddress))\r\n\r\n" % (buffer)
header2 = "POST / %s HTTP/1.1\r\nHost:(str(ipaddress))\r\n\r\n" % (buffer)
header3 = ( 'GET / HTTP/1.1\r\n' \
           'If-Modified-Since: , %s\r\n\r\n') %(buffer)
header4="GET / HTTP/1.1\r\n"
header4+="Host: " + buffer + "\r\n"
header4+="Content-Type: application/x-www-form-urlencoded\r\n"
header4+="User-Agent: Mozilla/5.0 (X11; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0.1\r\n"
header4+="Content-Length : 1048580\r\n\r\n"
#header bug pada service http lain dapat ditambah sendiri

try:
 print "  -----------------------"
 print "  X-code HTTP Fuzzer v0.1"
 print "  Oleh Kurniawan"
 print "  trainingxcode@gmail.com"
 print "  xcode.or.id"
 print "  -----------------------"
 print "" 
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((str(ipaddress),(port)))
 print "  Kirim paket"
 s.send(header1)
 s.close()

 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((str(ipaddress),(port)))
 print "  Kirim paket"
 s.send(header2)
 s.close()

 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((str(ipaddress),(port)))
 print "  Kirim paket"
 s.send(header3)
 s.close()

 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((str(ipaddress),(port)))
 print "Kirim paket"
 s.send(header4)
 s.close()

#fungsi untuk connect dan send dapat ditambah sendiri sesuai dengan header http yang ditambah
 
except:
  print "  Tidak dapat terkoneksi ke server web"