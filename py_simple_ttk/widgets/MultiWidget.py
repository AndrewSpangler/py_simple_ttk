import tkinter as tk
from tkinter import ttk


class MultiWidgetMixin:
    """An abstract mixin that provides a way to easily instantiate multiple of the same class of a widget and making complicated forms with simple get/set methods."""

    __desc__ = """MultiWidgets support a simple get/set system. \
Calling get without a configuration list returns a dict of subwidget \
keys mapped to the values of each subwidget's .get value. Passing a \
list of subwidget keys limits MultiWidgetMixin.get to said subwidgets. \
Subclassing a multiwidget with one or more instances of one class \
and then calling multiwidget.add() with different classes after is \
acceptable assuming the widget supports being added and .get / .set / \
.enable / .disable / .clear methods."""

    def __init__(self, widget_type: type, config: dict = {}, default_kwargs: dict = {}):
        """Provide a widget type and a configuration dictionary in kwargs format"""
        self.widget_type = widget_type
        self.widgets = {}
        self.default_kwargs = default_kwargs
        for k in config:
            args, kwargs = config[k]
            if not kwargs.get("is_child"):
                kwargs["is_child"] = True
            self.add(self, k, args, kwargs)

    def add(
        self,
        parent: ttk.Frame,
        key: str,
        args: list = [],
        kwargs: dict = {},
        widget_type: type = None,
        fill: str = "x",
        padx: tuple = (20, 0),
        pady: tuple = (5, 0),
        side: str = tk.TOP,
        expand: bool = False,
    ) -> object:
        """Method for adding different widgets to a multiwidget post-instantiation"""
        (kw := self.default_kwargs.copy()).update(kwargs)
        widget_type = widget_type or self.widget_type
        w = widget_type(parent, key, *args, **kw)
        w.pack(fill=fill, expand=expand, side=side, padx=padx, pady=pady)
        self.widgets[key] = w
        return w

    def get(self, config: list = None) -> dict:
        """Pass a list of widget keys to get a dict of outputs"""
        out = {}
        widgets = config or self.widgets
        for w in widgets:
            out[w] = self.widgets[w].get()
        return out

    def set(self, config: dict) -> None:
        """Pass a map of widget keys and their values"""
        for w in config:
            self.widgets[w].set(config[w])

    def enable(self, config: list = None) -> None:
        """Pass a list of subwidgets to enable or all are enabled"""
        widgets = config or self.widgets
        for w in widgets:
            self.widgets[w].enable()

    def disable(self, config: list = None) -> None:
        """Pass a list of subwidgets to disable or all are disabled"""
        widgets = config or self.widgets
        for w in widgets:
            self.widgets[w].disable()

    def clear(self, config: list = None) -> None:
        """Pass a list of subwidgets to clear or all are set to default"""
        widgets = config or self.widgets
        for w in widgets:
            self.widgets[w].clear()
