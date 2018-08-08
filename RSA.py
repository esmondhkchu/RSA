import gmpy2

################
# Generate Keys#
################
import random
def gen_key(seed):
    """ generate all the keys needed
    """
    random.seed(seed)
#   x, y = random.randint(10**52,10**53), random.randint(10**52,10**52)
    x, y = random.randint(1,100), random.randint(1,100)
    p = int(gmpy2.next_prime(x))
    q = int(gmpy2.next_prime(y))
    n = p * q
    phi_n = (p-1)*(q-1)
    #picked 13 as our e
    e = 13
    d = int(gmpy2.invert(e, phi_n))

    return p, q, n, phi_n, e, d

#####################
# Turn words to nums#
# Turn nums to words#
#####################
def word2num(word):
    """ turn word to number for encryption

    argument (str): word

    returns: int
    """
    pw = [int(ord(i)) for i in word]
    return pw

def num2word(num):
    """ turn number to word

    argument (list): the list of encryted message number

    returns: str
    """
    wd = [chr(i) for i in num]
    return ''.join(wd)

#############
# Encryption#
#############
def RSA_encryption(n, e, msg):
    """ encrypt message based on the keys

    arguments: n(int), e(int), msg(str)

    return (list): a list of encrypted message
    """

    def RSA_encryption_single(n, e, m):
        #encrypt message
        enc_c = (m**e) % n

        return enc_c

    msg_list = word2num(msg)
    encry_msg = [RSA_encryption_single(n, e, i) for i in msg_list]

    return encry_msg

#decrypt
def RSA_decryption(n, d, enc_msg):
    """ decrypt message based on the keys

    arguments: n(int), d(int), msg(list)

    return (str): the decrypted message
    """
    def RSA_decryption_single(n, d, c):
        #decrypt message
        dec_m = (c**d) % n

        return dec_m

    decry_msg = [RSA_decryption_single(n, d, i) for i in enc_msg]
    return num2word(decry_msg)

##########
# Example#
##########
p, q, n, phi_n, e, d = gen_key(94523)

start = RSA_encryption(n, e, 'esmond')
print(start)

end = RSA_decryption(n, d, start)
print(end)
