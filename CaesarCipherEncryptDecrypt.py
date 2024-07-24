#Assignment-2 #Question-4

class CaesarCipher:
    def __init__(self, shift):
        # Initialize the CaesarCipher object with a given shift value
        self.shift = shift

    def transform(self, text, direction):
        # Transform the given text by shifting each alphabetic character by the shift value
        transformedText = ""
        for char in text:
            if char.isalpha():
                # Check if the character is alphabetic
                # Convert the character to lowercase, calculate the shifted character's ASCII value,
                # and convert it back to a character
                shiftedChar = chr((ord(char.lower()) - 97 + direction * self.shift) % 26 + 97)
                if char.isupper():
                    # If the original character was uppercase, convert the shifted character to uppercase as well
                    shiftedChar = shiftedChar.upper()
                transformedText += shiftedChar
            else:
                # If the character is not alphabetic, leave it unchanged
                transformedText += char
        return transformedText

    def encrypt(self, plaintext):
        # Encrypt the plaintext by applying the transform method with a direction of 1 (forward shift)
        return self.transform(plaintext, 1)

    def decrypt(self, ciphertext):
        # Decrypt the ciphertext by applying the transform method with a direction of -1 (backward shift)
        return self.transform(ciphertext, -1)


while True:
    # Create a CaesarCipher object with a shift value of 3
    cipher = CaesarCipher(3)
    # Prompt the user to enter a string
    plaintext = input("Enter a string: ")
    # Encrypt the plaintext using the CaesarCipher object
    ciphertext = cipher.encrypt(plaintext)
    # Print the encrypted text
    print(f"The encrypted text is: {ciphertext}")
    # Decrypt the ciphertext using the same CaesarCipher object
    decrypted_plaintext = cipher.decrypt(ciphertext)
    # Print the decrypted text
    print(f"The decrypted text is: {decrypted_plaintext}")

