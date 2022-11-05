# py_simple_ttk 0.1.17<a name="mark0"></a>

***Themes don't have to be hard.***

- [About](#mark1)
- [Requirements](#mark2)
- [Configuring ini.json](#mark3)
- [Widgets](#mark4)
	- [Button Widgets](#mark5)
		- [LabeledButton](#mark6)
	- [Core Functions](#mark7)
		- [bbox_to_width_and_height](#mark8)
		- [center_window](#mark9)
		- [check_in_bounds](#mark10)
		- [complex_widget_search](#mark11)
		- [copy_to_user_clipboard](#mark12)
		- [create_round_rectangle](#mark13)
		- [default_pack](#mark14)
		- [default_separator](#mark15)
		- [default_vertical_pack](#mark16)
		- [default_vertical_separator](#mark17)
		- [enable_notebook_movement](#mark18)
		- [focus_next](#mark19)
		- [force_aspect](#mark20)
		- [get_asset](#mark21)
		- [get_bundled_themes_list](#mark22)
		- [get_generated_font_images_lookup](#mark23)
		- [get_local_appdata_folder](#mark24)
		- [get_themes_folder](#mark25)
		- [open_link](#mark26)
		- [recursive_widget_search](#mark27)
		- [run_cl](#mark28)
	- [Core Widgets](#mark29)
		- [MultiWidgetMixin](#mark30)
		- [SuperWidgetMixin](#mark31)
	- [Tabs](#mark32)
		- [Tab](#mark33)
		- [LauncherTab](#mark34)
		- [BrowserLauncherTab](#mark35)
		- [CommandLauncherTab](#mark36)
		- [ConsoleTab](#mark37)
		- [TableTab](#mark38)
		- [TreeTableTab](#mark39)
	- [Canvas Widgets](#mark40)
		- [ResizableCanvas](#mark41)
		- [ScrolledCanvas](#mark42)
		- [TiledCanvas](#mark43)
		- [ExampleTile](#mark44)
	- [Checkbutton Widgets](#mark45)
		- [LabeledCheckbutton](#mark46)
		- [LabeledMultiCheckbutton](#mark47)
	- [Combobox Widgets](#mark48)
		- [LabeledCombobox](#mark49)
		- [LabeledMultiCombobox](#mark50)
	- [Console Widgets](#mark51)
		- [ConsoleWidget](#mark52)
	- [Constraining Functions](#mark53)
		- [check_entry_type](#mark54)
		- [check_entry_int](#mark55)
		- [check_entry_float](#mark56)
		- [check_entry_contents](#mark57)
		- [check_entry_ascii_lowercase](#mark58)
		- [check_entry_ascii_uppercase](#mark59)
		- [check_entry_ascii_letters](#mark60)
		- [check_entry_ascii_digits](#mark61)
		- [check_entry_ascii_uppercase_digits](#mark62)
		- [check_entry_ascii_lowercase_digits](#mark63)
		- [check_entry_ascii_hexdigits](#mark64)
		- [check_entry_ascii_octdigits](#mark65)
		- [check_entry_ascii_letters_digits](#mark66)
		- [check_entry_ascii_printable](#mark67)
	- [Entry Widgets](#mark68)
		- [ScrolledEntry](#mark69)
		- [LabeledEntry](#mark70)
		- [LabeledMultiEntry](#mark71)
		- [LabeledButtonEntry](#mark72)
		- [LabeledMultiButtonEntry](#mark73)
		- [LabeledPathEntry](#mark74)
		- [PasswordEntry](#mark75)
		- [ConstrainedEntry](#mark76)
		- [LabeledConstrainedEntry](#mark77)
		- [IntEntry](#mark78)
		- [LabeledIntEntry](#mark79)
		- [LabeledMultiIntEntry](#mark80)
		- [FloatEntry](#mark81)
		- [LabeledFloatEntry](#mark82)
		- [LabeledMultiFloatEntry](#mark83)
		- [LowercaseEntry](#mark84)
		- [LabeledLowercaseEntry](#mark85)
		- [LabeledMultiLowercaseEntry](#mark86)
		- [UppercaseEntry](#mark87)
		- [LabeledUppercaseEntry](#mark88)
		- [LabeledMultiUppercaseEntry](#mark89)
		- [LettersEntry](#mark90)
		- [LabeledLettersEntry](#mark91)
		- [LabeledMultiLettersEntry](#mark92)
		- [DigitsEntry](#mark93)
		- [LabeledDigitsEntry](#mark94)
		- [LabeledMultiDigitsEntry](#mark95)
		- [UppercaseDigitsEntry](#mark96)
		- [LabeledUppercaseDigitsEntry](#mark97)
		- [LabeledMultiUppercaseDigitsEntry](#mark98)
		- [LowercaseDigitsEntry](#mark99)
		- [LabeledLowercaseDigitsEntry](#mark100)
		- [LabeledMultiLowercaseDigitsEntry](#mark101)
		- [LettersDigitsEntry](#mark102)
		- [LabeledLettersDigitsEntry](#mark103)
		- [LabeledMultiLettersDigitsEntry](#mark104)
		- [HexdigitsEntry](#mark105)
		- [LabeledHexdigitsEntry](#mark106)
		- [LabeledMultiHexdigitsEntry](#mark107)
		- [OctdigitsEntry](#mark108)
		- [LabeledOctdigitsEntry](#mark109)
		- [LabeledMultiOctdigitsEntry](#mark110)
		- [PrintableEntry](#mark111)
		- [LabeledPrintableEntry](#mark112)
		- [LabeledMultiPrintableEntry](#mark113)
	- [KeyPad Widgets](#mark114)
		- [KeypadButton](#mark115)
		- [BaseKeypad](#mark116)
		- [DialerKeypad](#mark117)
	- [Labeler Widget](#mark118)
		- [LabeledButton](#mark119)
	- [ListBox Widgets](#mark120)
		- [ScrolledListBox](#mark121)
		- [Table](#mark122)
	- [OptionMenu Widgets](#mark123)
		- [LabeledOptionMenu](#mark124)
		- [LabeledMultiOptionMenu](#mark125)
	- [ProgressBar Widgets](#mark126)
		- [LabeledProgressbar](#mark127)
		- [LabeledMultiProgressbar](#mark128)
	- [Radiobutton Widgets](#mark129)
		- [LabeledRadiobutton](#mark130)
		- [LabeledMultiRadiobutton](#mark131)
	- [Scale Widgets](#mark132)
		- [LabeledScale](#mark133)
		- [LabeledMultiScale](#mark134)
	- [Text Widgets](#mark135)
		- [ScrolledText](#mark136)
		- [CopyBox](#mark137)
	- [Toplevel Widgets](#mark138)
		- [FocusedToplevel](#mark139)
		- [NoticeWindow](#mark140)
		- [YesNoCancelWindow](#mark141)
		- [PromptWindow](#mark142)
		- [PasswordWindow](#mark143)
		- [ListWindow](#mark144)
	- [Misc Widgets](#mark145)
		- [ToolTip](#mark146)
		- [EasySizegrip](#mark147)
- [SuperLib.utils](#mark148)
	- [Utils](#mark149)
		- [check_if_module_installed](#mark150)
		- [check_string_contains](#mark151)
		- [dummy_function](#mark152)
		- [get_friendly_time](#mark153)
		- [get_installed_packages](#mark154)
		- [get_unix_timestamp](#mark155)
		- [get_unix_timestring](#mark156)
		- [get_user_home_folder](#mark157)
		- [open_folder_in_explorer](#mark158)
		- [sort_dict_by_keys](#mark159)
		- [timer_decorator](#mark160)
	- [File Generators](#mark161)
		- [HTML_Generator](#mark162)
		- [TXT_Generator](#mark163)
		- [MD_Generator](#mark164)
	- [History Mixin](#mark165)
		- [HistoryMixin](#mark166)
	- [Color Functions](#mark167)
		- [reduce_255](#mark168)
		- [rgb_to_hex](#mark169)
		- [rgba_to_hex](#mark170)
		- [hex_to_rgb](#mark171)
		- [hex_to_rgba](#mark172)
		- [get_gradient](#mark173)
		- [rgb_to_scalar](#mark174)
		- [scalar_to_rgb](#mark175)
		- [linear_gradient](#mark176)
		- [get_rainbow](#mark177)
- [MegaWidgets](#mark178)
	- [Notes MegaWidget](#mark179)
		- [NotesTab](#mark180)
	- [Conversation MegaWidget](#mark181)
		- [ConversationsTab](#mark182)
	- [Profile Management](#mark183)
		- [ProfilesSystem](#mark184)
		- [UserProfile](#mark185)
		- [get_profiles_folder](#mark186)
		- [get_profiles_list](#mark187)
- [Changelog](#mark188)
	- [0.1.17](#mark189)
	- [0.1.16](#mark190)
	- [0.1.15](#mark191)
	- [0.1.14](#mark192)
	- [0.1.13](#mark193)
	- [0.1.12](#mark194)
	- [0.1.11](#mark195)
	- [0.1.10](#mark196)
	- [0.1.9](#mark197)
	- [0.1.8](#mark198)
	- [0.1.7](#mark199)
	- [0.1.6](#mark200)
	- [0.1.5](#mark201)
	- [0.1.4](#mark202)
	- [0.1.3](#mark203)
	- [0.1.2](#mark204)
	- [0.1.1](#mark205)
	- [0.1.0](#mark206)

---

# About<a name="mark1"></a>[^](#mark0)

py_simple_ttk exists because I got tired of rewriting the same code over and over for simple projects. The goal is to provide a variety of meta widgets with consistent get/set/enable/disable/destroy methods and mega-widgets that make ttk development easier and faster. Features include built-in theme support, a score of labeled and multi-widgets, tools for easy form building, a sample application demonstrating many of py_simple_ttk's features, a configuration file system, and much more. ![Lines of code](https://img.shields.io/tokei/lines/github/AndrewSpangler/py_simple_ttk)

# Requirements<a name="mark2"></a>[^](#mark0)



# Configuring ini.json<a name="mark3"></a>[^](#mark0)

```python
+--------------------+-------------------------------------------+
|        Key         |                   Value                   |
+--------------------+-------------------------------------------+
| application        | Application Name (String)                 |
| version            | Application Version (String)              |
| icon               | Application Icon Path (String)            |
| width              | Startup Window Width (Int)                |
| height             | Startup Window Height (Int)               |
| minwidth           | Window Minimum Width (Int)                |
| minheight          | Window Minimum Height (Int)               |
| scaling            | Window Scaling (Float)                    |
| scale_minsize      | Scale application Minimum Size (Boolean)  |
| scale_startsize    | Scale application Start Size (Boolean)    |
| resizable_width    | Enable Window Width Resizing (Boolean)    |
| resizable_height   | Enable Window Height Resizing (Boolean)   |
| start_maximized    | Start Window Maximized (Boolean)          |
| enable_maximized   | Enable Window Maximized (Boolean)         |
| start_fullscreen   | Start Window in Fullscreen mode (Boolean) |
| enable_fullscreen  | Enable Window Fullscreen option (Boolean) |
| enable_themes_menu | Enable Themes Dropdown (Boolean)          |
| movable_tabs       | Enable Moveable Notebook Tabs (Boolean)   |
| enable_users       | Enable a User Profiles System             |
+--------------------+-------------------------------------------+
```
# Widgets<a name="mark4"></a>[^](#mark0)

## Button Widgets<a name="mark5"></a>[^](#mark4)

### LabeledButton<a name="mark6"></a>[^](#mark5)
> **Labeled Button widget**
> 
> ```py
> class LabeledButton(Labeler, Button):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, is_child: bool = False, command=None, **kw):
> 		...
> 	def clear(self) -> None:
> 		"""Set button text to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> str:
> 		"""Get button text"""
> 	def set(self, val: str) -> None:
> 		"""Set button text"""
> ```
## Core Functions<a name="mark7"></a>[^](#mark4)

### py_simple_ttk.widgets.WidgetsCore.bbox_to_width_and_height<a name="mark8"></a>[^](#mark7)
> **Takes a bbox and converts it to a width and height tuple.**
> 
> ```python
def bbox_to_width_and_height(bbox: tuple):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.center_window<a name="mark9"></a>[^](#mark7)
> **Centers spawn window on main window. Call win.update_idletasks() on either window before calling this if said window is not yet shown.**
> 
> ```python
def center_window(main_window: tkinter.Tk, spawn_window: tkinter.Toplevel):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.check_in_bounds<a name="mark10"></a>[^](#mark7)
> **Checks if a position is within a given bounds. Pos is generally a mouse event position tuple, bounds is generally a canvas.bbox(), but a (left, top, right, bottom) tuple will work too.**
> 
> ```python
def check_in_bounds(pos: tuple, bounds: tuple):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.complex_widget_search<a name="mark11"></a>[^](#mark7)
> **A more robust version of the widget search with lists for multiple widget types found in one go**
> 
> ```python
def complex_widget_search(node_widget, widget_types_to_find: list, found_lists={}):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.copy_to_user_clipboard<a name="mark12"></a>[^](#mark7)
> **Copies a string to the user's clipboard.**
> 
> ```python
def copy_to_user_clipboard(widget, value):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.create_round_rectangle<a name="mark13"></a>[^](#mark7)
> **Draws a rounded rectangle of a given radius on a tk.canvas**
> 
> ```python
def create_round_rectangle(canvas, x1, y1, x2, y2, r=20, fill='', outline='#000000', **kwargs):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.default_pack<a name="mark14"></a>[^](#mark7)
> **Apply a consistent descending packing method.**
> 
> ```python
def default_pack(widget, bottom: bool = False, padx=5):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.default_separator<a name="mark15"></a>[^](#mark7)
> **Apply a consistent horizontal separator.**
> 
> ```python
def default_separator(f: tkinter.ttk.Frame, padx: int = 35, pady=(10, 5)):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.default_vertical_pack<a name="mark16"></a>[^](#mark7)
> **Apply a consistent packing method to vertically packed widgets.**
> 
> ```python
def default_vertical_pack(widget, expand: bool = False, fill: str = 'both', padx: int = 0):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.default_vertical_separator<a name="mark17"></a>[^](#mark7)
> **Apply a consistent vertical separator.**
> 
> ```python
def default_vertical_separator(frame: tkinter.ttk.Frame, pady: int = 15, padx: int = 10):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.enable_notebook_movement<a name="mark18"></a>[^](#mark7)
> **Copyright CJB 2010-07-31: https://wiki.tcl-lang.org/page/Drag+and+Drop+Notebook+Tabs Enables Tab dragging in subsequently created notebooks. Only run this function once.**
> 
> ```python
def enable_notebook_movement(app):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.focus_next<a name="mark19"></a>[^](#mark7)
> **Forces focus to the widget after the one that triggered the event**
> 
> ```python
def focus_next(event):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.force_aspect<a name="mark20"></a>[^](#mark7)
> **Forces an inner frame to maintain an aspect ratio regardless of the outer frame's size**
> 
> ```python
def force_aspect(inner_frame: tkinter.ttk.Frame, outer_frame: tkinter.ttk.Frame, ratio=1.7777777777777777):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.get_asset<a name="mark21"></a>[^](#mark7)
> **Gets an asset from the included assets folder by relative path. Works with pyinstaller.**
> 
> ```python
def get_asset(path, folder='C:\\Users\\arcti\\github\\py_simple_ttk\\py_simple_ttk\\./assets'):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.get_bundled_themes_list<a name="mark22"></a>[^](#mark7)
> **None**
> 
> ```python
def get_bundled_themes_list(verbose=False):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.get_generated_font_images_lookup<a name="mark23"></a>[^](#mark7)
> **Makes a lookup for the pre-generated open-sans font monograms that ship with py_simple_ttk.**
> 
> ```python
def get_generated_font_images_lookup(path=None):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.get_local_appdata_folder<a name="mark24"></a>[^](#mark7)
> **Opens user's Windows home folder. Only works on Windows for obvious reasons.**
> 
> ```python
def get_local_appdata_folder():
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.get_themes_folder<a name="mark25"></a>[^](#mark7)
> **Gets the absolute path to the included themes folder**
> 
> ```python
def get_themes_folder():
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.open_link<a name="mark26"></a>[^](#mark7)
> **Opens a link in the user's default web browser. `Returns None`**
> 
> ```python
def open_link(link: str):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.recursive_widget_search<a name="mark27"></a>[^](#mark7)
> **Adds widgets of a given type to a list as it travels up, away from the root of a widget tree. This method can be slow on large widget trees but is useful for retheming tk widgets with ttk formatting on theme changes. `Returns a list of widgets`**
> 
> ```python
def recursive_widget_search(node_widget, widget_type_to_find, found_list=[]):
> 	...
> ```
### py_simple_ttk.widgets.WidgetsCore.run_cl<a name="mark28"></a>[^](#mark7)
> **Runs something via command line. `Returns None`**
> 
> ```python
def run_cl(commands: list):
> 	...
> ```
## Core Widgets<a name="mark29"></a>[^](#mark4)

### py_simple_ttk.widgets.MultiWidget.MultiWidgetMixin<a name="mark30"></a>[^](#mark29)
> **An abstract mixin that provides a way to easily instantiate multiple of the same class of a widget and making complicated forms with simple get/set methods.**
> 
> MultiWidgets support a simple get/set system. Calling get without a configuration list returns a dict of subwidget keys mapped to the values of each subwidget's .get value. Passing a list of subwidget keys limits MultiWidgetMixin.get to said subwidgets. Subclassing a multiwidget with one or more instances of one class and then calling multiwidget.add() with different classes after is acceptable assuming the widget supports being added and .get / .set / .enable / .disable / .clear methods.
> ```py
> class MultiWidgetMixin(object):
> 	def __init__(self, widget_type, config: dict):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.WidgetsCore.SuperWidgetMixin<a name="mark31"></a>[^](#mark29)
> **Mixin to easily bind many of the common tkinter events.**
> 
> This class serves to add bindings for the majority of common tkinter widget events. The bindings are made in add mode to prevent previous / new bindings from causing unintended side-effects.
> ```py
> class SuperWidgetMixin(object):
> 	def __init__(self, on_mouse_enter=None, on_mouse_leave=None, on_mouse_move=None, on_mouse_wheel=None, on_left_click=None, on_middle_click=None, on_right_click=None, on_configure=None, bind_mouse_scroll=False):
> 		...
> ```
## Tabs<a name="mark32"></a>[^](#mark4)

### py_simple_ttk.widgets.Tabs.Tab<a name="mark33"></a>[^](#mark32)
> **The core Tab class.**
> 
> The notebook object can be any ttk.Notebook, automatically adds itself to its parent notebook with title being the tab label. This class may be instantiated directly and added to or subclassed based on need.
> ```py
> class Tab(Frame):
> 	def __init__(self, notebook: tkinter.ttk.Notebook, title: str):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
### py_simple_ttk.widgets.Tabs.LauncherTab<a name="mark34"></a>[^](#mark32)
> **Basic Tab for launching tasks from a list.**
> 
> Performs an action on a list of options. The options argument is formatted as such: `options = {"Button Text 1": val1,"Button Text 2": val2}` Button presses will call `action(val)`
> ```py
> class LauncherTab(Tab):
> 	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, options: dict, action: Callable):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
### py_simple_ttk.widgets.Tabs.BrowserLauncherTab<a name="mark35"></a>[^](#mark32)
> **LauncherTab that opens a list of URLS/Files**
> 
> Takes a dict of button texts as keys and urls to open as values
> ```py
> class BrowserLauncherTab(LauncherTab):
> 	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, options: dict):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
### py_simple_ttk.widgets.Tabs.CommandLauncherTab<a name="mark36"></a>[^](#mark32)
> **LauncherTab that runs a list of commands**
> 
> Takes a dict of button texts as keys and command prompt commands to execute as values
> ```py
> class CommandLauncherTab(LauncherTab):
> 	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, options: dict):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
### py_simple_ttk.widgets.Tabs.ConsoleTab<a name="mark37"></a>[^](#mark32)
> **Basic console tab using a ConsoleWidget**
> 
> ```py
> class ConsoleTab(Tab):
> 	def __init__(self, notebook: tkinter.ttk.Notebook, **kwargs):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
### py_simple_ttk.widgets.Tabs.TableTab<a name="mark38"></a>[^](#mark32)
> **Basic Table Tab**
> 
> table_contents is a dictionary whose keys map to lists with the column contents
> ```py
> class TableTab(Tab):
> 	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, table_contents: dict, **kw):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
### py_simple_ttk.widgets.Tabs.TreeTableTab<a name="mark39"></a>[^](#mark32)
> **Improved Table Tab**
> 
> table_contents is a dictionary whose keys map to list with the column contents
> ```py
> class TreeTableTab(Tab):
> 	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, table_contents: dict = {}, **kw):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
## Canvas Widgets<a name="mark40"></a>[^](#mark4)

### py_simple_ttk.widgets.ResizableCanvas.ResizableCanvas<a name="mark41"></a>[^](#mark40)
> **Resizeable Canvas**
> 
> Canvas resizes to fit frame on configure event.
> ```py
> class ResizableCanvas(Canvas):
> 	def __init__(self, parent, **kw):
> 		...
> 	def create_arc(self, *args, **kw):
> 		"""Create arc shaped region with coordinates x1,y1,x2,y2."""
> 	def create_bitmap(self, *args, **kw):
> 		"""Create bitmap with coordinates x1,y1."""
> 	def create_image(self, *args, **kw):
> 		"""Create image item with coordinates x1,y1."""
> 	def create_line(self, *args, **kw):
> 		"""Create line with coordinates x1,y1,...,xn,yn."""
> 	def create_oval(self, *args, **kw):
> 		"""Create oval with coordinates x1,y1,x2,y2."""
> 	def create_polygon(self, *args, **kw):
> 		"""Create polygon with coordinates x1,y1,...,xn,yn."""
> 	def create_rectangle(self, *args, **kw):
> 		"""Create rectangle with coordinates x1,y1,x2,y2."""
> 	def create_round_rectangle(self, x1: float, y1: float, x2: float, y2: float, r: float = 20, fill: str = '', outline: str = '#000000', **kwargs):
> 		"""Draws a rounded rectangle of a given radius on a tk.canvas."""
> 	def create_text(self, *args, **kw):
> 		"""Create text with coordinates x1,y1."""
> 	def create_window(self, *args, **kw):
> 		"""Create window with coordinates x1,y1,x2,y2."""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def refresh(self):
> 		"""Refresh Canvas"""
> ```
### py_simple_ttk.widgets.ScrolledCanvas.ScrolledCanvas<a name="mark42"></a>[^](#mark40)
> **Resizeable, Auto-Scrollbarred Canvas**
> 
> Canvas resizes to fit frame on configure event. Canvas has automatic Scrollbars that appear when needed. Canvas background color is based on current theme. Due to how the scrolling is handled the actual Canvas is accessd via `ScrolledCanvas().canvas`.
> ```py
> class ScrolledCanvas(Frame):
> 	def __init__(self, parent, on_mouse_enter=None, on_mouse_leave=None, on_mouse_move=None, on_mouse_wheel=None, on_left_click=None, on_middle_click=None, on_right_click=None, on_configure=None, bind_canvas_scroll=True, **kw):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get_adjusted_y_view(self, event):
> 		"""Gets a canvas y-view adjusted based on its scrolled position"""
> 	def use_style(self, style):
> 		"""Reformat with a given ttk style. `Returns None`"""
> ```
### py_simple_ttk.widgets.ScrolledCanvas.TiledCanvas<a name="mark43"></a>[^](#mark40)
> ```py
> class TiledCanvas(ScrolledCanvas):
> 	def __init__(self, *args, tile_width=400, tile_height=100, tile_padx=5, tile_pady=5, tile_color='#424548', text_color='#CCCCCC', border_color='#000000', on_tile_left_click=None, on_tile_middle_click=None, on_tile_right_click=None, override_tile_width=False, **kw):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get_adjusted_y_view(self, event):
> 		"""Gets a canvas y-view adjusted based on its scrolled position"""
> 	def refresh(self, event=None):
> 		"""Redraw the canvas"""
> 	def use_style(self, style):
> 		"""Reformat with a given ttk style. `Returns None`"""
> ```
### py_simple_ttk.widgets.ScrolledCanvas.ExampleTile<a name="mark44"></a>[^](#mark40)
> **An example tile for a Scrolled Canvas**
> 
> ```py
> class ExampleTile(object):
> 	def __init__(self, manager, text):
> 		...
> 	def activate(self):
> 		"""Calls the manager to activate the widget."""
> 	def deactivate(self):
> 		"""Calls the manager to deactivate the widget."""
> 	def is_in_range(self, pointer_x, pointer_y):
> 		"""Checks if the mouse pointer is in the tile."""
> 	def set_position(self, x, y):
> 		"""Sets a tiles position for the draw manager's draw method."""
> ```
## Checkbutton Widgets<a name="mark45"></a>[^](#mark4)

### py_simple_ttk.widgets.CheckbuttonWidgets.LabeledCheckbutton<a name="mark46"></a>[^](#mark45)
> **Labeled Checkbutton**
> 
> The "replace_output" keyword argument allows the user to provide a tuple of len 2 to replace the default True/False return values. The "is_child" keyword is used by the multiwidget mixin for label configuration and should probably be left alone unless you are making your own multiwidgets.
> ```py
> class LabeledCheckbutton(Labeler, Checkbutton):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str = '', replace_output: list = None, default: bool = False, is_child: bool = False, **kw):
> 		...
> 	def clear(self):
> 		"""Sets the Checkbutton to its default value, usually *False* `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Checkbutton. `Returns None`"""
> 	def enable(self):
> 		"""Enable Checkbutton. `Returns None`"""
> 	def get(self):
> 		"""Get Checkbutton value. `Returns a Boolean unless replace_output is set`"""
> 	def set(self, val: bool):
> 		"""Set Checkbutton value. `Returns None`"""
> ```
### py_simple_ttk.widgets.CheckbuttonWidgets.LabeledMultiCheckbutton<a name="mark47"></a>[^](#mark45)
> **Labeled MultiWidget LabeledCheckbutton.**
> 
> Used when you need multiple, vertically stacked Labeled Checkbuttons
> ```py
> class LabeledMultiCheckbutton(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
## Combobox Widgets<a name="mark48"></a>[^](#mark4)

### py_simple_ttk.widgets.ComboboxWidgets.LabeledCombobox<a name="mark49"></a>[^](#mark48)
> **Labeled Combobox with the Super Widget mixin**
> 
> Set custom_values keyword to "False" to disable custom user-entered values. Set the "default" keyword to the index of the value to display by default from the "values" keyword.
> ```py
> class LabeledCombobox(Labeler, Combobox, SuperWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, command: Callable = None, default: int = 0, on_keystroke: bool = False, bind_enter: bool = True, bind_escape_clear: bool = True, values: list = (), custom_values: bool = True, labelside: str = 'left', is_child: bool = False, min_width: int = 0, widgetargs={}, **kw):
> 		...
> 	def clear(self):
> 		"""Sets Combobox to its default value. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Combobox. `Returns None`"""
> 	def enable(self):
> 		"""Enable Combobox. `Returns None`"""
> 	def get(self):
> 		"""Get Combobox value. `Returns a String`"""
> 	def set(self, val: str):
> 		"""Set Combobox value. `Returns None`"""
> ```
### py_simple_ttk.widgets.ComboboxWidgets.LabeledMultiCombobox<a name="mark50"></a>[^](#mark48)
> **Labeled MultiWidget LabeledCombobox**
> 
> Used when you need mutiple, vertically stacked Labeled Comboboxes
> ```py
> class LabeledMultiCombobox(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
## Console Widgets<a name="mark51"></a>[^](#mark4)

### py_simple_ttk.widgets.ConsoleWidgets.ConsoleWidget<a name="mark52"></a>[^](#mark51)
> **Set labeltext, even if temporarily at init or the label widget will be ignored**
> 
> Used when you need to drop a console interface into an application. To write to the console call console.print(value). Pass a function as the "command" keyword argument to handle the entry input.
> ```py
> class ConsoleWidget(Labeler, Frame):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str = 'Console: ', entrylabeltext: str = 'Command: ', labelside: str = 'top', button_text: str = 'Run', is_child: bool = False, **kwargs):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def print(self, val, end: str = '\n'):
> 		"""Prints a line to the console with a customizable line ending. `Returns None`"""
> ```
## Constraining Functions<a name="mark53"></a>[^](#mark4)

### check_entry_type<a name="mark54"></a>[^](#mark53)
> **Core type checker function. Limits entry to chars that construct a given type**
> 
> ```python
def check_entry_type(val: str, typ: type) -> bool:
> 	...
> ```
### check_entry_int<a name="mark55"></a>[^](#mark53)
> **Check if an entry input is a valid integer**
> 
> ```python
def check_entry_int(val: str) -> bool:
> 	...
> ```
### check_entry_float<a name="mark56"></a>[^](#mark53)
> **Check if an entry input is a valid float**
> 
> ```python
def check_entry_float(val: str) -> bool:
> 	...
> ```
### check_entry_contents<a name="mark57"></a>[^](#mark53)
> **Core content checker function. Limits entry to a list of chars ['a', 'b', 'c', ...] or     the chars contained in a simple string 'abc...'**
> 
> ```python
def check_entry_contents(val: str, limiter: list) -> bool:
> 	...
> ```
### check_entry_ascii_lowercase<a name="mark58"></a>[^](#mark53)
> **Check if entry input is made only of lowercase ascii**
> 
> ```python
def check_entry_ascii_lowercase(val: str) -> bool:
> 	...
> ```
### check_entry_ascii_uppercase<a name="mark59"></a>[^](#mark53)
> **Check if entry input is made only of uppercase ascii**
> 
> ```python
def check_entry_ascii_uppercase(val: str) -> bool:
> 	...
> ```
### check_entry_ascii_letters<a name="mark60"></a>[^](#mark53)
> **Check if entry input is made only of uppercase and lowercase ascii**
> 
> ```python
def check_entry_ascii_letters(val: str) -> bool:
> 	...
> ```
### check_entry_ascii_digits<a name="mark61"></a>[^](#mark53)
> **Check if entry input is made only of digits**
> 
> ```python
def check_entry_ascii_digits(val: str) -> bool:
> 	...
> ```
### check_entry_ascii_uppercase_digits<a name="mark62"></a>[^](#mark53)
> **Check if entry input is made only of uppercase ascii and digits**
> 
> ```python
def check_entry_ascii_uppercase_digits(val: str) -> bool:
> 	...
> ```
### check_entry_ascii_lowercase_digits<a name="mark63"></a>[^](#mark53)
> **Check if entry input is made only of lowercase ascii and digits**
> 
> ```python
def check_entry_ascii_lowercase_digits(val: str) -> bool:
> 	...
> ```
### check_entry_ascii_hexdigits<a name="mark64"></a>[^](#mark53)
> **Check if entry input is made only of hexigits**
> 
> ```python
def check_entry_ascii_hexdigits(val: str) -> bool:
> 	...
> ```
### check_entry_ascii_octdigits<a name="mark65"></a>[^](#mark53)
> **Check if entry input is made only of octdigits**
> 
> ```python
def check_entry_ascii_octdigits(val: str) -> bool:
> 	...
> ```
### check_entry_ascii_letters_digits<a name="mark66"></a>[^](#mark53)
> **Check if entry input is made only of ascii lowercase, ascii uppercase, and digits**
> 
> ```python
def check_entry_ascii_letters_digits(val) -> bool:
> 	...
> ```
### check_entry_ascii_printable<a name="mark67"></a>[^](#mark53)
> **Check if entry input is made only of printable characters**
> 
> ```python
def check_entry_ascii_printable(val: str) -> bool:
> 	...
> ```
## Entry Widgets<a name="mark68"></a>[^](#mark4)

### py_simple_ttk.widgets.EntryWidgets.ScrolledEntry<a name="mark69"></a>[^](#mark68)
> **Scrolled ttk.Entry with SuperWidgetMixin**
> 
> This class is here for completeness but most of the time you will want to use the ScrolledText widget. Used when you need a scrollable text entry box.
> ```py
> class ScrolledEntry(Scroller, Entry, SuperWidgetMixin):
> 	def __init__(self, parent, **kw):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self):
> 		"""Return the text."""
> ```
### py_simple_ttk.widgets.EntryWidgets.LabeledEntry<a name="mark70"></a>[^](#mark68)
> **Labeled ttk.Entry with SuperWidgetMixin**
> 
> Used when you need a Labeled Entry
> ```py
> class LabeledEntry(Labeler, Entry, SuperWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, command: Callable = None, default: str = '', on_keystroke: bool = False, bind_enter: bool = True, bind_escape_clear: bool = True, is_child: bool = False, min_width: int = 0, widgetargs={}, **kw):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self):
> 		"""Get Entry value. `Returns a String`"""
> 	def set(self, val):
> 		"""Set Entry value. `Returns None`"""
> ```
### py_simple_ttk.widgets.EntryWidgets.LabeledMultiEntry<a name="mark71"></a>[^](#mark68)
> **Labeled MultiWidget LabeledEntry**
> 
> Used when you need multiple, vertically stacked Labeled Entries
> ```py
> class LabeledMultiEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.EntryWidgets.LabeledButtonEntry<a name="mark72"></a>[^](#mark68)
> **LabeledEntry with a ttk.Button on the right**
> 
> ```py
> class LabeledButtonEntry(LabeledEntry):
> 	def __init__(self, *args, button_text='', **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self):
> 		"""Get Entry value. `Returns a String`"""
> 	def set(self, val):
> 		"""Set Entry value. `Returns None`"""
> ```
### py_simple_ttk.widgets.EntryWidgets.LabeledMultiButtonEntry<a name="mark73"></a>[^](#mark68)
> **Labeled MultiWidget LabeledEntry**
> 
> Used when you need multiple, vertically stacked Labeled Button Entries
> ```py
> class LabeledMultiButtonEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.EntryWidgets.LabeledPathEntry<a name="mark74"></a>[^](#mark68)
> **LabeledEntry with a ttk.Button bound to a file- or folder-picker for easy     system path selection. Defaults to tk.filedialog.askopenfilename if no     tk.filedialog specified.**
> 
> ```py
> class LabeledPathEntry(LabeledEntry):
> 	def __init__(self, *args, button_text: str = '...', dialog=None, dialog_args: dict = {}, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self):
> 		"""Get Entry value. `Returns a String`"""
> 	def set(self, val):
> 		"""Set Entry value. `Returns None`"""
> ```
### py_simple_ttk.widgets.EntryWidgets.PasswordEntry<a name="mark75"></a>[^](#mark68)
> **Username / Password Entry**
> 
> A username/password entry widget with optional password peeking. Set password_char to `''` to show password by default. The provided command will always be called with the tuple `(username_entry.get(), password_entry.get())` as the only argument even if one of the entries is disabled.
> ```py
> class PasswordEntry(Frame):
> 	def __init__(self, *args, instruction_text: str = '', username_text: str = 'Username: ', username_enabled: bool = True, password_text: str = 'Password: ', password_enabled: bool = True, button_text: str = 'Submit', command=<built-in function print>, password_char: str = '*', peek_enabled: bool = True, invert_peek_colors: bool = False, **kwargs):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def on_peek_press(self, event=None):
> 		"""Show the contents of the password entry while it is being pressed"""
> 	def on_peek_release(self, event=None):
> 		"""Rehide the contents of the password entry"""
> 	def on_submit(self, event=None):
> 		"""Calls the provided "command" function with the contents of the entry box. `Returns None`"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.ConstrainedEntry<a name="mark76"></a>[^](#mark68)
> **An Entry widget that allows certain constraints to be placed on the input with a given check_function that returns true if the input is allowed for each keystroke / input.**
> 
> ```py
> class ConstrainedEntry(Frame):
> 	def __init__(self, parent, check_function, return_type: type = <class 'str'>, default: str = '', widgetargs={}, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledConstrainedEntry<a name="mark77"></a>[^](#mark68)
> **Labeled Constrained Entry with SuperWidgetMixin**
> 
> ```py
> class LabeledConstrainedEntry(Labeler, ConstrainedEntry, SuperWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, check_function: Callable, labeltext: str, command: Callable = None, default: str = '', on_keystroke: bool = False, bind_enter: bool = True, bind_escape_clear: bool = True, is_child: bool = False, min_width: int = 0, widgetargs={}, **kw):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.IntEntry<a name="mark78"></a>[^](#mark68)
> **Int Entry Widget**
> 
> ```py
> class IntEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledIntEntry<a name="mark79"></a>[^](#mark68)
> **Labeled Int Entry Widget**
> 
> ```py
> class LabeledIntEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiIntEntry<a name="mark80"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Int Entry**
> 
> ```py
> class LabeledMultiIntEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.FloatEntry<a name="mark81"></a>[^](#mark68)
> ```py
> class FloatEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledFloatEntry<a name="mark82"></a>[^](#mark68)
> ```py
> class LabeledFloatEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiFloatEntry<a name="mark83"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Float Entry**
> 
> ```py
> class LabeledMultiFloatEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LowercaseEntry<a name="mark84"></a>[^](#mark68)
> ```py
> class LowercaseEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledLowercaseEntry<a name="mark85"></a>[^](#mark68)
> ```py
> class LabeledLowercaseEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiLowercaseEntry<a name="mark86"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Lowercase Entry**
> 
> ```py
> class LabeledMultiLowercaseEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.UppercaseEntry<a name="mark87"></a>[^](#mark68)
> ```py
> class UppercaseEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledUppercaseEntry<a name="mark88"></a>[^](#mark68)
> ```py
> class LabeledUppercaseEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiUppercaseEntry<a name="mark89"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Uppercase Entry**
> 
> ```py
> class LabeledMultiUppercaseEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LettersEntry<a name="mark90"></a>[^](#mark68)
> ```py
> class LettersEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledLettersEntry<a name="mark91"></a>[^](#mark68)
> ```py
> class LabeledLettersEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiLettersEntry<a name="mark92"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Letters Entry**
> 
> ```py
> class LabeledMultiLettersEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.DigitsEntry<a name="mark93"></a>[^](#mark68)
> ```py
> class DigitsEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledDigitsEntry<a name="mark94"></a>[^](#mark68)
> ```py
> class LabeledDigitsEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiDigitsEntry<a name="mark95"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Digits Entry**
> 
> ```py
> class LabeledMultiDigitsEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.UppercaseDigitsEntry<a name="mark96"></a>[^](#mark68)
> ```py
> class UppercaseDigitsEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledUppercaseDigitsEntry<a name="mark97"></a>[^](#mark68)
> ```py
> class LabeledUppercaseDigitsEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiUppercaseDigitsEntry<a name="mark98"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Uppercase Digits Entry**
> 
> ```py
> class LabeledMultiUppercaseDigitsEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LowercaseDigitsEntry<a name="mark99"></a>[^](#mark68)
> ```py
> class LowercaseDigitsEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledLowercaseDigitsEntry<a name="mark100"></a>[^](#mark68)
> ```py
> class LabeledLowercaseDigitsEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiLowercaseDigitsEntry<a name="mark101"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Lowercase Digits Entry**
> 
> ```py
> class LabeledMultiLowercaseDigitsEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LettersDigitsEntry<a name="mark102"></a>[^](#mark68)
> ```py
> class LettersDigitsEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledLettersDigitsEntry<a name="mark103"></a>[^](#mark68)
> ```py
> class LabeledLettersDigitsEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiLettersDigitsEntry<a name="mark104"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Letters Digits Entry**
> 
> ```py
> class LabeledMultiLettersDigitsEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.HexdigitsEntry<a name="mark105"></a>[^](#mark68)
> ```py
> class HexdigitsEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledHexdigitsEntry<a name="mark106"></a>[^](#mark68)
> ```py
> class LabeledHexdigitsEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiHexdigitsEntry<a name="mark107"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Hexdigits Entry**
> 
> ```py
> class LabeledMultiHexdigitsEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.OctdigitsEntry<a name="mark108"></a>[^](#mark68)
> ```py
> class OctdigitsEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledOctdigitsEntry<a name="mark109"></a>[^](#mark68)
> ```py
> class LabeledOctdigitsEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiOctdigitsEntry<a name="mark110"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Octdigits Entry**
> 
> ```py
> class LabeledMultiOctdigitsEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.PrintableEntry<a name="mark111"></a>[^](#mark68)
> ```py
> class PrintableEntry(ConstrainedEntry):
> 	def __init__(self, parent, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledPrintableEntry<a name="mark112"></a>[^](#mark68)
> ```py
> class LabeledPrintableEntry(LabeledConstrainedEntry):
> 	def __init__(self, parent, labeltext, *args, **kwargs):
> 		...
> 	def clear(self):
> 		"""Set Entry value to default, empty unless default set. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Disable Entry. `Returns None`"""
> 	def enable(self):
> 		"""Enable Entry. `Returns None`"""
> 	def get(self) -> object:
> 		...
> 	def set(self, val) -> None:
> 		...
> ```
### py_simple_ttk.widgets.ConstrainedEntryWidgets.LabeledMultiPrintableEntry<a name="mark113"></a>[^](#mark68)
> **Labeled MultiWidget Labeled Printable Entry**
> 
> ```py
> class LabeledMultiPrintableEntry(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
## KeyPad Widgets<a name="mark114"></a>[^](#mark4)

### py_simple_ttk.widgets.KeyPadWidgets.KeypadButton<a name="mark115"></a>[^](#mark114)
> **Base Keypad Button**
> 
> Keypad button that automatically packs itself based on given coordinates. This object is not usually directly instantiated.
> ```py
> class KeypadButton(Button):
> 	def __init__(self, frame, value, coords, callback):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
### py_simple_ttk.widgets.KeyPadWidgets.BaseKeypad<a name="mark116"></a>[^](#mark114)
> **Base Keypad Class**
> 
> Either instantiate directly with a custom layout or subclass with each subclass supplying a custom layout for more keypads. Subclass KeypadButton and supply the class as the "button_type" kwarg for custom buttons.
> ```py
> class BaseKeypad(Frame):
> 	def __init__(self, layout, callback, button_class=<class 'py_simple_ttk.widgets.KeyPadWidgets.KeypadButton'>, *args, **kwargs):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
### py_simple_ttk.widgets.KeyPadWidgets.DialerKeypad<a name="mark117"></a>[^](#mark114)
> **Phone Dialer Keypad**
> 
> Example 12-button keypad, subclass BaseKeypad and supply a custom layout for more keypads.
> ```py
> class DialerKeypad(BaseKeypad):
> 	def __init__(self, callback, *args, **kwargs):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
## Labeler Widget<a name="mark118"></a>[^](#mark4)

### LabeledButton<a name="mark119"></a>[^](#mark118)
> **Labeled Button widget**
> 
> ```py
> class LabeledButton(Labeler, Button):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, is_child: bool = False, command=None, **kw):
> 		...
> 	def clear(self) -> None:
> 		"""Set button text to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self) -> str:
> 		"""Get button text"""
> 	def set(self, val: str) -> None:
> 		"""Set button text"""
> ```
## ListBox Widgets<a name="mark120"></a>[^](#mark4)

### py_simple_ttk.widgets.ListBoxWidgets.ScrolledListBox<a name="mark121"></a>[^](#mark120)
> **Scrolled Listbox with SuperWidget mixin**
> 
> ```py
> class ScrolledListBox(Scroller, Listbox, SuperWidgetMixin):
> 	def __init__(self, parent, **kw):
> 		...
> 	def activate(self, index):
> 		"""Activate item identified by INDEX."""
> 	def curselection(self):
> 		"""Return the indices of currently selected item."""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self, first, last=None):
> 		"""Get list of items from FIRST to LAST (included)."""
> ```
### py_simple_ttk.widgets.ListBoxWidgets.Table<a name="mark122"></a>[^](#mark120)
> **Listboxes bound to scroll in union. Additional bindings will be needed in order to handle clicking.**
> 
> Tested on Mac/Windows/Linux. In most cases a TreeTable widget will be superior to this.
> ```py
> class Table(Frame):
> 	def __init__(self, *args, min_column_width: int = 100, start_column_width: int = 100, on_selection=None, visible_rows=0, **kw):
> 		...
> 	def build(self, contents: dict):
> 		"""Rebuild the table"""
> 	def clear(self):
> 		"""Clears the table"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def get(self):
> 		"""Gets the currently selected items from the table. `Returns a List of Strings`"""
> 	def use_style(self, style: tkinter.ttk.Style):
> 		"""Update to match supplied ttk.Style object. `Returns None`"""
> ```
## OptionMenu Widgets<a name="mark123"></a>[^](#mark4)

### py_simple_ttk.widgets.OptionMenuWidgets.LabeledOptionMenu<a name="mark124"></a>[^](#mark123)
> **Labeled OptionMenu widget**
> 
> ```py
> class LabeledOptionMenu(Labeler, OptionMenu):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, options: list, default: int = 0, is_child: bool = False):
> 		...
> 	def clear(self):
> 		"""Sets OptionMenu to its default value. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this widget and its associated variable."""
> 	def disable(self):
> 		"""Disable OptionMenu. `Returns None`"""
> 	def enable(self):
> 		"""Enable OptionMenu. `Returns None`"""
> 	def get(self):
> 		"""Get OptionMenu value. `Returns a String`"""
> 	def set(self, val):
> 		"""Set OptionMenu value. `Returns None`"""
> 	def set_menu(self, default=None, *values):
> 		"""Build a new menu of radiobuttons with *values and optionally
>         a default value."""
> ```
### py_simple_ttk.widgets.OptionMenuWidgets.LabeledMultiOptionMenu<a name="mark125"></a>[^](#mark123)
> **Labeled MultiWidget LabeledOptionMenu**
> 
> ```py
> class LabeledMultiOptionMenu(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
## ProgressBar Widgets<a name="mark126"></a>[^](#mark4)

### py_simple_ttk.widgets.ProgressbarWidgets.LabeledProgressbar<a name="mark127"></a>[^](#mark126)
> **Labeled Progressbar**
> 
> ```py
> class LabeledProgressbar(Labeler, Progressbar):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, orient='horizontal', labelside='left', is_child=False, default: float = 0, **kw):
> 		...
> 	def clear(self):
> 		"""Sets Progresbar progress to its default value `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Enable Progresbar. `Returns None`"""
> 	def enable(self):
> 		"""Disable Progresbar. `Returns None`"""
> 	def get(self):
> 		"""Set Progresbar progress. `Returns None`"""
> 	def link(self, widget):
> 		"""Easily link to other widgets, sets the progressbar var to the passed widget's var. `Returns None`"""
> 	def set(self, val):
> 		"""Get Progresbar progress. `Returns a String`"""
> 	def start(self, interval=None):
> 		"""Begin autoincrement mode: schedules a recurring timer event
>         that calls method step every interval milliseconds.
> 
>         interval defaults to 50 milliseconds (20 steps/second) if omitted."""
> 	def step(self, amount=None):
> 		"""Increments the value option by amount.
> 
>         amount defaults to 1.0 if omitted."""
> 	def stop(self):
> 		"""Stop autoincrement mode: cancels any recurring timer event
>         initiated by start."""
> ```
### py_simple_ttk.widgets.ProgressbarWidgets.LabeledMultiProgressbar<a name="mark128"></a>[^](#mark126)
> **Labeled MultiWidget LabeledProgressbar**
> 
> ```py
> class LabeledMultiProgressbar(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top', orient='horizontal'):
> 		...
> 	def add(self, parent: tkinter.ttk.Frame, key: str, args, kwargs, widget_type=None):
> 		"""Overrides MultiWidgetMixin to deal with vertical orientation `Returns None`"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def link(self, config: dict):
> 		"""Link to other widgets with a dict of subwidget keys to link to `Returns None`"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
## Radiobutton Widgets<a name="mark129"></a>[^](#mark4)

### py_simple_ttk.widgets.RadiobuttonWidgets.LabeledRadiobutton<a name="mark130"></a>[^](#mark129)
> **Labeled Radiobutton widget**
> 
> ```py
> class LabeledRadiobutton(Labeler, Frame):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, options: list = [], default: int = 0, is_child: bool = False, **kw):
> 		...
> 	def clear(self):
> 		"""Sets Radiobutton to its default value. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Enable Radiobutton. `Returns None`"""
> 	def enable(self):
> 		"""Disable Radiobutton. `Returns None`"""
> 	def get(self):
> 		"""Get Radiobutton value. `Returns a Bool`"""
> 	def set(self, val: bool):
> 		"""Set Radiobutton value. `Returns None`"""
> ```
### py_simple_ttk.widgets.RadiobuttonWidgets.LabeledMultiRadiobutton<a name="mark131"></a>[^](#mark129)
> **Labeled MultiWidget LabeledRadiobutton**
> 
> ```py
> class LabeledMultiRadiobutton(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top'):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Method for adding different widgets to a multiwidget post-instantiation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
## Scale Widgets<a name="mark132"></a>[^](#mark4)

### py_simple_ttk.widgets.ScaleWidgets.LabeledScale<a name="mark133"></a>[^](#mark132)
> **Labeled Scale**
> 
> ```py
> class LabeledScale(Labeler, Scale):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, command: Callable = None, default: float = 0, orient: bool = 'horizontal', is_child: bool = False, from_=0, to=100, **kwargs):
> 		...
> 	def clear(self):
> 		"""Sets Scale to its default value. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		"""Enable Scale. `Returns None`"""
> 	def enable(self):
> 		"""Disable Scale. `Returns None`"""
> 	def get(self):
> 		"""Get Scale value. `Returns a Float`"""
> 	def set(self, val):
> 		"""Set Scale value. `Returns None`"""
> ```
### py_simple_ttk.widgets.ScaleWidgets.LabeledMultiScale<a name="mark134"></a>[^](#mark132)
> **Labeled MultiWidget Labeled Scale**
> 
> ```py
> class LabeledMultiScale(Labeler, Frame, MultiWidgetMixin):
> 	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top', orient='horizontal', command=None):
> 		...
> 	def add(self, parent, key, args, kwargs, widget_type=None):
> 		"""Override MultiWidgetMixin for vertical orientation"""
> 	def clear(self, config: list = None):
> 		"""Pass a list of subwidgets to clear or all are set to default"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self, config: list = None):
> 		"""Pass a list of subwidgets to disable or all are disabled"""
> 	def enable(self, config: list = None):
> 		"""Pass a list of subwidgets to enable or all are enabled"""
> 	def get(self, config: list = None):
> 		"""Pass a list of widget keys to get a dict of outputs"""
> 	def set(self, config: dict):
> 		"""Pass a map of widget keys and their values"""
> ```
## Text Widgets<a name="mark135"></a>[^](#mark4)

### py_simple_ttk.widgets.TextWidgets.ScrolledText<a name="mark136"></a>[^](#mark135)
> **Scrolled Textbox**
> 
> Scrolled SuperWidget Text. Configure text by passing the `textkw` argument as a dict formatted like a standard kwarg dict.
> ```py
> class ScrolledText(Scroller, Text, SuperWidgetMixin):
> 	def __init__(self, parent, **kw):
> 		...
> 	def clear(self):
> 		"""Empties the text box. `Returns None`"""
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		...
> 	def edit_undo(self):
> 		"""Undoes the last edit action
> 
>         If the undo option is true. An edit action is defined
>         as all the insert and delete commands that are recorded
>         on the undo stack in between two separators. Generates
>         an error when the undo stack is empty. Does nothing
>         when the undo option is false
>         """
> 	def enable(self):
> 		...
> 	def get(self, start='1.0', end='end'):
> 		"""Returns the contents of the text box with optional start/end kwargs. `Returns a String`"""
> 	def get_cursor(self):
> 		"""Get the current location of the cursor. `Returns None`"""
> 	def select_all(self, event=None):
> 		"""Selects all text. `Returns None`"""
> 	def set(self, val):
> 		"""Sets the text. `Returns a String`"""
> 	def window_create(self, index, cnf={}, **kw):
> 		"""Create a window at INDEX."""
> ```
### py_simple_ttk.widgets.TextWidgets.CopyBox<a name="mark137"></a>[^](#mark135)
> **Scrolled Text with "Copy tp Clipboard" Button**
> 
> A widget with a scrolled textbox and button that copies the textbox contents to the user's clipboard. Useful for form output, etc.
> ```py
> class CopyBox(Frame):
> 	def __init__(self, parent: tkinter.ttk.Frame, **kw):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def disable(self):
> 		...
> 	def enable(self):
> 		...
> ```
## Toplevel Widgets<a name="mark138"></a>[^](#mark4)

### py_simple_ttk.widgets.ToplevelWidgets.FocusedToplevel<a name="mark139"></a>[^](#mark138)
> **Base Focused Toplevel Class**
> 
> Window that takes focus and center's itself on the current window. Used as a base class for other windows.
> ```py
> class FocusedToplevel(Toplevel):
> 	def __init__(self, *args, title=None, window=None, on_close=None, **kwargs):
> 		...
> 	def destroy(self):
> 		...
> 	def iconify(self):
> 		"""Display widget as icon."""
> 	def iconmask(self, bitmap=None):
> 		"""Set mask for the icon bitmap of this widget. Return the
>         mask if None is given."""
> ```
### py_simple_ttk.widgets.ToplevelWidgets.NoticeWindow<a name="mark140"></a>[^](#mark138)
> **Provides the user with a notice.**
> 
> `button_action` can call a function to help with determining acceptance vs. the user hitting the exit button.
> ```py
> class NoticeWindow(FocusedToplevel):
> 	def __init__(self, *args, text=None, button_text='Continue', button_action=None, **kwargs):
> 		...
> 	def destroy(self):
> 		...
> 	def iconify(self):
> 		"""Display widget as icon."""
> 	def iconmask(self, bitmap=None):
> 		"""Set mask for the icon bitmap of this widget. Return the
>         mask if None is given."""
> ```
### py_simple_ttk.widgets.ToplevelWidgets.YesNoCancelWindow<a name="mark141"></a>[^](#mark138)
> **Provides the user with a yes/no/cancel option.**
> 
> `no_destroy` can be set to `True` to allow the window to remain open after a selection is made.
> ```py
> class YesNoCancelWindow(FocusedToplevel):
> 	def __init__(self, *args, text: str = None, yes_enabled: bool = True, on_yes=None, yes_text: str = 'Yes', no_enabled: bool = True, on_no=None, no_text: str = 'No', cancel_enabled: bool = True, on_cancel=None, cancel_text: str = 'Cancel', no_destroy: bool = False, focus='', **kwargs):
> 		...
> 	def destroy(self):
> 		...
> 	def iconify(self):
> 		"""Display widget as icon."""
> 	def iconmask(self, bitmap=None):
> 		"""Set mask for the icon bitmap of this widget. Return the
>         mask if None is given."""
> ```
### py_simple_ttk.widgets.ToplevelWidgets.PromptWindow<a name="mark142"></a>[^](#mark138)
> **Prompts the user for a text input**
> 
> `no_destroy` can be set to `True` to allow the window to remain open after a selection is made, useful for informing the user a string input was invalid via setting label_var. If the select_type kwarg is set to true the user will be prompted to select a data type (int / string) to return.
> ```py
> class PromptWindow(FocusedToplevel):
> 	def __init__(self, *args, text: str = 'Enter Text:', on_yes=None, yes_text: str = 'Continue', on_cancel=None, cancel_text: str = 'Cancel', bind_enter: bool = True, no_destroy: bool = False, select_type: bool = False, focus='', **kwargs):
> 		...
> 	def destroy(self):
> 		...
> 	def iconify(self):
> 		"""Display widget as icon."""
> 	def iconmask(self, bitmap=None):
> 		"""Set mask for the icon bitmap of this widget. Return the
>         mask if None is given."""
> ```
### py_simple_ttk.widgets.ToplevelWidgets.PasswordWindow<a name="mark143"></a>[^](#mark138)
> **Password Entry window.**
> 
> Demo Password Entry Window, you will want to copy the source for this widget and rewrite it.
> ```py
> class PasswordWindow(FocusedToplevel):
> 	def __init__(self, window=None, **kwargs):
> 		...
> 	def destroy(self):
> 		...
> 	def iconify(self):
> 		"""Display widget as icon."""
> 	def iconmask(self, bitmap=None):
> 		"""Set mask for the icon bitmap of this widget. Return the
>         mask if None is given."""
> ```
### py_simple_ttk.widgets.ToplevelWidgets.ListWindow<a name="mark144"></a>[^](#mark138)
> **Window to select an option from a Scrolled Listbox**
> 
> ```py
> class ListWindow(FocusedToplevel):
> 	def __init__(self, *args, options: list, text: str = 'Select Item:', on_yes=None, yes_text: str = 'Continue', on_cancel=None, cancel_text: str = 'Cancel', no_destroy: bool = False, select_mode: str = 'single', **kwargs):
> 		...
> 	def destroy(self):
> 		...
> 	def iconify(self):
> 		"""Display widget as icon."""
> 	def iconmask(self, bitmap=None):
> 		"""Set mask for the icon bitmap of this widget. Return the
>         mask if None is given."""
> ```
## Misc Widgets<a name="mark145"></a>[^](#mark4)

### py_simple_ttk.widgets.ToolTip.ToolTip<a name="mark146"></a>[^](#mark145)
> **Easy ToolTip**
> 
> Easily show theme-friendly tooltip. Currently only left and right align are supported.
> ```py
> class ToolTip(ToolTipBase):
> 	def __init__(self, tipwidget, text: str, align='left'):
> 		...
> ```
### py_simple_ttk.widgets.SizegripWidgets.EasySizegrip<a name="mark147"></a>[^](#mark145)
> **Sizegrip widget with bindings**
> 
> Automatically packs self and binds mouse presses for systems that don't bind automatically.
> ```py
> class EasySizegrip(Sizegrip):
> 	def __init__(self, *args, **kwargs):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> ```
# SuperLib.utils<a name="mark148"></a>[^](#mark0)

## Utils<a name="mark149"></a>[^](#mark148)

### py_simple_ttk.utils.utils.check_if_module_installed<a name="mark150"></a>[^](#mark149)
> **Indicates if a packages is installed. `Returns a Boolean`**
> 
> ```python
def check_if_module_installed(package):
> 	...
> ```
### py_simple_ttk.utils.utils.check_string_contains<a name="mark151"></a>[^](#mark149)
> **Returns `(True, char_index)` if any character from the list exists in the string otherwise returns `(False, None)`**
> 
> ```python
def check_string_contains(string: str, contains_list: tuple):
> 	...
> ```
### py_simple_ttk.utils.utils.dummy_function<a name="mark152"></a>[^](#mark149)
> **Dummy function that nicely prints out any passed args and kwargs. `Returns None`**
> 
> ```python
def dummy_function(*args, **kwargs):
> 	...
> ```
### py_simple_ttk.utils.utils.get_friendly_time<a name="mark153"></a>[^](#mark149)
> **Gets a time string in one of several modes. Modes: `all, time, date, nice_date`. `Returns a String`**
> 
> ```python
def get_friendly_time(timestamp, mode='all'):
> 	...
> ```
### py_simple_ttk.utils.utils.get_installed_packages<a name="mark154"></a>[^](#mark149)
> **Get an alphabetized list of available packages. `Returns a List`**
> 
> ```python
def get_installed_packages():
> 	...
> ```
### py_simple_ttk.utils.utils.get_unix_timestamp<a name="mark155"></a>[^](#mark149)
> **Get a unix timestamp. `Returns a Float`**
> 
> ```python
def get_unix_timestamp():
> 	...
> ```
### py_simple_ttk.utils.utils.get_unix_timestring<a name="mark156"></a>[^](#mark149)
> **Get a unix timestring. `Returns a String`**
> 
> ```python
def get_unix_timestring():
> 	...
> ```
### py_simple_ttk.utils.utils.get_user_home_folder<a name="mark157"></a>[^](#mark149)
> **Cross-platform function to get a user's home folder**
> 
> ```python
def get_user_home_folder():
> 	...
> ```
### py_simple_ttk.utils.utils.open_folder_in_explorer<a name="mark158"></a>[^](#mark149)
> **Cross-platform way to open a folder in the default file manager for a system**
> 
> ```python
def open_folder_in_explorer(path):
> 	...
> ```
### py_simple_ttk.utils.utils.sort_dict_by_keys<a name="mark159"></a>[^](#mark149)
> **Sorts a dictionary by its keys**
> 
> ```python
def sort_dict_by_keys(source: dict, reverse: bool = False):
> 	...
> ```
### py_simple_ttk.utils.utils.timer_decorator<a name="mark160"></a>[^](#mark149)
> **Decorator to add timing to a function**
> 
> ```python
def timer_decorator(proc):
> 	...
> ```
## File Generators<a name="mark161"></a>[^](#mark148)

### py_simple_ttk.utils.HTML_Generator.HTML_Generator<a name="mark162"></a>[^](#mark161)
> ```py
> class HTML_Generator(object):
> 	def __init__(self, indent='\t'):
> 		...
> 	def add_body_line(self, text=''):
> 		...
> 	def add_bold(self, text=''):
> 		...
> 	def add_center(self, text=''):
> 		...
> 	def add_comment(self, text):
> 		...
> 	def add_div(self, text=''):
> 		...
> 	def add_divider(self):
> 		...
> 	def add_list(self, items=[], ordered=False):
> 		...
> 	def add_list_item(self, item: str):
> 		...
> 	def add_paragraph(self, text=''):
> 		...
> 	def assemble(self):
> 		...
> 	def end_bold(self):
> 		...
> 	def end_center(self):
> 		...
> 	def end_div(self):
> 		...
> 	def end_list(self, ordered=False):
> 		...
> 	def end_paragraph(self):
> 		...
> 	def get_indent(self, offset=0):
> 		...
> 	def save(self, path):
> 		...
> 	def start_bold(self, text=''):
> 		...
> 	def start_center(self, text=''):
> 		...
> 	def start_div(self, text=''):
> 		...
> 	def start_list(self, items=[], ordered=False):
> 		...
> 	def start_paragraph(self, text=''):
> 		...
> ```
### py_simple_ttk.utils.TXT_Generator.TXT_Generator<a name="mark163"></a>[^](#mark161)
> ```py
> class TXT_Generator(object):
> 	def __init__(self, ):
> 		...
> 	def add_body_line(self, text=''):
> 		...
> 	def add_divider(self):
> 		...
> 	def assemble(self):
> 		...
> 	def save(self, path):
> 		...
> ```
### py_simple_ttk.utils.MD_Generator.MD_Generator<a name="mark164"></a>[^](#mark161)
> ```py
> class MD_Generator(object):
> 	def __init__(self, title=None, footnote_title='Notes:', footnote_heading_level=2, numbered_toc=False):
> 		...
> 	def add_blockquote(self, text, end='\n\n'):
> 		...
> 	def add_bold(self, text, end='\n\n'):
> 		...
> 	def add_bold_italic(self, text, end='\n'):
> 		...
> 	def add_break(self):
> 		...
> 	def add_code_block(self, text, lang='', end='\n'):
> 		...
> 	def add_heading_1(self, text, **kwargs):
> 		...
> 	def add_heading_2(self, text, **kwargs):
> 		...
> 	def add_heading_3(self, text, **kwargs):
> 		...
> 	def add_heading_4(self, text, **kwargs):
> 		...
> 	def add_heading_5(self, text, **kwargs):
> 		...
> 	def add_heading_6(self, text, **kwargs):
> 		...
> 	def add_horizontal_rule(self):
> 		...
> 	def add_italic(self, text, end='\n'):
> 		...
> 	def add_link(self, link, text=None, tooltip=None):
> 		...
> 	def add_multi_blockquote(self, texts):
> 		...
> 	def add_ordered_list(self, texts, indent=0):
> 		...
> 	def add_paragraph(self, text, end='\n\n'):
> 		...
> 	def add_to_ordered_list(self, index, text, indent=0):
> 		...
> 	def add_to_unordered_list(self, text, indent=0):
> 		...
> 	def add_toc(self, title, end='\n\n'):
> 		...
> 	def add_unordered_list(self, texts, indent=0):
> 		...
> 	def assemble(self):
> 		...
> 	def decrease_toc_depth(self):
> 		...
> 	def get_prefix(self):
> 		...
> 	def increase_toc_depth(self):
> 		...
> 	def insert_footnote(self, text):
> 		...
> 	def save(self, path):
> 		...
> 	def set_slogan(self, slogan):
> 		...
> ```
## History Mixin<a name="mark165"></a>[^](#mark148)

### py_simple_ttk.utils.History.HistoryMixin<a name="mark166"></a>[^](#mark165)
> **Abstract mixin to add history-tracking to an application**
> 
> This object is meant to be used as a mixin rather than instantiated directly most of the time.
> ```py
> class HistoryMixin(object):
> 	def __init__(self, data):
> 		...
> 	def add_history(self, data):
> 		...
> 	def clear_history(self, data):
> 		...
> 	def get_history_uid(self):
> 		...
> 	def redo(self):
> 		...
> 	def undo(self):
> 		...
> ```
## Color Functions<a name="mark167"></a>[^](#mark148)

### py_simple_ttk.utils.color.reduce_255<a name="mark168"></a>[^](#mark167)
> **Limits a val to a range of 0 to 255**
> 
> ```python
def reduce_255(in_value: int, maxval: int = 255):
> 	...
> ```
### py_simple_ttk.utils.color.rgb_to_hex<a name="mark169"></a>[^](#mark167)
> **Converts an rgb tuple to hex**
> 
> ```python
def rgb_to_hex(rgb: tuple):
> 	...
> ```
### py_simple_ttk.utils.color.rgba_to_hex<a name="mark170"></a>[^](#mark167)
> **Converts an rgba tuple to rgba hex**
> 
> ```python
def rgba_to_hex(rgba: tuple):
> 	...
> ```
### py_simple_ttk.utils.color.hex_to_rgb<a name="mark171"></a>[^](#mark167)
> **Converts hex to rgb tuple**
> 
> ```python
def hex_to_rgb(hex: str):
> 	...
> ```
### py_simple_ttk.utils.color.hex_to_rgba<a name="mark172"></a>[^](#mark167)
> **Tries to convert rgba hex to rgba, on failure converts rgb hex to rgb and sets a full opacity**
> 
> ```python
def hex_to_rgba(hex: str):
> 	...
> ```
### py_simple_ttk.utils.color.get_gradient<a name="mark173"></a>[^](#mark167)
> **Generates a black / white gradient with a given number of steps**
> 
> ```python
def get_gradient(steps: int):
> 	...
> ```
### py_simple_ttk.utils.color.rgb_to_scalar<a name="mark174"></a>[^](#mark167)
> **Converts an rgb itterable to scalar list**
> 
> ```python
def rgb_to_scalar(rgb: tuple):
> 	...
> ```
### py_simple_ttk.utils.color.scalar_to_rgb<a name="mark175"></a>[^](#mark167)
> **Converts rgb scalar to rgb list**
> 
> ```python
def scalar_to_rgb(rgb: tuple):
> 	...
> ```
### py_simple_ttk.utils.color.linear_gradient<a name="mark176"></a>[^](#mark167)
> **Generates a linear gradient between two colors, accepts html hex or rgb formats**
> 
> ```python
def linear_gradient(start_hex: str = '#000000', finish_hex: str = '#FFFFFF', n: int = 10):
> 	...
> ```
### py_simple_ttk.utils.color.get_rainbow<a name="mark177"></a>[^](#mark167)
> **Generates a rainbow with a given number of steps. Steps must be divisible by 4)**
> 
> ```python
def get_rainbow(steps: int):
> 	...
> ```
# MegaWidgets<a name="mark178"></a>[^](#mark0)

## Notes MegaWidget<a name="mark179"></a>[^](#mark178)

### py_simple_ttk.mega_widgets.notes.NotesTab<a name="mark180"></a>[^](#mark179)
> ```py
> class NotesTab(Tab):
> 	def __init__(self, notebook, app):
> 		...
> 	def copy_note(self, note):
> 		...
> 	def delete_note(self, note):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def export_note_html(self, note):
> 		...
> 	def export_note_json(self, note):
> 		...
> 	def export_note_markdown(self, note):
> 		...
> 	def export_note_text(self, note):
> 		...
> 	def load_notes(self):
> 		...
> 	def make_new_note(self, title):
> 		...
> 	def new_note(self, event=None):
> 		...
> 	def on_toplevel_destroy(self, *args):
> 		"""Function for toplevels to call on no / cancel"""
> 	def reload_notes(self):
> 		...
> 	def rename_note(self, note):
> 		...
> 	def start_new_note(self, title=None):
> 		...
> ```
## Conversation MegaWidget<a name="mark181"></a>[^](#mark178)

### py_simple_ttk.mega_widgets.chat.ConversationsTab<a name="mark182"></a>[^](#mark181)
> ```py
> class ConversationsTab(Tab):
> 	def __init__(self, notebook, app):
> 		...
> 	def copy_conversation(self, conversation):
> 		...
> 	def delete_conversation(self, conversation):
> 		...
> 	def destroy(self):
> 		"""Destroy this and all descendants widgets."""
> 	def export_conversation_html(self, conversation):
> 		...
> 	def export_conversation_json(self, conversation):
> 		...
> 	def export_conversation_markdown(self, conversation):
> 		...
> 	def export_conversation_text(self, conversation):
> 		...
> 	def get_cached_icon(self, size, color, char):
> 		...
> 	def get_user_icon(self, user):
> 		...
> 	def load_conversations(self):
> 		...
> 	def make_new_conversation(self, title):
> 		...
> 	def new_conversation(self, event=None):
> 		...
> 	def on_toplevel_destroy(self, *args):
> 		"""Function for toplevels to call on no / cancel"""
> 	def reload_conversations(self):
> 		...
> 	def rename_conversation(self, conversation):
> 		...
> 	def start_new_conversation(self, title=None):
> 		...
> ```
## Profile Management<a name="mark183"></a>[^](#mark178)

### py_simple_ttk.utils.ProfilesSystem.ProfilesSystem<a name="mark184"></a>[^](#mark183)
> ```py
> class ProfilesSystem(object):
> 	def __init__(self, select_profile_actions: list = [], refresh_profiles_actions: list = [], profiles_dir: str = 'C:\\Users\\arcti\\github\\py_simple_ttk\\Profiles', handle_duplicates: bool = True):
> 		...
> 	def add_refresh_profiles_action(self, action):
> 		"""Add an action to the profiles list refresh actions"""
> 	def add_refresh_profiles_actions(self, actions: list):
> 		"""Add a list of actions to the profiles list refresh actions"""
> 	def add_select_profile_action(self, action):
> 		"""Add an action to the profile switch actions"""
> 	def add_select_profile_actions(self, actions: list):
> 		"""Add a list of actions to the profile switch actions"""
> 	def check_if_name_exists_in_profiles(self, name: str, profiles: list = None):
> 		"""Check if a name exists in a list of profiles, if no list is provided uses the list of all profiles. `Returns a Bool`"""
> 	def clear_refresh_profile_actions(self, new: list = []):
> 		"""Clear out the profiles list refresh actions, optionally replacing them with new ones"""
> 	def clear_select_profile_actions(self, new: list = []):
> 		"""Clear out the profile switch actions, optionally replacing them with new ones"""
> 	def create_profile(self, name: str):
> 		"""Creates a profile with a given name. `Raises ValueError` if the profile name already exists. `Returns a UserProfile`"""
> 	def delete_profile(self, profile: py_simple_ttk.utils.ProfilesSystem.UserProfile):
> 		...
> 	def get_last_used_profile(self, profiles: list = None):
> 		"""Returns the most recently accessed profile"""
> 	def get_profile_by_username(self, name: str):
> 		...
> 	def get_profile_names(self):
> 		"""Returns an alphabetically sorted list of profile names"""
> 	def handle_duplicate_profile_names(self, name: str):
> 		"""Makes profile names unique if they have identical names. The most recently accessed profile (according to the file json) keeps its name untouched. `Returns None`"""
> 	def handle_refresh_profiles_actions(self):
> 		"""Handle on-refresh-profiles actions"""
> 	def handle_select_profile_actions(self):
> 		"""Handle on-profile-selection actions"""
> 	def select_profile(self, profile: py_simple_ttk.utils.ProfilesSystem.UserProfile):
> 		"""Change the currently selected profile"""
> 	def select_profile_by_username(self, name: str):
> 		...
> 	def sort_profiles_by_accessed(self, profiles: list = None):
> 		"""Sort a list of profiles by last accessed, if no list is provided returns a sorted list of all profiles in the system. `Returns a List`"""
> ```
### py_simple_ttk.utils.ProfilesSystem.UserProfile<a name="mark185"></a>[^](#mark183)
> **A class to represent a User / User's Preferences**
> 
> Must pass a unique username and a unique identifier for new profile.
> ```py
> class UserProfile(object):
> 	def __init__(self, path, username: str = None, atomic: str = None):
> 		...
> 	def clear_preferences(self, preferences: list = None):
> 		...
> 	def get_preference(self, key: str):
> 		...
> 	def load(self, path: str = None, overwrite_path=False):
> 		...
> 	def save(self, path: str = None, overwrite_path=False):
> 		...
> 	def set_preference(self, key: str, value: str):
> 		...
> 	def set_username(self, name: str):
> 		...
> ```
### py_simple_ttk.utils.ProfilesSystem.get_profiles_folder<a name="mark186"></a>[^](#mark185)
> **Gets the absolute path to the included profiles folder. `Returns a String`**
> 
> ```python
def get_profiles_folder():
> 	...
> ```
### py_simple_ttk.utils.ProfilesSystem.get_profiles_list<a name="mark187"></a>[^](#mark185)
> **Gets a list of profile files at a given path. `Returns a List of Path strings`**
> 
> ```python
def get_profiles_list(path='./Profiles', verbose=False):
> 	...
> ```
# Changelog<a name="mark188"></a>[^](#mark0)

## 0.1.17<a name="mark189"></a>[^](#mark188)

Add set_desktop_background to WidgetsCore.py

## 0.1.16<a name="mark190"></a>[^](#mark188)

Add needs_white_text to color.py, add pyinstaller compatibility to WidgetsCore.get_asset

## 0.1.15<a name="mark191"></a>[^](#mark188)

Fix misnamed function in color.py

## 0.1.14<a name="mark192"></a>[^](#mark188)

Fix missing import in app.py

## 0.1.13<a name="mark193"></a>[^](#mark188)

reduced variety of packaged font images, fixed bug with constrained widgets command not triggering

## 0.1.12<a name="mark194"></a>[^](#mark188)

Add Constrained + Labeled + Multi Entries (>35 widgets)

## 0.1.11<a name="mark195"></a>[^](#mark188)

Fix LabeledPathEntry error when no dialog type was specified

## 0.1.10<a name="mark196"></a>[^](#mark188)

Add LabeledPathEntry to EntryWidgets.py

## 0.1.9<a name="mark197"></a>[^](#mark188)

Add pencil icons to assets

## 0.1.8<a name="mark198"></a>[^](#mark188)

Fix labeled button not running command on press

## 0.1.7<a name="mark199"></a>[^](#mark188)

add labeled button

## 0.1.6<a name="mark200"></a>[^](#mark188)

Fix missing Labeler import

## 0.1.5<a name="mark201"></a>[^](#mark188)

Fix broken package

## 0.1.4<a name="mark202"></a>[^](#mark188)

Fix broken package

## 0.1.3<a name="mark203"></a>[^](#mark188)

More cleanup, input fixes.py

## 0.1.2<a name="mark204"></a>[^](#mark188)

Cleanup, move type lists to generate_readme.py

## 0.1.1<a name="mark205"></a>[^](#mark188)

Fix missing 'ListWindow' import in app.py

## 0.1.0<a name="mark206"></a>[^](#mark188)

Modulize



Generated with [py_simple_readme](https://github.com/AndrewSpangler/py_simple_readme)