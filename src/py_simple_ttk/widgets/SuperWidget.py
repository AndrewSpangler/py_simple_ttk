from typing import Callable


class SuperWidgetMixin:
    """Mixin to easily bind many of the common tkinter events."""

    __desc__ = """This class serves to add bindings for the majority \
    of common tkinter widget events. The bindings are made in add mode to \
    prevent previous / new bindings from causing unintended side-effects \
    like unmapping etc."""

    def __init__(
        self,
        on_mouse_enter: Callable = None,
        on_mouse_leave: Callable = None,
        on_mouse_move: Callable = None,
        on_mouse_wheel: Callable = None,
        on_left_click: Callable = None,
        on_double_left_click: Callable = None,
        on_middle_click: Callable = None,
        on_double_middle_click: Callable = None,
        on_right_click: Callable = None,
        on_double_right_click: Callable = None,
        on_configure: Callable = None,
    ):
        self.on_mouse_enter = on_mouse_enter
        self.on_mouse_leave = on_mouse_leave
        self.on_mouse_move = on_mouse_move
        self.on_left_click = on_left_click
        self.on_double_left_click = on_double_left_click
        self.on_middle_click = on_middle_click
        self.on_double_middle_click = on_double_middle_click
        self.on_right_click = on_right_click
        self.on_double_right_click = on_double_right_click
        self.on_mouse_wheel = on_mouse_wheel
        self.on_configure = on_configure
        event_map = {
            "<Enter>": self._on_mouse_enter,
            "<Leave>": self._on_mouse_leave,
            "<Motion>": self._on_mouse_move,
            "<Button-1>": self._on_left_click,
            "<Double-1>": self._on_double_left_click,
            "<Button-2>": self._on_middle_click,
            "<Double-2>": self._on_double_middle_click,
            "<Button-3>": self._on_right_click,
            "<Double-3>": self._on_double_right_click,
            "<Configure>": self._on_configure,
            "<MouseWheel>": self._on_mouse_wheel,
        }
        for event in event_map:
            self.bind(event, event_map[event], add="+")

    # fmt: off
    def _on_mouse_enter(self, event) -> None:
        if self.on_mouse_enter: self.on_mouse_enter(event)
    def _on_mouse_leave(self, event) -> None:
        if self.on_mouse_leave: self.on_mouse_leave(event)
    def _on_mouse_move(self, event) -> None:
        if self.on_mouse_move: self.on_mouse_move(event)
    def _on_mouse_wheel(self, event) -> None:
        if self.on_mouse_wheel: self.on_mouse_wheel(event)
    def _on_left_click(self, event) -> None:
        if self.on_left_click: self.on_left_click(event)
    def _on_double_left_click(self, event) -> None:
        if self.on_double_left_click: self.on_double_left_click(event)
    def _on_middle_click(self, event) -> None:
        if self.on_middle_click: self.on_middle_click(event)
    def _on_double_middle_click(self, event) -> None:
        if self.on_double_middle_click: self.on_double_middle_click(event)
    def _on_right_click(self, event) -> None:
        if self.on_right_click: self.on_right_click(event)
    def _on_double_right_click(self, event) -> None:
        if self.on_double_right_click: self.on_double_right_click(event)
    def _on_configure(self, event) -> None:
        if self.on_configure: self.on_configure(event)
