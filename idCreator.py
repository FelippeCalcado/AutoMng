import tkinter as tk


class IdCreator:
    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email

    def save_user(self):
        print(f'''
Bom Dia, Sr(a) {self.user_name},
Ficaste identificado como:

Nome:   {self.user_name}
E-mail: {self.email}''')


class GuiIdCreator:
    def __init__(self, root):
        self.root = root

    def create_gui(self):
        name_entry = tk.Entry(self.root)
        email_entry = tk.Entry(self.root)

        def get_name():
            user_id = IdCreator(name_entry.get(), email_entry.get())
            user_id.save_user()
            return user_id

        get_button = tk.Button(self.root, text="Get Data", command=get_name)
        name_entry.pack()
        email_entry.pack()
        get_button.pack()


def main():
    app = tk.Tk()
    GuiIdCreator(app).create_gui()

    app.mainloop()


if __name__ == '__main__':
    main()
