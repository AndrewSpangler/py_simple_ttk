import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ..widgets.WidgetsCore import force_aspect
from ..widgets.ScaleWidgets import LabeledScale

PAUSED = False
RUNNING = True


class GifLoader:
    def __init__(self, path: str, load_tk_frames: bool = True):
        self.image = Image.open(path)
        self.frames = []
        # pallet = self.image.getpalette()
        self.tk_frames = None
        self.tk_frames_loaded = False
        frame_index = 0
        try:
            while True:
                # self.image.putpalette(pallet)
                new_image = Image.new("RGB", self.image.size)
                new_image.paste(self.image)
                self.frames.append(new_image)
                frame_index += 1
                self.image.seek(self.image.tell() + 1)
        except EOFError:
            pass
        if load_tk_frames:  # Can chose to defer load
            self.load_tk_frames()

    def load_tk_frames(self) -> None:
        if self.tk_frames_loaded:
            raise ValueError("Tk frames already loaded")
        self.tk_frames = [ImageTk.PhotoImage(f) for f in self.frames]
        self.tk_frames_loaded = True


class GifViewer(ttk.Frame):
    def __init__(self, loader: GifLoader, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        self.loader = loader
        self.image = None
        self.width = loader.image.width
        self.height = loader.image.height
        self.delay = 1000
        self.index = 0

        self.outer_frame = ttk.Frame(self)
        self.outer_frame.pack(side="top", fill="both", expand=True, padx=4, pady=4)
        self.outer_frame.config(width=250, height=200)
        self.inner_frame = ttk.Frame(self)
        force_aspect(
            self.inner_frame, self.outer_frame, float(self.width) / float(self.height)
        )

        self.canvas = tk.Canvas(self.inner_frame, relief="sunken")
        self.canvas.config(
            width=50,
            height=50,
        )
        self.canvas.config()
        self.canvas_frame = ttk.Frame(
            self.canvas,
            border=0,
        )
        self.canvas.create_window(0, 0, window=self.canvas_frame, anchor="nw")
        self.canvas_frame.config(width=50, height=50)
        self.canvas.pack(fill="both", expand=True)

        self.playback_scale = LabeledScale(
            self,
            "Playback Speed ",
            command=self.set_delay,
            default=int(self.delay / 1000),
            orient="horizontal",
            from_=0,
            to=60,
        )
        self.playback_scale.pack(fill="both", expand=False, padx=4, pady=4)
        # self.playback_scale = ttk.Scale(self, orient = "horizontal", from_ = 0, to = 30, command = self.set_delay)
        # self.playback_scale.set(int(self.delay/1000))
        # self.playback_scale.pack(fill = "both", expand = False, padx = 4, pady = 4)

        self.display_loop()

    def set_delay(self, fps) -> None:
        if float(fps) < float(1.0):
            self.delay = None
            return
        self.delay = int(1000.0 / float(fps))

    """
	Approximates an fps, milage will vary, it would be 
	better for to run this as a thread spawned by a
	timer thread that acts as the loop, so the fps 
	would more closely match the one selected with the menu bar
	"""

    def display_loop(self) -> None:
        if self.index > len(self.loader.tk_frames) - 1:
            self.index = 0

        self.image = self.loader.frames[self.index]
        self.image = self.image.resize(
            (self.inner_frame.winfo_width(), self.inner_frame.winfo_height()), Image.BOX
        )
        self.image = ImageTk.PhotoImage(self.image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        self.index += 1
        if not self.delay or self.delay < 10:
            delay = 10
        delay = self.delay or 1000
        self.after(delay, self.display_loop)
