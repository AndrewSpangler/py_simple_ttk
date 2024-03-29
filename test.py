import json
import tkinter as tk
from tkinter import ttk

from src import (
    ActiveLabel,
    ActiveSpinbox,
    App,
    BrowserLauncherTab,
    ColumnFrame,
    CommandLauncherTab,
    ConsoleTab,
    ConstrainedEntry,
    ConversationsTab,
    CopyBox,
    Counter,
    CycleButton,
    default_pack,
    default_separator,
    default_vertical_pack,
    default_vertical_separator,
    DigitsEntry,
    ExampleTile,
    FloatCounter,
    FloatEntry,
    get_asset,
    get_generated_font_images,
    GifLoader,
    GifViewer,
    HexdigitsEntry,
    IntEntry,
    LabeledCheckbutton,
    LabeledCombobox,
    LabeledConstrainedEntry,
    LabeledCopyBox,
    LabeledCounter,
    LabeledCycleButton,
    LabeledDigitsEntry,
    LabeledEntry,
    LabeledFloatCounter,
    LabeledFloatEntry,
    LabeledHexdigitsEntry,
    LabeledIntEntry,
    LabeledLettersDigitsEntry,
    LabeledLettersEntry,
    LabeledLowercaseDigitsEntry,
    LabeledLowercaseEntry,
    LabeledMultiCheckbutton,
    LabeledMultiCombobox,
    LabeledMultiCopyBox,
    LabeledMultiCounter,
    LabeledMultiCycleButton,
    LabeledMultiDigitsEntry,
    LabeledMultiEntry,
    LabeledMultiFloatCounter,
    LabeledMultiFloatEntry,
    LabeledMultiHexdigitsEntry,
    LabeledMultiIntEntry,
    LabeledMultiLettersDigitsEntry,
    LabeledMultiLettersEntry,
    LabeledMultiLowercaseDigitsEntry,
    LabeledMultiLowercaseEntry,
    LabeledMultiOctdigitsEntry,
    LabeledMultiOptionMenu,
    LabeledMultiPrintableEntry,
    LabeledMultiProgressbar,
    LabeledMultiRadioTable,
    LabeledMultiScale,
    LabeledMultiSimpleRadioTable,
    LabeledMultiSpinbox,
    LabeledMultiUppercaseDigitsEntry,
    LabeledMultiUppercaseEntry,
    LabeledOctdigitsEntry,
    LabeledOptionMenu,
    LabeledPathEntry,
    LabeledPrintableEntry,
    LabeledProgressbar,
    LabeledRadioTable,
    LabeledScale,
    LabeledSimpleRadioTable,
    LabeledSpinbox,
    LabeledUppercaseDigitsEntry,
    LabeledUppercaseEntry,
    LabeledValue,
    LauncherTools,
    LettersDigitsEntry,
    LettersEntry,
    ListManipulator,
    LowercaseDigitsEntry,
    LowercaseEntry,
    NotesTab,
    NoticeWindow,
    OctdigitsEntry,
    OrderedListbox,
    PasswordEntry,
    PasswordWindow,
    PILLOW_AVAILABLE,
    PrintableEntry,
    PromptWindow,
    ScrolledText,
    ShoppingListTab,
    Tab,
    tcl_bell,
    tcl_center_window,
    tcl_choose_font,
    tcl_download_file,
    TextWindow,
    TiledCanvas,
    TimecardTab,
    ToolTip,
    TreeTableTab,
    UppercaseDigitsEntry,
    UppercaseEntry,
    WattageTab,
    YesNoCancelWindow,
)

from math import sin

from py_simple_lorem import lorem

print("py_simple_ttk Example / Test")

links = {
    "Google": "https://www.google.com/",
    "YouTube": "http://youtu.be/",
    "Gmail": "https://www.gmail.com/",
}
apps = {
    "System Info": ["C:\Windows\System32\msinfo32.exe"],
    "Winver": ["C:\Windows\System32\winver.exe"],
    "Task Manager": ["C:\Windows\System32\Taskmgr.exe"],  # Fails on some systems
}


