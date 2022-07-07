import pikepdf
from tqdm import tqdm

class PDFCracker():
    def __init__(self):
        return None

    def crack(wordlist_path, file_path):
        passwords = [line.strip() for line in open(wordlist_path)]
        for password in tqdm(passwords, "Decripting PDF"):
            try:
                with pikepdf.open(file_path, password=password) as pdf:
                    print("\n[+] Password found:", password)
                break
            except pikepdf._qpdf.PasswordError as e:
                continue
