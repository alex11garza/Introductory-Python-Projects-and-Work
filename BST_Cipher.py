#  File: BST_Cipher.py
#  Student Name: Alex Garza
#  Student UT EID: ang3489


import sys

# One node in the BST Cipher Tree


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None


# The BST Cipher Tree
class Tree:

    # Create the BST Cipher tree based on the key
    def __init__(self, key):
        self.root = None
        for ch in key:
            self.insert(ch)

    # Insert one new charater/Node to the BST Cipher tree
    # If the character already exists, don't add it.
    def insert(self, ch):
        if not self.isValidCh(ch):
            return
        self.root = self._insert(self.root, ch)
    
    def _insert(self, node, ch):
        if node is None:
            return Node(ch)
        if ch < node.ch:
            node.left = self._insert(node.left, ch)
        elif ch > node.ch:
            node.right = self._insert(node.right, ch)
        return node


    # Encrypts a text message using the BST Tree
    def encrypt(self, message):
            # The first character does not get prefixed with "*"
            encrypted_message = self.encrypt_ch(message[0])[1:]

            for ch in message[1:]:
                encrypted_message += self.encrypt_ch(ch)
            if str(encrypted_message[0]) =="!":
                return "*"+encrypted_message[1:]
            return encrypted_message

    def encrypt_ch(self, ch):
            return self._encrypt_ch(self.root, ch,'!')

    def _encrypt_ch(self, node, ch, code):
            if node is None:
                return ''
            if node.ch == ch:
                return code
            if ch < node.ch:
                return self._encrypt_ch(node.left, ch, code + '<')
            else:
                return self._encrypt_ch(node.right, ch, code + '>')

    def decrypt(self, codes_string):
        return ''.join(self.decrypt_code(code) for code in codes_string.split('!') if code)

    def decrypt_code(self, code):
        return self._decrypt_code(self.root, code, 0)

    def _decrypt_code(self, node, code, idx):
        if node is None:
            return ''
        if idx == len(code) or code[idx] == '*':
            return node.ch
        if code[idx] == '<':
            return self._decrypt_code(node.left, code, idx + 1)
        else:
            return self._decrypt_code(node.right, code, idx + 1)


    def clean(self, text):
        cleanText = ""
        for i in range(len(text)):
            if (self.isValidCh(text[i])):
                cleanText += text[i]
        return cleanText

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()