class TextBoxTestTab(Tab):
    def __init__(self, notebook: ttk.Notebook):
        Tab.__init__(self, notebook, "AutoScrollbarredTextbox")
        self.text = ScrolledText(
            self,
            widgetargs={
                "on_mouse_move": self.update_mouse,
                "on_left_click": self.update_cursor,
                "on_right_click": self.update_cursor,
                "on_middle_click": self.update_cursor,
            },
        )
        self.text.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        self.text.insert("1.0", lorem(1000))
        self.text.bind("<KeyRelease>", self.update_cursor)

        self.footer = ttk.Frame(self)
        self.footer.pack(side=tk.BOTTOM, fill="x", expand=False)

        self.cursor_x, self.cursor_y = self.text.get_cursor().split(".")

        self.info_var = tk.StringVar()
        default_separator(self.footer, pady=0, padx=0)
        self.info_label = ttk.Label(self.footer, textvariable=self.info_var)
        default_pack(self.info_label)

    def update_mouse(self, event):
        self.cursor_x, self.cursor_y = self.text.get_cursor().split(".")
        self.mouse_x, self.mouse_y = event.x, event.y
        self.update_info()

    def update_cursor(self, event=None):
        self.cursor_x, self.cursor_y = self.text.get_cursor().split(".")
        self.update_info()

    def update_info(self, event=None):
        sel = ""
        if self.text.tag_ranges(tk.SEL):
            sel = self.text.get(tk.SEL_FIRST, tk.SEL_LAST)

        if sel:
            if len(sel) > 1:
                sel = f" | {len(sel)} Characters Selcted"
            else:
                sel = " | 1 Character Selected"

        self.info_var.set(
            f"Cursor: Line {self.cursor_x}, Column {self.cursor_y} | Mouse: {self.mouse_x} {self.mouse_y}{sel}"
        )


class FormWidgetDemoTab(Tab):
    def __init__(self, notebook: ttk.Notebook):
        Tab.__init__(self, notebook, "Basic Widgets")
        (frames := ColumnFrame(self, 3)).pack(fill="both", expand=True)
        self.frames = frames
        left, mid, right = frames.frames
        self.entry = LabeledEntry(left, "LabeledEntry")
        default_pack(self.entry)
        entry_config = {
            "Entry 1": ([], {"default": ""}),
            "Entry 2": ([], {"default": "Always 2 except when it's not..."}),
            "Entry 3": ([], {"default": "101010000100101"}),
            "Entry 4": ([], {"default": ""}),
        }
        self.entries = LabeledMultiEntry(left, "LabeledMultiEntry", entry_config)
        default_pack(self.entries)
        default_separator(left)
        self.path_entry = LabeledPathEntry(left, "LabeledPathEntry (File Mode)")
        default_pack(self.path_entry)
        self.dir_entry = LabeledPathEntry(
            left, "LabeledPathEntry (Dir mode)", dialog=tk.filedialog.askdirectory
        )
        default_pack(self.dir_entry)
        default_separator(left)
        self.option_menu = LabeledOptionMenu(
            left, "LabeledOptionMenu", ["Option 1", "Option 2"]
        )
        default_pack(self.option_menu)
        option_menu_config = {
            "Menu 1": ([["Option A", "Option B"]], {}),
            "Menu 2": ([["ALPHA", "BRAVO"]], {"default": 1}),
            "Menu 3": ([["A", "B", "C", "D", "E"]], {"default": 4}),
        }
        self.option_menus = LabeledMultiOptionMenu(
            left, "LabeledMultiOptionMenu", option_menu_config
        )
        default_pack(self.option_menus)
        default_separator(left)
        self.check_button = LabeledCheckbutton(
            left,
            "LabeledCheckButton",
            text="Button Text",
            replace_output=["Unchecked", "Checked"],
            default=True,
        )
        default_pack(self.check_button)
        check_buttons_config = {
            "Int Button": (
                [],
                {
                    "text": "This button will return an int",
                    "replace_output": [0, 1],
                },
            ),
            "Bool Button": (
                [],
                {
                    "text": "This button will return a bool",
                    "default": True,
                    "replace_output": [False, True],
                },
            ),
            "String Button": (
                [],
                {
                    "text": "This button will return a string",
                    "replace_output": ["Unchecked", "Checked"],
                },
            ),
        }
        self.check_buttons = LabeledMultiCheckbutton(
            left, "LabeledMultiCheckButton", check_buttons_config
        )
        default_pack(self.check_buttons)
        default_separator(left)

        # Middle Column
        self.box = LabeledCombobox(mid, "LabeledCombobox", values=("A", "B"), default=0)
        default_pack(self.box)
        conf = {
            "Box 1": ([], {"values": ("C", "D"), "default": 0}),
            "Box 2": ([], {"values": ("E", "F"), "default": 1}),
            "Box 3": ([], {"values": ("G", "H"), "default": 0}),
        }
        self.boxes = LabeledMultiCombobox(mid, "LabeledMultiCombobox", config=conf)
        default_pack(self.boxes)
        default_separator(mid)

        options = ["Option 1", "Option 2", "Option 3"]
        self.radio = LabeledSimpleRadioTable(
            mid, "LabeledRadioTable", options=options, default=0
        )
        default_pack(self.radio)

        conf = {
            "Radios 1": ([["Option 4", "Option 5", "Option 6"]], {"default": 1}),
            "Radios 2": ([["Option 7", "Option 8", "Option 9"]], {"default": 2}),
        }
        self.radios = LabeledMultiSimpleRadioTable(
            mid, "LabeledMultiRadioTable", config=conf
        )
        default_pack(self.radios)
        default_separator(mid)
        # ActiveLabel
        self.labeled_value = LabeledValue(mid, "LabeledValue", "The Value")
        default_pack(self.labeled_value)

        self.cycle = LabeledCycleButton(
            right,
            "LabeledCycleButton (0 -> 5)",
            tuple(str(i) for i in range(6)),
        )
        default_pack(self.cycle)
        conf = {
            "Cycle 1 (5 -> 0)": ([[str(i) for i in reversed(range(6))]], {}),
            "Cycle 2 (-5 -> 5)": ([[str(i) for i in range(-5, 6)]], {}),
        }
        self.multi_cycle = LabeledMultiCycleButton(
            right, "LabeledMultiCycleButton", config=conf
        )
        default_pack(self.multi_cycle)
        default_separator(right)
        self.spin = LabeledSpinbox(right, "LabeledSpinbox (0 -> 500)", from_=0, to=500)
        default_pack(self.spin)
        conf = {
            "Spin 1 (20-30)": [(), {"from_": 20, "to": 30}],
            "Spin 2 (60-80)": [(), {"from_": 60, "to": 80}],
        }
        self.multi_spin = LabeledMultiSpinbox(right, "LabeledMultiSpinbox", config=conf)
        default_pack(self.multi_spin)

        self.labeled_counter = LabeledCounter(right, "Labeled Counter")
        default_pack(self.labeled_counter)
        self.labeled_float_counter = LabeledFloatCounter(
            right, "Labeled Counter", integer_level=2, step=0.2
        )
        default_pack(self.labeled_float_counter)
        self.labeled_multi_counter = LabeledMultiCounter(
            right,
            "LabeledMultiCounter",
            {"Counter A": ((), {}), "Counter B": ((), {})},
        )
        default_pack(self.labeled_multi_counter)
        self.labeled_multi_float_counter = LabeledMultiFloatCounter(
            right,
            "LabeledMultiFloatCounter",
            {"Counter A": ((), {}), "Counter B": ((), {})},
        )
        default_pack(self.labeled_multi_float_counter)

        default_pack(ttk.Button(self, command=self.on_button_click, text="Run Test"))
        self.copy_box = CopyBox(self)
        self.copy_box.pack(fill=tk.BOTH, expand=True, padx=5)

    def on_button_click(self, event=None):
        entry_value = self.entry.get()
        self.entry.clear()
        entries_value = json.dumps(self.entries.get(), indent=4)
        self.entries.clear()
        path_value = self.path_entry.get()
        self.path_entry.clear()
        dir_value = self.dir_entry.get()
        self.dir_entry.clear()
        option_value = self.option_menu.get()
        self.option_menu.clear()
        options_value = json.dumps(self.option_menus.get(), indent=4)
        self.option_menus.clear()
        check_value = self.check_button.get()
        self.check_button.clear()
        checks_value = json.dumps(self.check_buttons.get(), indent=4)
        self.check_buttons.clear()
        # Col 2
        box_value = self.box.get()
        self.box.clear()
        boxes_value = json.dumps(self.boxes.get(), indent=4)
        self.boxes.clear()
        radio_value = self.radio.get()
        self.radio.clear()
        radios_value = json.dumps(self.radios.get(), indent=4)
        self.radios.clear()
        # Col 3
        cycle_value = json.dumps(self.cycle.get(), indent=4)
        self.cycle.clear()
        multi_cycle_value = json.dumps(self.multi_cycle.get(), indent=4)
        self.multi_cycle.clear()

        col_1_values = "Entry Value: {}\nPath Value: {}\nDir Value: {}\nMulti Entry Value: {}\nOption Value: {}\nMulti Option Value: {}\nCheck Value: {}\nMulti Check Value: {}\n".format(
            entry_value,
            path_value,
            dir_value,
            entries_value,
            option_value,
            options_value,
            check_value,
            checks_value,
        )

        col_2_values = "Combobox Value: {}\nMulti Combobox Value: {}\nRadio Value: {}\nRadios Value: {}\n".format(
            box_value,
            boxes_value,
            radio_value,
            radios_value,
        )

        col_3_values = "CycleButton Value: {}\nMultiCycleButton Value: {}\n".format(
            cycle_value, multi_cycle_value
        )

        self.copy_box.set(col_1_values + col_2_values + col_3_values)


