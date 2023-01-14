#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from .Labeler import Labeler
from .MultiWidget import MultiWidgetMixin

class ActiveProgressbar(ttk.Progressbar):
    """ttk.Progressbar with added features"""

    def __init__(
        self,
        parent: ttk.Frame,
        default: float = 0,
        **kw
    ):
        ttk.Progressbar.__init__(self, self.frame, **kw)
        self["value"] = self.default = default

    def enable(self):
        """Disable Progressbar. `Returns None`"""
        self["state"] = tk.NORMAL

    def disable(self):
        """Enable Progressbar. `Returns None`"""
        self["state"] = tk.DISABLED

    def set(self, val):
        """Get Progressbar progress. `Returns a String`"""
        self["value"] = val

    def get(self):
        """Set Progressbar progress. `Returns None`"""
        return self["value"]

    def clear(self):
        """Sets Progressbar progress to its default value `Returns None`"""
        self["value"] = self.default

    def link(self, widget):
        """Easily link to other widgets, sets the progressbar var to the passed widget's var. `Returns None`"""
        self.configure(variable=widget.var)

        

class LabeledProgressbar(Labeler, ActiveProgressbar):
    """Labeled Progressbar"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        orient=tk.HORIZONTAL,
        labelside=tk.LEFT,
        is_child=False,
        default: float = 0,
        **kw,
    ):
        self.is_child = is_child
        self.default = default
        kw.update({"orient":orient})
        if orient == tk.VERTICAL:
            # Force labelside redirect for vertical Progress bars
            labelside=tk.TOP
            pack = {"fill":"y", "expand":True, "side":tk.TOP}
        elif orient == tk.HORIZONTAL:
            pack = {"fill":"x", "expand":True, "side":tk.RIGHT}
        else:
            raise ValueError(f"Bad orientation - {orient}")
        Labeler.__init__(self, parent, labeltext, labelside=labelside, header=not is_child)
        ActiveProgressbar.__init__(self, self.frame, **kw)
        ActiveProgressbar.pack(self, **pack)

        
class LabeledMultiProgressbar(Labeler, ttk.Frame, MultiWidgetMixin):
    """Labeled MultiWidget LabeledProgressbar"""

    def __init__(
        self,
        parent: ttk.Frame,
        labeltext: str,
        config: dict,
        is_child: bool = False,
        labelside=tk.TOP,
        orient=tk.HORIZONTAL,
    ):
        self.orient = orient
        self.is_child = is_child
        self.parent = parent
        Labeler.__init__(
            self, parent, labeltext, labelside=labelside, header=not is_child
        )
        ttk.Frame.__init__(self, self.frame)
        ttk.Frame.pack(self, fill=tk.BOTH, expand=True, side=tk.TOP)
        MultiWidgetMixin.__init__(self, LabeledProgressbar, config)

    def add(
        self, parent: ttk.Frame, key: str, args, kwargs, widget_type=None
    ) -> object:
        """Overrides normal MultiWidgetMixin behavior to deal with vertical orientation. Will break most added widgets  `Returns None`"""
        widget_type = widget_type or self.widget_type
        kwargs["orient"] = self.orient
        w = widget_type(parent, key, *args, **kwargs)
        if self.orient == tk.HORIZONTAL:
            w.pack(fill="x", expand=False, side=tk.TOP, padx=(20, 0))
        elif self.orient == tk.VERTICAL:
            w.pack(fill="y", expand=True, side=tk.LEFT)
        else:
            raise ValueError(f"Bad orientation - {self.orient}")
        self.widgets[key] = w
        return w

    def link(self, config: dict) -> None:
        """Link to other widgets with a dict of subwidget keys to link to. This function will break if widgets without the link method are added to the MultiWidget. `Returns None`"""
        for k in config:
            self.widgets[k].link(config[k])
