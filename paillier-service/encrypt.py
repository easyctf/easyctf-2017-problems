#/usr/bin/env python

import SocketServer,threading,os,time
import signal


PORT = 8570

class incoming(SocketServer.BaseRequestHandler):
    def handle(self):
        atfork()
        req = self.request

        def recvline():
            buf = ""
            while not buf.endswith("\n"):
                buf += req.recv(1)
            return buf
        signal.alarm(120)

        try:
            p = 8144194198641127053467521063088973929365485175581336279930490759203400725623086153929294542350943040473375790841894343662879542882143670576484983482676929
            q = 9349990237178389195581522619084514015305492951423232071317276234453300521753669715890246992825146527366147991960266180184131002960074501683578205688324193
            n = p*q
            l = (p-1)*(q-1)
            g = n+1
            mu = 50461441817124067084598541006218828107720370909059246792962232658242869571003990015294541684702084151173329882441771747115542549562899610400402036968340066285127945127930744036805832623326255171902722383305695091973581469008587730106329093915495096858331002656658189454919392650001488548518482449865519307486
            #m = int(req.recv('Enter a message to encrypt: '))
            req.sendall('Enter a message to encrypt: \n')
            m = int(recvline())

            req.sendall('Enter r (int): \n')
            r = int(recvline())
            if m > 100000000000000000 or m < 0:
                print('Bad m. We only take m from 0 to 100000000000000000.')
                exit()
            if r > 100000000000000000 or r < 0:
                print('Bad r. We only take r from 0 to 100000000000000000.')
                exit()
            c = (pow(g,m,n**2)*pow(r,n,n**2))%(n**2)
            print 'c: '+str(c)
        except:
            pass

        req.sendall("Bye!\n")
        req.close()

class ReusableTCPServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
  pass

SocketServer.TCPServer.allow_reuse_address = True
server = ReusableTCPServer(("0.0.0.0", PORT), incoming)

print "Server listening on port %d" % PORT
server.serve_forever()
