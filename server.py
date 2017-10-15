# Server Socket - to be run first

from socket import *
from random import *

# Base for the exponentiation, which must be the same for both devices
BASE = 2

s = socket()
s.bind((gethostname(), 55555))
s.listen(1024)
c, addr = s.accept()
print "Client connected"

# Base is sent to client. It does not matter if this is intercepted.
print "Base: " + str(BASE)
c.send(str(BASE))

# Choosing own exponent from 1 - 10. Note that in real systems,
# this should be large so as to be difficult to crack.
EXPONENT = randint(1, 10)
print "Exponent: " + str(EXPONENT)

# Send calculated power, and receive client's calculated power
power = BASE ** EXPONENT
c.send(str(power))
CLIENTVALUE = int(c.recv(1024))
print "Sending: " + str(BASE) + "^" + str(EXPONENT) + " = " + str(power)
print "Received: " + str(CLIENTVALUE)

# Obtain final key value by raising client's power to own exponent
c.send(str(CLIENTVALUE ** EXPONENT))
print "Key value: " + str(CLIENTVALUE) + "^" + str(EXPONENT) + " = " + str(c.recv(1024))

c.close();