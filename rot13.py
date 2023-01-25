import tkinter as tk

def rot13_decrypt(string):
    decrypted = ""
    for char in string:
        if char.isalpha():
            char_code = ord(char)
            char_code += 13
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                decrypted += chr(char_code)
            else:
                if char_code > ord('z'):
                    char_code -= 26
                decrypted += chr(char_code)
        else:
            decrypted += char
    return decrypted

def on_rot13_button_click():
    string = input_field.get()
    decrypted_string = rot13_decrypt(string)
    output_field.config(state='normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.INSERT, decrypted_string)
    output_field.config(state='disabled')

root = tk.Tk()
root.title("ROT13 Decryption")

input_label = tk.Label(root, text="Enter the string to decrypt:")
input_label.pack()

input_field = tk.Entry(root)
input_field.pack()

rot13_button = tk.Button(root, text="Decrypt ROT13", command=on_rot13_button_click)
rot13_button.pack()

output_label = tk.Label(root, text="Decrypted string:")
output_label.pack()

output_field = tk.Text(root, height=10, width=50)
output_field.pack()
output_field.config(state='disabled')

root.mainloop()