class LoadingBarDemo(Tab):
    def __init__(self, notebook: ttk.Notebook):
        Tab.__init__(self, notebook, "Bars & Scales")
        self.progress_bar = LabeledProgressbar(self, "Labeled Progress Bar")
        default_pack(self.progress_bar)
        self.slider = LabeledScale(self, "Labeled Scale", default=50)
        # self.progress_bar.set(self.slider.get())
        self.progress_bar.link(self.slider)
        default_pack(self.slider)
        default_separator(self)

        progress_config = {
            "A": ([], {}),
            "B": ([], {}),
            "C": ([], {}),
            "D": ([], {}),
        }
        self.progress_bars = LabeledMultiProgressbar(
            self, "Labeled Progress Bars", progress_config
        )
        default_pack(self.progress_bars)
        slider_options = {
            "A": ([], {"default": 0}),
            "B": ([], {"default": 25}),
            "C": ([], {"default": 50}),
            "D": ([], {"default": 75}),
        }
        self.sliders = LabeledMultiScale(self, "Labeled Scales", slider_options)
        default_pack(self.sliders)
        self.progress_bars.link(self.sliders.widgets)
        # self.progress_bars.set(self.sliders.get())
        default_separator(self)

        vertical_slider_frame = ttk.Frame(self)
        vertical_slider_frame.pack(
            fill="x", expand=tk.NO, side=tk.TOP, padx=10, pady=(0, 10)
        )

        self.v_progress_bar = LabeledProgressbar(
            vertical_slider_frame, "VBar", orient=tk.VERTICAL
        )
        default_vertical_pack(self.v_progress_bar)
        self.v_slider = LabeledScale(
            vertical_slider_frame,
            "VScl",
            orient=tk.VERTICAL,
            from_=100,
            to=0,
            default=10,
        )
        self.v_progress_bar.link(self.v_slider)
        default_vertical_pack(self.v_slider)
        default_vertical_separator(vertical_slider_frame)

        v_keys = ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]
        v_progress_options = {}
        v_slider_options = {}
        for k in v_keys:
            v_progress_options[k] = ([], {})
            v_slider_options[k] = (
                [],
                {
                    "from_": 100,
                    "to": 0,
                    "default": 50 + 30 * sin(v_keys.index(k) / 1.9),
                },
            )
        self.v_progress_bars = LabeledMultiProgressbar(
            vertical_slider_frame,
            "Labeled Vertical Progress Bars",
            v_progress_options,
            orient=tk.VERTICAL,
        )
        default_vertical_pack(self.v_progress_bars, expand=True)
        self.v_sliders = LabeledMultiScale(
            vertical_slider_frame,
            "Labeled Vertical Scales",
            v_slider_options,
            orient=tk.VERTICAL,
        )
        default_vertical_pack(self.v_sliders, expand=True, padx=(20, 0))
        self.v_progress_bars.link(self.v_sliders.widgets)
        default_separator(self)

        self.smooth_val = 0.0

        def update_smooth():
            self.smooth_val += 1
            self.determinate_smooth_loading_bar.set(self.smooth_val % 100)
            self.after(10, update_smooth)

        self.determinate_smooth_loading_bar = LabeledProgressbar(self, " Smooth")
        self.after(0, update_smooth)
        default_pack(self.determinate_smooth_loading_bar)

        self.stepped_val = 0.0

        def update_stepped():
            self.stepped_val += 6
            self.determinate_stepped_loading_bar.set(self.stepped_val % 100)
            self.after(400, update_stepped)

        self.after(0, update_stepped)
        self.determinate_stepped_loading_bar = LabeledProgressbar(
            self, " Stepped", labelside=tk.RIGHT
        )
        default_pack(self.determinate_stepped_loading_bar)
        default_separator(self)

        self.indeterminate_loading_bar = LabeledProgressbar(
            self, " Indeterminate", labelside=tk.TOP, mode="indeterminate"
        )
        self.indeterminate_loading_bar.start()
        default_pack(self.indeterminate_loading_bar)

        self.looped_val = 0.0

        def update_looped():
            self.looped_val += 1.1
            mod_val = self.looped_val % 100
            self.indeterminate_loading_looped_bar.set(mod_val)
            self.indeterminate_loading_looped_bar.label.configure(
                text=f" Indeterminate Looped: {str(mod_val)[:4]}%"
            )
            self.after(22, update_looped)

        self.after(0, update_looped)
        self.indeterminate_loading_looped_bar = LabeledProgressbar(
            self, " Indeterminate Looped", labelside=tk.BOTTOM, mode="indeterminate"
        )
        self.indeterminate_loading_looped_bar.label.configure(anchor="center")
        default_pack(self.indeterminate_loading_looped_bar)


# class ComboRadioTab(Tab):
#     def __init__(
#         self,
#         notebook: ttk.Notebook,
#     ):
#         Tab.__init__(self, notebook, "Radios & Combos")
# #         self.box = LabeledCombobox(
# #             self, "Labeled Combobox", values=("A", "B"), default=0
# #         )
# #         default_pack(self.box)
# #         conf = {
# #             "Box 1": ([], {"values": ("C", "D"), "default": 0}),
# #             "Box 2": ([], {"values": ("E", "F"), "default": 1}),
# #             "Box 3": ([], {"values": ("G", "H"), "default": 0}),
# #         }
# #         self.boxes = LabeledMultiCombobox(self, "Labeled Multi Combobox", config=conf)
# #         default_pack(self.boxes)
# #         default_separator(self)
#
# #         options = ["Option 1", "Option 2", "Option 3"]
# #         self.radio = LabeledSimpleRadioTable(
# #             self, "Labeled Radiobuttons", options=options, default=0
# #         )
# #         default_pack(self.radio)
#
# #         conf = {
# #             "Radios 1": ([["Option 4", "Option 5", "Option 6"]], {"default": 1}),
# #             "Radios 2": ([["Option 7", "Option 8", "Option 9"]], {"default": 2}),
# #         }
# #         self.radios = LabeledMultiSimpleRadioTable(
# #             self, "Labeled Multi Radiobuttons", config=conf
# #         )
# #         default_pack(self.radios)
# #         default_separator(self)

