"""
Generate functional widgets from json config files
All widgets spawn from a single MultiWidget Core
If the app is tabular it must be specified, each tab will be treated like it's own entity, eg tabs can't interact
"""
"""
Todo:
Custom Multi Widgets?
Tooltips should be simple
Name option to widgets?

bindings = {"on_left_click":{"target":NAME, action=ACTION}}
output="FILE"/"COPYBOX"
# Make widgets smart and be able too look up other widgets in the muti-widget with a "target" argument
"""

import io, json, tempfile
import tkinter as tk
from tkinter import ttk
from .app import App
from .widgets import (
    Tab,
    form_widgets_list,
    LabeledMultiWidgetMixin,
    default_pack,
    default_separator,
)

# print("\n\n")
# for f in form_widgets_list:
#     print(f.__name__)
# print("\n\n")

form_widget_map = {w.__name__: w for w in form_widgets_list}


class FormApp(App):
    def __init__(self, form_file: str):
        if isinstance(form_file, str):
            with open(form_file) as f:
                form = json.load(f)
        elif isinstance(form_file, dict):
            form = form_file
        else:
            raise TypeError(f"Invalid form_file argument type: {type(form_file)}")
        tp = tempfile.NamedTemporaryFile(delete=False)
        tp.write(bytes(json.dumps(form["config"]), "utf-8"))
        tp.flush()
        App.__init__(self, tp.name)
        if isinstance(form["body"], dict):
            self.tabular = True
            self.forms = {}
            for name in form["body"]:
                tab = Tab(self.notebook, name)
                self.forms[name] = self.build_form_section(
                    tab, name, form["body"][name]
                )
        elif isinstance(form["body"], list):
            self.tabular = False
            self.notebook.pack_forget()
            self.notebook.destroy()
            self.body = ttk.Frame(self.window)
            self.body.pack(fill="both", expand=True)
            self.forms = {
                "body": self.build_form_section(
                    self.body, self.ini_data["application"], form["body"]
                )
            }
        else:
            raise ValueError(f"Invalid body type - {type(form['body'])}")

    def build_form_section(
        self, parent, name: str, section_config: dict
    ) -> LabeledMultiWidgetMixin:
        (widget := LabeledMultiWidgetMixin(parent, name, None, {})).pack(fill="x")
        for widget_config in section_config:
            if not len(widget_config) >= 1:
                raise f"Invalid widget config - {widget_config}\nShould have form ('class definer (string)', 'label (string)', 'args (optional)', 'kwargs (optional)')"

            # fmt: off
            def handle_widget(
                par,
                widg,
                definer: str,
                label: str = None,
                args: list = [],
                kwargs: dict = {},
            ) -> object:  

                def handle_separator(p, label, args, kw):
                    return default_separator(p)

                def handle_multi_widget(p, label, args, kw):
                    subwidget = widg.add(p, label, (None, {}),  {}, widget_type=LabeledMultiWidgetMixin)
                    if (childen := kw.get("children")):
                        for conf in childen:
                            handle_widget(subwidget, subwidget, *conf)
                    return subwidget

                handlers = {
                    # Separator
                    "default_separator": handle_separator,
                    "sep": handle_separator,
                    "separator": handle_separator,
                    "hr": handle_separator,
                    "LabeledMultiWidget": handle_multi_widget,
                    "mw": handle_multi_widget,
                }

                if definer in handlers:
                    return handlers[definer](par, label, args, kwargs)

                classobj = form_widget_map.get(definer)
                if not classobj:
                    raise ValueError(f"Invalid definer - {typestring}")
                return widg.add(par, label, args, kwargs, widget_type=classobj)

            handle_widget(parent, widget, *widget_config)
        return widget
