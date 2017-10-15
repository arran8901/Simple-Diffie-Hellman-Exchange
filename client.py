# Client Socket - to be run while server is listening

from socket import *
from random import *

c = socket()
c.connect((gethostname(), 55555))
print "Connect to server"

# Base for the exponentiation, defined by the server.
BASE = int(c.recv(1024))
print "Base: " + str(BASE)

# Choosing own exponent from 1 - 10. Note that in real systems,
# this should be large so as to be difficult to crack.
EXPONENT = randint(1, 10)
print "Exponent: " + str(EXPONENT)

# Send calculated power, and receive server's calculated power
power = BASE ** EXPONENT
SERVERVALUE = int(c.recv(1024))
c.send(str(power))
print "Sending: " + str(BASE) + "^" + str(EXPONENT) + " = " + str(power)
print "Received: " + str(SERVERVALUE)

# Obtain final key value by raising server's power to own exponent
print "Key value: " + str(SERVERVALUE) + "^" + str(EXPONENT) + " = " + str(c.recv(1024))
c.send(str(SERVERVALUE ** EXPONENT))

c.close