# RSA Cryptosystem
A small program thats simulates the RSA Cryptosystem.

# The RSA Cryptosystem
The RSA is a public-key cryptosystem invented by Ron Rivest, Adi Shamir and Leonard Adleman and is heavily based on the characteristics of prime numbers. The RSA consists of a sets of public keys and private keys, which the users use the public keys to encrypt messages and decrypt message with the private keys. By their names, the public keys are supposed to be public and the private keys should be kept secret by the end-users. For more history, feel free to check out the [wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) page.

# My Curiosity on RSA
I heard RSA the first time in a Number Theory course offered by the Math Department, UC Davis. That was an introductory upper division number theory course with topics about prime numbers, congruences, Fermat's little theorem, Euler-Phi function, etc; and all of these are the main components of RSA.

# The Steps
(I am not a mathematician nor a math graduate student; I personally find the RSA interesting and would like to play around it with Python. Please forgive me for any conceptual mistakes or unclearness and missing of detail explanation for some steps; to be gentle to my computer, I also set all the keys to be relatively small values to achieve a demonstration purpose only which is not secure to use.)
## Key Generation
Based on prime factorization, every integer can be decomposed into products of prime numbers and when we multiply two large enough prime numbers, anyone would be almost impossible to find out which two prime numbers are chosen based on their product. <br/>
In RSA, we first need to pick two large enough prime numbers $p$ and $q$ and find out $n=p\cdot q$. Now with $n$, we need to find out the Euler's totient function $\phi(n)$, which is the numbers of elements that have a multiplicative inverse in a set of modulo integers. Since, $p$ and $q$ are prime numbers, so $\phi(n)=\phi(p\cdot q)=\phi(p)\cdot\phi(q)=(p-1)(q-1)$. The $\phi(n)$ is important for us to compute our private key to decrypt message, so as mentioned, the difficulty of factorizing our n to know our $p$ and $q$, our private key is therefore safe. I will let mathematicians to explain the theory behind, let's jump to key generation.
* p - a random large prime number.
* q - a random large prime number.
* $n=p\cdot q$
* $\phi(n)=(p-1)(q-1)$
* e, is one of our two public keys. Pick any odd, prime numbers between 3 and $\phi(n)$.
* with e, we need to compute private key d to decrypt message, d is given by: <br/> $e\cdot d=1\ mod\ \phi(n)$

This is the code to generate our keys.
```python
import random
def gen_key(seed):
    """ generate all the keys needed
    """
    random.seed(seed)
#   x, y = random.randint(10**52,10**52), random.randint(10**52,10**52)
    x, y = random.randint(1,100), random.randint(1,100)
    p = int(gmpy2.next_prime(x))
    q = int(gmpy2.next_prime(y))
    n = p * q
    phi_n = (p-1)*(q-1)
    #picked 13 as our e
    e = 13
    d = int(gmpy2.invert(e, phi_n))

    return p, q, n, phi_n, e, d
```
I originally put our random numbers to be $10^{52}$ large, but later I found that my computer isn't efficient enough to decrypt the message with such big numbers, and this is just for fun, so let's make it simple. I also fixed my $e$ as 13 here.

We need to transform our message(str) into integer(int) and we will do an opposite action later to decrypt messages.
```python
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
```

Now, we have a message $m$ to encrypt. We will use our two public keys $n$ and $e$ to do the work. The encryption formula is given by: <br/>
$c=m^e mod\ n$

```python
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
```

So with an encrypted message, we need to use our private key $d$ for decryption. The decryption formula is given by: <br/>
$m=c^d mod\ n$

```python
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
```

Now we are done with the whole process. <br/>
Here is a summary of the process:
* $p$ (private)
* $q$ (private)
* $n=p\cdot q$ (public, don't public $p$ and $q$)
* $\phi(n)=(p-1)(q-1)$ (private)
* $e$: random odd, prime number in $[3,\phi(n))$ (public)
* $d$: $e\cdot d=1mod\ \phi(n)$ (private)
* Encryption: $c=m^e\ mod\ n$
* Decryption: $m=c^d\ mod\ n$

## Example
We generate all our keys with seed 12345. <br/>
```python
p, q, n, phi_n, e, d = gen_key(12345)
```

The values we got are: <br/>
* $p=59$
* $q=97$
* $n=5723$
* $\phi(n)=5568$
* $e=13$
* $d=1285$

Then we try to encrypt the message 'esmond'.
```python
start = RSA_encryption(n, e, 'esmond')
print(start)
```
The encrypted message we got is [2227, 5521, 555, 3418, 4033, 2262]. <br/>
Now let's decrypt it.
```python
end = RSA_decryption(n, d, start)
print(end)
```
Here we got 'esmond' again.
