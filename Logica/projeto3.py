import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("250x150")
        self.center_window()  # Centralizar a janela de login
        self.username = "caio323"
        self.password = "3132"
        
        self.username_label = tk.Label(root, text="Nome de usuário:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        
        self.password_label = tk.Label(root, text="Senha:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()
        
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def center_window(self):
        # Obter a largura e altura da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular as coordenadas para centralizar a janela
        x = (screen_width - 250) / 2
        y = (screen_height - 150) / 2

        # Definir a geometria da janela para centralizá-la
        self.root.geometry("250x150+{}+{}".format(int(x), int(y)))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == self.username and password == self.password:
            self.root.destroy()
            BlocoDeNotasApp()

        else:
            messagebox.showerror("Erro de Login", "Credenciais inválidas. Tente novamente.")

class BlocoDeNotasApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bloco de Notas Seguro")
        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=True, fill='both')

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Novo", command=self.novo)
        self.file_menu.add_command(label="Abrir", command=self.abrir)
        self.file_menu.add_command(label="Salvar", command=self.salvar)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.sair)

        self.root.mainloop()

    def novo(self):
        self.text_area.delete(1.0, tk.END)

    def abrir(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)

    def salvar(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)

    def sair(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
