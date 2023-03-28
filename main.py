import tkinter as tk
from encryptdecrypt import encrypt, decrypt


def open_window(mode):
    window = tk.Toplevel()
    window.geometry("400x250")
    if mode == 1:
        window.title("Rail Fence")
    elif mode == 2:
        window.title("Matrix A")
    elif mode == 3:
        window.title("Matrix B")
    elif mode == 4:
        window.title("Matrix C")
    elif mode == 5:
        window.title("Cezar")
    elif mode == 6:
        window.title("Vigenere")

    text_label = tk.Label(window, text="Text:")
    text_label.pack()
    text_input = tk.Entry(window, width=30)
    text_input.pack()
    key_label = tk.Label(window, text="Key:")
    key_label.pack()
    key_input = tk.Entry(window, width=30)
    key_input.pack()
    output_label = tk.Label(window, text="Output:")
    output_label.pack()
    output = tk.Entry(window, width=30)
    output.pack()

    def encrypt_message():
        text = text_input.get()
        key = key_input.get()
        encrypted_text = encrypt(text, key, mode)
        output.delete(0, tk.END)
        output.insert(0, encrypted_text)

    def decrypt_message():
        text = text_input.get()
        key = key_input.get()
        decrypted_text = decrypt(text, key, mode)
        output.delete(0, tk.END)
        output.insert(0, decrypted_text)

    encrypt_button = tk.Button(window, text="Encrypt", width=10, command=encrypt_message)
    encrypt_button.pack(side=tk.LEFT, padx=50)
    decrypt_button = tk.Button(window, text="Decrypt", width=10, command=decrypt_message)
    decrypt_button.pack(side=tk.RIGHT, padx=50)


root = tk.Tk()
root.title("Main Menu")
root.geometry("400x300")


button1 = tk.Button(root, text="Rail Fence", command=lambda: open_window(1))
button1.pack(pady=10)

button2 = tk.Button(root, text="Matrix A", command=lambda: open_window(2))
button2.pack(pady=10)

button3 = tk.Button(root, text="Matrix B", command=lambda: open_window(3))
button3.pack(pady=10)

button4 = tk.Button(root, text="Matrix C", command=lambda: open_window(4))
button4.pack(pady=10)

button5 = tk.Button(root, text="Cezar", command=lambda: open_window(5))
button5.pack(pady=10)

button6 = tk.Button(root, text="Vigenere", command=lambda: open_window(6))
button6.pack(pady=10)


root.mainloop()
