import sqlite3
import tkinter


def path_from_id(id):
    conn = sqlite3.connect('db/db.sqlite3')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('SELECT * FROM color WHERE id=?', (id,))
    path = cur.fetchone()['path']

    conn.close()
    return path


class App(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.current_id = None
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

        self.path_label = tkinter.Label(self)
        self.path_label.pack()

    def show_image(self):
        id = self.item_id.get()
        if id == self.current_id:
            return
        self.current_id = id

        path = path_from_id(id)
        self.current_image = tkinter.PhotoImage(file=path)
        self.image_widget['image'] = self.current_image
        self.path_label['text'] = path


def main():
    root = tkinter.Tk()
    app = App(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
