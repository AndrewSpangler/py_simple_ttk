# py_simple_ttk 0.2.9<a name="mark0"></a>

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
		- [make_temp_config_file](#mark45)
		- [open_link](#mark46)
		- [recursive_widget_search](#mark47)
		- [run_cl](#mark48)
	- [Canvas Widgets](#mark49)
		- [ResizableCanvas](#mark50)
		- [ScrolledCanvas](#mark51)
		- [TiledCanvas](#mark52)
		- [ExampleTile](#mark53)
	- [Checkbutton Widgets](#mark54)
		- [ActiveCheckbutton](#mark55)
		- [LabeledCheckbutton](#mark56)
		- [LabeledMultiCheckbutton](#mark57)
	- [Combobox Widgets](#mark58)
		- [ActiveCombobox](#mark59)
		- [LabeledCombobox](#mark60)
		- [LabeledMultiCombobox](#mark61)
	- [Console Widgets](#mark62)
		- [ConsoleWidget](#mark63)
	- [Constraining Functions](#mark64)
		- [check_entry_type](#mark65)
		- [check_entry_int](#mark66)
		- [check_entry_float](#mark67)
		- [check_entry_contents](#mark68)
		- [check_entry_ascii_lowercase](#mark69)
		- [check_entry_ascii_uppercase](#mark70)
		- [check_entry_ascii_letters](#mark71)
		- [check_entry_ascii_digits](#mark72)
		- [check_entry_ascii_uppercase_digits](#mark73)
		- [check_entry_ascii_lowercase_digits](#mark74)
		- [check_entry_ascii_hexdigits](#mark75)
		- [check_entry_ascii_octdigits](#mark76)
		- [check_entry_ascii_letters_digits](#mark77)
		- [check_entry_ascii_printable](#mark78)
	- [Counter Widgets](#mark79)
		- [Counter](#mark80)
		- [FloatCounter](#mark81)
		- [LabeledCounter](#mark82)
		- [LabeledFloatCounter](#mark83)
		- [LabeledMultiCounter](#mark84)
		- [LabeledMultiFloatCounter](#mark85)
	- [Entry Widgets](#mark86)
		- [ActiveEntry](#mark87)
		- [ScrolledEntry](#mark88)
		- [LabeledEntry](#mark89)
		- [LabeledMultiEntry](#mark90)
		- [LabeledButtonEntry](#mark91)
		- [LabeledMultiButtonEntry](#mark92)
		- [LabeledPathEntry](#mark93)
		- [LabeledMultiPathEntry](#mark94)
		- [PasswordEntry](#mark95)
		- [LabeledPasswordEntry](#mark96)
		- [LabeledMultiPasswordEntry](#mark97)
		- [ConstrainedEntry](#mark98)
		- [LabeledConstrainedEntry](#mark99)
		- [LabeledMultiConstrainedEntry](#mark100)
		- [IntEntry](#mark101)
		- [LabeledIntEntry](#mark102)
		- [LabeledMultiIntEntry](#mark103)
		- [FloatEntry](#mark104)
		- [LabeledFloatEntry](#mark105)
		- [LabeledMultiFloatEntry](#mark106)
		- [LowercaseEntry](#mark107)
		- [LabeledLowercaseEntry](#mark108)
		- [LabeledMultiLowercaseEntry](#mark109)
		- [UppercaseEntry](#mark110)
		- [LabeledUppercaseEntry](#mark111)
		- [LabeledMultiUppercaseEntry](#mark112)
		- [LettersEntry](#mark113)
		- [LabeledLettersEntry](#mark114)
		- [LabeledMultiLettersEntry](#mark115)
		- [DigitsEntry](#mark116)
		- [LabeledDigitsEntry](#mark117)
		- [LabeledMultiDigitsEntry](#mark118)
		- [UppercaseDigitsEntry](#mark119)
		- [LabeledUppercaseDigitsEntry](#mark120)
		- [LabeledMultiUppercaseDigitsEntry](#mark121)
		- [LowercaseDigitsEntry](#mark122)
		- [LabeledLowercaseDigitsEntry](#mark123)
		- [LabeledMultiLowercaseDigitsEntry](#mark124)
		- [LettersDigitsEntry](#mark125)
		- [LabeledLettersDigitsEntry](#mark126)
		- [LabeledMultiLettersDigitsEntry](#mark127)
		- [HexdigitsEntry](#mark128)
		- [LabeledHexdigitsEntry](#mark129)
		- [LabeledMultiHexdigitsEntry](#mark130)
		- [OctdigitsEntry](#mark131)
		- [LabeledOctdigitsEntry](#mark132)
		- [LabeledMultiOctdigitsEntry](#mark133)
		- [PrintableEntry](#mark134)
		- [LabeledPrintableEntry](#mark135)
		- [LabeledMultiPrintableEntry](#mark136)
	- [Frame Widgets](#mark137)
		- [ColumnFrame](#mark138)
		- [HamburgerFrame](#mark139)
	- [KeyPad Widgets](#mark140)
		- [KeypadButton](#mark141)
		- [BaseKeypad](#mark142)
		- [DialerKeypad](#mark143)
	- [Label Widgets](#mark144)
		- [ActiveLabel](#mark145)
		- [LabeledValue](#mark146)
	- [Labeler Widget](#mark147)
		- [ActiveButton](#mark148)
		- [LabeledButton](#mark149)
		- [LabeledMultiButton](#mark150)
		- [CycleButton](#mark151)
		- [LabeledCycleButton](#mark152)
		- [LabeledMultiCycleButton](#mark153)
	- [ListBox Widgets](#mark154)
		- [ScrolledListBox](#mark155)
		- [OrderedListbox](#mark156)
		- [ListManipulator](#mark157)
		- [Table](#mark158)
	- [OptionMenu Widgets](#mark159)
		- [ActiveOptionMenu](#mark160)
		- [LabeledOptionMenu](#mark161)
		- [LabeledMultiOptionMenu](#mark162)
	- [ProgressBar Widgets](#mark163)
		- [ActiveProgressbar](#mark164)
		- [LabeledProgressbar](#mark165)
		- [LabeledMultiProgressbar](#mark166)
	- [Radiobutton Widgets](#mark167)
		- [ActiveRadiobutton](#mark168)
		- [RadioTable](#mark169)
		- [LabeledRadioTable](#mark170)
		- [LabeledMultiRadioTable](#mark171)
		- [SimpleRadioTable](#mark172)
		- [LabeledSimpleRadioTable](#mark173)
		- [LabeledMultiSimpleRadioTable](#mark174)
	- [Scale Widgets](#mark175)
		- [ActiveScale](#mark176)
		- [LabeledScale](#mark177)
		- [LabeledMultiScale](#mark178)
	- [Spinbox Widgets](#mark179)
		- [ActiveSpinbox](#mark180)
		- [LabeledSpinbox](#mark181)
		- [LabeledMultiSpinbox](#mark182)
	- [Text Widgets](#mark183)
		- [ScrolledText](#mark184)
		- [CopyBox](#mark185)
		- [LabeledCopyBox](#mark186)
		- [LabeledMultiCopyBox](#mark187)
	- [Toplevel Widgets](#mark188)
		- [FocusedToplevel](#mark189)
		- [NoticeWindow](#mark190)
		- [YesNoCancelWindow](#mark191)
		- [PromptWindow](#mark192)
		- [PasswordWindow](#mark193)
		- [ListWindow](#mark194)
		- [TextWindow](#mark195)
	- [Misc Widgets](#mark196)
		- [ToolTip](#mark197)
		- [EasySizegrip](#mark198)
- [SuperLib.utils](#mark199)
	- [Utils](#mark200)
		- [check_if_module_installed](#mark201)
		- [check_string_contains](#mark202)
		- [dummy_function](#mark203)
		- [get_friendly_time](#mark204)
		- [get_unix_timestamp](#mark205)
		- [get_unix_timestring](#mark206)
		- [get_user_home_folder](#mark207)
		- [open_folder_in_explorer](#mark208)
		- [sort_dict_by_keys](#mark209)
		- [timer_decorator](#mark210)
	- [File Generators](#mark211)
		- [HTML_Generator](#mark212)
		- [TXT_Generator](#mark213)
		- [MD_Generator](#mark214)
	- [History Mixin](#mark215)
		- [HistoryMixin](#mark216)
	- [Color Functions](#mark217)
		- [reduce_255](#mark218)
		- [rgb_to_hex](#mark219)
		- [rgba_to_hex](#mark220)
		- [hex_to_rgb](#mark221)
		- [hex_to_rgba](#mark222)
		- [get_gradient](#mark223)
		- [rgb_to_scalar](#mark224)
		- [scalar_to_rgb](#mark225)
		- [linear_gradient](#mark226)
		- [get_rainbow](#mark227)
- [MegaWidgets](#mark228)
	- [Notes MegaWidget](#mark229)
		- [NotesTab](#mark230)
	- [Conversation MegaWidget](#mark231)
		- [ConversationsTab](#mark232)
	- [Profile Management](#mark233)
		- [ProfilesSystem](#mark234)
		- [UserProfile](#mark235)
		- [get_profiles_folder](#mark236)
		- [get_profiles_list](#mark237)
- [PIL-Only Widgets and Functions](#mark238)
- [PIL-Only Widgets](#mark239)
	- [GifLoader](#mark240)
	- [GifViewer](#mark241)
- [PIL-Only Functions](#mark242)
	- [convert_image_to_blackandwhite](#mark243)
	- [convert_image_to_grayscale](#mark244)
	- [load_image_from_byte_array](#mark245)
	- [load_tk_image_from_bytes_array](#mark246)
	- [make_checkerboard](#mark247)
- [Changelog](#mark248)
	- [0.2.9](#mark249)
	- [0.2.8](#mark250)
	- [0.2.7](#mark251)
	- [0.2.6](#mark252)
	- [0.2.5](#mark253)
	- [0.2.4](#mark254)
	- [0.2.3](#mark255)
	- [0.2.2](#mark256)
	- [0.2.1](#mark257)
	- [0.2.0](#mark258)
	- [0.1.42](#mark259)
	- [0.1.41](#mark260)
	- [0.1.40](#mark261)
	- [0.1.39](#mark262)
	- [0.1.38](#mark263)
	- [0.1.37](#mark264)
	- [0.1.36](#mark265)
	- [0.1.35](#mark266)
	- [0.1.34](#mark267)
	- [0.1.33](#mark268)
	- [0.1.32](#mark269)
	- [0.1.31](#mark270)
	- [0.1.30](#mark271)
	- [0.1.29](#mark272)
	- [0.1.28](#mark273)
	- [0.1.27](#mark274)
	- [0.1.26](#mark275)
	- [0.1.25](#mark276)
	- [0.1.24](#mark277)
	- [0.1.23](#mark278)
	- [0.1.22](#mark279)
	- [0.1.21](#mark280)
	- [0.1.20](#mark281)
	- [0.1.19](#mark282)
	- [0.1.18](#mark283)
	- [0.1.17](#mark284)
	- [0.1.16](#mark285)
	- [0.1.15](#mark286)
	- [0.1.14](#mark287)
	- [0.1.13](#mark288)
	- [0.1.12](#mark289)
	- [0.1.11](#mark290)
	- [0.1.10](#mark291)
	- [0.1.9](#mark292)
	- [0.1.8](#mark293)
	- [0.1.7](#mark294)
	- [0.1.6](#mark295)
	- [0.1.5](#mark296)
	- [0.1.4](#mark297)
	- [0.1.3](#mark298)
	- [0.1.2](#mark299)
	- [0.1.1](#mark300)
	- [0.1.0](#mark301)

---

# About<a name="mark1"></a>[^](#mark0)

py_simple_ttk exists because I got tired of rewriting the same code over and over for simple projects. The goal is to provide a variety of meta widgets with consistent get/set/enable/disable/destroy methods and mega-widgets that make ttk development easier and faster. Features include built-in theme support, a score of labeled and multi-widgets, tools for easy form building, a sample application demonstrating many of py_simple_ttk's features, a configuration file system, and much more. Also contains a number of widgets and functions only available when PIL (an optional requirement) is installed.
![Lines of code](https://img.shields.io/tokei/lines/github/AndrewSpangler/py_simple_ttk)

# Requirements<a name="mark2"></a>[^](#mark0)

['py_simple_lorem']

# Configuring ini.json<a name="mark3"></a>[^](#mark0)

```
+------------------------+-------------------------------------------+
|        Key             |                   Value                   |
+------------------------+-------------------------------------------+
| application            | Application Name (String)                 |
| conversations_enabled  | Enable Convo System (Boolean)             |
| default_theme          | Default theme to use if available (String)|
| disable_notebook       | Disable default ttk.Notebook (Boolean)    |
| enable_fullscreen      | Enable Window Fullscreen option (Boolean) |
| enable_launcher        | Enable Dynamic Launcher System (Boolean)  |
| enable_maximized       | Enable Window Maximized (Boolean)         |
| enable_profiles        | Enable a User Profiles System (Boolean)   |
| enable_sizegrip        | Enable Window EasySizegrip (Boolean)      |
| enable_themes_menu     | Enable Themes Dropdown (Boolean)          |
| height                 | Startup Window Height (Int)               |
| icon                   | Application Icon Path (String)            |
| ignored_themes         | Themes to not display in menu (List)      |
| minheight              | Window Minimum Height (Int)               |
| minwidth               | Window Minimum Width (Int)                |
| movable_tabs           | Enable Moveable Notebook Tabs (Boolean)   |
| notes_enabled          | Enable Note System (Boolean)              |
| resizable_height       | Enable Window Height Resizing (Boolean)   |
| resizable_width        | Enable Window Width Resizing (Boolean)    |
| scale_minsize          | Scale application Minimum Size (Boolean)  |
| scale_startsize        | Scale application Start Size (Boolean)    |
| scaling                | Window Scaling (Float)                    |
| start_centered         | Center Window on launch (Boolean)         |
| start_fullscreen       | Start Window in Fullscreen mode (Boolean) |
| start_maximized        | Start Window Maximized (Boolean)          |
| theme_textboxes        | Apply theme colors to tk.Text (Boolean)   |
| version                | Application Version (String)              |
| width                  | Startup Window Width (Int)                |
+------------------------+-------------------------------------------+
```
# The App Object<a name="mark4"></a>[^](#mark0)

### App<a name="mark5"></a>[^](#mark4)
**Main Application Object**

```py
class App(object):
	def __init__(self, ini_file: str):
		...
	def apply_profile(self, profile: src.py_simple_ttk.utils.ProfilesSystem.UserProfile) -> str:
		"""Apply settings from the current profile. For more complicated profile systems override this function. `Returns the current theme as a String`"""
	def copy_to_user_clipboard(self, val: str) -> None:
		"""Copys a text val to the user's keyboard. `Returns None`"""
	def create_profile(self, name: str = None) -> str | None:
		"""Calling with no name brings up a popup, the popup calls this function again with name kw which instead makes a new profile or asks again for a name if the supplied name was invalid. `Returns the current theme as a String on success or None`"""
	def get_scaling(self) -> None:
		...
	def select_profile(self, name: str = None) -> str:
		"""Calling with no name brings up a popup, the popup calls this function again with the name which instead calls the Profiles System to use a certain profile. `Returns the current theme as a String`"""
	def start(self) -> None:
		"""Alias for App.mainloop(). `Never returns.`"""
	def toggle_full_screen(self, event=None) -> None:
		"""Toggles full screen. Returns None`"""
	def toggle_maximized(self, event=None) -> None:
		"""Toggles maximized window. Returns None`"""
	def update_default_title(self, indicate_profile=True) -> None:
		"""Update the window title with the default string, optionally with a profile indicator. `Returns None`"""
	def update_title(self, title) -> None:
		"""Updates the window title. `Returns None`"""
	def use_theme(self, theme: str = None, verbose: bool = False) -> str:
		"""Updates the app to use a certain theme. `Returns the current theme as a String`"""
```
# Core Widgets<a name="mark6"></a>[^](#mark0)

### MultiWidgetMixin<a name="mark7"></a>[^](#mark6)
**An abstract mixin that provides a way to easily instantiate multiple of the same class of a widget and making complicated forms with simple get/set methods.**

MultiWidgets support a simple get/set system. Calling get without a configuration list returns a dict of subwidget keys mapped to the values of each subwidget's .get value. Passing a list of subwidget keys limits MultiWidgetMixin.get to said subwidgets. Subclassing a multiwidget with one or more instances of one class and then calling multiwidget.add() with different classes after is acceptable assuming the widget supports being added and .get / .set / .enable / .disable / .clear methods.
```py
class MultiWidgetMixin(object):
	def __init__(self, widget_type: type, config: dict = {}, default_kwargs: dict = {}):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
### SuperWidgetMixin<a name="mark8"></a>[^](#mark6)
**Mixin to easily bind many of the common tkinter events.**

This class serves to add bindings for the majority of common tkinter widget events. The bindings are made in add mode to prevent previous / new bindings from causing unintended side-effects like unmapping etc.
```py
class SuperWidgetMixin(object):
	def __init__(self, on_mouse_enter: Callable = None, on_mouse_leave: Callable = None, on_mouse_move: Callable = None, on_mouse_wheel: Callable = None, on_left_click: Callable = None, on_double_left_click: Callable = None, on_middle_click: Callable = None, on_double_middle_click: Callable = None, on_right_click: Callable = None, on_double_right_click: Callable = None, on_configure: Callable = None):
		...
```
## Tabs<a name="mark9"></a>[^](#mark0)

### Tab<a name="mark10"></a>[^](#mark9)
**The core Tab class.**

The notebook object can be any ttk.Notebook, automatically adds itself to its parent notebook with title being the tab label. This class may be instantiated directly and added to or subclassed based on need.
```py
class Tab(Frame):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### LauncherTab<a name="mark11"></a>[^](#mark9)
**Basic Tab for launching tasks from a list.**

Performs an action on a list of options. The options argument is formatted as such: `options = {"Button Text 1": val1,"Button Text 2": val2}` Button presses will call `action(val)`
```py
class LauncherTab(Tab):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, options: dict, action: Callable):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### BrowserLauncherTab<a name="mark12"></a>[^](#mark9)
**LauncherTab that opens a list of URLS/Files**

Takes a dict of button texts as keys and urls to open as values
```py
class BrowserLauncherTab(LauncherTab):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, options: dict):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### CommandLauncherTab<a name="mark13"></a>[^](#mark9)
**LauncherTab that runs a list of commands**

Takes a dict of button texts as keys and command prompt commands to execute as values
```py
class CommandLauncherTab(LauncherTab):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, options: dict):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### ConsoleTab<a name="mark14"></a>[^](#mark9)
**Basic console tab using a ConsoleWidget**

```py
class ConsoleTab(Tab):
	def __init__(self, notebook: tkinter.ttk.Notebook, **kwargs):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### TableTab<a name="mark15"></a>[^](#mark9)
**Basic Table Tab**

table_contents is a dictionary whose keys map to lists of equal lengths with the column contents
```py
class TableTab(Tab):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, table_contents: dict, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### TreeTableTab<a name="mark16"></a>[^](#mark9)
**Improved Table Tab**

table_contents is a dictionary whose keys map to lists of equal lengths with the column contents
```py
class TreeTableTab(Tab):
	def __init__(self, notebook: tkinter.ttk.Notebook, title: str, table_contents: dict = {}, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
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
	def disable(self) -> None:
		"""Disable button"""
	def enable(self) -> None:
		"""Enable button"""
	def get(self) -> str:
		"""Get button text"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledButton<a name="mark20"></a>[^](#mark18)
**Labeled ActiveButton widget**

```py
class LabeledButton(Labeler, ActiveButton):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, command: Callable = '', default: str = '', is_child: bool = False, labelside: str = 'left', **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable button"""
	def enable(self) -> None:
		"""Enable button"""
	def get(self) -> str:
		"""Get button text"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
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
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### CycleButton<a name="mark22"></a>[^](#mark18)
**ActiveButton that cycles through options on each click**

```py
class CycleButton(ActiveButton):
	def __init__(self, parent: tkinter.ttk.Frame, options: list, default: int = 0, command: Callable = None, **kw):
		...
	def clear(self, event=None):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable button"""
	def enable(self) -> None:
		"""Enable button"""
	def get(self) -> str:
		"""Get button text"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledCycleButton<a name="mark23"></a>[^](#mark18)
**Labeled CycleButton widget**

```py
class LabeledCycleButton(Labeler, CycleButton):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, options: list, is_child: bool = False, labelside: str = 'left', **kw):
		...
	def clear(self, event=None):
		...
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable button"""
	def enable(self) -> None:
		"""Enable button"""
	def get(self) -> str:
		"""Get button text"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
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
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Core Functions<a name="mark25"></a>[^](#mark17)

### bbox_to_width_and_height<a name="mark26"></a>[^](#mark25)
> **Takes a bbox and converts it to a width and height tuple.**
> 
```python
def bbox_to_width_and_height(bbox: tuple) -> tuple:
> 	...
```
### center_window<a name="mark27"></a>[^](#mark25)
> **Centers spawn window on main window. Call win.update_idletasks() on either window before calling this if said window is not yet shown.**
> 
```python
def center_window(main_window: tkinter.Tk, spawn_window: tkinter.Toplevel) -> None:
> 	...
```
### check_in_bounds<a name="mark28"></a>[^](#mark25)
> **Checks if a position is within a given bounds. Pos is generally a mouse event position tuple, bounds is generally a canvas.bbox(), but a (left, top, right, bottom) tuple will work too.**
> 
```python
def check_in_bounds(pos: tuple, bounds: tuple) -> bool:
> 	...
```
### complex_widget_search<a name="mark29"></a>[^](#mark25)
> **A more robust version of the widget search with lists for multiple widget types found in one go**
> 
```python
def complex_widget_search(node_widget, widget_types_to_find: list | tuple, found_lists: dict = {}) -> dict:
> 	...
```
### copy_to_user_clipboard<a name="mark30"></a>[^](#mark25)
> **Copies a string to the user's clipboard.**
> 
```python
def copy_to_user_clipboard(widget, value: str) -> None:
> 	...
```
### create_round_rectangle<a name="mark31"></a>[^](#mark25)
> **Draws a rounded rectangle of a given radius on a tk.canvas**
> 
```python
def create_round_rectangle(canvas, x1: float, y1: float, x2: float, y2: float, r: float = 20, fill: str = '', outline: str = '#000000', **kwargs):
> 	...
```
### default_pack<a name="mark32"></a>[^](#mark25)
> **Apply a consistent descending packing method.**
> 
```python
def default_pack(widget, bottom: bool = False, padx: tuple = 5) -> None:
> 	...
```
### default_separator<a name="mark33"></a>[^](#mark25)
> **Apply a consistent horizontal separator.**
> 
```python
def default_separator(f: tkinter.ttk.Frame, padx: tuple = 35, pady: tuple = (10, 5)) -> tkinter.ttk.Separator:
> 	...
```
### default_vertical_pack<a name="mark34"></a>[^](#mark25)
> **Apply a consistent packing method to vertically packed widgets.**
> 
```python
def default_vertical_pack(widget, expand: bool = False, fill: str = 'both', padx: tuple = 0) -> None:
> 	...
```
### default_vertical_separator<a name="mark35"></a>[^](#mark25)
> **Apply a consistent vertical separator.**
> 
```python
def default_vertical_separator(frame: tkinter.ttk.Frame, pady: tuple = 15, padx: tuple = 10) -> tkinter.ttk.Separator:
> 	...
```
### enable_notebook_movement<a name="mark36"></a>[^](#mark25)
> **Copyright CJB 2010-07-31: https://wiki.tcl-lang.org/page/Drag+and+Drop+Notebook+Tabs Enables Tab dragging in subsequently created notebooks. Only run this function once.**
> 
```python
def enable_notebook_movement(app) -> None:
> 	...
```
### focus_next<a name="mark37"></a>[^](#mark25)
> **Forces focus to the widget after the one that triggered the event**
> 
```python
def focus_next(event) -> object:
> 	...
```
### force_aspect<a name="mark38"></a>[^](#mark25)
> **Forces an inner frame to maintain an aspect ratio regardless of the outer frame's size**
> 
```python
def force_aspect(inner_frame: tkinter.ttk.Frame, outer_frame: tkinter.ttk.Frame, ratio: float = 1.7777777777777777) -> None:
> 	...
```
### get_asset<a name="mark39"></a>[^](#mark25)
> **Gets an asset from the included assets folder by relative path. Works with pyinstaller.**
> 
```python
def get_asset(path, folder: str = 'C:\\Users\\arcti\\GitHub\\py_simple_ttk\\src\\py_simple_ttk\\./assets') -> str:
> 	...
```
### get_bundled_themes_list<a name="mark40"></a>[^](#mark25)
> **None**
> 
```python
def get_bundled_themes_list(verbose: bool = False) -> list:
> 	...
```
### get_generated_font_images_lookup<a name="mark41"></a>[^](#mark25)
> **Makes a lookup for the pre-generated open-sans font monograms that ship with py_simple_ttk.**
> 
```python
def get_generated_font_images_lookup(path: str = None) -> dict:
> 	...
```
### get_local_appdata_folder<a name="mark42"></a>[^](#mark25)
> **Opens user's Windows home folder. Only works on Windows for obvious reasons.**
> 
```python
def get_local_appdata_folder() -> str:
> 	...
```
### get_themes_folder<a name="mark43"></a>[^](#mark25)
> **Gets the absolute path to the included themes folder**
> 
```python
def get_themes_folder() -> str:
> 	...
```
### make_aspect_frames<a name="mark44"></a>[^](#mark25)
> **Creates an outer and inner frame within a parent frame. Forces the inner frame to maintain an aspect ratio. Returns the outer and inner frames.**
> 
```python
def make_aspect_frames(parent: tkinter.ttk.Frame, ratio: float = 1.7777777777777777) -> tuple:
> 	...
```
### make_temp_config_file<a name="mark45"></a>[^](#mark25)
> **Make a one-time-use app config file from a dict in the same form as a normal config json. `Returns file path as String`**
> 
```python
def make_temp_config_file(config: dict):
> 	...
```
### open_link<a name="mark46"></a>[^](#mark25)
> **Opens a link in the user's default web browser. `Returns None`**
> 
```python
def open_link(link: str) -> None:
> 	...
```
### recursive_widget_search<a name="mark47"></a>[^](#mark25)
> **
    Adds widgets of a given type to a list as it travels up,
    away from the root of a widget tree. This method can be slow on
    large widget trees but is useful for retheming tk widgets with
    ttk formatting on theme changes. `Returns a list of widgets`
    **
> 
```python
def recursive_widget_search(node_widget, widget_type_to_find: type, found_list: list = []) -> list:
> 	...
```
### run_cl<a name="mark48"></a>[^](#mark25)
> **Runs something via command line. `Returns None`**
> 
```python
def run_cl(commands: list) -> None:
> 	...
```
## Canvas Widgets<a name="mark49"></a>[^](#mark17)

### ResizableCanvas<a name="mark50"></a>[^](#mark49)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def refresh(self) -> None:
		"""Refresh Canvas"""
```
### ScrolledCanvas<a name="mark51"></a>[^](#mark49)
**Resizeable, Auto-Scrollbarred Canvas**

Canvas resizes to fit frame on configure event. Canvas has automatic Scrollbars that appear when needed. Canvas background color is based on current theme. Due to how the scrolling is handled the actual Canvas is accessd via `ScrolledCanvas().canvas`.
```py
class ScrolledCanvas(Frame):
	def __init__(self, parent, on_mouse_enter=None, on_mouse_leave=None, on_mouse_move=None, on_mouse_wheel=None, on_left_click=None, on_middle_click=None, on_right_click=None, on_configure=None, configure_delay: int = 100, bind_canvas_scroll=True, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get_adjusted_y_view(self, event) -> int:
		"""Gets a canvas y-view adjusted based on its scrolled position"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def use_style(self, style) -> None:
		"""Reformat with a given ttk style. `Returns None`"""
```
### TiledCanvas<a name="mark52"></a>[^](#mark49)
```py
class TiledCanvas(ScrolledCanvas):
	def __init__(self, *args, tile_width=400, tile_height=100, tile_padx=5, tile_pady=5, tile_color='#424548', text_color='#CCCCCC', border_color='#000000', on_tile_left_click=None, on_tile_middle_click=None, on_tile_right_click=None, override_tile_width=False, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get_adjusted_y_view(self, event) -> int:
		"""Gets a canvas y-view adjusted based on its scrolled position"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def refresh(self, event=None) -> None:
		"""Redraw the canvas"""
	def use_style(self, style) -> None:
		"""Reformat with a given ttk style. `Returns None`"""
```
### ExampleTile<a name="mark53"></a>[^](#mark49)
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
## Checkbutton Widgets<a name="mark54"></a>[^](#mark17)

### ActiveCheckbutton<a name="mark55"></a>[^](#mark54)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: bool) -> None:
		"""Set Checkbutton value. `Returns None`"""
```
### LabeledCheckbutton<a name="mark56"></a>[^](#mark54)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: bool) -> None:
		"""Set Checkbutton value. `Returns None`"""
```
### LabeledMultiCheckbutton<a name="mark57"></a>[^](#mark54)
**Labeled MultiWidget LabeledCheckbutton.**

Used when you need multiple, vertically stacked Labeled Checkbuttons
```py
class LabeledMultiCheckbutton(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Combobox Widgets<a name="mark58"></a>[^](#mark17)

### ActiveCombobox<a name="mark59"></a>[^](#mark58)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set Combobox value. `Returns None`"""
```
### LabeledCombobox<a name="mark60"></a>[^](#mark58)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set Combobox value. `Returns None`"""
```
### LabeledMultiCombobox<a name="mark61"></a>[^](#mark58)
**Labeled MultiWidget LabeledCombobox.**

Used when you need mutiple, vertically stacked Labeled Comboboxes
```py
class LabeledMultiCombobox(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Console Widgets<a name="mark62"></a>[^](#mark17)

### ConsoleWidget<a name="mark63"></a>[^](#mark62)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def print(self, val, end: str = '\n'):
		"""Prints a line to the console with a customizable line ending. `Returns None`"""
```
## Constraining Functions<a name="mark64"></a>[^](#mark17)

### check_entry_type<a name="mark65"></a>[^](#mark64)
> **Core type checker function. Limits entry to chars that construct a given type**
> 
```python
def check_entry_type(val: str, typ: type) -> bool:
> 	...
```
### check_entry_int<a name="mark66"></a>[^](#mark64)
> **Check if an entry input is a valid integer**
> 
```python
def check_entry_int(val: str) -> bool:
> 	...
```
### check_entry_float<a name="mark67"></a>[^](#mark64)
> **Check if an entry input is a valid float**
> 
```python
def check_entry_float(val: str) -> bool:
> 	...
```
### check_entry_contents<a name="mark68"></a>[^](#mark64)
> **Core content checker function. Limits entry to a list of chars ['a', 'b', 'c', ...] or     the chars contained in a simple string 'abc...'**
> 
```python
def check_entry_contents(val: str, limiter: list | str) -> bool:
> 	...
```
### check_entry_ascii_lowercase<a name="mark69"></a>[^](#mark64)
> **Check if entry input is made only of lowercase ascii**
> 
```python
def check_entry_ascii_lowercase(val: str) -> bool:
> 	...
```
### check_entry_ascii_uppercase<a name="mark70"></a>[^](#mark64)
> **Check if entry input is made only of uppercase ascii**
> 
```python
def check_entry_ascii_uppercase(val: str) -> bool:
> 	...
```
### check_entry_ascii_letters<a name="mark71"></a>[^](#mark64)
> **Check if entry input is made only of uppercase and lowercase ascii**
> 
```python
def check_entry_ascii_letters(val: str) -> bool:
> 	...
```
### check_entry_ascii_digits<a name="mark72"></a>[^](#mark64)
> **Check if entry input is made only of digits**
> 
```python
def check_entry_ascii_digits(val: str) -> bool:
> 	...
```
### check_entry_ascii_uppercase_digits<a name="mark73"></a>[^](#mark64)
> **Check if entry input is made only of uppercase ascii and digits**
> 
```python
def check_entry_ascii_uppercase_digits(val: str) -> bool:
> 	...
```
### check_entry_ascii_lowercase_digits<a name="mark74"></a>[^](#mark64)
> **Check if entry input is made only of lowercase ascii and digits**
> 
```python
def check_entry_ascii_lowercase_digits(val: str) -> bool:
> 	...
```
### check_entry_ascii_hexdigits<a name="mark75"></a>[^](#mark64)
> **Check if entry input is made only of hexigits**
> 
```python
def check_entry_ascii_hexdigits(val: str) -> bool:
> 	...
```
### check_entry_ascii_octdigits<a name="mark76"></a>[^](#mark64)
> **Check if entry input is made only of octdigits**
> 
```python
def check_entry_ascii_octdigits(val: str) -> bool:
> 	...
```
### check_entry_ascii_letters_digits<a name="mark77"></a>[^](#mark64)
> **Check if entry input is made only of ascii lowercase, ascii uppercase, and digits**
> 
```python
def check_entry_ascii_letters_digits(val) -> bool:
> 	...
```
### check_entry_ascii_printable<a name="mark78"></a>[^](#mark64)
> **Check if entry input is made only of printable characters**
> 
```python
def check_entry_ascii_printable(val: str) -> bool:
> 	...
```
## Counter Widgets<a name="mark79"></a>[^](#mark17)

### Counter<a name="mark80"></a>[^](#mark79)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: int, adjust: int = 0, no_command: bool = False) -> int:
		...
```
### FloatCounter<a name="mark81"></a>[^](#mark79)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: float, adjust: float = 0.0) -> float:
		...
```
### LabeledCounter<a name="mark82"></a>[^](#mark79)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: int, adjust: int = 0, no_command: bool = False) -> int:
		...
```
### LabeledFloatCounter<a name="mark83"></a>[^](#mark79)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: float, adjust: float = 0.0) -> float:
		...
```
### LabeledMultiCounter<a name="mark84"></a>[^](#mark79)
**Labeled MultiWidget LabeledCounter.**

Used when you need multiple, vertically stacked Labeled Counters
```py
class LabeledMultiCounter(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### LabeledMultiFloatCounter<a name="mark85"></a>[^](#mark79)
**Labeled MultiWidget Labeled FloatCounter.**

Used when you need multiple, vertically stacked Labeled FloatCounters
```py
class LabeledMultiFloatCounter(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Entry Widgets<a name="mark86"></a>[^](#mark17)

### ActiveEntry<a name="mark87"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### ScrolledEntry<a name="mark88"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledEntry<a name="mark89"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiEntry<a name="mark90"></a>[^](#mark86)
**Labeled MultiWidget LabeledEntry**

Used when you need multiple, vertically stacked Labeled Entries
```py
class LabeledMultiEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### LabeledButtonEntry<a name="mark91"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiButtonEntry<a name="mark92"></a>[^](#mark86)
**Labeled MultiWidget Labeled ButtonEntry**

Used when you need multiple, vertically stacked Labeled Entries
```py
class LabeledMultiButtonEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### LabeledPathEntry<a name="mark93"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiPathEntry<a name="mark94"></a>[^](#mark86)
**Labeled MultiWidget LabeledPathEntry**

Used when you need multiple, vertically stacked LabeledPathEntries
```py
class LabeledMultiPathEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### PasswordEntry<a name="mark95"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, values: tuple) -> None:
		...
```
### LabeledPasswordEntry<a name="mark96"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, values: tuple) -> None:
		...
```
### LabeledMultiPasswordEntry<a name="mark97"></a>[^](#mark86)
**Labeled MultiWidget Labeled PasswordEntry**

Used when you need multiple, vertically stacked Labeled Username/Password Entries
```py
class LabeledMultiPasswordEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### ConstrainedEntry<a name="mark98"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledConstrainedEntry<a name="mark99"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiConstrainedEntry<a name="mark100"></a>[^](#mark86)
**Labeled Multi Constrained Entry**

```py
class LabeledMultiConstrainedEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### IntEntry<a name="mark101"></a>[^](#mark86)
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
	def get(self) -> int:
		"""Get IntEntry value, `Returns an Int`"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledIntEntry<a name="mark102"></a>[^](#mark86)
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
	def get(self) -> int:
		"""Get IntEntry value, `Returns an Int`"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiIntEntry<a name="mark103"></a>[^](#mark86)
```py
class LabeledMultiIntEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### FloatEntry<a name="mark104"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledFloatEntry<a name="mark105"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiFloatEntry<a name="mark106"></a>[^](#mark86)
```py
class LabeledMultiFloatEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### LowercaseEntry<a name="mark107"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledLowercaseEntry<a name="mark108"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiLowercaseEntry<a name="mark109"></a>[^](#mark86)
```py
class LabeledMultiLowercaseEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### UppercaseEntry<a name="mark110"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledUppercaseEntry<a name="mark111"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiUppercaseEntry<a name="mark112"></a>[^](#mark86)
```py
class LabeledMultiUppercaseEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### LettersEntry<a name="mark113"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledLettersEntry<a name="mark114"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiLettersEntry<a name="mark115"></a>[^](#mark86)
```py
class LabeledMultiLettersEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### DigitsEntry<a name="mark116"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledDigitsEntry<a name="mark117"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiDigitsEntry<a name="mark118"></a>[^](#mark86)
```py
class LabeledMultiDigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### UppercaseDigitsEntry<a name="mark119"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledUppercaseDigitsEntry<a name="mark120"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiUppercaseDigitsEntry<a name="mark121"></a>[^](#mark86)
```py
class LabeledMultiUppercaseDigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### LowercaseDigitsEntry<a name="mark122"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledLowercaseDigitsEntry<a name="mark123"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiLowercaseDigitsEntry<a name="mark124"></a>[^](#mark86)
```py
class LabeledMultiLowercaseDigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### LettersDigitsEntry<a name="mark125"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledLettersDigitsEntry<a name="mark126"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiLettersDigitsEntry<a name="mark127"></a>[^](#mark86)
```py
class LabeledMultiLettersDigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### HexdigitsEntry<a name="mark128"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledHexdigitsEntry<a name="mark129"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiHexdigitsEntry<a name="mark130"></a>[^](#mark86)
```py
class LabeledMultiHexdigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### OctdigitsEntry<a name="mark131"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledOctdigitsEntry<a name="mark132"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiOctdigitsEntry<a name="mark133"></a>[^](#mark86)
```py
class LabeledMultiOctdigitsEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### PrintableEntry<a name="mark134"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledPrintableEntry<a name="mark135"></a>[^](#mark86)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set Entry value. `Returns None`"""
```
### LabeledMultiPrintableEntry<a name="mark136"></a>[^](#mark86)
```py
class LabeledMultiPrintableEntry(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Frame Widgets<a name="mark137"></a>[^](#mark17)

### ColumnFrame<a name="mark138"></a>[^](#mark137)
**A frame with a given number of children column ttk.Frames**

Takes a number of columns or a list of names when the `labeled` keyword is set to True
```py
class ColumnFrame(Frame):
	def __init__(self, parent: tkinter.ttk.Frame, columns: int | list = 1, labeled=False, pack_args: dict = {}, **kw):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def yield_frame(self):
		"""Cyclically returns frames"""
```
### HamburgerFrame<a name="mark139"></a>[^](#mark137)
**A ttk.Frame with a Hamburger Menu and supporting widgets**

Options is an iterable in the form ((label, callback), (label2, callback2), ...). See examples/hamburger_demo.py for usage.
```py
class HamburgerFrame(Frame):
	def __init__(self, parent: tkinter.ttk.Frame, options: collections.abc.Iterable, menu_width: int = 300, column_style='Hamburger.TFrame', **kw):
		...
	def close(self, event=None) -> None:
		"""Closes the menu. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def open(self, event=None) -> None:
		"""Opens the menu. `Returns None`"""
```
## KeyPad Widgets<a name="mark140"></a>[^](#mark17)

### KeypadButton<a name="mark141"></a>[^](#mark140)
**Base Keypad Button**

Keypad button that automatically packs itself based on given coordinates. This object is not usually directly instantiated.
```py
class KeypadButton(Button):
	def __init__(self, frame: tkinter.ttk.Frame, value: int, coords: tuple, command: Callable):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### BaseKeypad<a name="mark142"></a>[^](#mark140)
**Base Keypad Class**

Either instantiate directly with a custom layout or subclass with each subclass supplying a custom layout for more keypads. Subclass KeypadButton and supply the class as the "button_type" kwarg for custom buttons.
```py
class BaseKeypad(Frame):
	def __init__(self, layout, command, button_class=<class 'src.py_simple_ttk.widgets.KeyPadWidgets.KeypadButton'>, *args, **kwargs):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### DialerKeypad<a name="mark143"></a>[^](#mark140)
**Phone Dialer Keypad**

Example 12-button keypad, subclass BaseKeypad and supply a custom layout for more keypads.
```py
class DialerKeypad(BaseKeypad):
	def __init__(self, command: Callable, *args, **kwargs):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
## Label Widgets<a name="mark144"></a>[^](#mark17)

### ActiveLabel<a name="mark145"></a>[^](#mark144)
**Active ttk.Entry with added features and the SuperWidgetMixin**

```py
class ActiveLabel(Label, SuperWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, command: Callable = None, default: str = '', widgetargs: dict = {}, **kw):
		...
	def clear(self) -> None:
		"""Set label value to default, empty unless default set. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable label updates. `Returns None`"""
	def enable(self) -> None:
		"""Enable label updates. `Returns None`"""
	def get(self) -> str:
		"""Get label value. `Returns a String`"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set label value. `Returns None`"""
```
### LabeledValue<a name="mark146"></a>[^](#mark144)
**A pair of ActiveLabels in a frame acting as a label and value pair with the label in bold**

```py
class LabeledValue(Frame):
	def __init__(self, parent: tkinter.ttk.Frame, label_text: str = None, value_text: str = None, label_config: dict = {}, value_config: dict = {}, *args, **kwargs):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def get(self) -> str:
		"""Returns the label's and value's texts separated by a space. `Returns a String`"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: tuple):
		"""Set the label and value from two text strings in a tuple like ("label:", "value"). `Returns None`"""
```
## Labeler Widget<a name="mark147"></a>[^](#mark17)

### ActiveButton<a name="mark148"></a>[^](#mark147)
**ttk.Button with added features**

```py
class ActiveButton(Button, SuperWidgetMixin):
	def __init__(self, parent, default: str = '', command: Callable = None, widgetargs: dict = {}, **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable button"""
	def enable(self) -> None:
		"""Enable button"""
	def get(self) -> str:
		"""Get button text"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledButton<a name="mark149"></a>[^](#mark147)
**Labeled ActiveButton widget**

```py
class LabeledButton(Labeler, ActiveButton):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, command: Callable = '', default: str = '', is_child: bool = False, labelside: str = 'left', **kw):
		...
	def clear(self) -> None:
		"""Set button text to default"""
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable button"""
	def enable(self) -> None:
		"""Enable button"""
	def get(self) -> str:
		"""Get button text"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledMultiButton<a name="mark150"></a>[^](#mark147)
**Labeled MultiWidget LabeledButton.**

Used when you need multiple, vertically stacked Labeled ActiveButtons
```py
class LabeledMultiButton(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### CycleButton<a name="mark151"></a>[^](#mark147)
**ActiveButton that cycles through options on each click**

```py
class CycleButton(ActiveButton):
	def __init__(self, parent: tkinter.ttk.Frame, options: list, default: int = 0, command: Callable = None, **kw):
		...
	def clear(self, event=None):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable button"""
	def enable(self) -> None:
		"""Enable button"""
	def get(self) -> str:
		"""Get button text"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledCycleButton<a name="mark152"></a>[^](#mark147)
**Labeled CycleButton widget**

```py
class LabeledCycleButton(Labeler, CycleButton):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, options: list, is_child: bool = False, labelside: str = 'left', **kw):
		...
	def clear(self, event=None):
		...
	def clear_label_text(self) -> None:
		"""Clear a Labeled widget's Label text."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable button"""
	def enable(self) -> None:
		"""Enable button"""
	def get(self) -> str:
		"""Get button text"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set button text"""
```
### LabeledMultiCycleButton<a name="mark153"></a>[^](#mark147)
**Labeled MultiWidget LabeledCycleButton**

Used when you need multiple, vertically stacked Labeled CycleButtons
```py
class LabeledMultiCycleButton(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## ListBox Widgets<a name="mark154"></a>[^](#mark17)

### ScrolledListBox<a name="mark155"></a>[^](#mark154)
**Scrolled Listbox with SuperWidget mixin**

```py
class ScrolledListBox(Scroller, Listbox, SuperWidgetMixin):
	def __init__(self, parent, **kw) -> object:
		...
	def activate(self, index):
		"""Activate item identified by INDEX."""
	def add(self, val: str) -> None:
		"""Add an item to the end of the Listbox. `Returns None`"""
	def add_list(self, items: list) -> None:
		"""Add a list of items to the end of the Listbox. `Returns None`"""
	def clear(self) -> None:
		"""Clear Listbox. `Returns None`"""
	def curselection(self):
		"""Return the indices of currently selected item."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self):
		"""Disable Listbox. `Returns None`"""
	def enable(self):
		"""Disable Listbox. `Returns None`"""
	def get(self, first, last=None):
		"""Get list of items from FIRST to LAST (included)."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### OrderedListbox<a name="mark156"></a>[^](#mark154)
**A Scrolled Re-Orderable Listbox with SuperWidget mixin**

Used when you need a re-orderable listbox for list arrangement etc. "selectmode" can only be "single" for this Widget.
```py
class OrderedListbox(ScrolledListBox):
	def __init__(self, parent: tkinter.ttk.Frame, **kw):
		...
	def activate(self, index):
		"""Activate item identified by INDEX."""
	def add(self, val: str) -> None:
		"""Add an item to the end of the Listbox. `Returns None`"""
	def add_list(self, items: list) -> None:
		"""Add a list of items to the end of the Listbox. `Returns None`"""
	def clear(self) -> None:
		"""Clear Listbox. `Returns None`"""
	def curselection(self):
		"""Return the indices of currently selected item."""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self):
		"""Disable Listbox. `Returns None`"""
	def enable(self):
		"""Disable Listbox. `Returns None`"""
	def get(self, first, last=None):
		"""Get list of items from FIRST to LAST (included)."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### ListManipulator<a name="mark157"></a>[^](#mark154)
```py
class ListManipulator(Frame):
	def __init__(self, parent: tkinter.ttk.Frame, disable_entry: bool = False, load_button_text: str = 'Load', load_button_width: int = 6, clear_button_text='Clear', clear_button_width: int = 6, add_button_text: str = 'Add>', add_button_width: int = 6, listbox_height: int = 7, entry_text: str = 'Add item', **kwargs):
		...
	def add(self, val: str) -> None:
		"""Add an item to the listbox. `Returns None`"""
	def add_list(self, *args) -> None:
		"""Add a list to the listbox. `Returns None`"""
	def clear(self) -> None:
		"""Clear Entry and Listbox. `Returns None`"""
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def disable(self) -> None:
		"""Disable Listbox, Entry, and Buttons. `Returns None`"""
	def enable(self) -> None:
		"""Enable Listbox, Entry, and Buttons. `Returns None`"""
	def get(self) -> list:
		"""Get the list of items in the listbox. `Returns a list`"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def load(self) -> None:
		"""Load file, clear Listbox, insert each line from file into listbox. `Returns None`"""
```
### Table<a name="mark158"></a>[^](#mark154)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def use_style(self, style: tkinter.ttk.Style) -> None:
		"""Update to match supplied ttk.Style object. `Returns None`"""
```
## OptionMenu Widgets<a name="mark159"></a>[^](#mark17)

### ActiveOptionMenu<a name="mark160"></a>[^](#mark159)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set OptionMenu value. `Returns None`"""
	def set_menu(self, default=None, *values):
		"""Build a new menu of radiobuttons with *values and optionally a default value."""
```
### LabeledOptionMenu<a name="mark161"></a>[^](#mark159)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val) -> None:
		"""Set OptionMenu value. `Returns None`"""
	def set_menu(self, default=None, *values):
		"""Build a new menu of radiobuttons with *values and optionally a default value."""
```
### LabeledMultiOptionMenu<a name="mark162"></a>[^](#mark159)
**Labeled MultiWidget LabeledOptionMenu**

```py
class LabeledMultiOptionMenu(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## ProgressBar Widgets<a name="mark163"></a>[^](#mark17)

### ActiveProgressbar<a name="mark164"></a>[^](#mark163)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def link(self, widget):
		"""Easily link to other widgets, sets the progressbar var to the passed widget's var. `Returns None`"""
	def set(self, val):
		"""Get Progressbar progress. `Returns a String`"""
	def start(self, interval=None):
		"""Begin autoincrement mode: schedules a recurring timer event that calls method step every interval milliseconds. interval defaults to 50 milliseconds (20 steps/second) if omitted."""
	def step(self, amount=None):
		"""Increments the value option by amount. amount defaults to 1.0 if omitted."""
	def stop(self):
		"""Stop autoincrement mode: cancels any recurring timer event initiated by start."""
```
### LabeledProgressbar<a name="mark165"></a>[^](#mark163)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def link(self, widget):
		"""Easily link to other widgets, sets the progressbar var to the passed widget's var. `Returns None`"""
	def set(self, val):
		"""Get Progressbar progress. `Returns a String`"""
	def start(self, interval=None):
		"""Begin autoincrement mode: schedules a recurring timer event that calls method step every interval milliseconds. interval defaults to 50 milliseconds (20 steps/second) if omitted."""
	def step(self, amount=None):
		"""Increments the value option by amount. amount defaults to 1.0 if omitted."""
	def stop(self):
		"""Stop autoincrement mode: cancels any recurring timer event initiated by start."""
```
### LabeledMultiProgressbar<a name="mark166"></a>[^](#mark163)
**Labeled MultiWidget LabeledProgressbar**

```py
class LabeledMultiProgressbar(Labeler, Frame, MultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside='top', orient='horizontal'):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args, kwargs, widget_type=None) -> object:
		"""Overrides normal MultiWidgetMixin behavior to deal with vertical orientation. Will break most added widgets `Returns None`"""
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def link(self, config: dict) -> None:
		"""Link to other widgets with a dict of subwidget keys to link to. This function will break if widgets without the link method are added to the MultiWidget. `Returns None`"""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Radiobutton Widgets<a name="mark167"></a>[^](#mark17)

### ActiveRadiobutton<a name="mark168"></a>[^](#mark167)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str | int | float) -> None:
		"""Set value, input type varies base on tk variable type. `Returns None`"""
```
### RadioTable<a name="mark169"></a>[^](#mark167)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set Radiobutton value. `Returns None`"""
```
### LabeledRadioTable<a name="mark170"></a>[^](#mark167)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set Radiobutton value. `Returns None`"""
```
### LabeledMultiRadioTable<a name="mark171"></a>[^](#mark167)
**Labeled MultiWidget LabeledRadioTable**

Used when you need multiple, vertically stacked LabeledRadioTables
```py
class LabeledMultiRadioTable(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
### SimpleRadioTable<a name="mark172"></a>[^](#mark167)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set Radiobutton value. `Returns None`"""
```
### LabeledSimpleRadioTable<a name="mark173"></a>[^](#mark167)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set Radiobutton value. `Returns None`"""
```
### LabeledMultiSimpleRadioTable<a name="mark174"></a>[^](#mark167)
**Labeled MultiWidget LabeledSimpleRadioTable**

Used when you need multiple, vertically stacked LabeledSimpleRadioTables
```py
class LabeledMultiSimpleRadioTable(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Scale Widgets<a name="mark175"></a>[^](#mark17)

### ActiveScale<a name="mark176"></a>[^](#mark175)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: float) -> None:
		"""Set Scale value. `Returns None`"""
```
### LabeledScale<a name="mark177"></a>[^](#mark175)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: float) -> None:
		"""Set Scale value. `Returns None`"""
```
### LabeledMultiScale<a name="mark178"></a>[^](#mark175)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Spinbox Widgets<a name="mark179"></a>[^](#mark17)

### ActiveSpinbox<a name="mark180"></a>[^](#mark179)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: int) -> None:
		"""Set Spinbox value. `Returns None`"""
```
### LabeledSpinbox<a name="mark181"></a>[^](#mark179)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: int) -> None:
		"""Set Spinbox value. `Returns None`"""
```
### LabeledMultiSpinbox<a name="mark182"></a>[^](#mark179)
**Labeled MultiWidget Spinbox.**

Used when you need multiple, vertically stacked Labeled Spinboxes
```py
class LabeledMultiSpinbox(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Text Widgets<a name="mark183"></a>[^](#mark17)

### ScrolledText<a name="mark184"></a>[^](#mark183)
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
		"""Undoes the last edit action If the undo option is true. An edit action is defined as all the insert and delete commands that are recorded on the undo stack in between two separators. Generates an error when the undo stack is empty. Does nothing when the undo option is false"""
	def enable(self) -> None:
		"""Enable Text box"""
	def get(self, start: str = '1.0', end: str = 'end'):
		"""Returns the contents of the text box with optional start/end kwargs. `Returns a String`"""
	def get_cursor(self):
		"""Get the current location of the cursor. `Returns None`"""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def select_all(self, event=None) -> None:
		"""Selects all text. `Returns None`"""
	def set(self, val: str) -> None:
		"""Sets the text. `Returns a String`"""
	def window_create(self, index, cnf={}, **kw):
		"""Create a window at INDEX."""
```
### CopyBox<a name="mark185"></a>[^](#mark183)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set CopyBox Contents"""
```
### LabeledCopyBox<a name="mark186"></a>[^](#mark183)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, val: str) -> None:
		"""Set CopyBox Contents"""
```
### LabeledMultiCopyBox<a name="mark187"></a>[^](#mark183)
**Labeled MultiWidget CopyBox.**

Used when you need multiple, vertically stacked Labeled CopyBoxes
```py
class LabeledMultiCopyBox(LabeledMultiWidgetMixin):
	def __init__(self, parent: tkinter.ttk.Frame, labeltext: str, config: dict, is_child: bool = False, labelside: str = 'top', **kw):
		...
	def add(self, parent: tkinter.ttk.Frame, key: str, args: list = [], kwargs: dict = {}, widget_type: type = None, fill: str = 'x', padx: tuple = (20, 0), pady: tuple = (5, 0), side: str = 'top', expand: bool = False) -> object:
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set(self, config: dict) -> None:
		"""Pass a map of widget keys and their values"""
```
## Toplevel Widgets<a name="mark188"></a>[^](#mark17)

### FocusedToplevel<a name="mark189"></a>[^](#mark188)
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
		"""Set mask for the icon bitmap of this widget. Return the mask if None is given."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### NoticeWindow<a name="mark190"></a>[^](#mark188)
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
		"""Set mask for the icon bitmap of this widget. Return the mask if None is given."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### YesNoCancelWindow<a name="mark191"></a>[^](#mark188)
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
		"""Set mask for the icon bitmap of this widget. Return the mask if None is given."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### PromptWindow<a name="mark192"></a>[^](#mark188)
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
		"""Set mask for the icon bitmap of this widget. Return the mask if None is given."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### PasswordWindow<a name="mark193"></a>[^](#mark188)
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
		"""Set mask for the icon bitmap of this widget. Return the mask if None is given."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### ListWindow<a name="mark194"></a>[^](#mark188)
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
		"""Set mask for the icon bitmap of this widget. Return the mask if None is given."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
### TextWindow<a name="mark195"></a>[^](#mark188)
**Provides the user a cancelable Scrolled Text window**

`no_destroy` can be set to `True` to allow the window to remain open after a submission is made. on_yes callback must take the text value as a String.
```py
class TextWindow(FocusedToplevel):
	def __init__(self, *args, text: str = 'Enter Text', on_yes: Callable = None, yes_text: str = 'Submit', on_cancel: Callable = None, cancel_text: str = 'Cancel', no_destroy: bool = False, focus: str = '', default: str = '', height: int = 32, width: int = 88, **kwargs):
		...
	def destroy(self) -> None:
		...
	def iconify(self):
		"""Display widget as icon."""
	def iconmask(self, bitmap=None):
		"""Set mask for the icon bitmap of this widget. Return the mask if None is given."""
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
## Misc Widgets<a name="mark196"></a>[^](#mark17)

### ToolTip<a name="mark197"></a>[^](#mark196)
**Easy ToolTip**

Easily show theme-friendly tooltip. Currently only left and right align are supported.
```py
class ToolTip(ToolTipBase):
	def __init__(self, parent: object, text: str, align: str = 'left'):
		...
```
### EasySizegrip<a name="mark198"></a>[^](#mark196)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
```
# SuperLib.utils<a name="mark199"></a>[^](#mark0)

## Utils<a name="mark200"></a>[^](#mark199)

### check_if_module_installed<a name="mark201"></a>[^](#mark200)
> **Indicates if a packages is installed. `Returns a Boolean`**
> 
```python
def check_if_module_installed(package: str) -> bool:
> 	...
```
### check_string_contains<a name="mark202"></a>[^](#mark200)
> **Returns `(True, char_index)` if any character from the list exists in the string otherwise returns `(False, None)`**
> 
```python
def check_string_contains(string: str, contains_list: tuple) -> tuple:
> 	...
```
### dummy_function<a name="mark203"></a>[^](#mark200)
> **Dummy function that nicely prints out any passed args and kwargs. `Returns True`**
> 
```python
def dummy_function(*args, **kwargs) -> bool:
> 	...
```
### get_friendly_time<a name="mark204"></a>[^](#mark200)
> **Gets a time string in one of several modes. Modes: `all, time, date, nice_date`. `Returns a String`**
> 
```python
def get_friendly_time(timestamp, mode: str = 'all') -> str:
> 	...
```
### get_unix_timestamp<a name="mark205"></a>[^](#mark200)
> **Get a unix timestamp. `Returns a Float`**
> 
```python
def get_unix_timestamp() -> float:
> 	...
```
### get_unix_timestring<a name="mark206"></a>[^](#mark200)
> **Get a unix timestring. `Returns a String`**
> 
```python
def get_unix_timestring() -> str:
> 	...
```
### get_user_home_folder<a name="mark207"></a>[^](#mark200)
> **Cross-platform function to get a user's home folder**
> 
```python
def get_user_home_folder() -> str:
> 	...
```
### open_folder_in_explorer<a name="mark208"></a>[^](#mark200)
> **Cross-platform way to open a folder in the default file manager for a system**
> 
```python
def open_folder_in_explorer(path) -> None:
> 	...
```
### sort_dict_by_keys<a name="mark209"></a>[^](#mark200)
> **Sorts a dictionary by its keys**
> 
```python
def sort_dict_by_keys(source: dict, reverse: bool = False) -> collections.OrderedDict:
> 	...
```
### timer_decorator<a name="mark210"></a>[^](#mark200)
> **Decorator to add timing to a function**
> 
```python
def timer_decorator(func: Callable) -> None:
> 	...
```
## File Generators<a name="mark211"></a>[^](#mark199)

### HTML_Generator<a name="mark212"></a>[^](#mark211)
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
### TXT_Generator<a name="mark213"></a>[^](#mark211)
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
### MD_Generator<a name="mark214"></a>[^](#mark211)
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
## History Mixin<a name="mark215"></a>[^](#mark199)

### HistoryMixin<a name="mark216"></a>[^](#mark215)
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
## Color Functions<a name="mark217"></a>[^](#mark199)

### reduce_255<a name="mark218"></a>[^](#mark217)
> **Limits a val to a range of 0 to 255**
> 
```python
def reduce_255(in_value: int, maxval: int = 255) -> int:
> 	...
```
### rgb_to_hex<a name="mark219"></a>[^](#mark217)
> **Converts an rgb tuple to hex**
> 
```python
def rgb_to_hex(rgb: tuple) -> str:
> 	...
```
### rgba_to_hex<a name="mark220"></a>[^](#mark217)
> **Converts an rgba tuple to rgba hex**
> 
```python
def rgba_to_hex(rgba: tuple) -> str:
> 	...
```
### hex_to_rgb<a name="mark221"></a>[^](#mark217)
> **Converts hex to rgb tuple**
> 
```python
def hex_to_rgb(hex: str) -> tuple:
> 	...
```
### hex_to_rgba<a name="mark222"></a>[^](#mark217)
> **Tries to convert rgba hex to rgba, on failure converts rgb hex to rgb and sets a full opacity**
> 
```python
def hex_to_rgba(hex: str) -> tuple:
> 	...
```
### get_gradient<a name="mark223"></a>[^](#mark217)
> **Generates a black / white gradient with a given number of steps**
> 
```python
def get_gradient(steps: int) -> tuple:
> 	...
```
### rgb_to_scalar<a name="mark224"></a>[^](#mark217)
> **Converts an rgb itterable to scalar list**
> 
```python
def rgb_to_scalar(rgb: tuple) -> tuple:
> 	...
```
### scalar_to_rgb<a name="mark225"></a>[^](#mark217)
> **Converts rgb scalar to rgb list**
> 
```python
def scalar_to_rgb(rgb: tuple) -> tuple:
> 	...
```
### linear_gradient<a name="mark226"></a>[^](#mark217)
> **Generates a linear gradient between two colors, accepts html hex or rgb formats**
> 
```python
def linear_gradient(start_hex: str = '#000000', finish_hex: str = '#FFFFFF', n: int = 10) -> list:
> 	...
```
### get_rainbow<a name="mark227"></a>[^](#mark217)
> **Generates a rainbow with a given number of steps. Steps must be divisible by 4)**
> 
```python
def get_rainbow(steps: int) -> tuple:
> 	...
```
# MegaWidgets<a name="mark228"></a>[^](#mark0)

## Notes MegaWidget<a name="mark229"></a>[^](#mark228)

### NotesTab<a name="mark230"></a>[^](#mark229)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
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
## Conversation MegaWidget<a name="mark231"></a>[^](#mark228)

### ConversationsTab<a name="mark232"></a>[^](#mark231)
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
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
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
## Profile Management<a name="mark233"></a>[^](#mark228)

### ProfilesSystem<a name="mark234"></a>[^](#mark233)
```py
class ProfilesSystem(object):
	def __init__(self, select_profile_actions: list = [], refresh_profiles_actions: list = [], profiles_dir: str = 'C:\\Users\\arcti\\GitHub\\py_simple_ttk\\Profiles', handle_duplicates: bool = True):
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
	def create_profile(self, name: str) -> src.py_simple_ttk.utils.ProfilesSystem.UserProfile:
		"""Creates a profile with a given name. `Raises ValueError` if the profile name already exists. `Returns a UserProfile`"""
	def delete_profile(self, profile: src.py_simple_ttk.utils.ProfilesSystem.UserProfile) -> None:
		...
	def get_last_used_profile(self, profiles: list = None) -> src.py_simple_ttk.utils.ProfilesSystem.UserProfile:
		"""Returns the most recently accessed profile"""
	def get_profile_by_username(self, name: str) -> src.py_simple_ttk.utils.ProfilesSystem.UserProfile:
		...
	def get_profile_names(self) -> list:
		"""Returns an alphabetically sorted list of profile names"""
	def handle_duplicate_profile_names(self, name: str) -> None:
		"""Makes profile names unique if they have identical names. The most recently accessed profile (according to the file json) keeps its name untouched. `Returns None`"""
	def handle_refresh_profiles_actions(self) -> None:
		"""Handle on-refresh-profiles actions"""
	def handle_select_profile_actions(self) -> None:
		"""Handle on-profile-selection actions"""
	def select_profile(self, profile: src.py_simple_ttk.utils.ProfilesSystem.UserProfile) -> None:
		"""Change the currently selected profile"""
	def select_profile_by_username(self, name: str) -> None:
		...
	def sort_profiles_by_accessed(self, profiles: list = None) -> None:
		"""Sort a list of profiles by last accessed, if no list is provided returns a sorted list of all profiles in the system. `Returns a List`"""
```
### UserProfile<a name="mark235"></a>[^](#mark233)
**A class to represent a User / User's Preferences**

Must pass a unique username and a unique identifier for new profile.
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
### get_profiles_folder<a name="mark236"></a>[^](#mark235)
> **Gets the absolute path to the included profiles folder. `Returns a String`**
> 
```python
def get_profiles_folder() -> str:
> 	...
```
### get_profiles_list<a name="mark237"></a>[^](#mark235)
> **Gets a list of profile files at a given path. `Returns a List of Path strings`**
> 
```python
def get_profiles_list(path: str = './Profiles', verbose: bool = False) -> list:
> 	...
```
# PIL-Only Widgets and Functions<a name="mark238"></a>[^](#mark0)

py_simple_ttk has a number of widgets and functions only available when PIL is installed. By default, installing py_simple_ttk through pip does *NOT* install PIL. py_simple_ttk provides a method to check if PIL is available at runtime: `from py_simple_ttk import PILLOW_AVAILABLE` To enable PIL-only widgets run `pip install PIL`, when creating your own modules that use py_simple_ttk as a dependency ensure you add PIL to your project's requirements.txt / pyproject.toml file


## PIL-Only Widgets<a name="mark239"></a>[^](#mark0)

### GifLoader<a name="mark240"></a>[^](#mark239)
```py
class GifLoader(object):
	def __init__(self, path: str, defer_load: bool = False):
		...
	def load_tk_frames(self) -> None:
		"""Called during instantiation unless defer_load was set to False"""
```
### GifViewer<a name="mark241"></a>[^](#mark239)
```py
class GifViewer(Frame):
	def __init__(self, loader: src.py_simple_ttk.pillow_widgets.GifLoader.GifLoader, *args, **kwargs):
		...
	def destroy(self):
		"""Destroy this and all descendants widgets."""
	def display_loop(self) -> None:
		...
	def info_patchlevel(self):
		"""Returns the exact version of the Tcl library."""
	def set_delay(self, fps) -> None:
		...
```
## PIL-Only Functions<a name="mark242"></a>[^](#mark0)

### convert_image_to_blackandwhite<a name="mark243"></a>[^](#mark242)
> **Converts an image to black and white**
> 
```python
def convert_image_to_blackandwhite(image: PIL.Image.Image) -> PIL.Image.Image:
> 	...
```
### convert_image_to_grayscale<a name="mark244"></a>[^](#mark242)
> **Converts a PIL image to grayscale**
> 
```python
def convert_image_to_grayscale(image: PIL.Image.Image) -> PIL.Image.Image:
> 	...
```
### load_image_from_byte_array<a name="mark245"></a>[^](#mark242)
> **Converts a png encoded in bytes to a PIL Image**
> 
```python
def load_image_from_byte_array(byte_array: bytes) -> PIL.Image.Image:
> 	...
```
### load_tk_image_from_bytes_array<a name="mark246"></a>[^](#mark242)
> **Loads a png encoded in bytes to an image tkinter can process**
> 
```python
def load_tk_image_from_bytes_array(bytes_array: bytes) -> PIL.ImageTk.PhotoImage:
> 	...
```
### make_checkerboard<a name="mark247"></a>[^](#mark242)
> **Function to make a background checkerboard for displaying images on**
> 
```python
def make_checkerboard(width: int, height: int, repeat: int = 14, color_1: tuple = (127, 127, 127, 255), color_2: tuple = (64, 64, 64, 255)) -> PIL.Image.Image:
> 	...
```
# Changelog<a name="mark248"></a>[^](#mark0)

## 0.2.9<a name="mark249"></a>[^](#mark248)

Add more scroller imports to toplevel namespace

## 0.2.8<a name="mark250"></a>[^](#mark248)

Add get_scaling and bind_mousewheel to toplevel namespace import. Fix theme defaulting to winnative to fix unix system crash when theme not configured in ini.json

## 0.2.7<a name="mark251"></a>[^](#mark248)

Fix missing ImageDraw import in ImageCore.py

## 0.2.6<a name="mark252"></a>[^](#mark248)

Add more functions to pillow_widgets/ImageCore.py and cleaned up typehinting, added pillow widgets to readme

## 0.2.5<a name="mark253"></a>[^](#mark248)

Add utils/tcl_commands.py with tcl_bell, tcl_center_window, and tcl_choose_font functions

## 0.2.4<a name="mark254"></a>[^](#mark248)

Use recursive import on asset folders to fix ALL missing assets.

## 0.2.3<a name="mark255"></a>[^](#mark248)

Fix missing theme and font assets

## 0.2.2<a name="mark256"></a>[^](#mark248)

Fix readme, remove pkg_resources in favor of importlib

## 0.2.1<a name="mark257"></a>[^](#mark248)

Fix pkg_resources dependency

## 0.2.0<a name="mark258"></a>[^](#mark248)

Restructure for better pep compliance, breaks some imports.

## 0.1.42<a name="mark259"></a>[^](#mark248)

Add <<Modified>> custom event to ScrolledText

## 0.1.41<a name="mark260"></a>[^](#mark248)

Add enable / disable to ActiveButton

## 0.1.40<a name="mark261"></a>[^](#mark248)

Fix bug with TextWindow

## 0.1.39<a name="mark262"></a>[^](#mark248)

Add TextWindow to ToplevelWidgets.py

## 0.1.38<a name="mark263"></a>[^](#mark248)

Add 16px python icons to assets

## 0.1.37<a name="mark264"></a>[^](#mark248)

Multi-Widgets packing can be customized through multiwidget.add() kwargs

## 0.1.36<a name="mark265"></a>[^](#mark248)

More improvements to the font system, added font tab to test.py

## 0.1.35<a name="mark266"></a>[^](#mark248)

Added more label styles

## 0.1.34<a name="mark267"></a>[^](#mark248)

Add init option to disable default notebook. Add function to make config file from dict (for testing, parent applications launching apps with custom args, etc.). Add handling when no ini width / height specified. Added ListManipulator widget.

## 0.1.33<a name="mark268"></a>[^](#mark248)

Fix labeled checkbutton packing

## 0.1.32<a name="mark269"></a>[^](#mark248)

Cleanup

## 0.1.31<a name="mark270"></a>[^](#mark248)

Add ActiveLabel and LabeledValue, add image_encoder.py and list_compare.py to demos

## 0.1.30<a name="mark271"></a>[^](#mark248)

Cleanup, bug fixes, add HamburgerFrame

## 0.1.29<a name="mark272"></a>[^](#mark248)

Move TicTacToe to examples

## 0.1.28<a name="mark273"></a>[^](#mark248)

Move SuperWidgetMixin from WidgetsCore.py to SuperWidget.py

## 0.1.27<a name="mark274"></a>[^](#mark248)

Add ActiveButton, ActiveCheckButton, ActiveComboBox, ActiveEntry, ActiveOptionMenu, ActiveProgressbar, ActiveRadioButton, ActiveScale, ColumnFrame, CycleButton, LabeledButton, LabeledMultiButton, LabeledCycleButton, LabeledMultiCycleButton, LabeledMultiRadioTable, LabeledMultiSimpleRadioTable, LabeledRadioTable, LabeledSimpleRadioTable, RadioTable, SimpleRadioTable, Remove: LabeledRadioButton, LabeledMultiRadioButton

## 0.1.26<a name="mark275"></a>[^](#mark248)

Add Spinbox widgets, fix Copybox

## 0.1.25<a name="mark276"></a>[^](#mark248)

Reduce packaged fonts color pallete

## 0.1.24<a name="mark277"></a>[^](#mark248)

Update readme generator with more config keys, fix ini readme md code block being marked as python

## 0.1.23<a name="mark278"></a>[^](#mark248)

Add columns to Configurable Launcher

## 0.1.22<a name="mark279"></a>[^](#mark248)

Fix readme

## 0.1.21<a name="mark280"></a>[^](#mark248)

Fix readme

## 0.1.20<a name="mark281"></a>[^](#mark248)

Add counter widget.

## 0.1.19<a name="mark282"></a>[^](#mark248)

Add dynamic launcher system.

## 0.1.18<a name="mark283"></a>[^](#mark248)

Add Ordered Listbox, add more bindings to SuperWidget, cleanup

## 0.1.17<a name="mark284"></a>[^](#mark248)

Add set_desktop_background to WidgetsCore.py

## 0.1.16<a name="mark285"></a>[^](#mark248)

Add needs_white_text to color.py, add pyinstaller compatibility to WidgetsCore.get_asset

## 0.1.15<a name="mark286"></a>[^](#mark248)

Fix misnamed function in color.py

## 0.1.14<a name="mark287"></a>[^](#mark248)

Fix missing import in app.py

## 0.1.13<a name="mark288"></a>[^](#mark248)

reduced variety of packaged font images, fixed bug with constrained widgets command not triggering

## 0.1.12<a name="mark289"></a>[^](#mark248)

Add Constrained + Labeled + Multi Entries (>35 widgets)

## 0.1.11<a name="mark290"></a>[^](#mark248)

Fix LabeledPathEntry error when no dialog type was specified

## 0.1.10<a name="mark291"></a>[^](#mark248)

Add LabeledPathEntry to EntryWidgets.py

## 0.1.9<a name="mark292"></a>[^](#mark248)

Add pencil icons to assets

## 0.1.8<a name="mark293"></a>[^](#mark248)

Fix labeled button not running command on press

## 0.1.7<a name="mark294"></a>[^](#mark248)

add labeled button

## 0.1.6<a name="mark295"></a>[^](#mark248)

Fix missing Labeler import

## 0.1.5<a name="mark296"></a>[^](#mark248)

Fix broken package

## 0.1.4<a name="mark297"></a>[^](#mark248)

Fix broken package

## 0.1.3<a name="mark298"></a>[^](#mark248)

More cleanup, input fixes.py

## 0.1.2<a name="mark299"></a>[^](#mark248)

Cleanup, move type lists to generate_readme.py

## 0.1.1<a name="mark300"></a>[^](#mark248)

Fix missing 'ListWindow' import in app.py

## 0.1.0<a name="mark301"></a>[^](#mark248)

Modulize



Generated with [py_simple_readme](https://github.com/AndrewSpangler/py_simple_readme)