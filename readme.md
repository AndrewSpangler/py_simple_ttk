# py_simple_ttk 0.1.29<a name="mark0"></a>

***Themes don't have to be hard.***

- [About](#mark1)
- [Requirements](#mark2)
- [Configuring ini.json](#mark3)
- [The App Object](#mark4)
	- [App](#mark5)
- [Core Widgets](#mark6)
	- [MultiWidgetMixin](#mark7)
	- [SuperWidgetMixin](#mark8)
- [Tabs](#mark9)
	- [Tab](#mark10)
	- [LauncherTab](#mark11)
	- [BrowserLauncherTab](#mark12)
	- [CommandLauncherTab](#mark13)
	- [ConsoleTab](#mark14)
	- [TableTab](#mark15)
	- [TreeTableTab](#mark16)
- [Widgets](#mark17)
	- [Button Widgets](#mark18)
		- [ActiveButton](#mark19)
		- [LabeledButton](#mark20)
		- [LabeledMultiButton](#mark21)
		- [CycleButton](#mark22)
		- [LabeledCycleButton](#mark23)
		- [LabeledMultiCycleButton](#mark24)
	- [Core Functions](#mark25)
		- [bbox_to_width_and_height](#mark26)
		- [center_window](#mark27)
		- [check_in_bounds](#mark28)
		- [complex_widget_search](#mark29)
		- [copy_to_user_clipboard](#mark30)
		- [create_round_rectangle](#mark31)
		- [default_pack](#mark32)
		- [default_separator](#mark33)
		- [default_vertical_pack](#mark34)
		- [default_vertical_separator](#mark35)
		- [enable_notebook_movement](#mark36)
		- [focus_next](#mark37)
		- [force_aspect](#mark38)
		- [get_asset](#mark39)
		- [get_bundled_themes_list](#mark40)
		- [get_generated_font_images_lookup](#mark41)
		- [get_local_appdata_folder](#mark42)
		- [get_themes_folder](#mark43)
		- [make_aspect_frames](#mark44)
		- [open_link](#mark45)
		- [recursive_widget_search](#mark46)
		- [run_cl](#mark47)
	- [Canvas Widgets](#mark48)
		- [ResizableCanvas](#mark49)
		- [ScrolledCanvas](#mark50)
		- [TiledCanvas](#mark51)
		- [ExampleTile](#mark52)
	- [Checkbutton Widgets](#mark53)
		- [ActiveCheckbutton](#mark54)
		- [LabeledCheckbutton](#mark55)
		- [LabeledMultiCheckbutton](#mark56)
	- [Combobox Widgets](#mark57)
		- [ActiveCombobox](#mark58)
		- [LabeledCombobox](#mark59)
		- [LabeledMultiCombobox](#mark60)
	- [Console Widgets](#mark61)
		- [ConsoleWidget](#mark62)
	- [Constraining Functions](#mark63)
		- [check_entry_type](#mark64)
		- [check_entry_int](#mark65)
		- [check_entry_float](#mark66)
		- [check_entry_contents](#mark67)
		- [check_entry_ascii_lowercase](#mark68)
		- [check_entry_ascii_uppercase](#mark69)
		- [check_entry_ascii_letters](#mark70)
		- [check_entry_ascii_digits](#mark71)
		- [check_entry_ascii_uppercase_digits](#mark72)
		- [check_entry_ascii_lowercase_digits](#mark73)
		- [check_entry_ascii_hexdigits](#mark74)
		- [check_entry_ascii_octdigits](#mark75)
		- [check_entry_ascii_letters_digits](#mark76)
		- [check_entry_ascii_printable](#mark77)
	- [Counter Widgets](#mark78)
		- [Counter](#mark79)
		- [FloatCounter](#mark80)
		- [LabeledCounter](#mark81)
		- [LabeledFloatCounter](#mark82)
		- [LabeledMultiCounter](#mark83)
		- [LabeledMultiFloatCounter](#mark84)
	- [Entry Widgets](#mark85)
		- [ActiveEntry](#mark86)
		- [ScrolledEntry](#mark87)
		- [LabeledEntry](#mark88)
		- [LabeledMultiEntry](#mark89)
		- [LabeledButtonEntry](#mark90)
		- [LabeledMultiButtonEntry](#mark91)
		- [LabeledPathEntry](#mark92)
		- [LabeledMultiPathEntry](#mark93)
		- [PasswordEntry](#mark94)
		- [LabeledPasswordEntry](#mark95)
		- [LabeledMultiPasswordEntry](#mark96)
		- [ConstrainedEntry](#mark97)
		- [LabeledConstrainedEntry](#mark98)
		- [LabeledMultiConstrainedEntry](#mark99)
		- [IntEntry](#mark100)
		- [LabeledIntEntry](#mark101)
		- [LabeledMultiIntEntry](#mark102)
		- [FloatEntry](#mark103)
		- [LabeledFloatEntry](#mark104)
		- [LabeledMultiFloatEntry](#mark105)
		- [LowercaseEntry](#mark106)
		- [LabeledLowercaseEntry](#mark107)
		- [LabeledMultiLowercaseEntry](#mark108)
		- [UppercaseEntry](#mark109)
		- [LabeledUppercaseEntry](#mark110)
		- [LabeledMultiUppercaseEntry](#mark111)
		- [LettersEntry](#mark112)
		- [LabeledLettersEntry](#mark113)
		- [LabeledMultiLettersEntry](#mark114)
		- [DigitsEntry](#mark115)
		- [LabeledDigitsEntry](#mark116)
		- [LabeledMultiDigitsEntry](#mark117)
		- [UppercaseDigitsEntry](#mark118)
		- [LabeledUppercaseDigitsEntry](#mark119)
		- [LabeledMultiUppercaseDigitsEntry](#mark120)
		- [LowercaseDigitsEntry](#mark121)
		- [LabeledLowercaseDigitsEntry](#mark122)
		- [LabeledMultiLowercaseDigitsEntry](#mark123)
		- [LettersDigitsEntry](#mark124)
		- [LabeledLettersDigitsEntry](#mark125)
		- [LabeledMultiLettersDigitsEntry](#mark126)
		- [HexdigitsEntry](#mark127)
		- [LabeledHexdigitsEntry](#mark128)
		- [LabeledMultiHexdigitsEntry](#mark129)
		- [OctdigitsEntry](#mark130)
		- [LabeledOctdigitsEntry](#mark131)
		- [LabeledMultiOctdigitsEntry](#mark132)
		- [PrintableEntry](#mark133)
		- [LabeledPrintableEntry](#mark134)
		- [LabeledMultiPrintableEntry](#mark135)
	- [Frame Widgets](#mark136)
		- [ColumnFrame](#mark137)
	- [KeyPad Widgets](#mark138)
		- [KeypadButton](#mark139)
		- [BaseKeypad](#mark140)
		- [DialerKeypad](#mark141)
	- [Labeler Widget](#mark142)
		- [ActiveButton](#mark143)
		- [LabeledButton](#mark144)
		- [LabeledMultiButton](#mark145)
		- [CycleButton](#mark146)
		- [LabeledCycleButton](#mark147)
		- [LabeledMultiCycleButton](#mark148)
	- [ListBox Widgets](#mark149)
		- [ScrolledListBox](#mark150)
		- [OrderedListbox](#mark151)
		- [Table](#mark152)
	- [OptionMenu Widgets](#mark153)
		- [ActiveOptionMenu](#mark154)
		- [LabeledOptionMenu](#mark155)
		- [LabeledMultiOptionMenu](#mark156)
	- [ProgressBar Widgets](#mark157)
		- [ActiveProgressbar](#mark158)
		- [LabeledProgressbar](#mark159)
		- [LabeledMultiProgressbar](#mark160)
	- [Radiobutton Widgets](#mark161)
		- [ActiveRadiobutton](#mark162)
		- [RadioTable](#mark163)
		- [LabeledRadioTable](#mark164)
		- [LabeledMultiRadioTable](#mark165)
		- [SimpleRadioTable](#mark166)
		- [LabeledSimpleRadioTable](#mark167)
		- [LabeledMultiSimpleRadioTable](#mark168)
	- [Scale Widgets](#mark169)
		- [ActiveScale](#mark170)
		- [LabeledScale](#mark171)
		- [LabeledMultiScale](#mark172)
	- [Spinbox Widgets](#mark173)
		- [ActiveSpinbox](#mark174)
		- [LabeledSpinbox](#mark175)
		- [LabeledMultiSpinbox](#mark176)
	- [Text Widgets](#mark177)
		- [ScrolledText](#mark178)
		- [CopyBox](#mark179)
		- [LabeledCopyBox](#mark180)
		- [LabeledMultiCopyBox](#mark181)
	- [Toplevel Widgets](#mark182)
		- [FocusedToplevel](#mark183)
		- [NoticeWindow](#mark184)
		- [YesNoCancelWindow](#mark185)
		- [PromptWindow](#mark186)
		- [PasswordWindow](#mark187)
		- [ListWindow](#mark188)
	- [Misc Widgets](#mark189)
		- [ToolTip](#mark190)
		- [EasySizegrip](#mark191)
- [SuperLib.utils](#mark192)
	- [Utils](#mark193)
		- [check_if_module_installed](#mark194)
		- [check_string_contains](#mark195)
		- [dummy_function](#mark196)
		- [get_friendly_time](#mark197)
		- [get_installed_packages](#mark198)
		- [get_unix_timestamp](#mark199)
		- [get_unix_timestring](#mark200)
		- [get_user_home_folder](#mark201)
		- [open_folder_in_explorer](#mark202)
		- [sort_dict_by_keys](#mark203)
		- [timer_decorator](#mark204)
	- [File Generators](#mark205)
		- [HTML_Generator](#mark206)
		- [TXT_Generator](#mark207)
		- [MD_Generator](#mark208)
	- [History Mixin](#mark209)
		- [HistoryMixin](#mark210)
	- [Color Functions](#mark211)
		- [reduce_255](#mark212)
		- [rgb_to_hex](#mark213)
		- [rgba_to_hex](#mark214)
		- [hex_to_rgb](#mark215)
		- [hex_to_rgba](#mark216)
		- [get_gradient](#mark217)
		- [rgb_to_scalar](#mark218)
		- [scalar_to_rgb](#mark219)
		- [linear_gradient](#mark220)
		- [get_rainbow](#mark221)
- [MegaWidgets](#mark222)
	- [Notes MegaWidget](#mark223)
		- [NotesTab](#mark224)
	- [Conversation MegaWidget](#mark225)
		- [ConversationsTab](#mark226)
	- [Profile Management](#mark227)
		- [ProfilesSystem](#mark228)
		- [UserProfile](#mark229)
		- [get_profiles_folder](#mark230)
		- [get_profiles_list](#mark231)
- [Changelog](#mark232)
	- [0.1.29](#mark233)
	- [0.1.28](#mark234)
	- [0.1.27](#mark235)
	- [0.1.26](#mark236)
	- [0.1.25](#mark237)
	- [0.1.24](#mark238)
	- [0.1.23](#mark239)
	- [0.1.22](#mark240)
	- [0.1.21](#mark241)
	- [0.1.20](#mark242)
	- [0.1.19](#mark243)
	- [0.1.18](#mark244)
	- [0.1.17](#mark245)
	- [0.1.16](#mark246)
	- [0.1.15](#mark247)
	- [0.1.14](#mark248)
	- [0.1.13](#mark249)
	- [0.1.12](#mark250)
	- [0.1.11](#mark251)
	- [0.1.10](#mark252)
	- [0.1.9](#mark253)
	- [0.1.8](#mark254)
	- [0.1.7](#mark255)
	- [0.1.6](#mark256)
	- [0.1.5](#mark257)
	- [0.1.4](#mark258)
	- [0.1.3](#mark259)
	- [0.1.2](#mark260)
	- [0.1.1](#mark261)
	- [0.1.0](#mark262)

---

# About<a name="mark1"></a>[^](#mark0)

py_simple_ttk exists because I got tired of rewriting the same code over and over for simple projects. The goal is to provide a variety of meta widgets with consistent get/set/enable/disable/destroy methods and mega-widgets that make ttk development easier and faster. Features include built-in theme support, a score of labeled and multi-widgets, tools for easy form building, a sample application demonstrating many of py_simple_ttk's features, a configuration file system, and much more. ![Lines of code](https://img.shields.io/tokei/lines/github/AndrewSpangler/py_simple_ttk)

# Requirements<a name="mark2"></a>[^](#mark0)



# Configuring ini.json<a name="mark3"></a>[^](#mark0)

```
+------------------------+-------------------------------------------+
|        Key             |                   Value                   |
+------------------------+-------------------------------------------+
| application            | Application Name (String)                 |
| version                | Application Version (String)              |
| icon                   | Application Icon Path (String)            |
| width                  | Startup Window Width (Int)                |
| height                 | Startup Window Height (Int)               |
| minwidth               | Window Minimum Width (Int)                |
| minheight              | Window Minimum Height (Int)               |
| scaling                | Window Scaling (Float)                    |
| scale_minsize          | Scale application Minimum Size (Boolean)  |
| scale_startsize        | Scale application Start Size (Boolean)    |
| resizable_width        | Enable Window Width Resizing (Boolean)    |
| resizable_height       | Enable Window Height Resizing (Boolean)   |
| enable_sizegrip        | Enable Window EasySizegrip (Boolean)      |
| start_maximized        | Start Window Maximized (Boolean)          |
| enable_maximized       | Enable Window Maximized (Boolean)         |
| start_fullscreen       | Start Window in Fullscreen mode (Boolean) |
| enable_fullscreen      | Enable Window Fullscreen option (Boolean) |
| ignored_themes         | Themes to not display in menu (List)      |
| enable_themes_menu     | Enable Themes Dropdown (Boolean)          |
| enable_launcher        | Enable Dynamic Launcher System (Boolean)  |
| movable_tabs           | Enable Moveable Notebook Tabs (Boolean)   |
| enable_profiles        | Enable a User Profiles System (Boolean)   |
| conversations_enabled  | Enable Convo System (Boolean)             |
| notes_enabled          | Enable Note System (Boolean)              |
| theme_textboxes        | Apply theme colors to tk.Text (Boolean)   ||
+------------------------+-------------------------------------------+
```
# The App Object<a name="mark4"></a>[^](#mark0)

### py_simple_ttk.app.App<a name="mark5"></a>[^](#mark4)
**Main Application Object**

```py
class App(object):
	def __init__(self, ini_file: str):
		...
	def apply_profile(self, profile: py_simple_ttk.utils.ProfilesSystem.UserProfile):
		"""Apply settings from the current profile. For more complicated profile systems override this function."""
	def copy_to_user_clipboard(self, val: str):
		"""Copys a text val to the user's keyboard"""
	def create_profile(self, name: str = None):
		"""Calling with no name brings up a popup, the popup calls this function again with name kw which instead makes a new profile or asks again for a name if the supplied name was invalid"""
	def select_profile(self, name: str = None):
		"""Calling with no name brings up a popup, the popup calls this function again with the name which instead calls the Profiles System to use a certain profile"""
	def toggle_full_screen(self, event=None):
		"""Toggles full screen."""
	def toggle_maximized(self, event=None):
		"""Toggles maximized window."""
	def update_default_title(self, indicate_profile=True):
		"""Update the window title with the default string, optionally with a profile indicator."""
	def update_title(self, title):
		"""Updates the window title"""
	def use_theme(self, theme: str = None, verbose: bool = False):
		"""Updates the app to use a certain theme."""
```
# Core Widgets<a name="mark6"></a>[^](#mark0)

### py_simple_ttk.widgets.MultiWidget.MultiWidgetMixin<a name="mark7"></a>[^](#mark6)
**An abstract mixin that provides a way to easily instantiate multiple of the same class of a widget and making complicated forms with simple get/set methods.**

MultiWidgets support a simple get/set system. Calling get without a configuration list returns a dict of subwidget keys mapped to the values of each subwidget's .get value. Passing a list of subwidget keys limits MultiWidgetMixin.get to said subwidgets. Subclassing a multiwidget with one or more instances of one class and then calling multiwidget.add() with different classes after is acceptable assuming the widget supports being added and .get / .set / .enable / .disable / .clear methods.
```py
class MultiWidgetMixin(object):
	def __init__(self, widget_type: type, config: dict):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.SuperWidget.SuperWidgetMixin<a name="mark8"></a>[^](#mark6)
**Mixin to easily bind many of the common tkinter events.**

This class serves to add bindings for the majority     of common tkinter widget events. The bindings are made in add mode to     prevent previous / new bindings from causing unintended side-effects     like unmapping etc.
```py
class SuperWidgetMixin(object):
	def __init__(self, on_mouse_enter: Callable = None, on_mouse_leave: Callable = None, on_mouse_move: Callable = None, on_mouse_wheel: Callable = None, on_left_click: Callable = None, on_double_left_click: Callable = None, on_middle_click: Callable = None, on_double_middle_click: Callable = None, on_right_click: Callable = None, on_double_right_click: Callable = None, on_configure: Callable = None):
		...
```
## Tabs<a name="mark9"></a>[^](#mark0)

### py_simple_ttk.widgets.Tabs.Tab<a name="mark10"></a>[^](#mark9)
**The core Tab class.**

The notebook object can be any ttk.Notebook, automatically adds itself to its parent notebook with title being the tab label. This class may be instantiated directly and added to or subclassed based on need.
```py
class Tab(Frame):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
```
### py_simple_ttk.widgets.Tabs.LauncherTab<a name="mark11"></a>[^](#mark9)
**Basic Tab for launching tasks from a list.**

Performs an action on a list of options. The options argument is formatted as such: `options = {"Button Text 1": val1,"Button Text 2": val2}` Button presses will call `action(val)`
```py
class LauncherTab(Tab):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, options: dict, action: Callable):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
```
### py_simple_ttk.widgets.Tabs.BrowserLauncherTab<a name="mark12"></a>[^](#mark9)
**LauncherTab that opens a list of URLS/Files**

Takes a dict of button texts as keys and urls to open as values
```py
class BrowserLauncherTab(LauncherTab):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, options: dict):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
```
### py_simple_ttk.widgets.Tabs.CommandLauncherTab<a name="mark13"></a>[^](#mark9)
**LauncherTab that runs a list of commands**

Takes a dict of button texts as keys and command prompt commands to execute as values
```py
class CommandLauncherTab(LauncherTab):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, options: dict):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
```
### py_simple_ttk.widgets.Tabs.ConsoleTab<a name="mark14"></a>[^](#mark9)
**Basic console tab using a ConsoleWidget**

```py
class ConsoleTab(Tab):
	def __init__(self, notebook: tkinter.ttk.Notebook, **kwargs):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
```
### py_simple_ttk.widgets.Tabs.TableTab<a name="mark15"></a>[^](#mark9)
**Basic Table Tab**

table_contents is a dictionary whose keys map to lists of equal lengths with the column contents
```py
class TableTab(Tab):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, table_contents: dict, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
```
### py_simple_ttk.widgets.Tabs.TreeTableTab<a name="mark16"></a>[^](#mark9)
**Improved Table Tab**

table_contents is a dictionary whose keys map to lists of equal lengths with the column contents
```py
class TreeTableTab(Tab):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, table_contents: dict = {}, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
```
# Widgets<a name="mark17"></a>[^](#mark0)

## Button Widgets<a name="mark18"></a>[^](#mark17)

### ActiveButton<a name="mark19"></a>[^](#mark18)
**ttk.Button with added features**

```py
class ActiveButton(Button, SuperWidgetMixin):
	def __init__(self, parent, default: str = '', command: Callable = None, widgetargs: dict = {}, **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> str:
		"""Get button text"""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledButton<a name="mark20"></a>[^](#mark18)
**Labeled ActiveButton widget**

```py
class LabeledButton(Labeler, ActiveButton):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, command: str = '', is_child: bool = False, labelside: str = 'left', **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> str:
		"""Get button text"""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledMultiButton<a name="mark21"></a>[^](#mark18)
**Labeled MultiWidget LabeledButton.**

Used when you need multiple, vertically stacked Labeled ActiveButtons
```py
class LabeledMultiButton(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### CycleButton<a name="mark22"></a>[^](#mark18)
**ActiveButton that cycles through options on each click**

```py
class CycleButton(ActiveButton):
	def __init__(self, parent: tkinter.ttk.Frame, options: list, default: int = 0, command: Callable = None, **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> str:
		"""Get button text"""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledCycleButton<a name="mark23"></a>[^](#mark18)
**Labeled CycleButton widget**

```py
class LabeledCycleButton(Labeler, CycleButton):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, options: list, is_child: bool = False, labelside: str = 'left', **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> str:
		"""Get button text"""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledMultiCycleButton<a name="mark24"></a>[^](#mark18)
**Labeled MultiWidget LabeledCycleButton**

Used when you need multiple, vertically stacked Labeled CycleButtons
```py
class LabeledMultiCycleButton(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Core Functions<a name="mark25"></a>[^](#mark17)

### py_simple_ttk.widgets.WidgetsCore.bbox_to_width_and_height<a name="mark26"></a>[^](#mark25)
> **Takes a bbox and converts it to a width and height tuple.**
> 
```python
def bbox_to_width_and_height(bbox: tuple) -> tuple:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.center_window<a name="mark27"></a>[^](#mark25)
> **Centers spawn window on main window. Call win.update_idletasks() on either window before calling this if said window is not yet shown.**
> 
```python
def center_window(main_window: tkinter.Tk, spawn_window: tkinter.Toplevel) -> None:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.check_in_bounds<a name="mark28"></a>[^](#mark25)
> **Checks if a position is within a given bounds. Pos is generally a mouse event position tuple, bounds is generally a canvas.bbox(), but a (left, top, right, bottom) tuple will work too.**
> 
```python
def check_in_bounds(pos: tuple, bounds: tuple) -> bool:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.complex_widget_search<a name="mark29"></a>[^](#mark25)
> **A more robust version of the widget search with lists for multiple widget types found in one go**
> 
```python
def complex_widget_search(node_widget, widget_types_to_find: list, found_lists: dict = {}) -> dict:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.copy_to_user_clipboard<a name="mark30"></a>[^](#mark25)
> **Copies a string to the user's clipboard.**
> 
```python
def copy_to_user_clipboard(widget, value: str) -> None:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.create_round_rectangle<a name="mark31"></a>[^](#mark25)
> **Draws a rounded rectangle of a given radius on a tk.canvas**
> 
```python
def create_round_rectangle(canvas, x1: float, y1: float, x2: float, y2: float, r: float = 20, fill: str = '', outline: str = '#000000', **kwargs):
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.default_pack<a name="mark32"></a>[^](#mark25)
> **Apply a consistent descending packing method.**
> 
```python
def default_pack(widget, bottom: bool = False, padx: tuple = 5) -> None:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.default_separator<a name="mark33"></a>[^](#mark25)
> **Apply a consistent horizontal separator.**
> 
```python
def default_separator(f: tkinter.ttk.Frame, padx: tuple = 35, pady: tuple = (10, 5)) -> tkinter.ttk.Separator:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.default_vertical_pack<a name="mark34"></a>[^](#mark25)
> **Apply a consistent packing method to vertically packed widgets.**
> 
```python
def default_vertical_pack(widget, expand: bool = False, fill: str = 'both', padx: tuple = 0) -> None:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.default_vertical_separator<a name="mark35"></a>[^](#mark25)
> **Apply a consistent vertical separator.**
> 
```python
def default_vertical_separator(frame: tkinter.ttk.Frame, pady: tuple = 15, padx: tuple = 10) -> tkinter.ttk.Separator:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.enable_notebook_movement<a name="mark36"></a>[^](#mark25)
> **Copyright CJB 2010-07-31: https://wiki.tcl-lang.org/page/Drag+and+Drop+Notebook+Tabs Enables Tab dragging in subsequently created notebooks. Only run this function once.**
> 
```python
def enable_notebook_movement(app) -> None:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.focus_next<a name="mark37"></a>[^](#mark25)
> **Forces focus to the widget after the one that triggered the event**
> 
```python
def focus_next(event) -> object:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.force_aspect<a name="mark38"></a>[^](#mark25)
> **Forces an inner frame to maintain an aspect ratio regardless of the outer frame's size**
> 
```python
def force_aspect(inner_frame: tkinter.ttk.Frame, outer_frame: tkinter.ttk.Frame, ratio: float = 1.7777777777777777) -> None:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.get_asset<a name="mark39"></a>[^](#mark25)
> **Gets an asset from the included assets folder by relative path. Works with pyinstaller.**
> 
```python
def get_asset(path, folder: str = 'C:\\Users\\arcti\\github\\py_simple_ttk\\py_simple_ttk\\./assets') -> str:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.get_bundled_themes_list<a name="mark40"></a>[^](#mark25)
> **None**
> 
```python
def get_bundled_themes_list(verbose: bool = False) -> list:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.get_generated_font_images_lookup<a name="mark41"></a>[^](#mark25)
> **Makes a lookup for the pre-generated open-sans font monograms that ship with py_simple_ttk.**
> 
```python
def get_generated_font_images_lookup(path: str = None) -> dict:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.get_local_appdata_folder<a name="mark42"></a>[^](#mark25)
> **Opens user's Windows home folder. Only works on Windows for obvious reasons.**
> 
```python
def get_local_appdata_folder() -> str:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.get_themes_folder<a name="mark43"></a>[^](#mark25)
> **Gets the absolute path to the included themes folder**
> 
```python
def get_themes_folder() -> str:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.make_aspect_frames<a name="mark44"></a>[^](#mark25)
> **Creates an outer and inner frame within a parent frame. Forces the inner frame to maintain an aspect ratio. Returns the outer and inner frames.**
> 
```python
def make_aspect_frames(parent: tkinter.ttk.Frame, ratio: float = 1.7777777777777777) -> tuple:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.open_link<a name="mark45"></a>[^](#mark25)
> **Opens a link in the user's default web browser. `Returns None`**
> 
```python
def open_link(link: str) -> None:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.recursive_widget_search<a name="mark46"></a>[^](#mark25)
> **Adds widgets of a given type to a list as it travels up, away from the root of a widget tree. This method can be slow on large widget trees but is useful for retheming tk widgets with ttk formatting on theme changes. `Returns a list of widgets`**
> 
```python
def recursive_widget_search(node_widget, widget_type_to_find: type, found_list: list = []) -> list:
> 	...
```
### py_simple_ttk.widgets.WidgetsCore.run_cl<a name="mark47"></a>[^](#mark25)
> **Runs something via command line. `Returns None`**
> 
```python
def run_cl(commands: list) -> None:
> 	...
```
## Canvas Widgets<a name="mark48"></a>[^](#mark17)

### py_simple_ttk.widgets.ResizableCanvas.ResizableCanvas<a name="mark49"></a>[^](#mark48)
**Resizeable Canvas**

Canvas resizes to fit frame on configure event.
```py
class ResizableCanvas(Canvas):
	def __init__(self, parent, **kw):
		...
	def create_arc(self, *args, **kw):
		"""Create arc shaped region with coordinates x1,y1,x2,y2."""
	def create_bitmap(self, *args, **kw):
		"""Create bitmap with coordinates x1,y1."""
	def create_image(self, *args, **kw):
		"""Create image item with coordinates x1,y1."""
	def create_line(self, *args, **kw):
		"""Create line with coordinates x1,y1,...,xn,yn."""
	def create_oval(self, *args, **kw):
		"""Create oval with coordinates x1,y1,x2,y2."""
	def create_polygon(self, *args, **kw):
		"""Create polygon with coordinates x1,y1,...,xn,yn."""
	def create_rectangle(self, *args, **kw):
		"""Create rectangle with coordinates x1,y1,x2,y2."""
	def create_round_rectangle(self, x1: float, y1: float, x2: float, y2: float, r: float = 20, fill: str = '', outline: str = '#000000', **kwargs) -> None:
		"""Draws a rounded rectangle of a given radius on a tk.canvas."""
	def create_text(self, *args, **kw):
		"""Create text with coordinates x1,y1."""
	def create_window(self, *args, **kw):
		"""Create window with coordinates x1,y1,x2,y2."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def refresh(self) -> None:
		"""Refresh Canvas"""
```
### py_simple_ttk.widgets.ScrolledCanvas.ScrolledCanvas<a name="mark50"></a>[^](#mark48)
**Resizeable, Auto-Scrollbarred Canvas**

Canvas resizes to fit frame on configure event. Canvas has automatic Scrollbars that appear when needed. Canvas background color is based on current theme. Due to how the scrolling is handled the actual Canvas is accessd via `ScrolledCanvas().canvas`.
```py
class ScrolledCanvas(Frame):
	def __init__(self, parent, on_mouse_enter=None, on_mouse_leave=None, on_mouse_move=None, on_mouse_wheel=None, on_left_click=None, on_middle_click=None, on_right_click=None, on_configure=None, bind_canvas_scroll=True, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get_adjusted_y_view(self, event) -> int:
		"""Gets a canvas y-view adjusted based on its scrolled position"""
	def use_style(self, style) -> None:
		"""Reformat with a given ttk style. `Returns None`"""
```
### py_simple_ttk.widgets.ScrolledCanvas.TiledCanvas<a name="mark51"></a>[^](#mark48)
```py
class TiledCanvas(ScrolledCanvas):
	def __init__(self, *args, tile_width=400, tile_height=100, tile_padx=5, tile_pady=5, tile_color='#424548', text_color='#CCCCCC', border_color='#000000', on_tile_left_click=None, on_tile_middle_click=None, on_tile_right_click=None, override_tile_width=False, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get_adjusted_y_view(self, event) -> int:
		"""Gets a canvas y-view adjusted based on its scrolled position"""
	def refresh(self, event=None) -> None:
		"""Redraw the canvas"""
	def use_style(self, style) -> None:
		"""Reformat with a given ttk style. `Returns None`"""
```
### py_simple_ttk.widgets.ScrolledCanvas.ExampleTile<a name="mark52"></a>[^](#mark48)
**An example tile for a Scrolled Canvas**

```py
class ExampleTile(object):
	def __init__(self, manager, text: str):
		...
	def activate(self) -> None:
		"""Calls the manager to activate the widget."""
	def deactivate(self) -> None:
		"""Calls the manager to deactivate the widget."""
	def is_in_range(self, pointer_x: float, pointer_y: float) -> bool:
		"""Checks if the mouse pointer is in the tile."""
	def set_position(self, x: float, y: float) -> None:
		"""Sets a tiles position for the draw manager's draw method."""
```
## Checkbutton Widgets<a name="mark53"></a>[^](#mark17)

### py_simple_ttk.widgets.CheckbuttonWidgets.ActiveCheckbutton<a name="mark54"></a>[^](#mark53)
**ttk.Checkbutton with added features**

The "replace_output" keyword argument allows the user to provide a tuple of length 2 to replace the default True/False return values.
```py
class ActiveCheckbutton(Checkbutton):
	def __init__(self, parent: tkinter.ttk.Frame, replace_output: list = None, default: bool = False, **kw):
		...
	def clear(self) -> None:
		"""Sets the Checkbutton to its default value, usually *False* `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Checkbutton. `Returns None`"""
	def enable(self) -> None:
		"""Enable Checkbutton. `Returns None`"""
	def get(self) -> bool:
		"""Get Checkbutton value. `Returns a Boolean unless replace_output is set`"""
	def set(self, val: bool) -> None:
		"""Set Checkbutton value. `Returns None`"""
```
### py_simple_ttk.widgets.CheckbuttonWidgets.LabeledCheckbutton<a name="mark55"></a>[^](#mark53)
**Labeled Checkbutton**

ActiveCheckbutton with a Label
```py
class LabeledCheckbutton(Labeler, ActiveCheckbutton):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str = '', is_child: bool = False, **kw):
		...
	def clear(self) -> None:
		"""Sets the Checkbutton to its default value, usually *False* `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Checkbutton. `Returns None`"""
	def enable(self) -> None:
		"""Enable Checkbutton. `Returns None`"""
	def get(self) -> bool:
		"""Get Checkbutton value. `Returns a Boolean unless replace_output is set`"""
	def set(self, val: bool) -> None:
		"""Set Checkbutton value. `Returns None`"""
```
### py_simple_ttk.widgets.CheckbuttonWidgets.LabeledMultiCheckbutton<a name="mark56"></a>[^](#mark53)
**Labeled MultiWidget LabeledCheckbutton.**

Used when you need multiple, vertically stacked Labeled Checkbuttons
```py
class LabeledMultiCheckbutton(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Combobox Widgets<a name="mark57"></a>[^](#mark17)

### py_simple_ttk.widgets.ComboboxWidgets.ActiveCombobox<a name="mark58"></a>[^](#mark57)
**ttk.Combobox with added features and the SuperWidgetMixin**

```py
class ActiveCombobox(Combobox, SuperWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, command: Callable = None, default: int = 0, on_keystroke: bool = False, bind_enter: bool = True, bind_escape_clear: bool = True, values: list = (), custom_values: bool = True, widgetargs: dict = {}, **kw):
		...
	def clear(self) -> None:
		"""Sets Combobox to its default value. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Combobox. `Returns None`"""
	def enable(self) -> None:
		"""Enable Combobox. `Returns None`"""
	def get(self) -> str:
		"""Get Combobox value. `Returns a String`"""
	def set(self, val: str) -> None:
		"""Set Combobox value. `Returns None`"""
```
### py_simple_ttk.widgets.ComboboxWidgets.LabeledCombobox<a name="mark59"></a>[^](#mark57)
**Labeled Combobox with the Super Widget mixin**

Set custom_values keyword to "False" to disable custom user-entered values. Set the "default" keyword to the index of the value to display by default from the "values" keyword.
```py
class LabeledCombobox(Labeler, ActiveCombobox):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, labelside: str = 'left', is_child: bool = False, widgetargs={}, **kw):
		...
	def clear(self) -> None:
		"""Sets Combobox to its default value. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Combobox. `Returns None`"""
	def enable(self) -> None:
		"""Enable Combobox. `Returns None`"""
	def get(self) -> str:
		"""Get Combobox value. `Returns a String`"""
	def set(self, val: str) -> None:
		"""Set Combobox value. `Returns None`"""
```
### py_simple_ttk.widgets.ComboboxWidgets.LabeledMultiCombobox<a name="mark60"></a>[^](#mark57)
**Labeled MultiWidget LabeledCombobox.**

Used when you need mutiple, vertically stacked Labeled Comboboxes
```py
class LabeledMultiCombobox(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Console Widgets<a name="mark61"></a>[^](#mark17)

### py_simple_ttk.widgets.ConsoleWidgets.ConsoleWidget<a name="mark62"></a>[^](#mark61)
**Set labeltext, even if temporarily at init or the label widget will be ignored**

Used when you need to drop a console interface into an application. To write to the console call console.print(value). Pass a function as the "command" keyword argument to handle the entry input.
```py
class ConsoleWidget(Labeler, Frame):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str = 'Console: ', entrylabeltext: str = 'Command: ', labelside: str = 'top', button_text: str = 'Run', is_child: bool = False, **kwargs):
		...
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def print(self, val, end: str = '\n'):
		"""Prints a line to the console with a customizable line ending. `Returns None`"""
```
## Constraining Functions<a name="mark63"></a>[^](#mark17)

### check_entry_type<a name="mark64"></a>[^](#mark63)
> **Core type checker function. Limits entry to chars that construct a given type**
> 
```python
def check_entry_type(val: str, typ: type) -> bool:
> 	...
```
### check_entry_int<a name="mark65"></a>[^](#mark63)
> **Check if an entry input is a valid integer**
> 
```python
def check_entry_int(val: str) -> bool:
> 	...
```
### check_entry_float<a name="mark66"></a>[^](#mark63)
> **Check if an entry input is a valid float**
> 
```python
def check_entry_float(val: str) -> bool:
> 	...
```
### check_entry_contents<a name="mark67"></a>[^](#mark63)
> **Core content checker function. Limits entry to a list of chars ['a', 'b', 'c', ...] or     the chars contained in a simple string 'abc...'**
> 
```python
def check_entry_contents(val: str, limiter: list | str) -> bool:
> 	...
```
### check_entry_ascii_lowercase<a name="mark68"></a>[^](#mark63)
> **Check if entry input is made only of lowercase ascii**
> 
```python
def check_entry_ascii_lowercase(val: str) -> bool:
> 	...
```
### check_entry_ascii_uppercase<a name="mark69"></a>[^](#mark63)
> **Check if entry input is made only of uppercase ascii**
> 
```python
def check_entry_ascii_uppercase(val: str) -> bool:
> 	...
```
### check_entry_ascii_letters<a name="mark70"></a>[^](#mark63)
> **Check if entry input is made only of uppercase and lowercase ascii**
> 
```python
def check_entry_ascii_letters(val: str) -> bool:
> 	...
```
### check_entry_ascii_digits<a name="mark71"></a>[^](#mark63)
> **Check if entry input is made only of digits**
> 
```python
def check_entry_ascii_digits(val: str) -> bool:
> 	...
```
### check_entry_ascii_uppercase_digits<a name="mark72"></a>[^](#mark63)
> **Check if entry input is made only of uppercase ascii and digits**
> 
```python
def check_entry_ascii_uppercase_digits(val: str) -> bool:
> 	...
```
### check_entry_ascii_lowercase_digits<a name="mark73"></a>[^](#mark63)
> **Check if entry input is made only of lowercase ascii and digits**
> 
```python
def check_entry_ascii_lowercase_digits(val: str) -> bool:
> 	...
```
### check_entry_ascii_hexdigits<a name="mark74"></a>[^](#mark63)
> **Check if entry input is made only of hexigits**
> 
```python
def check_entry_ascii_hexdigits(val: str) -> bool:
> 	...
```
### check_entry_ascii_octdigits<a name="mark75"></a>[^](#mark63)
> **Check if entry input is made only of octdigits**
> 
```python
def check_entry_ascii_octdigits(val: str) -> bool:
> 	...
```
### check_entry_ascii_letters_digits<a name="mark76"></a>[^](#mark63)
> **Check if entry input is made only of ascii lowercase, ascii uppercase, and digits**
> 
```python
def check_entry_ascii_letters_digits(val) -> bool:
> 	...
```
### check_entry_ascii_printable<a name="mark77"></a>[^](#mark63)
> **Check if entry input is made only of printable characters**
> 
```python
def check_entry_ascii_printable(val: str) -> bool:
> 	...
```
## Counter Widgets<a name="mark78"></a>[^](#mark17)

### Counter<a name="mark79"></a>[^](#mark78)
**Up / down counter widgets**

```py
class Counter(Frame):
	def __init__(self, parent: tkinter.ttk.Frame, default: int = 0, min_value: int = None, max_value: int = None, step: int = 1, state: str = 'normal', command: Callable = None, depth: int = 1, **kwargs):
		...
	def clear(self) -> int:
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		...
	def enable(self) -> None:
		...
	def set(self, val: int, adjust: int = 0, no_command: bool = False) -> int:
		...
```
### FloatCounter<a name="mark80"></a>[^](#mark78)
**Float Counter Widget**

```py
class FloatCounter(Frame):
	def __init__(self, parent=<class 'tkinter.ttk.Frame'>, default: float = 0.0, min_value: float = None, max_value: float = None, step: float = 1.0, state: str = 'normal', command: Callable = None, decimal_level: int = 1, integer_level: int = 1, **kwargs):
		...
	def clear(self) -> float:
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		...
	def enable(self) -> None:
		...
	def get(self) -> float:
		...
	def set(self, val: float, adjust: float = 0.0) -> float:
		...
```
### LabeledCounter<a name="mark81"></a>[^](#mark78)
**Labeled Counter Widget**

```py
class LabeledCounter(Labeler, Counter, SuperWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, command: Callable = None, labelside: str = 'left', is_child: bool = False, state: str = 'normal', widgetargs: dict = {}, **kw):
		...
	def clear(self) -> int:
		...
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		...
	def enable(self) -> None:
		...
	def set(self, val: int, adjust: int = 0, no_command: bool = False) -> int:
		...
```
### LabeledFloatCounter<a name="mark82"></a>[^](#mark78)
**Labeled Float Counter Widget**

```py
class LabeledFloatCounter(Labeler, FloatCounter, SuperWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, command: Callable = None, labelside: str = 'left', is_child: bool = False, state: str = 'normal', widgetargs: dict = {}, **kw):
		...
	def clear(self) -> float:
		...
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		...
	def enable(self) -> None:
		...
	def get(self) -> float:
		...
	def set(self, val: float, adjust: float = 0.0) -> float:
		...
```
### LabeledMultiCounter<a name="mark83"></a>[^](#mark78)
**Labeled MultiWidget LabeledCounter.**

Used when you need multiple, vertically stacked Labeled Counters
```py
class LabeledMultiCounter(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### LabeledMultiFloatCounter<a name="mark84"></a>[^](#mark78)
**Labeled MultiWidget Labeled FloatCounter.**

Used when you need multiple, vertically stacked Labeled FloatCounters
```py
class LabeledMultiFloatCounter(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Entry Widgets<a name="mark85"></a>[^](#mark17)

### py_simple_ttk.widgets.EntryWidgets.ActiveEntry<a name="mark86"></a>[^](#mark85)
**Active ttk.Entry with added features and the SuperWidgetMixin**

```py
class ActiveEntry(Entry, SuperWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, command: Callable = None, default: str = '', on_keystroke: bool = False, bind_enter: bool = True, bind_escape_clear: bool = True, widgetargs: dict = {}, **kw):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> str:
		"""Get Entry value. `Returns a String`"""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.EntryWidgets.ScrolledEntry<a name="mark87"></a>[^](#mark85)
**Scrolled ttk.Entry with SuperWidgetMixin**

This class is here for completeness but most of the time you will want to use the ScrolledText widget. Used when you need a scrollable text entry box.
```py
class ScrolledEntry(Scroller, ActiveEntry):
	def __init__(self, parent, **kw) -> object:
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> str:
		"""Get Entry value. `Returns a String`"""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.EntryWidgets.LabeledEntry<a name="mark88"></a>[^](#mark85)
**Labeled ActiveEntry**

ActiveEntry with Label
```py
class LabeledEntry(Labeler, ActiveEntry):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, labelside: str = 'left', is_child: bool = False, **kw):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> str:
		"""Get Entry value. `Returns a String`"""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.EntryWidgets.LabeledMultiEntry<a name="mark89"></a>[^](#mark85)
**Labeled MultiWidget LabeledEntry**

Used when you need multiple, vertically stacked Labeled Entries
```py
class LabeledMultiEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.EntryWidgets.LabeledButtonEntry<a name="mark90"></a>[^](#mark85)
**LabeledEntry with a ttk.Button on the right**

```py
class LabeledButtonEntry(LabeledEntry):
	def __init__(self, *args, button_text='', **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> str:
		"""Get Entry value. `Returns a String`"""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.EntryWidgets.LabeledMultiButtonEntry<a name="mark91"></a>[^](#mark85)
**Labeled MultiWidget Labeled ButtonEntry**

Used when you need multiple, vertically stacked Labeled Entries
```py
class LabeledMultiButtonEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.EntryWidgets.LabeledPathEntry<a name="mark92"></a>[^](#mark85)
**LabeledEntry with a ttk.Button bound to a file- or folder-picker for easy     system path selection. Defaults to tk.filedialog.askopenfilename if no     tk.filedialog specified.**

```py
class LabeledPathEntry(LabeledEntry):
	def __init__(self, *args, button_text: str = '...', dialog=None, dialog_args: dict = {}, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> str:
		"""Get Entry value. `Returns a String`"""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.EntryWidgets.LabeledMultiPathEntry<a name="mark93"></a>[^](#mark85)
**Labeled MultiWidget LabeledPathEntry**

Used when you need multiple, vertically stacked LabeledPathEntries
```py
class LabeledMultiPathEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.EntryWidgets.PasswordEntry<a name="mark94"></a>[^](#mark85)
**Username / Password Entry**

A username/password entry widget with optional password peeking. Set password_char to `''` to show password by default. The provided command will always be called with the tuple `(username_entry.get(), password_entry.get())` as the only argument even if one of the entries is disabled.
```py
class PasswordEntry(Frame):
	def __init__(self, *args, instruction_text: str = '', username_text: str = 'Username: ', username_enabled: bool = True, password_text: str = 'Password: ', password_enabled: bool = True, button_text: str = 'Submit', command=<built-in function print>, password_char: str = '*', peek_enabled: bool = True, invert_peek_colors: bool = False, **kwargs):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> tuple:
		...
	def set(self, values: tuple) -> None:
		...
```
### py_simple_ttk.widgets.EntryWidgets.LabeledPasswordEntry<a name="mark95"></a>[^](#mark85)
**Labeled Username/Password entry**

```py
class LabeledPasswordEntry(Labeler, PasswordEntry):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, *args, is_child: bool = False, **kw):
		...
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> tuple:
		...
	def set(self, values: tuple) -> None:
		...
```
### py_simple_ttk.widgets.EntryWidgets.LabeledMultiPasswordEntry<a name="mark96"></a>[^](#mark85)
**Labeled MultiWidget Labeled PasswordEntry**

Used when you need multiple, vertically stacked Labeled Username/Password Entries
```py
class LabeledMultiPasswordEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.ConstrainedEntry<a name="mark97"></a>[^](#mark85)
**Constrained ActiveEntry**

An Entry widget that allows certain constraints to be placed on the input with a given check_function that returns true if the input is allowed for each keystroke / input.
```py
class ConstrainedEntry(ActiveEntry):
	def __init__(self, parent: tkinter.ttk.Frame, check_function: Callable, return_type: type = <class 'str'>, **kw):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledConstrainedEntry<a name="mark98"></a>[^](#mark85)
**Labeled Constrained Entry**

```py
class LabeledConstrainedEntry(Labeler, ConstrainedEntry):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, *args, is_child: bool = False, **kw):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiConstrainedEntry<a name="mark99"></a>[^](#mark85)
**Labeled Multi Constrained Entry**

```py
class LabeledMultiConstrainedEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.IntEntry<a name="mark100"></a>[^](#mark85)
**Int Entry Widget**

```py
class IntEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledIntEntry<a name="mark101"></a>[^](#mark85)
**Labeled Int Entry Widget**

```py
class LabeledIntEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiIntEntry<a name="mark102"></a>[^](#mark85)
```py
class LabeledMultiIntEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.FloatEntry<a name="mark103"></a>[^](#mark85)
```py
class FloatEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledFloatEntry<a name="mark104"></a>[^](#mark85)
```py
class LabeledFloatEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiFloatEntry<a name="mark105"></a>[^](#mark85)
```py
class LabeledMultiFloatEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LowercaseEntry<a name="mark106"></a>[^](#mark85)
```py
class LowercaseEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledLowercaseEntry<a name="mark107"></a>[^](#mark85)
```py
class LabeledLowercaseEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiLowercaseEntry<a name="mark108"></a>[^](#mark85)
```py
class LabeledMultiLowercaseEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.UppercaseEntry<a name="mark109"></a>[^](#mark85)
```py
class UppercaseEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledUppercaseEntry<a name="mark110"></a>[^](#mark85)
```py
class LabeledUppercaseEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiUppercaseEntry<a name="mark111"></a>[^](#mark85)
```py
class LabeledMultiUppercaseEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LettersEntry<a name="mark112"></a>[^](#mark85)
```py
class LettersEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledLettersEntry<a name="mark113"></a>[^](#mark85)
```py
class LabeledLettersEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiLettersEntry<a name="mark114"></a>[^](#mark85)
```py
class LabeledMultiLettersEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.DigitsEntry<a name="mark115"></a>[^](#mark85)
```py
class DigitsEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledDigitsEntry<a name="mark116"></a>[^](#mark85)
```py
class LabeledDigitsEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiDigitsEntry<a name="mark117"></a>[^](#mark85)
```py
class LabeledMultiDigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.UppercaseDigitsEntry<a name="mark118"></a>[^](#mark85)
```py
class UppercaseDigitsEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledUppercaseDigitsEntry<a name="mark119"></a>[^](#mark85)
```py
class LabeledUppercaseDigitsEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiUppercaseDigitsEntry<a name="mark120"></a>[^](#mark85)
```py
class LabeledMultiUppercaseDigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LowercaseDigitsEntry<a name="mark121"></a>[^](#mark85)
```py
class LowercaseDigitsEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledLowercaseDigitsEntry<a name="mark122"></a>[^](#mark85)
```py
class LabeledLowercaseDigitsEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiLowercaseDigitsEntry<a name="mark123"></a>[^](#mark85)
```py
class LabeledMultiLowercaseDigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LettersDigitsEntry<a name="mark124"></a>[^](#mark85)
```py
class LettersDigitsEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledLettersDigitsEntry<a name="mark125"></a>[^](#mark85)
```py
class LabeledLettersDigitsEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiLettersDigitsEntry<a name="mark126"></a>[^](#mark85)
```py
class LabeledMultiLettersDigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.HexdigitsEntry<a name="mark127"></a>[^](#mark85)
```py
class HexdigitsEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledHexdigitsEntry<a name="mark128"></a>[^](#mark85)
```py
class LabeledHexdigitsEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiHexdigitsEntry<a name="mark129"></a>[^](#mark85)
```py
class LabeledMultiHexdigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.OctdigitsEntry<a name="mark130"></a>[^](#mark85)
```py
class OctdigitsEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledOctdigitsEntry<a name="mark131"></a>[^](#mark85)
```py
class LabeledOctdigitsEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiOctdigitsEntry<a name="mark132"></a>[^](#mark85)
```py
class LabeledMultiOctdigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.PrintableEntry<a name="mark133"></a>[^](#mark85)
```py
class PrintableEntry(ConstrainedEntry):
	def __init__(self, parent, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledPrintableEntry<a name="mark134"></a>[^](#mark85)
```py
class LabeledPrintableEntry(LabeledConstrainedEntry):
	def __init__(self, parent, labeltext, *args, **kwargs):
		...
	def clear(self) -> None:
		"""Set Entry value to default, empty unless default set. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Entry. `Returns None`"""
	def enable(self) -> None:
		"""Enable Entry. `Returns None`"""
	def get(self) -> object:
		"""Get Entry value, return type varies based on Entry constraint."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiPrintableEntry<a name="mark135"></a>[^](#mark85)
```py
class LabeledMultiPrintableEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Frame Widgets<a name="mark136"></a>[^](#mark17)

### py_simple_ttk.widgets.FrameWidgets.ColumnFrame<a name="mark137"></a>[^](#mark136)
**A frame with a given number of children column frames**

```py
class ColumnFrame(Frame):
	def __init__(self, parent: tkinter.ttk.Frame, columns: int = 1, pack_args: dict = {}, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def yield_frame(self):
		"""Cyclically returns frames"""
```
## KeyPad Widgets<a name="mark138"></a>[^](#mark17)

### py_simple_ttk.widgets.KeyPadWidgets.KeypadButton<a name="mark139"></a>[^](#mark138)
**Base Keypad Button**

Keypad button that automatically packs itself based on given coordinates. This object is not usually directly instantiated.
```py
class KeypadButton(Button):
	def __init__(self, frame: tkinter.ttk.Frame, value: int, coords: tuple, command: Callable):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
```
### py_simple_ttk.widgets.KeyPadWidgets.BaseKeypad<a name="mark140"></a>[^](#mark138)
**Base Keypad Class**

Either instantiate directly with a custom layout or subclass with each subclass supplying a custom layout for more keypads. Subclass KeypadButton and supply the class as the "button_type" kwarg for custom buttons.
```py
class BaseKeypad(Frame):
	def __init__(self, layout, command, button_class=<class 'py_simple_ttk.widgets.KeyPadWidgets.KeypadButton'>, *args, **kwargs):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
```
### py_simple_ttk.widgets.KeyPadWidgets.DialerKeypad<a name="mark141"></a>[^](#mark138)
**Phone Dialer Keypad**

Example 12-button keypad, subclass BaseKeypad and supply a custom layout for more keypads.
```py
class DialerKeypad(BaseKeypad):
	def __init__(self, command: Callable, *args, **kwargs):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
```
## Labeler Widget<a name="mark142"></a>[^](#mark17)

### ActiveButton<a name="mark143"></a>[^](#mark142)
**ttk.Button with added features**

```py
class ActiveButton(Button, SuperWidgetMixin):
	def __init__(self, parent, default: str = '', command: Callable = None, widgetargs: dict = {}, **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> str:
		"""Get button text"""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledButton<a name="mark144"></a>[^](#mark142)
**Labeled ActiveButton widget**

```py
class LabeledButton(Labeler, ActiveButton):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, command: str = '', is_child: bool = False, labelside: str = 'left', **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> str:
		"""Get button text"""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledMultiButton<a name="mark145"></a>[^](#mark142)
**Labeled MultiWidget LabeledButton.**

Used when you need multiple, vertically stacked Labeled ActiveButtons
```py
class LabeledMultiButton(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### CycleButton<a name="mark146"></a>[^](#mark142)
**ActiveButton that cycles through options on each click**

```py
class CycleButton(ActiveButton):
	def __init__(self, parent: tkinter.ttk.Frame, options: list, default: int = 0, command: Callable = None, **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> str:
		"""Get button text"""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledCycleButton<a name="mark147"></a>[^](#mark142)
**Labeled CycleButton widget**

```py
class LabeledCycleButton(Labeler, CycleButton):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, options: list, is_child: bool = False, labelside: str = 'left', **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> str:
		"""Get button text"""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledMultiCycleButton<a name="mark148"></a>[^](#mark142)
**Labeled MultiWidget LabeledCycleButton**

Used when you need multiple, vertically stacked Labeled CycleButtons
```py
class LabeledMultiCycleButton(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## ListBox Widgets<a name="mark149"></a>[^](#mark17)

### py_simple_ttk.widgets.ListBoxWidgets.ScrolledListBox<a name="mark150"></a>[^](#mark149)
**Scrolled Listbox with SuperWidget mixin**

```py
class ScrolledListBox(Scroller, Listbox, SuperWidgetMixin):
	def __init__(self, parent, **kw) -> object:
		...
	def activate(self, index):
		"""Activate item identified by INDEX."""
	def curselection(self):
		"""Return the indices of currently selected item."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self, first, last=None):
		"""Get list of items from FIRST to LAST (included)."""
```
### py_simple_ttk.widgets.ListBoxWidgets.OrderedListbox<a name="mark151"></a>[^](#mark149)
**A Scrolled Re-Orderable Listbox with SuperWidget mixin**

Used when you need a re-orderable listbox for list arrangement etc. "selectmode" can only be "single" for this Widget.
```py
class OrderedListbox(ScrolledListBox):
	def __init__(self, parent: tkinter.ttk.Frame, **kw):
		...
	def activate(self, index):
		"""Activate item identified by INDEX."""
	def curselection(self):
		"""Return the indices of currently selected item."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self, first, last=None):
		"""Get list of items from FIRST to LAST (included)."""
```
### py_simple_ttk.widgets.ListBoxWidgets.Table<a name="mark152"></a>[^](#mark149)
**Listboxes bound to scroll in union. Additional bindings will be needed in order to handle clicking.**

Tested on Mac/Windows/Linux. In most cases a TreeTable widget will be superior to this.
```py
class Table(Frame):
	def __init__(self, *args, min_column_width: int = 100, start_column_width: int = 100, on_selection: Callable = None, visible_rows=0, **kw):
		...
	def build(self, contents: dict) -> None:
		"""Rebuild the table"""
	def clear(self) -> None:
		"""Clears the table"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> list:
		"""Gets the currently selected items from the table. `Returns a List of Strings`"""
	def use_style(self, style: tkinter.ttk.Style) -> None:
		"""Update to match supplied ttk.Style object. `Returns None`"""
```
## OptionMenu Widgets<a name="mark153"></a>[^](#mark17)

### py_simple_ttk.widgets.OptionMenuWidgets.ActiveOptionMenu<a name="mark154"></a>[^](#mark153)
**ttk.OptionMenu with added features and SuperWidgetMixin**

```py
class ActiveOptionMenu(OptionMenu, SuperWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, options: list, default: int = 0, on_keystroke: bool = False, bind_enter: bool = True, bind_escape_clear: bool = True, command: Callable = None, widgetargs: dict = {}):
		...
	def clear(self) -> None:
		"""Sets OptionMenu to its default value. `Returns None`"""
	def destroy(self):
		"""Destroy this widget and its associated variable."""
	def disable(self) -> None:
		"""Disable OptionMenu. `Returns None`"""
	def enable(self) -> None:
		"""Enable OptionMenu. `Returns None`"""
	def get(self) -> str:
		"""Get OptionMenu value. `Returns a String`"""
	def set(self, val) -> None:
		"""Set OptionMenu value. `Returns None`"""
	def set_menu(self, default=None, *values):
		"""Build a new menu of radiobuttons with *values and optionally
        a default value."""
```
### py_simple_ttk.widgets.OptionMenuWidgets.LabeledOptionMenu<a name="mark155"></a>[^](#mark153)
**Labeled ActiveOptionMenu**

```py
class LabeledOptionMenu(Labeler, ActiveOptionMenu):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, *args, is_child: bool = False, **kw):
		...
	def clear(self) -> None:
		"""Sets OptionMenu to its default value. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this widget and its associated variable."""
	def disable(self) -> None:
		"""Disable OptionMenu. `Returns None`"""
	def enable(self) -> None:
		"""Enable OptionMenu. `Returns None`"""
	def get(self) -> str:
		"""Get OptionMenu value. `Returns a String`"""
	def set(self, val) -> None:
		"""Set OptionMenu value. `Returns None`"""
	def set_menu(self, default=None, *values):
		"""Build a new menu of radiobuttons with *values and optionally
        a default value."""
```
### py_simple_ttk.widgets.OptionMenuWidgets.LabeledMultiOptionMenu<a name="mark156"></a>[^](#mark153)
**Labeled MultiWidget LabeledOptionMenu**

```py
class LabeledMultiOptionMenu(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## ProgressBar Widgets<a name="mark157"></a>[^](#mark17)

### py_simple_ttk.widgets.ProgressbarWidgets.ActiveProgressbar<a name="mark158"></a>[^](#mark157)
**ttk.Progressbar with added features**

```py
class ActiveProgressbar(Progressbar):
	def __init__(self, parent: tkinter.ttk.Frame, default: float = 0, **kw):
		...
	def clear(self):
		"""Sets Progressbar progress to its default value `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self):
		"""Enable Progressbar. `Returns None`"""
	def enable(self):
		"""Disable Progressbar. `Returns None`"""
	def get(self):
		"""Set Progressbar progress. `Returns None`"""
	def link(self, widget):
		"""Easily link to other widgets, sets the progressbar var to the passed widget's var. `Returns None`"""
	def set(self, val):
		"""Get Progressbar progress. `Returns a String`"""
	def start(self, interval=None):
		"""Begin autoincrement mode: schedules a recurring timer event
        that calls method step every interval milliseconds.

        interval defaults to 50 milliseconds (20 steps/second) if omitted."""
	def step(self, amount=None):
		"""Increments the value option by amount.

        amount defaults to 1.0 if omitted."""
	def stop(self):
		"""Stop autoincrement mode: cancels any recurring timer event
        initiated by start."""
```
### py_simple_ttk.widgets.ProgressbarWidgets.LabeledProgressbar<a name="mark159"></a>[^](#mark157)
**Labeled Progressbar**

```py
class LabeledProgressbar(Labeler, ActiveProgressbar):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, orient='horizontal', labelside='left', is_child=False, default: float = 0, **kw):
		...
	def clear(self):
		"""Sets Progressbar progress to its default value `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self):
		"""Enable Progressbar. `Returns None`"""
	def enable(self):
		"""Disable Progressbar. `Returns None`"""
	def get(self):
		"""Set Progressbar progress. `Returns None`"""
	def link(self, widget):
		"""Easily link to other widgets, sets the progressbar var to the passed widget's var. `Returns None`"""
	def set(self, val):
		"""Get Progressbar progress. `Returns a String`"""
	def start(self, interval=None):
		"""Begin autoincrement mode: schedules a recurring timer event
        that calls method step every interval milliseconds.

        interval defaults to 50 milliseconds (20 steps/second) if omitted."""
	def step(self, amount=None):
		"""Increments the value option by amount.

        amount defaults to 1.0 if omitted."""
	def stop(self):
		"""Stop autoincrement mode: cancels any recurring timer event
        initiated by start."""
```
### py_simple_ttk.widgets.ProgressbarWidgets.LabeledMultiProgressbar<a name="mark160"></a>[^](#mark157)
**Labeled MultiWidget LabeledProgressbar**

```py
class LabeledMultiProgressbar(Labeler, Frame, MultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top', orient='horizontal'):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args, kwargs, widget_type=None) -> object:
		"""Overrides normal MultiWidgetMixin behavior to deal with vertical orientation. Will break most added widgets  `Returns None`"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def link(self, config: dict) -> None:
		"""Link to other widgets with a dict of subwidget keys to link to. This function will break if widgets without the link method are added to the MultiWidget. `Returns None`"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Radiobutton Widgets<a name="mark161"></a>[^](#mark17)

### py_simple_ttk.widgets.RadiobuttonWidgets.ActiveRadiobutton<a name="mark162"></a>[^](#mark161)
**ttk.Radiobutton with added features and the SuperWidgetMixin**

```py
class ActiveRadiobutton(Radiobutton, SuperWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, text: str, value: str, variable: tkinter.StringVar | tkinter.IntVar | tkinter.DoubleVar, widgetargs: dict = {}, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		...
	def enable(self) -> None:
		...
	def get(self) -> bool:
		"""`Returns a bool if the button is clicked`"""
	def set(self, val: str | int | float) -> None:
		"""Set value, input type varies base on tk variable type. `Returns None`"""
```
### py_simple_ttk.widgets.RadiobuttonWidgets.RadioTable<a name="mark163"></a>[^](#mark161)
**A table of ttk.RadioButtons**

```py
class RadioTable(Frame):
	def __init__(self, parent: tkinter.ttk.Frame, options: tuple, default: int = 0, variable_type: type = <class 'tkinter.StringVar'>, state: str = 'normal', columns: int = 1, pack_args: dict = {}, **kw):
		...
	def clear(self) -> None:
		"""Sets Radiobutton to its default value. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Enable Radiobutton. `Returns None`"""
	def enable(self) -> None:
		"""Disable Radiobutton. `Returns None`"""
	def get(self) -> str:
		"""Get Radiobutton value. `Returns a String`"""
	def set(self, val: bool) -> None:
		"""Set Radiobutton value. `Returns None`"""
```
### py_simple_ttk.widgets.RadiobuttonWidgets.LabeledRadioTable<a name="mark164"></a>[^](#mark161)
**Labeled RadioTable widget**

```py
class LabeledRadioTable(Labeler, RadioTable):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def clear(self) -> None:
		"""Sets Radiobutton to its default value. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Enable Radiobutton. `Returns None`"""
	def enable(self) -> None:
		"""Disable Radiobutton. `Returns None`"""
	def get(self) -> str:
		"""Get Radiobutton value. `Returns a String`"""
	def set(self, val: bool) -> None:
		"""Set Radiobutton value. `Returns None`"""
```
### py_simple_ttk.widgets.RadiobuttonWidgets.LabeledMultiRadioTable<a name="mark165"></a>[^](#mark161)
**Labeled MultiWidget LabeledRadioTable**

Used when you need multiple, vertically stacked LabeledRadioTables
```py
class LabeledMultiRadioTable(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### py_simple_ttk.widgets.RadiobuttonWidgets.SimpleRadioTable<a name="mark166"></a>[^](#mark161)
**A simplified RadioTable where the text is used at the value.**

Uses a tk.StringVar variable type only. Takes a tuple in the form `(value1, value2, ...)`
```py
class SimpleRadioTable(RadioTable):
	def __init__(self, parent: tkinter.ttk.Frame, options: tuple, **kw):
		...
	def clear(self) -> None:
		"""Sets Radiobutton to its default value. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Enable Radiobutton. `Returns None`"""
	def enable(self) -> None:
		"""Disable Radiobutton. `Returns None`"""
	def get(self) -> str:
		"""Get Radiobutton value. `Returns a String`"""
	def set(self, val: bool) -> None:
		"""Set Radiobutton value. `Returns None`"""
```
### py_simple_ttk.widgets.RadiobuttonWidgets.LabeledSimpleRadioTable<a name="mark167"></a>[^](#mark161)
**Labeled SimpleRadioTable widget**

```py
class LabeledSimpleRadioTable(Labeler, SimpleRadioTable):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, options: list, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def clear(self) -> None:
		"""Sets Radiobutton to its default value. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Enable Radiobutton. `Returns None`"""
	def enable(self) -> None:
		"""Disable Radiobutton. `Returns None`"""
	def get(self) -> str:
		"""Get Radiobutton value. `Returns a String`"""
	def set(self, val: bool) -> None:
		"""Set Radiobutton value. `Returns None`"""
```
### py_simple_ttk.widgets.RadiobuttonWidgets.LabeledMultiSimpleRadioTable<a name="mark168"></a>[^](#mark161)
**Labeled MultiWidget LabeledSimpleRadioTable**

Used when you need multiple, vertically stacked LabeledSimpleRadioTables
```py
class LabeledMultiSimpleRadioTable(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Scale Widgets<a name="mark169"></a>[^](#mark17)

### py_simple_ttk.widgets.ScaleWidgets.ActiveScale<a name="mark170"></a>[^](#mark169)
**ttk.Scale with added features and the SuperWidget mixin**

```py
class ActiveScale(Scale, SuperWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, command: Callable = None, default: float = 0, widgetargs: dict = {}, **kw):
		...
	def clear(self) -> None:
		"""Sets Scale to its default value. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Enable Scale. `Returns None`"""
	def enable(self) -> None:
		"""Disable Scale. `Returns None`"""
	def get(self) -> float:
		"""Get Scale value. `Returns a Float`"""
	def set(self, val: float) -> None:
		"""Set Scale value. `Returns None`"""
```
### py_simple_ttk.widgets.ScaleWidgets.LabeledScale<a name="mark171"></a>[^](#mark169)
**Labeled ActiveScale**

```py
class LabeledScale(Labeler, ActiveScale):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, command: Callable = None, orient: bool = 'horizontal', is_child: bool = False, labelside: str = 'left', **kw):
		...
	def clear(self) -> None:
		"""Sets Scale to its default value. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Enable Scale. `Returns None`"""
	def enable(self) -> None:
		"""Disable Scale. `Returns None`"""
	def get(self) -> float:
		"""Get Scale value. `Returns a Float`"""
	def set(self, val: float) -> None:
		"""Set Scale value. `Returns None`"""
```
### py_simple_ttk.widgets.ScaleWidgets.LabeledMultiScale<a name="mark172"></a>[^](#mark169)
**Labeled MultiWidget Labeled Scale**

```py
class LabeledMultiScale(Labeler, Frame, MultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top', orient='horizontal', command=None):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Override MultiWidgetMixin for vertical orientation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Spinbox Widgets<a name="mark173"></a>[^](#mark17)

### ActiveSpinbox<a name="mark174"></a>[^](#mark173)
**Spinbox with added features**

```py
class ActiveSpinbox(Spinbox, SuperWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, command: Callable = None, default: int = 0, on_keystroke: bool = False, bind_enter: bool = True, bind_escape_clear: bool = True, bind_mouse_wheel: bool = True, custom_values: bool = True, widgetargs: dict = {}, **kw):
		...
	def clear(self) -> None:
		"""Sets Spinbox to its default value. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Spinbox. `Returns None`"""
	def enable(self) -> None:
		"""Enable Spinbox. `Returns None`"""
	def get(self) -> int:
		"""Get Spinbox value. `Returns an Int`"""
	def set(self, val: str) -> None:
		"""Set Spinbox value. `Returns None`"""
```
### LabeledSpinbox<a name="mark175"></a>[^](#mark173)
**Labeled Spinbox with the SuperWidget mixin**

```py
class LabeledSpinbox(Labeler, ActiveSpinbox):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, labelside: str = 'left', is_child: bool = False, **kw):
		...
	def clear(self) -> None:
		"""Sets Spinbox to its default value. `Returns None`"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Spinbox. `Returns None`"""
	def enable(self) -> None:
		"""Enable Spinbox. `Returns None`"""
	def get(self) -> int:
		"""Get Spinbox value. `Returns an Int`"""
	def set(self, val: str) -> None:
		"""Set Spinbox value. `Returns None`"""
```
### LabeledMultiSpinbox<a name="mark176"></a>[^](#mark173)
**Labeled MultiWidget Spinbox.**

Used when you need multiple, vertically stacked Labeled Spinboxes
```py
class LabeledMultiSpinbox(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Text Widgets<a name="mark177"></a>[^](#mark17)

### py_simple_ttk.widgets.TextWidgets.ScrolledText<a name="mark178"></a>[^](#mark177)
**Scrolled Text with SuperWidget mixin**

Scrolled Text SuperWidget
```py
class ScrolledText(Scroller, Text, SuperWidgetMixin):
	def __init__(self, parent, **kw) -> object:
		...
	def clear(self) -> None:
		"""Empties the text box. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		...
	def edit_undo(self):
		"""Undoes the last edit action

        If the undo option is true. An edit action is defined
        as all the insert and delete commands that are recorded
        on the undo stack in between two separators. Generates
        an error when the undo stack is empty. Does nothing
        when the undo option is false
        """
	def enable(self) -> None:
		"""Enable Text box"""
	def get(self, start: str = '1.0', end: str = 'end'):
		"""Returns the contents of the text box with optional start/end kwargs. `Returns a String`"""
	def get_cursor(self):
		"""Get the current location of the cursor. `Returns None`"""
	def select_all(self, event=None) -> None:
		"""Selects all text. `Returns None`"""
	def set(self, val: str) -> None:
		"""Sets the text. `Returns a String`"""
	def window_create(self, index, cnf={}, **kw):
		"""Create a window at INDEX."""
```
### py_simple_ttk.widgets.TextWidgets.CopyBox<a name="mark179"></a>[^](#mark177)
**Scrolled Text with "Copy to Clipboard" Button**

A widget with a scrolled textbox and button that copies the textbox contents to the user's clipboard. Useful for form output, etc.
```py
class CopyBox(Frame):
	def __init__(self, parent: tkinter.ttk.Frame, **kw):
		...
	def clear(self) -> None:
		"""Clear CopyBox Contents"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable CopyBox"""
	def enable(self) -> None:
		"""Enable CopyBox"""
	def get(self) -> None:
		"""Get CopyBox contents"""
	def set(self, val: str) -> None:
		"""Set CopyBox Contents"""
```
### py_simple_ttk.widgets.TextWidgets.LabeledCopyBox<a name="mark180"></a>[^](#mark177)
**Labeled CopyBox widget**

```py
class LabeledCopyBox(Labeler, CopyBox):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, is_child: bool = False, labelside: str = 'left', **kw):
		...
	def clear(self) -> None:
		"""Clear CopyBox Contents"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable CopyBox"""
	def enable(self) -> None:
		"""Enable CopyBox"""
	def get(self) -> None:
		"""Get CopyBox contents"""
	def set(self, val: str) -> None:
		"""Set CopyBox Contents"""
```
### py_simple_ttk.widgets.TextWidgets.LabeledMultiCopyBox<a name="mark181"></a>[^](#mark177)
**Labeled MultiWidget CopyBox.**

Used when you need multiple, vertically stacked Labeled CopyBoxes
```py
class LabeledMultiCopyBox(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent, key: str, args: list, kwargs: dict, widget_type: type = None) -> object:
		"""Method for adding different widgets to a multiwidget post-instantiation"""
	def clear(self, config: list = None) -> None:
		"""Pass a list of subwidgets to clear or all are set to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to disable or all are disabled"""
	def enable(self, config: list = None) -> None:
		"""Pass a list of subwidgets to enable or all are enabled"""
	def get(self, config: list = None) -> dict:
		"""Pass a list of widget keys to get a dict of outputs"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Toplevel Widgets<a name="mark182"></a>[^](#mark17)

### py_simple_ttk.widgets.ToplevelWidgets.FocusedToplevel<a name="mark183"></a>[^](#mark182)
**Base Focused Toplevel Class**

Window that takes focus and center's itself on the current window. Used as a base class for other windows.
```py
class FocusedToplevel(Toplevel):
	def __init__(self, *args, title: str = None, window: tkinter.Toplevel = None, on_close: Callable = None, **kwargs):
		...
	def destroy(self) -> None:
		...
	def iconify(self):
		"""Display widget as icon."""
	def iconmask(self, bitmap=None):
		"""Set mask for the icon bitmap of this widget. Return the
        mask if None is given."""
```
### py_simple_ttk.widgets.ToplevelWidgets.NoticeWindow<a name="mark184"></a>[^](#mark182)
**Provides the user with a notice.**

`button_action` can call a function to help with determining acceptance vs. the user hitting the exit button.
```py
class NoticeWindow(FocusedToplevel):
	def __init__(self, *args, text: str = None, button_text: str = 'Continue', button_action: Callable = None, **kwargs):
		...
	def destroy(self) -> None:
		...
	def iconify(self):
		"""Display widget as icon."""
	def iconmask(self, bitmap=None):
		"""Set mask for the icon bitmap of this widget. Return the
        mask if None is given."""
```
### py_simple_ttk.widgets.ToplevelWidgets.YesNoCancelWindow<a name="mark185"></a>[^](#mark182)
**Provides the user with a yes/no/cancel option.**

`no_destroy` can be set to `True` to allow the window to remain open after a selection is made.
```py
class YesNoCancelWindow(FocusedToplevel):
	def __init__(self, *args, text: str = None, yes_enabled: bool = True, on_yes: Callable = None, yes_text: str = 'Yes', no_enabled: bool = True, on_no: Callable = None, no_text: str = 'No', cancel_enabled: bool = True, on_cancel: Callable = None, cancel_text: str = 'Cancel', no_destroy: bool = False, focus: str = '', **kwargs):
		...
	def destroy(self) -> None:
		...
	def iconify(self):
		"""Display widget as icon."""
	def iconmask(self, bitmap=None):
		"""Set mask for the icon bitmap of this widget. Return the
        mask if None is given."""
```
### py_simple_ttk.widgets.ToplevelWidgets.PromptWindow<a name="mark186"></a>[^](#mark182)
**Prompts the user for a text input**

`no_destroy` can be set to `True` to allow the window to remain open after a selection is made, useful for informing the user a string input was invalid via setting label_var. If the select_type kwarg is set to true the user will be prompted to select a data type (int / string) to return.
```py
class PromptWindow(FocusedToplevel):
	def __init__(self, *args, text: str = 'Enter Text:', on_yes=None, yes_text: str = 'Continue', on_cancel=None, cancel_text: str = 'Cancel', bind_enter: bool = True, no_destroy: bool = False, select_type: bool = False, focus='', **kwargs):
		...
	def destroy(self) -> None:
		...
	def iconify(self):
		"""Display widget as icon."""
	def iconmask(self, bitmap=None):
		"""Set mask for the icon bitmap of this widget. Return the
        mask if None is given."""
```
### py_simple_ttk.widgets.ToplevelWidgets.PasswordWindow<a name="mark187"></a>[^](#mark182)
**Password Entry window.**

Demo Password Entry Window, you will want to copy the source for this widget and rewrite it.
```py
class PasswordWindow(FocusedToplevel):
	def __init__(self, window=None, **kwargs):
		...
	def destroy(self) -> None:
		...
	def iconify(self):
		"""Display widget as icon."""
	def iconmask(self, bitmap=None):
		"""Set mask for the icon bitmap of this widget. Return the
        mask if None is given."""
```
### py_simple_ttk.widgets.ToplevelWidgets.ListWindow<a name="mark188"></a>[^](#mark182)
**Window to select an option from a Scrolled Listbox**

```py
class ListWindow(FocusedToplevel):
	def __init__(self, *args, options: list, text: str = 'Select Item:', on_yes=None, yes_text: str = 'Continue', on_cancel=None, cancel_text: str = 'Cancel', no_destroy: bool = False, select_mode: str = 'single', **kwargs):
		...
	def destroy(self) -> None:
		...
	def iconify(self):
		"""Display widget as icon."""
	def iconmask(self, bitmap=None):
		"""Set mask for the icon bitmap of this widget. Return the
        mask if None is given."""
```
## Misc Widgets<a name="mark189"></a>[^](#mark17)

### py_simple_ttk.widgets.ToolTip.ToolTip<a name="mark190"></a>[^](#mark189)
**Easy ToolTip**

Easily show theme-friendly tooltip. Currently only left and right align are supported.
```py
class ToolTip(ToolTipBase):
	def __init__(self, parent: object, text: str, align: str = 'left'):
		...
```
### py_simple_ttk.widgets.SizegripWidgets.EasySizegrip<a name="mark191"></a>[^](#mark189)
**Sizegrip widget with bindings**

Automatically packs self and binds mouse presses for systems that don't bind automatically.
```py
class EasySizegrip(Sizegrip):
	def __init__(self, *args, **kwargs):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self):
		...
	def enable(self):
		...
```
# SuperLib.utils<a name="mark192"></a>[^](#mark0)

## Utils<a name="mark193"></a>[^](#mark192)

### py_simple_ttk.utils.utils.check_if_module_installed<a name="mark194"></a>[^](#mark193)
> **Indicates if a packages is installed. `Returns a Boolean`**
> 
```python
def check_if_module_installed(package: str) -> bool:
> 	...
```
### py_simple_ttk.utils.utils.check_string_contains<a name="mark195"></a>[^](#mark193)
> **Returns `(True, char_index)` if any character from the list exists in the string otherwise returns `(False, None)`**
> 
```python
def check_string_contains(string: str, contains_list: tuple) -> tuple:
> 	...
```
### py_simple_ttk.utils.utils.dummy_function<a name="mark196"></a>[^](#mark193)
> **Dummy function that nicely prints out any passed args and kwargs. `Returns True`**
> 
```python
def dummy_function(*args, **kwargs) -> bool:
> 	...
```
### py_simple_ttk.utils.utils.get_friendly_time<a name="mark197"></a>[^](#mark193)
> **Gets a time string in one of several modes. Modes: `all, time, date, nice_date`. `Returns a String`**
> 
```python
def get_friendly_time(timestamp, mode: str = 'all') -> str:
> 	...
```
### py_simple_ttk.utils.utils.get_installed_packages<a name="mark198"></a>[^](#mark193)
> **Get an alphabetized list of available packages. `Returns a List`**
> 
```python
def get_installed_packages() -> list:
> 	...
```
### py_simple_ttk.utils.utils.get_unix_timestamp<a name="mark199"></a>[^](#mark193)
> **Get a unix timestamp. `Returns a Float`**
> 
```python
def get_unix_timestamp() -> float:
> 	...
```
### py_simple_ttk.utils.utils.get_unix_timestring<a name="mark200"></a>[^](#mark193)
> **Get a unix timestring. `Returns a String`**
> 
```python
def get_unix_timestring() -> str:
> 	...
```
### py_simple_ttk.utils.utils.get_user_home_folder<a name="mark201"></a>[^](#mark193)
> **Cross-platform function to get a user's home folder**
> 
```python
def get_user_home_folder() -> str:
> 	...
```
### py_simple_ttk.utils.utils.open_folder_in_explorer<a name="mark202"></a>[^](#mark193)
> **Cross-platform way to open a folder in the default file manager for a system**
> 
```python
def open_folder_in_explorer(path) -> None:
> 	...
```
### py_simple_ttk.utils.utils.sort_dict_by_keys<a name="mark203"></a>[^](#mark193)
> **Sorts a dictionary by its keys**
> 
```python
def sort_dict_by_keys(source: dict, reverse: bool = False) -> collections.OrderedDict:
> 	...
```
### py_simple_ttk.utils.utils.timer_decorator<a name="mark204"></a>[^](#mark193)
> **Decorator to add timing to a function**
> 
```python
def timer_decorator(func: Callable) -> None:
> 	...
```
## File Generators<a name="mark205"></a>[^](#mark192)

### py_simple_ttk.utils.HTML_Generator.HTML_Generator<a name="mark206"></a>[^](#mark205)
```py
class HTML_Generator(object):
	def __init__(self, indent='\t'):
		...
	def add_body_line(self, text=''):
		...
	def add_bold(self, text=''):
		...
	def add_center(self, text=''):
		...
	def add_comment(self, text):
		...
	def add_div(self, text=''):
		...
	def add_divider(self):
		...
	def add_list(self, items=[], ordered=False):
		...
	def add_list_item(self, item: str):
		...
	def add_paragraph(self, text=''):
		...
	def assemble(self):
		...
	def end_bold(self):
		...
	def end_center(self):
		...
	def end_div(self):
		...
	def end_list(self, ordered=False):
		...
	def end_paragraph(self):
		...
	def get_indent(self, offset=0):
		...
	def save(self, path):
		...
	def start_bold(self, text=''):
		...
	def start_center(self, text=''):
		...
	def start_div(self, text=''):
		...
	def start_list(self, items=[], ordered=False):
		...
	def start_paragraph(self, text=''):
		...
```
### py_simple_ttk.utils.TXT_Generator.TXT_Generator<a name="mark207"></a>[^](#mark205)
```py
class TXT_Generator(object):
	def __init__(self, ):
		...
	def add_body_line(self, text=''):
		...
	def add_divider(self):
		...
	def assemble(self):
		...
	def save(self, path):
		...
```
### py_simple_ttk.utils.MD_Generator.MD_Generator<a name="mark208"></a>[^](#mark205)
```py
class MD_Generator(object):
	def __init__(self, title=None, footnote_title='Notes:', footnote_heading_level=2, numbered_toc=False):
		...
	def add_blockquote(self, text, end='\n\n'):
		...
	def add_bold(self, text, end='\n\n'):
		...
	def add_bold_italic(self, text, end='\n'):
		...
	def add_break(self):
		...
	def add_code_block(self, text, lang='', end='\n'):
		...
	def add_heading_1(self, text, **kwargs):
		...
	def add_heading_2(self, text, **kwargs):
		...
	def add_heading_3(self, text, **kwargs):
		...
	def add_heading_4(self, text, **kwargs):
		...
	def add_heading_5(self, text, **kwargs):
		...
	def add_heading_6(self, text, **kwargs):
		...
	def add_horizontal_rule(self):
		...
	def add_italic(self, text, end='\n'):
		...
	def add_link(self, link, text=None, tooltip=None):
		...
	def add_multi_blockquote(self, texts):
		...
	def add_ordered_list(self, texts, indent=0):
		...
	def add_paragraph(self, text, end='\n\n'):
		...
	def add_to_ordered_list(self, index, text, indent=0):
		...
	def add_to_unordered_list(self, text, indent=0):
		...
	def add_toc(self, title, end='\n\n'):
		...
	def add_unordered_list(self, texts, indent=0):
		...
	def assemble(self):
		...
	def decrease_toc_depth(self):
		...
	def get_prefix(self):
		...
	def increase_toc_depth(self):
		...
	def insert_footnote(self, text):
		...
	def save(self, path):
		...
	def set_slogan(self, slogan):
		...
```
## History Mixin<a name="mark209"></a>[^](#mark192)

### py_simple_ttk.utils.History.HistoryMixin<a name="mark210"></a>[^](#mark209)
**Abstract mixin to add history-tracking to an application**

This object is meant to be used as a mixin rather than instantiated directly most of the time.
```py
class HistoryMixin(object):
	def __init__(self, data):
		...
	def add_history(self, data):
		...
	def clear_history(self, data):
		...
	def get_history_uid(self):
		...
	def redo(self):
		...
	def undo(self):
		...
```
## Color Functions<a name="mark211"></a>[^](#mark192)

### py_simple_ttk.utils.color.reduce_255<a name="mark212"></a>[^](#mark211)
> **Limits a val to a range of 0 to 255**
> 
```python
def reduce_255(in_value: int, maxval: int = 255) -> int:
> 	...
```
### py_simple_ttk.utils.color.rgb_to_hex<a name="mark213"></a>[^](#mark211)
> **Converts an rgb tuple to hex**
> 
```python
def rgb_to_hex(rgb: tuple) -> str:
> 	...
```
### py_simple_ttk.utils.color.rgba_to_hex<a name="mark214"></a>[^](#mark211)
> **Converts an rgba tuple to rgba hex**
> 
```python
def rgba_to_hex(rgba: tuple) -> str:
> 	...
```
### py_simple_ttk.utils.color.hex_to_rgb<a name="mark215"></a>[^](#mark211)
> **Converts hex to rgb tuple**
> 
```python
def hex_to_rgb(hex: str) -> tuple:
> 	...
```
### py_simple_ttk.utils.color.hex_to_rgba<a name="mark216"></a>[^](#mark211)
> **Tries to convert rgba hex to rgba, on failure converts rgb hex to rgb and sets a full opacity**
> 
```python
def hex_to_rgba(hex: str) -> tuple:
> 	...
```
### py_simple_ttk.utils.color.get_gradient<a name="mark217"></a>[^](#mark211)
> **Generates a black / white gradient with a given number of steps**
> 
```python
def get_gradient(steps: int) -> tuple:
> 	...
```
### py_simple_ttk.utils.color.rgb_to_scalar<a name="mark218"></a>[^](#mark211)
> **Converts an rgb itterable to scalar list**
> 
```python
def rgb_to_scalar(rgb: tuple) -> tuple:
> 	...
```
### py_simple_ttk.utils.color.scalar_to_rgb<a name="mark219"></a>[^](#mark211)
> **Converts rgb scalar to rgb list**
> 
```python
def scalar_to_rgb(rgb: tuple) -> tuple:
> 	...
```
### py_simple_ttk.utils.color.linear_gradient<a name="mark220"></a>[^](#mark211)
> **Generates a linear gradient between two colors, accepts html hex or rgb formats**
> 
```python
def linear_gradient(start_hex: str = '#000000', finish_hex: str = '#FFFFFF', n: int = 10) -> list:
> 	...
```
### py_simple_ttk.utils.color.get_rainbow<a name="mark221"></a>[^](#mark211)
> **Generates a rainbow with a given number of steps. Steps must be divisible by 4)**
> 
```python
def get_rainbow(steps: int) -> tuple:
> 	...
```
# MegaWidgets<a name="mark222"></a>[^](#mark0)

## Notes MegaWidget<a name="mark223"></a>[^](#mark222)

### py_simple_ttk.mega_widgets.notes.NotesTab<a name="mark224"></a>[^](#mark223)
```py
class NotesTab(Tab):
	def __init__(self, notebook, app):
		...
	def copy_note(self, note):
		...
	def delete_note(self, note):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def export_note_html(self, note):
		...
	def export_note_json(self, note):
		...
	def export_note_markdown(self, note):
		...
	def export_note_text(self, note):
		...
	def load_notes(self):
		...
	def make_new_note(self, title):
		...
	def new_note(self, event=None):
		...
	def on_toplevel_destroy(self, *args):
		"""Function for toplevels to call on no / cancel"""
	def reload_notes(self):
		...
	def rename_note(self, note):
		...
	def start_new_note(self, title=None):
		...
```
## Conversation MegaWidget<a name="mark225"></a>[^](#mark222)

### py_simple_ttk.mega_widgets.chat.ConversationsTab<a name="mark226"></a>[^](#mark225)
```py
class ConversationsTab(Tab):
	def __init__(self, notebook, app):
		...
	def copy_conversation(self, conversation):
		...
	def delete_conversation(self, conversation):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def export_conversation_html(self, conversation):
		...
	def export_conversation_json(self, conversation):
		...
	def export_conversation_markdown(self, conversation):
		...
	def export_conversation_text(self, conversation):
		...
	def get_cached_icon(self, size, color, char):
		...
	def get_user_icon(self, user):
		...
	def load_conversations(self):
		...
	def make_new_conversation(self, title):
		...
	def new_conversation(self, event=None):
		...
	def on_toplevel_destroy(self, *args):
		"""Function for toplevels to call on no / cancel"""
	def reload_conversations(self):
		...
	def rename_conversation(self, conversation):
		...
	def start_new_conversation(self, title=None):
		...
```
## Profile Management<a name="mark227"></a>[^](#mark222)

### py_simple_ttk.utils.ProfilesSystem.ProfilesSystem<a name="mark228"></a>[^](#mark227)
```py
class ProfilesSystem(object):
	def __init__(self, select_profile_actions: list = [], refresh_profiles_actions: list = [], profiles_dir: str = 'C:\\Users\\arcti\\github\\py_simple_ttk\\Profiles', handle_duplicates: bool = True):
		...
	def add_refresh_profiles_action(self, action: Callable) -> None:
		"""Add an action to the profiles list refresh actions"""
	def add_refresh_profiles_actions(self, actions: list) -> None:
		"""Add a list of actions to the profiles list refresh actions"""
	def add_select_profile_action(self, action: Callable) -> None:
		"""Add an action to the profile switch actions"""
	def add_select_profile_actions(self, actions: list) -> None:
		"""Add a list of actions to the profile switch actions"""
	def check_if_name_exists_in_profiles(self, name: str, profiles: list = None) -> bool:
		"""Check if a name exists in a list of profiles, if no list is provided uses the list of all profiles. `Returns a Bool`"""
	def clear_refresh_profile_actions(self, new: list = []) -> None:
		"""Clear out the profiles list refresh actions, optionally replacing them with new ones"""
	def clear_select_profile_actions(self, new: list = []) -> None:
		"""Clear out the profile switch actions, optionally replacing them with new ones"""
	def create_profile(self, name: str) -> py_simple_ttk.utils.ProfilesSystem.UserProfile:
		"""Creates a profile with a given name. `Raises ValueError` if the profile name already exists. `Returns a UserProfile`"""
	def delete_profile(self, profile: py_simple_ttk.utils.ProfilesSystem.UserProfile) -> None:
		...
	def get_last_used_profile(self, profiles: list = None) -> py_simple_ttk.utils.ProfilesSystem.UserProfile:
		"""Returns the most recently accessed profile"""
	def get_profile_by_username(self, name: str) -> py_simple_ttk.utils.ProfilesSystem.UserProfile:
		...
	def get_profile_names(self) -> list:
		"""Returns an alphabetically sorted list of profile names"""
	def handle_duplicate_profile_names(self, name: str) -> None:
		"""Makes profile names unique if they have identical names. The most recently accessed profile (according to the file json) keeps its name untouched. `Returns None`"""
	def handle_refresh_profiles_actions(self) -> None:
		"""Handle on-refresh-profiles actions"""
	def handle_select_profile_actions(self) -> None:
		"""Handle on-profile-selection actions"""
	def select_profile(self, profile: py_simple_ttk.utils.ProfilesSystem.UserProfile) -> None:
		"""Change the currently selected profile"""
	def select_profile_by_username(self, name: str) -> None:
		...
	def sort_profiles_by_accessed(self, profiles: list = None) -> None:
		"""Sort a list of profiles by last accessed, if no list is provided returns a sorted list of all profiles in the system. `Returns a List`"""
```
### py_simple_ttk.utils.ProfilesSystem.UserProfile<a name="mark229"></a>[^](#mark227)
**A class to represent a User / User's Preferences**

Must pass a unique username and a unique     identifier for new profile.
```py
class UserProfile(object):
	def __init__(self, path: str, username: str = None, atomic: str = None):
		...
	def clear_preferences(self, preferences: list = None) -> None:
		...
	def get_preference(self, key: str) -> object:
		...
	def load(self, path: str = None, overwrite_path: bool = False) -> None:
		...
	def save(self, path: str = None, overwrite_path: bool = False) -> None:
		...
	def set_preference(self, key: str, value: str) -> None:
		...
	def set_username(self, name: str) -> None:
		...
```
### py_simple_ttk.utils.ProfilesSystem.get_profiles_folder<a name="mark230"></a>[^](#mark229)
> **Gets the absolute path to the included profiles folder. `Returns a String`**
> 
```python
def get_profiles_folder() -> str:
> 	...
```
### py_simple_ttk.utils.ProfilesSystem.get_profiles_list<a name="mark231"></a>[^](#mark229)
> **Gets a list of profile files at a given path. `Returns a List of Path strings`**
> 
```python
def get_profiles_list(path: str = './Profiles', verbose: bool = False) -> list:
> 	...
```
# Changelog<a name="mark232"></a>[^](#mark0)

## 0.1.29<a name="mark233"></a>[^](#mark232)

Move TicTacToe to examples

## 0.1.28<a name="mark234"></a>[^](#mark232)

Move SuperWidgetMixin from WidgetsCore.py to SuperWidget.py

## 0.1.27<a name="mark235"></a>[^](#mark232)

Add ActiveButton, ActiveCheckButton, ActiveComboBox, ActiveEntry, ActiveOptionMenu, ActiveProgressbar, ActiveRadioButton, ActiveScale, ColumnFrame, CycleButton, LabeledButton, LabeledMultiButton, LabeledCycleButton, LabeledMultiCycleButton, LabeledMultiRadioTable, LabeledMultiSimpleRadioTable, LabeledRadioTable, LabeledSimpleRadioTable, RadioTable, SimpleRadioTable, Remove: LabeledRadioButton, LabeledMultiRadioButton

## 0.1.26<a name="mark236"></a>[^](#mark232)

Add Spinbox widgets, fix Copybox

## 0.1.25<a name="mark237"></a>[^](#mark232)

Reduce packaged fonts color pallete

## 0.1.24<a name="mark238"></a>[^](#mark232)

Update readme generator with more config keys, fix ini readme md code block being marked as python

## 0.1.23<a name="mark239"></a>[^](#mark232)

Add columns to Configurable Launcher

## 0.1.22<a name="mark240"></a>[^](#mark232)

Fix readme

## 0.1.21<a name="mark241"></a>[^](#mark232)

Fix readme

## 0.1.20<a name="mark242"></a>[^](#mark232)

Add counter widget.

## 0.1.19<a name="mark243"></a>[^](#mark232)

Add dynamic launcher system.

## 0.1.18<a name="mark244"></a>[^](#mark232)

Add Ordered Listbox, add more bindings to SuperWidget, cleanup

## 0.1.17<a name="mark245"></a>[^](#mark232)

Add set_desktop_background to WidgetsCore.py

## 0.1.16<a name="mark246"></a>[^](#mark232)

Add needs_white_text to color.py, add pyinstaller compatibility to WidgetsCore.get_asset

## 0.1.15<a name="mark247"></a>[^](#mark232)

Fix misnamed function in color.py

## 0.1.14<a name="mark248"></a>[^](#mark232)

Fix missing import in app.py

## 0.1.13<a name="mark249"></a>[^](#mark232)

reduced variety of packaged font images, fixed bug with constrained widgets command not triggering

## 0.1.12<a name="mark250"></a>[^](#mark232)

Add Constrained + Labeled + Multi Entries (>35 widgets)

## 0.1.11<a name="mark251"></a>[^](#mark232)

Fix LabeledPathEntry error when no dialog type was specified

## 0.1.10<a name="mark252"></a>[^](#mark232)

Add LabeledPathEntry to EntryWidgets.py

## 0.1.9<a name="mark253"></a>[^](#mark232)

Add pencil icons to assets

## 0.1.8<a name="mark254"></a>[^](#mark232)

Fix labeled button not running command on press

## 0.1.7<a name="mark255"></a>[^](#mark232)

add labeled button

## 0.1.6<a name="mark256"></a>[^](#mark232)

Fix missing Labeler import

## 0.1.5<a name="mark257"></a>[^](#mark232)

Fix broken package

## 0.1.4<a name="mark258"></a>[^](#mark232)

Fix broken package

## 0.1.3<a name="mark259"></a>[^](#mark232)

More cleanup, input fixes.py

## 0.1.2<a name="mark260"></a>[^](#mark232)

Cleanup, move type lists to generate_readme.py

## 0.1.1<a name="mark261"></a>[^](#mark232)

Fix missing 'ListWindow' import in app.py

## 0.1.0<a name="mark262"></a>[^](#mark232)

Modulize



Generated with [py_simple_readme](https://github.com/AndrewSpangler/py_simple_readme)