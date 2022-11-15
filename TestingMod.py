import Moduele
if __name__ == "__main__":
    app = Moduele.app("Hi")
    app.position(100,100)
    app.text("Hello World")
    app.pack()
    app.seperator()
    app.pack(fill="x",padx=10)
    app.launch()