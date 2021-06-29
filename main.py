import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("wordlist.txt")]

for password in tqdm(passwords, "Decripting PDF"):
    try:
        with pikepdf.open("file.pdf", password=password) as pdf:
            print("\n[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue
