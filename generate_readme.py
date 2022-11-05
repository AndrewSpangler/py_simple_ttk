import json

from py_simple_readme import readme_generator
from py_simple_ttk import *


CORE_FUNCTIONS = [
    bbox_to_width_and_height,
    center_window,
    check_in_bounds,
    complex_widget_search,
    copy_to_user_clipboard,
    create_round_rectangle,
    default_pack,
    default_separator,
    default_vertical_pack,
    default_vertical_separator,
    enable_notebook_movement,
    focus_next,
    force_aspect,
    get_asset,
    get_bundled_themes_list,
    get_generated_font_images_lookup,
    get_local_appdata_folder,
    get_themes_folder,
    open_link,
    recursive_widget_search,
    run_cl,
]
CORE_OBJECTS = [MultiWidgetMixin, SuperWidgetMixin]

TEXT_WIDGETS = [ScrolledText, CopyBox]
TABS = [
    Tab,
    LauncherTab,
    BrowserLauncherTab,
    CommandLauncherTab,
    ConsoleTab,
    TableTab,
    TreeTableTab,
]
SCALE_WIDGETS = [LabeledScale, LabeledMultiScale]
RADIOBUTTON_WIDGETS = [LabeledRadiobutton, LabeledMultiRadiobutton]
PROGRESSBAR_WIDGETS = [LabeledProgressbar, LabeledMultiProgressbar]
OPTIONMENU_WIDGETS = [LabeledOptionMenu, LabeledMultiOptionMenu]
LISTBOX_WIDGETS = [ScrolledListBox, OrderedListbox, Table]
KEYPAD_WIDGETS = [KeypadButton, BaseKeypad, DialerKeypad]
ENTRY_WIDGETS = [
    ScrolledEntry,
    LabeledEntry,
    LabeledMultiEntry,
    LabeledButtonEntry,
    LabeledMultiButtonEntry,
    LabeledPathEntry,
    PasswordEntry,
]
CONSTRAINEDENTRY_WIDGETS = [
    ConstrainedEntry,
    LabeledConstrainedEntry,
    IntEntry,
    LabeledIntEntry,
    LabeledMultiIntEntry,
    FloatEntry,
    LabeledFloatEntry,
    LabeledMultiFloatEntry,
    LowercaseEntry,
    LabeledLowercaseEntry,
    LabeledMultiLowercaseEntry,
    UppercaseEntry,
    LabeledUppercaseEntry,
    LabeledMultiUppercaseEntry,
    LettersEntry,
    LabeledLettersEntry,
    LabeledMultiLettersEntry,
    DigitsEntry,
    LabeledDigitsEntry,
    LabeledMultiDigitsEntry,
    UppercaseDigitsEntry,
    LabeledUppercaseDigitsEntry,
    LabeledMultiUppercaseDigitsEntry,
    LowercaseDigitsEntry,
    LabeledLowercaseDigitsEntry,
    LabeledMultiLowercaseDigitsEntry,
    LettersDigitsEntry,
    LabeledLettersDigitsEntry,
    LabeledMultiLettersDigitsEntry,
    HexdigitsEntry,
    LabeledHexdigitsEntry,
    LabeledMultiHexdigitsEntry,
    OctdigitsEntry,
    LabeledOctdigitsEntry,
    LabeledMultiOctdigitsEntry,
    PrintableEntry,
    LabeledPrintableEntry,
    LabeledMultiPrintableEntry,
]
CONSTRAINEDENTRY_FUNCTIONS = [
    check_entry_type,
    check_entry_int,
    check_entry_float,
    check_entry_contents,
    check_entry_ascii_lowercase,
    check_entry_ascii_uppercase,
    check_entry_ascii_letters,
    check_entry_ascii_digits,
    check_entry_ascii_uppercase_digits,
    check_entry_ascii_lowercase_digits,
    check_entry_ascii_hexdigits,
    check_entry_ascii_octdigits,
    check_entry_ascii_letters_digits,
    check_entry_ascii_printable,
]
CONSOLE_WIDGETS = [ConsoleWidget]
COMBOBOX_WIDGETS = [LabeledCombobox, LabeledMultiCombobox]
CHECKBUTTON_WIDGETS = [LabeledCheckbutton, LabeledMultiCheckbutton]
CANVAS_WIDGETS = [ResizableCanvas, ScrolledCanvas, TiledCanvas, ExampleTile]
TOPLEVEL_WIDGETS = [
    FocusedToplevel,
    NoticeWindow,
    YesNoCancelWindow,
    PromptWindow,
    PasswordWindow,
    ListWindow,
]

