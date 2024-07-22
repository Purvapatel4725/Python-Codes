class PlayfairCipher:
    def __init__(self, key):
        self.key = key.lower().replace("j", "i")
        self.matrix = self.generate_matrix()

    def generate_matrix(self):
        alphabet = 'abcdefghiklmnopqrstuvwxyz0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        keyChars = set(self.key)
        matrix = []
        for alpha in self.key + alphabet:
            if alpha not in keyChars:
                keyChars.add(alpha)
                matrix.append(alpha)
                if len(matrix) == 25:
                    break
        matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return matrix

    def find_char(self, alpha):
        for i, row in enumerate(self.matrix):
            if alpha in row:
                j = row.index(alpha)
                return (i, j)
        return None

    def encrypt(self, plaintext):
        plaintext = plaintext.lower().replace('j', 'i').replace(' ', '')
        plaintext = "".join(filter(str.isalnum, plaintext))
        if len(plaintext) % 2 == 1:
            plaintext += 'x'
        ciphertext = ""
        for i in range(0, len(plaintext), 2):
            a, b = plaintext[i:i+2]
            pos_a = self.find_char(a)
            pos_b = self.find_char(b)
            if not pos_a or not pos_b:
                ciphertext += a + b
                continue
            r1, c1 = pos_a
            r2, c2 = pos_b
            if r1 == r2:
                ciphertext += self.matrix[r1][(c1+1)%5] + self.matrix[r2][(c2+1)%5]
            elif c1 == c2:
                ciphertext += self.matrix[(r1+1)%5][c1] + self.matrix[(r2+1)%5][c2]
            else:
                ciphertext += self.matrix[r1][c2] + self.matrix[r2][c1]
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = "".join(filter(str.isalnum, ciphertext))
        plaintext = ""
        for i in range(0, len(ciphertext), 2):
            a, b = ciphertext[i:i+2]
            pos_a = self.find_char(a)
            pos_b = self.find_char(b)
            if not pos_a or not pos_b:
                plaintext += a + b
                continue
            r1, c1 = pos_a
            r2, c2 = pos_b
            if r1 == r2:
                plaintext += self.matrix[r1][(c1-1)%5] + self.matrix[r2][(c2-1)%5]
            elif c1 == c2:
                plaintext += self.matrix[(r1-1)%5][c1] + self.matrix[(r2-1)%5][c2]
            else:
                plaintext += self.matrix[r1][c2] + self.matrix[r2][c1]
        plaintext = plaintext.replace('x', '')
        return plaintext

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift
    
    def transform(self, text, direction):
        transformed_text = ""
        for char in text:
            if char.isalpha():
                shifted_char = chr((ord(char.lower()) - 97 + direction*self.shift) % 26 + 97)
                if char.isupper():
                    shifted_char = shifted_char.upper()
                transformed_text += shifted_char
            else:
                transformed_text += char
        return transformed_text
    
    def encrypt(self, plaintext):
        return self.transform(plaintext, 1)
    
    def decrypt(self, ciphertext):
        return self.transform(ciphertext, -1)



############################################################################################################################
cipher = PlayfairCipher('keyword')
plaintext = 'hey there it is working 123'
ciphertext = cipher.encrypt(plaintext)
print(ciphertext) 
##############################################
decrypted_text = cipher.decrypt(ciphertext)
print(decrypted_text) 
############################################################################################################################
############################################################################################################################
############################################################################################################################
cipher = CaesarCipher(3)
plaintext = "HelloWorld"
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)  
##############################################
decrypted_plaintext = cipher.decrypt(ciphertext)
print(decrypted_plaintext)  
############################################################################################################################




''' 
Key: "gatmdzitpaurwx"
grid:
    g a t m d
    z i p u r
    w x b c e
    f h k l n
    o q s v y 
            '''