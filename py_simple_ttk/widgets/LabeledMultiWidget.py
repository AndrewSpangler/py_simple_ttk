import tkinter as tk
from tkinter import ttk

from .Labeler import Labeler
from .MultiWidget import MultiWidgetMixin


class LabeledMultiWidgetMixin(Labeler, ttk.Frame, MultiWidgetMixin):
    """Generic mixin for making Labeled MultiWidgets"""

    def __init__(
        self,
        widget_class: type,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside: str = tk.TOP,
        **kw
    ):
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame, **kw)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, widget_class, config)
        self.widget_class, self.is_child = widget_class, is_child
