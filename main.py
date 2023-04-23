import tkinter as tk
from encryptdecrypt import encrypt, decrypt
from tkinter import filedialog
from stream import stream_encrypt, stream_decrypt

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


def stream_open_window(mode):
    window = tk.Toplevel()
    window.geometry("400x250")
    window.title("Stream")

    def save_file(text):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(text)

    def load_file():
        polynomial = polynomial_input.get()
        if polynomial.isnumeric() and int(polynomial) > 1:
            file_path = filedialog.askopenfilename()
            with open(file_path, 'r', encoding="utf-8") as file:
                text = file.read()
                if mode == 1:
                    encrypted_text = stream_encrypt(text, int(polynomial))
                elif mode == 2:
                    encrypted_text = stream_decrypt(text, polynomial)
                save_file_button = tk.Button(window, text="Save file", width=25, command=lambda: save_file(encrypted_text))
                save_file_button.pack(pady=10)
        else:
            tk.messagebox.showerror("Error", "Enter correct value")

    if mode == 1:
        polynomial_label = tk.Label(window, text="Enter a polynomial (Must be higher than 1)")
    elif mode == 2:
        polynomial_label = tk.Label(window, text="Enter the key")
    polynomial_label.pack()

    polynomial_input = tk.Entry(window, width=30)
    polynomial_input.pack()
    select_file_button = tk.Button(window, text="Select a file", width=10, command=lambda: load_file())
    select_file_button.pack(pady=10)


root = tk.Tk()
root.title("Main Menu")
root.geometry("400x400")


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

button7 = tk.Button(root, text="Stream Encrypt", command=lambda: stream_open_window(1))
button7.pack(pady=10)

button8 = tk.Button(root, text="Stream Decrypt", command=lambda: stream_open_window(2))
button8.pack(pady=10)

root.mainloop()
