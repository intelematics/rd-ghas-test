#!/usr/bin/env python
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.asymmetric import ec, dsa, rsa
from random import random


#Crypto and Cryptodome have same API
if random():
    from Crypto.PublicKey import DSA
    from Crypto.PublicKey import RSA
else:
    from Cryptodome.PublicKey import DSA
    from Cryptodome.PublicKey import RSA

RSA_WEAK = 1024
RSA_OK = 2048
RSA_STRONG = 3072
BIG = 4096

#EC_WEAK = FakeWeakEllipticCurve()
EC_OK = ec.SECP224R1()
EC_STRONG = ec.SECP384R1()
EC_BIG = ec.SECT571R1()

dsa_gen_key = dsa.generate_private_key
ec_gen_key = ec.generate_private_key
rsa_gen_key = rsa.generate_private_key

default = backends.default_backend()

#Strong and OK keys.

dsa_gen_key(key_size=RSA_OK, backend=default)
dsa_gen_key(key_size=RSA_STRONG, backend=default)
dsa_gen_key(key_size=BIG, backend=default)
#ec_gen_key(curve=EC_OK, backend=default)
#ec_gen_key(curve=EC_STRONG, backend=default)
#ec_gen_key(curve=EC_BIG, backend=default)
rsa_gen_key(public_exponent=65537, key_size=RSA_OK, backend=default)
rsa_gen_key(public_exponent=65537, key_size=RSA_STRONG, backend=default)
rsa_gen_key(public_exponent=65537, key_size=BIG, backend=default)

DSA.generate(bits=RSA_OK)
DSA.generate(bits=RSA_STRONG)
RSA.generate(bits=RSA_OK)
RSA.generate(bits=RSA_STRONG)

dsa_gen_key(RSA_OK, backend=default)
dsa_gen_key(RSA_STRONG, backend=default)
dsa_gen_key(BIG, backend=default)
#ec_gen_key(EC_OK, backend=default)
#ec_gen_key(EC_STRONG, backend=default)
#ec_gen_key(EC_BIG, backend=default)
rsa_gen_key(65537, RSA_OK, backend=default)
rsa_gen_key(65537, RSA_STRONG, backend=default)
rsa_gen_key(65537, BIG, backend=default)

DSA.generate(RSA_OK)
DSA.generate(RSA_STRONG)
RSA.generate(RSA_OK)
RSA.generate(RSA_STRONG)


# Weak keys

dsa_gen_key(RSA_WEAK, backend=default)
#ec_gen_key(EC_WEAK, backend=default)
rsa_gen_key(65537, RSA_WEAK, backend=default)

dsa_gen_key(key_size=RSA_WEAK, backend=default)
#ec_gen_key(curve=EC_WEAK, backend=default)
rsa_gen_key(65537, key_size=RSA_WEAK, backend=default)

print(DSA.generate(RSA_WEAK))
print(RSA.generate(RSA_WEAK))

print('Done!')