MEGA_WIDGETS = [ConversationsTab, NotesTab, ConfigurableLauncher, LauncherTools]
UTILS = [
    check_if_module_installed,
    check_string_contains,
    dummy_function,
    get_friendly_time,
    get_installed_packages,
    get_unix_timestamp,
    get_unix_timestring,
    get_user_home_folder,
    open_folder_in_explorer,
    sort_dict_by_keys,
    timer_decorator,
]
FILE_GENERATORS = [
    HTML_Generator,
    TXT_Generator,
    MD_Generator,
]
MISC_WIDGETS = [ToolTip, EasySizegrip]
ZIP_FUNCTIONS = [
    package_folder,
    get_package_file,
    get_package_manifest,
    get_package_manifest_json,
]
COLOR_FUNCTIONS = [
    reduce_255,
    rgb_to_hex,
    rgba_to_hex,
    hex_to_rgb,
    hex_to_rgba,
    get_gradient,
    rgb_to_scalar,
    scalar_to_rgb,
    linear_gradient,
    get_rainbow,
]
PROFILES_OBJECTS = [
    ProfilesSystem,
    UserProfile,
]
PROFILES_FUNCTIONS = [
    get_profiles_folder,
    get_profiles_list,
]
LABELER_OBJECTS = [Labeler]
BUTTON_WIDGETS = [LabeledButton]

# fmt: off
IGNORED_METHODS = ["addtag","addtag_above","addtag_all","addtag_below","addtag_closest","addtag_enclosed","addtag_overlapping","addtag_withtag","after","after_cancel","after_idle","anchor","aspect","attributes","bbox","bell","bind","bind_all","bind_class","bindtags","canvasx","canvasy","cget","client","clipboard_append","clipboard_clear","clipboard_get","colormapwindows","columnconfigure","command","compare","config","configure","coords","count","current","dchars","debug","deiconify","delete","deletecommand","dlineinfo","dtag","dump","edit","edit_modified","edit_redo","edit_reset","edit_separator","edit_und","event_add","event_delete","event_generate","event_info","find","find_above","find_all","find_below","find_closest","find_enclosed","find_overlapping","find_withtag","focus","focus_displayof","focus_force","focus_get","focus_lastfor","focus_set","focusmodel","forget","frame","geometry","getboolean","getdouble","getint","gettags","getvar","grab_current","grab_release","grab_set","grab_set_global","grab_status","grid","grid_anchor","grid_bbox","grid_columnconfigure","grid_configure","grid_forget","grid_info","grid_location","grid_propagate","grid_remove","grid_rowconfigure","grid_size","grid_slaves","group","iconbitmap","iconify""iconmask","iconname","iconphoto","iconposition","iconwindow","icursor","identify","image_cget","image_configure","image_create","image_names","image_types","index","info","insert","instate","invoke","itemcget","itemconfig","itemconfigure","keys","lift","location","lower","mainloop","manage","mark_gravity","mark_names","mark_next","mark_previous","mark_set","mark_unset","maxsize","minsize","move","moveto","moveto","nametowidget","nearest","option_add","option_clear","option_get","option_readfile","overrideredirect","pack","pack_configure","pack_forget","pack_info","pack_propagate","pack_slaves","peer_create","peer_names","place","place_configure","place_forget","place_info","place_slaves","positionfrom","postscript","propagate","protocol","quit","register","replace","resizable","rowconfigure","scale","scan_dragto","scan_mark","search","see","select_adjust","select_anchor","select_clear","select_from","select_includes","select_item","select_present","select_range","select_set","select_to","selection_adjust","selection_anchor","selection_clear","selection_clear","selection_from","selection_get","selection_handle","selection_includes","selection_own","selection_own_get","selection_present","selection_range","selection_set","selection_to","send","set_cursor","set_label_text","setvar","size","sizefrom","slaves","state","tag_add","tag_bind","tag_bing","tag_cget","tag_config","tag_configure","tag_delete","tag_lower","tag_names","tag_nextrange","tag_prevrange","tag_raise","tag_ranges","tag_remove","tag_unbind","title","tk_bisque","tk_focusFollowsMouse","tk_focusNext","tk_focusPrev","tk_setPalette","tk_strictMotif","tkraise","transient","type","unbind","unbind_all","unbind_class","update","update_idletasks","validate","wait_variable","wait_visibility","wait_window","waitvar","window_cget","window_config","window_configure","window_names","winfo_atom","winfo_atomname","winfo_cells","winfo_children","winfo_class","winfo_colormapfull","winfo_containing","winfo_depth","winfo_exists","winfo_fpixels","winfo_geometry","winfo_height","winfo_id","winfo_interps","winfo_ismapped","winfo_manager","winfo_name","winfo_parent","winfo_pathname","winfo_pixels","winfo_pointerx","winfo_pointerxy","winfo_pointery","winfo_reqheight","winfo_reqwidth","winfo_rgb","winfo_rootx","winfo_rooty","winfo_screen","winfo_screencells","winfo_screendepth","winfo_screenheight","winfo_screenmmheight","winfo_screenmmwidth","winfo_screenvisual","winfo_screenwidth","winfo_server","winfo_toplevel","winfo_viewable","winfo_visual","winfo_visualid","winfo_visualsavailable","winfo_vrootheight","winfo_vrootwidth","winfo_vrootx","winfo_vrooty","winfo_width","winfo_x","winfo_y","withdraw","wm_aspect","wm_attributes","wm_client","wm_colormapwindows","wm_command","wm_deiconify","wm_focusmode","wm_focusmodel","wm_forget","wm_frame","wm_geometry","wm_grid","wm_group","wm_iconbitmap","wm_iconify","wm_iconmask","wm_iconname","wm_iconphoto","wm_iconposition","wm_iconwindow","wm_manage","wm_maxsize","wm_minsize","wm_overrideredirect","wm_positionfrom","wm_protocol","wm_resizable","wm_sizefrom","wm_state","wm_title","wm_transient","wm_withdraw","xview","xview_moveto","xview_scroll","yview","yview_moveto","yview_pickplace","yview_scroll"]
# fmt: on

