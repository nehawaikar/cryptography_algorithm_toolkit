\# Cryptography Algorithms Toolkit



A Python-based Cryptography and Network Security project that demonstrates the implementation of four commonly used cryptographic techniques:



\- AES Encryption and Decryption

\- RSA Encryption and Decryption

\- SHA-256 Hashing

\- HMAC-SHA1



The project uses a simple command-line interface that allows users to select and execute different cryptographic operations.



\---



\## Table of Contents



\- \[Project Overview](#project-overview)

\- \[Objectives](#objectives)

\- \[Features](#features)

\- \[Technologies Used](#technologies-used)

\- \[Algorithms Implemented](#algorithms-implemented)

\- \[Project Structure](#project-structure)

\- \[Requirements](#requirements)

\- \[Installation](#installation)

\- \[How to Run](#how-to-run)

\- \[How the Project Works](#how-the-project-works)

\- \[Sample Operations](#sample-operations)

\- \[Screenshots](#screenshots)

\- \[Security Considerations](#security-considerations)

\- \[Learning Outcomes](#learning-outcomes)

\- \[Future Enhancements](#future-enhancements)

\- \[Author](#author)

\- \[Conclusion](#conclusion)



\---



\## Project Overview



Cryptography is an important part of cybersecurity that protects information from unauthorized access and modification.



This project provides a practical implementation of different cryptographic techniques using Python. It demonstrates the difference between symmetric encryption, asymmetric encryption, hashing, and message authentication.



The application provides a menu through which users can perform encryption, decryption, hashing, and authentication operations.



\---



\## Objectives



The main objectives of this project are:



1\. To understand the basic concepts of cryptography.

2\. To implement AES encryption and decryption.

3\. To implement RSA encryption and decryption.

4\. To generate SHA-256 hash values.

5\. To implement HMAC-SHA1 message authentication.

6\. To understand the difference between encryption and hashing.

7\. To understand the use of public and private keys.

8\. To gain practical experience in implementing cryptographic algorithms using Python.



\---



\## Features



The project includes the following features:



\### AES



\- AES encryption

\- AES decryption

\- Random 256-bit key generation

\- CBC mode encryption

\- Base64 encoding of encrypted data



\### RSA



\- 2048-bit RSA key generation

\- Public key generation

\- Private key generation

\- RSA encryption

\- RSA decryption

\- PEM file storage for RSA keys



\### SHA-256



\- Accepts text input from the user

\- Generates a SHA-256 hash

\- Displays the hash in hexadecimal format



\### HMAC-SHA1



\- Accepts a secret key

\- Accepts a message

\- Generates an HMAC-SHA1 authentication code



\---



\## Technologies Used



| Technology | Purpose |

|------------|---------|

| Python 3 | Programming language |

| PyCryptodome | AES and RSA implementation |

| hashlib | SHA-256 and SHA-1 hashing |

| hmac | HMAC-SHA1 generation |

| base64 | Encoding encrypted data |

| Windows | Development environment |



\---



\## Algorithms Implemented



\## 1. AES Encryption and Decryption



AES stands for Advanced Encryption Standard.



AES is a symmetric encryption algorithm. It uses the same secret key for both encryption and decryption.



In this project, a random 256-bit AES key is generated for encryption.



AES is implemented using CBC (Cipher Block Chaining) mode.



The encrypted output contains:



\- Initialization Vector (IV)

\- Ciphertext



The complete encrypted data is converted into Base64 format for easy display and handling.



\### AES Process



```text

Plaintext

&#x20;   |

&#x20;   v

AES Encryption

&#x20;   |

&#x20;   v

Encrypted Data

&#x20;   |

&#x20;   v

Base64 Encoding

&#x20;   |

&#x20;   v

Encrypted Output

