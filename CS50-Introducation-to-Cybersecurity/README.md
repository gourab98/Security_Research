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

## 2. Securing Systems

   ### Wi-Fi, Wi-Fi protected access, HTTP, HTML, Machine-in-the-Middle Attacks, Packet Sniffing, Cookies, Session Hijacking, HTTPS(With Encryption), TLS(Improved version of SSL), Certificate(X.509), Certificate Authority(CA), SSL Stripping, HSTS, VPN, SSH, Port, Port Scanning, Penetration Testing, Ethical Hacking, Firewall, IP Address, Deep Packet Inspection, Proxy, Malware, Virus, Worm, Botnet, Denial-of-Service(DoS) Attack, Distributed Denial-of-Service(DDoS) Attack, Antivirus, Automatic Updates, Zero-Day Attacks!

## 3. Securing Software

   ### Phishing, Code Injection, Cross-Site Scripting(XSS), Reflected, Stored, Content-Security-Policy: script-src https://example.com, SQL Injection -> Prepared Statements, Command Injection, system, eval, Character Escapes: &lt; (<), &gt; (>), &amp; (&), &quot; ("), &apos; ('), ...

   ### Developer Tools, Client-Side Validation, Server-Side Validation, Cross-Site Request Forgery(CSRF), GET, POST, Open Worldwide Application Security Project(OWASP)   

   ### Arbitrary Code Execution(ACE), Remote Code Execution(RCE), Buffer Overflow, Stack Overflow,  
   

## 4. Preserving Privacy
