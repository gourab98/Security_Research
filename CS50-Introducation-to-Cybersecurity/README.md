[Class Website](https://cs50.harvard.edu/cybersecurity/2023/)

# Five topics:

## 0. Securing Accounts

   -> Use at least an 8-character password(Alphabets, Numbers, Special Characters), which decreases the (6,095,689,385,410,816)possibility of being compromised.

   -> It is not a good idea to change passwords periodically.

   -> Limit your wrong attempts.

   -> Two Factor Authentication (2FA) (Knowledge, Possession, Inherence).

   -> Use Password Manager.

   -> Use Single Sign On.

## 1. Securing Data

   -> Hashing (Password -> Hash) input→ f(input)→ output

   -> Dictionary Attack, Brute-Force Attack, Rainbow Tables Attack, Salting.     

   -> One-Way Hash Function / Cryptographic Hash Function (Arbitrary Length -> Fixed Length)

   ### Cryptography:

   -> Codes: (Encode: Plaintext -> Codetext) || (Decode: Codetext -> Plaintext)

   -> Cipher: (Encrypt: Plaintext -> Ciphertext) || (Decrypt: Ciphertext -> Plaintext)

   ### Secret-Key Cryptography:
   
   Symmetric-Key Encryption: Users use the exact same key. (Key + Plaintext → Ciphertext) Example: AES, Triple DES.

   ### Public-Key Cryptography: 

   Asymmetric-Key Encryption: Users use two keys. (Public Key + Plaintext → Ciphertext) && (Private Key + Ciphertext → Plaintext) Example: RSA, Diffie-Hellman, MQV.

   RSA:
   n = p . q ,
   c = m<sup>e</sup> mod n ,
   m = c<sup>d</sup> mod n

   Diffie-Hellman(Key Exchange):
   A = g<sup>a</sup> mod p ,
   B = g<sup>b</sup> mod p ,
   s = B<sup>a</sup> mod p ,
   s = A<sup>b</sup> mod p ,
   s = g<sup>ab</sup> mod p
   
   ### Digital Signatures: 
   
   Sign:(Message → Hash) -> (Private Key + Hash → Signature) &&
   Verify:(Message → Hash) -> (Public Key + Signature → Hash) Hash == Hash
   
   Example: DSA, ECDSA, RSA
    
   ### Passkeys\WebAuthn: 
   
   SignIn Process: The device creates public and private keys and sends the public key to the website.
   
   Login Process: The website sent a challenge. The device was sent back to the website (Private Key + Challenge → Signature). The website processes and verifies you ( Public Key + Signature → Challenge).

   ### Encryption in Transit → End-to-End Encryption

   ### Secure Deletion: Full-Disk Encryption, Encryption at Rest


## 2. Securing Software
## 3. Preserving Privacy