#         run_button = ttk.Button(self, command=self.on_button_click, text="Run Test")
#         default_pack(run_button)

#         self.copy_box = CopyBox(self)
#         self.copy_box.pack(fill=tk.BOTH, expand=True, padx=5)

#     def on_button_click(self, event=None):
#         box_value = self.box.get()
#         self.box.clear()
#         boxes_value = json.dumps(self.boxes.get(), indent=4)
#         self.boxes.clear()
#         radio_value = self.radio.get()
#         self.radio.clear()
#         radios_value = json.dumps(self.radios.get(), indent=4)
#         self.radios.clear()
#         self.copy_box.set(
#             "Combobox Value: {}\nMulti Combobox Value: {}\nRadio Value: {}\nRadios Value: {}".format(
#                 box_value, boxes_value, radio_value, radios_value
#             )
#         )


class ToolTipTab(Tab):
    def __init__(
        self,
        notebook: ttk.Notebook,
    ):
        Tab.__init__(self, notebook, "Tooltips")
        header = ttk.Frame(self)
        header.pack(fill="x", expand=False, side=tk.TOP)
        self.entry_x = LabeledEntry(header, labeltext="Width", default=5)
        self.entry_y = LabeledEntry(header, labeltext="Height", default=5)
        button = ttk.Button(header, text="Rebuild", command=self.remake)
        for w in (self.entry_x, self.entry_y, button):
            w.pack(fill=tk.BOTH, expand="true", side=tk.LEFT)
        self.container = None  # placeholder for ttk frame

    def remake(self, evt=None):
        if self.container:
            self.container.destroy()
        self.container = ttk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True, side=tk.TOP, padx=5, pady=5)
        width = self.entry_x.get()
        try:
            width = int(width)
        except:
            self.entry_x.set("Err")
            return
        height = self.entry_y.get()
        try:
            height = int(height)
        except:
            self.entry_y.set("Err")
            return
        for y in range(height):
            f = ttk.Frame(self.container)
            f.pack(fill=tk.BOTH, expand="true", side=tk.TOP)
            for x in range(width):
                val = width * y + x
                val = f"00{val}" if val < 10 else (f"0{val}" if val < 100 else val)
                b = ttk.Button(
                    f,
                    text=val,
                    padding=0,
                    width=0,
                    command=lambda val=val: print(f"Pressed {val}"),
                )
                b.pack(fill=tk.BOTH, expand="true", side=tk.LEFT)
                ToolTip(b, f"Tooltip for button {val}")


class CanvasTab(Tab):
    def __init__(
        self,
        notebook: ttk.Notebook,
    ):
        Tab.__init__(self, notebook, "Canvas")
        self.canvas = TiledCanvas(
            self,
            on_mouse_move=self.update,
            on_tile_left_click=print,
            override_tile_width=True,
        )
        self.footer = ttk.Frame(self)
        self.footer.pack(side=tk.BOTTOM, fill="x", expand=False)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.info_var = tk.StringVar()
        default_separator(self.footer, pady=0, padx=0)
        self.info_label = ttk.Label(self.footer, textvariable=self.info_var)
        default_pack(self.info_label)
        self.canvas.tiles = [ExampleTile(self.canvas, i) for i in range(1000)]
        self.canvas.refresh()

    def update(self, event, pos):
        x, y = pos
        t = self.canvas.hovered.text if self.canvas.hovered else "N/A"
        self.info_var.set(f"Pos: {event.x} {event.y} | AdjPos: {x}, {y} | Hovered: {t}")


class PasswordEntryTab(Tab):
    def __init__(self, notebook, *args, **kwargs):
        Tab.__init__(self, notebook, "Password Entry")
        self.password_entry = PasswordEntry(self)
        self.password_entry.pack(fill=tk.BOTH, expand=False, padx=10, pady=10)


class DemoTableTab(TreeTableTab):
    def __init__(self, notebook):
        data = {
            "Label A": [i for i in range(100)],
            "Label B": [f"B{i}" for i in range(100)],
            "Label C": [f"C{i}" for i in range(100)],
        }
        TreeTableTab.__init__(
            self, notebook, "Table", table_contents=data, min_column_width=100
        )


class PopupsTab(Tab):
    def __init__(self, notebook, app):
        Tab.__init__(self, notebook, "Popup Windows")

        def on_yes(*args):
            print(f"Yes - {args}")

        def on_no(*args):
            print(f"No - {args}")

        def on_cancel(*args):
            print(f"Cancel - {args}")

        notice = lambda: NoticeWindow(text="Hello", window=app.window)
        prompt = lambda: PromptWindow(
            text="Hello", on_yes=on_yes, on_cancel=on_cancel, window=app.window
        )
        yesno = lambda: YesNoCancelWindow(
            text="Hello",
            on_yes=on_yes,
            on_no=on_no,
            on_cancel=on_cancel,
            window=app.window,
        )
        password = lambda: PasswordWindow(
            window=app.window,
            instruction_text="Logging in to nothing, this is a test...",
        )
        text = lambda: TextWindow(window=app.window)

        for b in [
            ttk.Button(self, text="Notice Window", command=notice),
            ttk.Button(self, text="YesNo Window", command=yesno),
            ttk.Button(self, text="Prompt Window", command=prompt),
            ttk.Button(self, text="Password Window", command=password),
            ttk.Button(self, text="Text Window", command=text),
        ]:
            b.pack(side=tk.TOP, fill="x", padx=10, pady=0)


class ConstrainedTab(Tab):
    def __init__(self, notebook):
        Tab.__init__(self, notebook, "Constrained")

        (left := ttk.Frame(self)).pack(
            fill="both", expand="true", side="left", pady=10, padx=(20, 10)
        )
        (middle := ttk.Frame(self)).pack(
            fill="both", expand="true", side="left", pady=10, padx=10
        )
        (right := ttk.Frame(self)).pack(
            fill="both", expand="true", side="left", pady=10, padx=(10, 20)
        )

        self.int = LabeledIntEntry(left, "Int Entry")
        self.int.pack(side="top", fill="x", expand=False)
        conf = {"Int 1": ([], {}), "Int 2": ([], {})}
        self.multi_int = LabeledMultiIntEntry(left, "Multi Int Entry", conf)
        self.multi_int.pack(side="top", fill="x", expand=False)
        default_separator(left)
        self.float = LabeledFloatEntry(left, "Float Entry")
        self.float.pack(side="top", fill="x", expand=False)
        conf = {"Float 1": ([], {}), "Float 2": ([], {})}
        self.multi_float = LabeledMultiFloatEntry(left, "Multi Float Entry", conf)
        self.multi_float.pack(side="top", fill="x", expand=False)
        default_separator(left)
        self.lowercase = LabeledLowercaseEntry(left, "Lowercase Entry")
        self.lowercase.pack(side="top", fill="x", expand=False)
        conf = {"Lowercase 1": ([], {}), "Lowercase 2": ([], {})}
        self.multi_lowercase = LabeledMultiLowercaseEntry(
            left, "Multi Lowercase Entry", conf
        )
        self.multi_lowercase.pack(side="top", fill="x", expand=False)
        default_separator(left)
        self.uppercase = LabeledUppercaseEntry(left, "Uppercase Entry")
        self.uppercase.pack(side="top", fill="x", expand=False)
        conf = {"Uppercase 1": ([], {}), "Uppercase 2": ([], {})}
        self.multi_uppercase = LabeledMultiUppercaseEntry(
            left, "Multi Uppercase Entry", conf
        )
        self.multi_uppercase.pack(side="top", fill="x", expand=False)

        # Middle Transistion
        # #
        self.letters = LabeledLettersEntry(middle, "Letters Entry")
        self.letters.pack(side="top", fill="x", expand=False)
        conf = {"Letters 1": ([], {}), "Letters 2": ([], {})}
        self.multi_letters = LabeledMultiLettersEntry(
            middle, "Multi Letters Entry", conf
        )
        self.multi_letters.pack(side="top", fill="x", expand=False)
        default_separator(middle)
        self.digits = LabeledDigitsEntry(middle, "Digits Entry")
        self.digits.pack(side="top", fill="x", expand=False)
        conf = {"Digits 1": ([], {}), "Digits 2": ([], {})}
        self.multi_digits = LabeledMultiDigitsEntry(middle, "Multi Digits Entry", conf)
        self.multi_digits.pack(side="top", fill="x", expand=False)
        default_separator(middle)
        self.uppercasedigits = LabeledUppercaseDigitsEntry(
            middle, "Uppercase Digits Entry"
        )
        self.uppercasedigits.pack(side="top", fill="x", expand=False)
        conf = {"Uppercase Digits 1": ([], {}), "Uppercase Digits 2": ([], {})}
        self.multi_uppercasedigits = LabeledMultiUppercaseDigitsEntry(
            middle, "Multi Uppercase Digits Entry", conf
        )
        self.multi_uppercasedigits.pack(side="top", fill="x", expand=False)
        default_separator(middle)
        self.lowercase = LabeledLowercaseDigitsEntry(middle, "Lowercase Digits Entry")
        self.lowercase.pack(side="top", fill="x", expand=False)
        conf = {"Lowercase Digits 1": ([], {}), "Lowercase Digits 2": ([], {})}
        self.multi_lowercase = LabeledMultiLowercaseDigitsEntry(
            middle, "Multi Lowercase Digits Entry", conf
        )
        self.multi_lowercase.pack(side="top", fill="x", expand=False)

        # Right Transition
        # #
        self.lettersdigits = LabeledLettersDigitsEntry(right, "Letters Digits Entry")
        self.lettersdigits.pack(side="top", fill="x", expand=False)
        conf = {"Letters Digits 1": ([], {}), "Letters Digits 2": ([], {})}
        self.multi_lettersdigits = LabeledMultiLettersDigitsEntry(
            right, "Multi Letter Digits Entry", conf
        )
        self.multi_lettersdigits.pack(side="top", fill="x", expand=False)
        default_separator(right)
        self.hexdigits = LabeledHexdigitsEntry(right, "Hexdigits Entry")
        self.hexdigits.pack(side="top", fill="x", expand=False)
        conf = {"Hexdigits 1": ([], {}), "Hexdigits 2": ([], {})}
        self.multi_hexdigits = LabeledMultiHexdigitsEntry(
            right, "Multi Hexdigits Entry", conf
        )
        self.multi_hexdigits.pack(side="top", fill="x", expand=False)
        default_separator(right)
        self.octdigits = LabeledOctdigitsEntry(right, "Octdigits Entry")
        self.octdigits.pack(side="top", fill="x", expand=False)
        conf = {"Octdigits 1": ([], {}), "Octdigits 2": ([], {})}
        self.multi_octdigits = LabeledMultiOctdigitsEntry(
            right, "Multi Octdigits Entry", conf
        )
        self.multi_octdigits.pack(side="top", fill="x", expand=False)
        default_separator(right)
        self.printable = LabeledOctdigitsEntry(right, "Printable Entry")
        self.printable.pack(side="top", fill="x", expand=False)
        conf = {"Printable 1": ([], {}), "Printable 2": ([], {})}
        self.multi_printable = LabeledMultiOctdigitsEntry(
            right, "Multi Printable Entry", conf
        )
        self.multi_printable.pack(side="top", fill="x", expand=False)


class GifTab(Tab):
    def __init__(self, notebook):
        Tab.__init__(self, notebook, "GIF Viewer")
        self.gif = GifLoader(get_asset("test.gif"))
        self.viewer = GifViewer(self.gif, self)
        self.viewer.pack(fill=tk.BOTH, expand=True)


class PillowTab(Tab):
    def __init__(self, notebook: ttk.Notebook):
        Tab.__init__(self, notebook, "Pillow Widgets")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.gif_tab = GifTab(self.notebook)


class ToolsTab(Tab):
    def __init__(self, notebook: ttk.Notebook):
        Tab.__init__(self, notebook, "Tools")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.wattage_tab = WattageTab(self.notebook)
        self.timecard_tab = TimecardTab(self.notebook)


class ListboxTab(Tab):
    def __init__(self, notebook: ttk.Notebook):
        Tab.__init__(self, notebook, "Listboxes")
        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        default_pack(
            ActiveLabel(self.frame, default="OrderedListbox", style="LargeBold.TLabel")
        )
        lb = OrderedListbox(self.frame)
        lb.pack(fill="x", side="top")

        default_pack(
            ActiveLabel(self.frame, default="ListManipulator", style="LargeBold.TLabel")
        )
        lb2 = ListManipulator(self.frame)
        lb2.pack(fill="x", side="top")

        for l in [lb]:
            for i in range(300):
                l.add(i)
        lb.disable()


# class CounterTab(Tab):
#     def __init__(self, notebook: ttk.Notebook):
#         Tab.__init__(self, notebook, "Counters")
#         self.frame = ttk.Frame(self)
#         self.frame.pack(fill=tk.BOTH, expand=True)
#         self.labeled_counter = LabeledCounter(self.frame, "Labeled Counter")
#         default_pack(self.labeled_counter)
#         self.labeled_float_counter = LabeledFloatCounter(
#             self.frame, "Labeled Counter", integer_level=2, step=0.2
#         )
#         default_pack(self.labeled_float_counter)
#         self.labeled_multi_counter = LabeledMultiCounter(
#             self.frame,
#             "LabeledMultiCounter",
#             {"Counter A": ((), {}), "Counter B": ((), {})},
#         )
#         default_pack(self.labeled_multi_counter)
#         self.labeled_multi_float_counter = LabeledMultiFloatCounter(
#             self.frame,
#             "LabeledMultiFloatCounter",
#             {"Counter A": ((), {}), "Counter B": ((), {})},
#         )
#         default_pack(self.labeled_multi_float_counter)


class CopyBoxTab(Tab):
    def __init__(self, notebook: ttk.Notebook):
        Tab.__init__(self, notebook, "CopyBoxes")
        (frame := ttk.Frame(self)).pack(fill=tk.BOTH, expand=True)
        (lcb := LabeledCopyBox(frame, "Labeled CopyBox")).pack(fill="x", expand=True)
        lcb.set(lorem(3))
        # LabeledMultiCopyBox


