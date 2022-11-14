# AppBuilder
App Builder is a python library made to create python apps easier than ever before.

It uses the `tkinter` library to create apps and offers a front end way communicating with apps.

A code to make a window may look like this:
```python
import AppBuilder
app = Moduele.app("Hello World")
app.text("The Best App!")
app.pack()
app.seperator()
app.pack()
app.launch()
```
