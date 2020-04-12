import sqlite3
import tkinter


def path_from_id(id):
    conn = sqlite3.connect('db/db.sqlite3')
    cur = conn.cursor()

    cur.execute('SELECT path FROM color WHERE id=?', (id,))
    path = cur.fetchone()[0]

    conn.close()
    return path


class App(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.item_id = tkinter.IntVar()

        self.draw_gui()
        self.show_image()

    def draw_gui(self):
        id_selector = tkinter.Spinbox(
            self, from_=1, to=3, increment=1,
            textvariable=self.item_id, command=self.show_image
        )
        id_selector.pack()

        self.image_widget = tkinter.Label(self)
        self.image_widget.pack()

    def show_image(self):
        path = path_from_id(self.item_id.get())
        self.current_image = tkinter.PhotoImage(file=path)
        self.image_widget['image'] = self.current_image


def main():
    root = tkinter.Tk()
    app = App(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
