# Simple-Diffie-Hellman-Exchange
A simplified Diffie-Hellman key exchange algorithm using python sockets.
Small numbers and no modulo is used for simplicity.

The Diffie-Hellman key exchange is a method for two units in a computer system to agree on a secret key, despite all messages being intercepted.

It is based on the principle that:
(x^a)^b = (x^b)^a

Additionally, it relies on the Discrete Logarithm Problem; the principle that exponentiation is (relatively) easy to calculate. By 'easy', it would not take more than a few seconds for an average computer's processing power to compute. On the contrary, it is difficult (i.e. there is no efficient solution for the most powerful supercomputer to calculate) the exponent from base and power: if x^a = n, there is no efficient method for calculating a = log_x(n).

It is important to reiterate that this algorithm is simplified. Besides the use of larger exponents, computers also take the modulo of each calculated power by a very large prime number for added security as well as to reduce values to smaller ones.

Discrete Logarithm: https://en.wikipedia.org/wiki/Discrete_logarithm
Diffie-Hellman exchange: https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange
