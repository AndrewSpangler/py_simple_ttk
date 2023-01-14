import io, json, tempfile
import tkinter as tk
from tkinter import ttk
from py_simple_ttk import FormApp, CopyBox, default_separator, default_pack

test_data = {
    "config": {
        "application": "Form Test",
        "version": "0.0.1",
        "width": 800,
        "height": 600,
        "minwidth": 60,
        "minheight": 60,
        "resizable_width": True,
        "resizable_height": True,
        "start_maximized": False,
        "start_fullscreen": False,
        "enable_fullscreen": True,
        "scaling": 1.5,
        "enable_themes_menu": True,
        "enable_profiles": False,
        "enable_launcher": False,
        "movable_tabs": False,
        "conversations_enabled": False,
        "notes_enabled": False,
    },
    "body": [
        # ('definer', 'label', 'args:list', 'kwargs:dict', 'children:list'),
        ("LabeledLettersEntry", "Letters"),
        ("LabeledIntEntry", "Int"),
        ("LabeledLowercaseEntry", "Lowercase"),
        ("LabeledFloatCounter", "Float Counter"),
        ("default_separator",),
        (
            "mw",
            "Multi",
            [],
            {
                "children": [
                    ("LabeledLettersEntry", "Letters5"),
                    ("LabeledLettersEntry", "Letters6"),
                    ("LabeledLettersEntry", "Letters7"),
                    ("LabeledLettersEntry", "Letters8"),
                ]
            },
        ),
        ("default_separator",),
        (
            "LabeledMultiOptionMenu",
            "Options",
            (
                {
                    "Menu 1": ([["Option A", "Option B"]], {}),
                    "Menu 2": ([["ALPHA", "BRAVO"]], {"default": 1}),
                    "Menu 3": ([["A", "B", "C", "D", "E"]], {"default": 4}),
                },
            ),
        )
        # (
        #     "LabeledSimpleRadioTable",
        #     "Radios",
        #     (),
        #     {"options": ("A", "B", "C", "D", "E", "F", "G"), "columns": 1},
        # ),
    ],
}


class TestFormApp(FormApp):
    def __init__(self):
        tp = tempfile.NamedTemporaryFile(delete=False)
        tp.write(bytes(json.dumps(test_data), "utf-8"))
        tp.flush()
        FormApp.__init__(self, tp.name)

        # ttk.Button(self.body, text="Test", command=self.test).pack(fill="x")

    #     self.copy_box = CopyBox(self.body)

    #     default_pack(self.copy_box)
    #     self.test()

    # def test(self):
    #     self.copy_box.set(json.dumps(self.forms["body"].get(), indent=4))


if __name__ == "__main__":
    TestFormApp().mainloop()
