import sys
import serial
import signal
import SimpleHTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import SocketServer

PORT = 8000
httpd = None

def signal_handler(signal, frame):
    print "Shutting down server"
    print "Exiting program"
    if(httpd):
        httpd.close();
    sys.exit(0)

def readSerial(p):
    ser = serial.Serial(p, 9600, timeout=1);
    x = []
    while len(x) < 5:
        x = ser.readline() 
        x = x.strip()
        x = x.split(",")
    ser.close()
    d = {'temp':x[0], 'light':x[1], 'pressure':x[2]}
    print "Read: "+str(d)
    return d


class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print "Handling request for: "+self.path
        if self.path == "/" or self.path == "/index.html":
            try: 
                print "Attempting to load index.html"
                self.send_response(200)
                self.end_headers()
                f = open("./index.html", 'r')
                self.wfile.write(self.getRenderedFile(f.read()))
                f.close()
            except:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("index.html not defined in same directory as the server")
        else:
            try:
                self.send_response(200)
                self.end_headers()
                f = open("."+self.path, "r")
                self.wfile.write(f.read())
                f.close()
            except:
                self.send_response(404)
                self.end_headers()


    def getRenderedFile(self, inText):
        d = readSerial(self.serial_port)
        inText = inText.replace("{TEMP}", d['temp'])
        inText = inText.replace("{LIGHT}", d['light'])
        inText = inText.replace("{PRESSURE}", d['pressure'])
        return inText

def main():
    signal.signal(signal.SIGINT, signal_handler)
    handler = GetHandler
    handler.serial_port = '/dev/tty.usbmodem1411'
    httpd = SocketServer.TCPServer(("", PORT), handler)
    print "serving at port", PORT
    httpd.serve_forever()

if __name__ == '__main__':
    main()
