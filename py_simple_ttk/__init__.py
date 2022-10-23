from .widgets import (
    BaseKeypad,
    bbox_to_width_and_height,
    BrowserLauncherTab,
    center_window,
    check_in_bounds,
    CHECKBUTTON_WIDGETS,
    COMBOBOX_WIDGETS,
    CommandLauncherTab,
    complex_widget_search,
    CONSOLE_WIDGETS,
    ConsoleTab,
    ConsoleWidget,
    copy_to_user_clipboard,
    CopyBox,
    CORE_FUNCTIONS,
    CORE_OBJECTS,
    create_round_rectangle,
    default_pack,
    default_separator,
    default_vertical_pack,
    default_vertical_separator,
    DialerKeypad,
    EasySizegrip,
    enable_notebook_movement,
    ENTRY_WIDGETS,
    ExampleTile,
    FocusedToplevel,
    force_aspect,
    get_asset,
    get_bundled_themes_list,
    get_generated_font_image,
    get_generated_font_images_lookup,
    get_themes_folder,
    KEYPAD_WIDGETS,
    KeypadButton,
    LabeledButtonEntry,
    LabeledCheckbutton,
    LabeledCombobox,
    LabeledEntry,
    LabeledMultiButtonEntry,
    LabeledMultiCheckbutton,
    LabeledMultiCombobox,
    LabeledMultiEntry,
    LabeledMultiOptionMenu,
    LabeledMultiProgressbar,
    LabeledMultiRadiobutton,
    LabeledMultiScale,
    LabeledOptionMenu,
    LabeledProgressbar,
    LabeledRadiobutton,
    LabeledScale,
    LauncherTab,
    LISTBOX_WIDGETS,
    ListWindow,
    NoticeWindow,
    open_link,
    OPTIONMENU_WIDGETS,
    PasswordEntry,
    PasswordWindow,
    PROGRESSBAR_WIDGETS,
    PromptWindow,
    RADIOBUTTON_WIDGETS,
    recursive_widget_search,
    ResizableCanvas,
    run_cl,
    SCALE_WIDGETS,
    ScrolledCanvas,
    ScrolledListBox,
    ScrolledText,
    ScrolledTree,
    SuperWidgetMixin,
    Tab,
    Table,
    TableTab,
    TABS,
    TEXT_WIDGETS,
    TiledCanvas,
    ToolTip,
    TreeTable,
    TreeTableTab,
    WINDOWS_SYMBOL,
    YesNoCancelWindow,
)

from .utils.color import (
    reduce,
    rgb_to_hex,
    rgba_to_hex,
    hex_to_rgb,
    hex_to_rgba,
    get_gradient,
    rgb_to_scalar,
    scalar_to_rgb,
    linear_gradient,
    get_rainbow,
    COLOR_FUNCTIONS,
)

from .utils.HTML_Generator import HTML_Generator
from .utils.TXT_Generator import TXT_Generator
from .utils.MD_Generator import MD_Generator
from .utils.utils import (
    check_if_module_installed,
    check_string_contains,
    dummy_function,
    format_SI,
    get_friendly_modified_time,
    get_friendly_time,
    get_installed_packages,
    get_unix_timestamp,
    get_unix_timestring,
    get_user_home_folder,
    modify_filename,
    open_folder_in_explorer,
    sort_dict_by_keys,
    timer_decorator,
)
from .utils.History import HistoryMixin
from .utils.scaling import enable_dpi_awareness
from .utils.ProfilesSystem import (
    ProfilesSystem,
    UserProfile,
    get_profiles_folder,
    get_profiles_list,
    PROFILES_OBJECTS,
    PROFILES_FUNCTIONS,
)
from .mega_widgets.chat import ConversationsTab
from .mega_widgets.notes import NotesTab
from .mega_widgets.profile_manager import ProfilesWindow
from .mega_widgets.timecard_maker import TimecardTab, TimecardMaker
from .mega_widgets.wattage_calculator import WattageTab, WattageCalculator
from .mega_widgets.shopping_list import ShoppingListTab, ShoppingList
from .mega_widgets.tictactoe import TicTacToeTab, TicTacToe

from .app import App

CANVAS_WIDGETS = [ResizableCanvas, ScrolledCanvas, TiledCanvas, ExampleTile]
TOPLEVEL_WIDGETS = [
    FocusedToplevel,
    NoticeWindow,
    YesNoCancelWindow,
    PromptWindow,
    PasswordWindow,
    ListWindow,
]
MEGA_WIDGETS = [ConversationsTab, NotesTab]
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


if not check_if_module_installed("pillow"):
    PILLOW_AVAILABLE = False
    print("Pillow not detected, not importing pillow-only widgets")
else:
    PILLOW_AVAILABLE = True
    print("Pillow detected, importing pillow-only widgets")
    from .pillow_widgets.GifLoader import GifLoader, GifViewer
    from .pillow_widgets.ImageCore import load_tk_image_from_bytes_array
