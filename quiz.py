a = [ 104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 115, 100, 102, 103, 119, 114, 52, 52, 104, 114, 102, 104, 102, 104, 45, 119, 115 ]

print("".join([chr(i) for i in a]))

# https://engineering-application.britecore.com/quiz/sdfgwr44hrfhfh-ws

from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABckHX2KQoB7hqJERnUzsdI9yOQV6O9ALaZ_dkqy0wNolJmXev2J_iORBUXTK5ZLfwVbrZ0FJy8SFLCkMnfIQEuLofsEyzvr0EAzVeMwtOfD5bzY2UmtFcTIMakgQq7Q5_mjtB5AWpsvAuVTFOWSbQ7LFTo2tOw31zvAD5g5fEX1nnBnQtKXAgLJV0P83OhtBQ-fVUi'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()

# https://engineering-application.britecore.com/e/t19e119s2t/testImplementationEngineer