slogan = "Themes don't have to be hard."

about_text = """py_simple_ttk exists because I got tired of rewriting the same code over \
and over for simple projects. The goal is to provide a variety of meta widgets with \
consistent get/set/enable/disable/destroy methods and mega-widgets that make ttk \
development easier and faster. Features include built-in theme support, a score of \
labeled and multi-widgets, tools for easy form building, a sample application \
demonstrating many of py_simple_ttk's features, a configuration file system, and much more. \
![Lines of code](https://img.shields.io/tokei/lines/github/AndrewSpangler/py_simple_ttk)"""

requirements_text = ""

ini_conf = """
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
| enable_profiles    | Enable a User Profiles System             |
+--------------------+-------------------------------------------+
""".strip()


def generate_readme(tables: dict, changelog: dict):
    name = tables["project"]["name"]
    version = tables["project"]["version"]
    gen = readme_generator(
        title=f"{name} {version}", slogan=slogan, ignored=IGNORED_METHODS
    )
    gen.set_changelog(changelog)
    gen.add_heading_1("About", add_toc=True)
    gen.add_paragraph(about_text)
    gen.add_heading_1("Requirements", add_toc=True)
    gen.add_paragraph(requirements_text)
    gen.add_heading_1("Configuring ini.json", add_toc=True)
    gen.add_code_block(ini_conf)
    gen.add_heading_1("Widgets", add_toc=True)
    gen.increase_toc_depth()
    gen.add_heading_2("Button Widgets", add_toc=True)
    gen.handle_class_list(BUTTON_WIDGETS)
    gen.add_heading_2("Core Functions", add_toc=True)
    gen.handle_function_list(CORE_FUNCTIONS, show_submodule=True)
    gen.add_heading_2("Core Widgets", add_toc=True)
    gen.handle_class_list(CORE_OBJECTS, show_submodule=True)
    gen.add_heading_2("Tabs", add_toc=True)
    gen.handle_class_list(TABS, show_submodule=True)
    gen.add_heading_2("Canvas Widgets", add_toc=True)
    gen.handle_class_list(CANVAS_WIDGETS, show_submodule=True)
    gen.add_heading_2("Checkbutton Widgets", add_toc=True)
    gen.handle_class_list(CHECKBUTTON_WIDGETS, show_submodule=True)
    gen.add_heading_2("Combobox Widgets", add_toc=True)
    gen.handle_class_list(COMBOBOX_WIDGETS, show_submodule=True)
    gen.add_heading_2("Console Widgets", add_toc=True)
    gen.handle_class_list(CONSOLE_WIDGETS, show_submodule=True)
    gen.add_heading_2("Constraining Functions", add_toc=True)
    gen.handle_function_list(CONSTRAINEDENTRY_FUNCTIONS)
    gen.add_heading_2("Entry Widgets", add_toc=True)
    ENTRY_WIDGETS.extend(CONSTRAINEDENTRY_WIDGETS)
    gen.handle_class_list(ENTRY_WIDGETS, show_submodule=True)
    gen.add_heading_2("KeyPad Widgets", add_toc=True)
    gen.handle_class_list(KEYPAD_WIDGETS, show_submodule=True)
    gen.add_heading_2("Labeler Widget", add_toc=True)
    gen.handle_class_list(BUTTON_WIDGETS)
    gen.add_heading_2("ListBox Widgets", add_toc=True)
    gen.handle_class_list(LISTBOX_WIDGETS, show_submodule=True)
    gen.add_heading_2("OptionMenu Widgets", add_toc=True)
    gen.handle_class_list(OPTIONMENU_WIDGETS, show_submodule=True)
    gen.add_heading_2("ProgressBar Widgets", add_toc=True)
    gen.handle_class_list(PROGRESSBAR_WIDGETS, show_submodule=True)
    gen.add_heading_2("Radiobutton Widgets", add_toc=True)
    gen.handle_class_list(RADIOBUTTON_WIDGETS, show_submodule=True)
    gen.add_heading_2("Scale Widgets", add_toc=True)
    gen.handle_class_list(SCALE_WIDGETS, show_submodule=True)
    gen.add_heading_2("Text Widgets", add_toc=True)
    gen.handle_class_list(TEXT_WIDGETS, show_submodule=True)
    gen.add_heading_2("Toplevel Widgets", add_toc=True)
    gen.handle_class_list(TOPLEVEL_WIDGETS, show_submodule=True)
    gen.add_heading_2("Misc Widgets", add_toc=True)
    gen.handle_class_list(MISC_WIDGETS, show_submodule=True)
    gen.decrease_toc_depth()
    gen.add_heading_1("SuperLib.utils", add_toc=True)
    gen.increase_toc_depth()
    gen.add_heading_2("Utils", add_toc=True)
    gen.handle_function_list(UTILS, show_submodule=True)
    gen.add_heading_2("File Generators", add_toc=True)
    gen.handle_class_list(FILE_GENERATORS, show_submodule=True)
    gen.add_heading_2("History Mixin", add_toc=True)
    gen.handle_class_list([HistoryMixin], show_submodule=True)
    gen.add_heading_2("Color Functions", add_toc=True)
    gen.handle_function_list(COLOR_FUNCTIONS, show_submodule=True)
    gen.decrease_toc_depth()
    gen.add_heading_1("MegaWidgets", add_toc=True)
    gen.increase_toc_depth()
    gen.add_heading_2("Notes MegaWidget", add_toc=True)
    gen.handle_class_list([NotesTab], show_submodule=True)
    gen.add_heading_2("Conversation MegaWidget", add_toc=True)
    gen.handle_class_list([ConversationsTab], show_submodule=True)
    gen.add_heading_2("Profile Management", add_toc=True)
    gen.handle_class_list(PROFILES_OBJECTS, show_submodule=True)
    gen.handle_function_list(PROFILES_FUNCTIONS, show_submodule=True)
    gen.decrease_toc_depth()
    return gen.assemble()