class FontTab(Tab):
    def __init__(self, notebook: ttk.Notebook, app: App):
        Tab.__init__(self, notebook, "Fonts")
        self.app = app
        styles = app.generated_styles
        great = [s for s in styles if s.startswith("Great")]
        good = [s for s in styles if s.startswith("Good")]
        warn = [s for s in styles if s.startswith("Warn")]
        error = [s for s in styles if s.startswith("Error")]
        critical = [s for s in styles if s.startswith("Critical")]
        normal = [
            s
            for s in styles
            if not any((s in i for i in (great, good, warn, error, critical)))
        ]
        (colsa := ColumnFrame(self, 3)).pack(fill="x")
        (colsb := ColumnFrame(self, 3)).pack(fill="x")
        for (stys, f) in zip(
            (great, good, normal, warn, error, critical), (*colsa.frames, *colsa.frames)
        ):
            for s in stys:
                if s.endswith("TLabel"):
                    ActiveLabel(f, default=s.replace(".TLabel", ""), style=s).pack(
                        fill="x"
                    )

        (chooser_frame := ttk.LabelFrame(self, text="font_chooser")).pack(
            fill="x", expand=True
        )
        ttk.Button(chooser_frame, command=self.set_font, text="Select Font").pack(
            side="top"
        )
        self.font_var = tk.StringVar(value="Selected Font: None")
        self.font_label = ttk.Label(chooser_frame, textvariable=self.font_var)
        self.font_label.pack(side="top")

    def set_font(self):
        self.font_var.set(f"Selected Font: {tcl_choose_font(self.app.window)}")


# class SpinboxTab(Tab):
#     def __init__(self, notebook: ttk.Notebook):
#         Tab.__init__(self, notebook, "Spinboxes")
#         (frame := ttk.Frame(self)).pack(fill=tk.BOTH, expand=True)
#         self.spinbox = LabeledSpinbox(frame, "Labeled Spinbox", from_=0, to=500)
#         self.spinbox.pack()
#         # LabeledMultiSpinbox


# class ButtonTab(Tab):
#     def __init__(self, notebook: ttk.Notebook):
#         Tab.__init__(self, notebook, "Buttons")
#         (frame := ttk.Frame(self)).pack(fill=tk.BOTH, expand=True)
#         LabeledCycleButton(
#             frame,
#             "LabeledCycleButton (0->5)",
#             tuple(str(i) for i in range(6)),
#             command=print,
#         ).pack(fill="x", padx=20)


class BasicWidgetsTab(Tab):
    def __init__(self, notebook: ttk.Notebook, app):
        Tab.__init__(self, notebook, "Basic Widgets")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.form_tab = FormWidgetDemoTab(self.notebook)
        # self.button_tab = ButtonTab(self.notebook)
        # self.spinbox_tab = SpinboxTab(self.notebook)
        self.copybox_tab = CopyBoxTab(self.notebook)
        self.constrained_tab = ConstrainedTab(self.notebook)

        # self.counter_tab = CounterTab(self.notebook)
        self.listbox_tab = ListboxTab(self.notebook)
        self.table_tab = DemoTableTab(self.notebook)
        self.textbox_tab = TextBoxTestTab(self.notebook)
        self.loading_bar = LoadingBarDemo(self.notebook)
        # self.combo_tab = ComboRadioTab(self.notebook)
        self.popups_tab = PopupsTab(self.notebook, app)
        self.password_tab = PasswordEntryTab(self.notebook)


# class MessageTab(Tab):
#     def __init__(self, notebook: ttk.Notebook):
#         Tab.__init__(self, notebook, "Message Widget")

#         tk.Message(self, text="Test").pack(fill="x")


class ExampleApp(App):
    """Example Implementation"""

    def __init__(self):
        App.__init__(self, "ini.json")

        self.basic = BasicWidgetsTab(self.notebook, self)
        self.fonts = FontTab(self.notebook, self)
        self.shopping_list = ShoppingListTab(self.notebook, self)
        if PILLOW_AVAILABLE:
            self.pillow_tab = PillowTab(self.notebook)
        self.tools = ToolsTab(self.notebook)
        self.note_tab = NotesTab(self.notebook, self)
        self.chat_tab = ConversationsTab(self.notebook, self)
        self.canvas_tab = CanvasTab(self.notebook)
        self.tooltip_demp = ToolTipTab(self.notebook)
        self.links_tab = BrowserLauncherTab(self.notebook, "Quick Links", links)
        self.apps_tab = CommandLauncherTab(self.notebook, "Applications", apps)
        self.console_tab = ConsoleTab(self.notebook)
        self.console_tab.console.command = self.console_tab.console.print
        # self.message_tab = MessageTab(self.notebook)
        self.use_theme()  # Do this last to apply theme to text boxes
        # Center window
        tcl_center_window(self.window)
        # play bell to indicate window is loaded
        tcl_bell(self.window)
        # print(tcl_font_chooser(self.window))

        # tcl_download_file(
        #     self.window, "http://file-examples.com/", "example.html", loadafter=True
        # )


app = ExampleApp()
app.mainloop()
