import io
from PIL import Image
from tkinter import ttk
from py_simple_ttk import App, Tab, LabeledPathEntry, CopyBox


def encode_image(path: str) -> bytes:
    """Returns an RGBA PNG encoded as a bytestring"""
    Image.open(path).convert("RGBA").save(bytes_array := io.BytesIO(), format="PNG")
    return str(bytes_array.getvalue())


class EncodeDemo(App):
    def __init__(self):
        App.__init__(self, "image_encoder.json")
        self.notebook.pack_forget()
        (frame := ttk.Frame(self.window)).pack(fill="x", padx=10, pady=10)
        (path_entry := LabeledPathEntry(frame, "Image Path:")).pack(fill="x")
        (button := ttk.Button(frame, text="Encode Image")).pack(fill="x")
        (copy_box := CopyBox(frame)).pack(expand=True, fill="both")

        def encode():
            if not (path := path_entry.get()):
                return copy_box.set("No image selected")
            copy_box.set(encode_image(path))

        button.configure(command=encode)


if __name__ == "__main__":
    EncodeDemo().mainloop()
