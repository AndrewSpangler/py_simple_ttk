from .widgets import (
    BaseKeypad,
    bbox_to_width_and_height,
    BrowserLauncherTab,
    center_window,
    check_in_bounds,
    CommandLauncherTab,
    complex_widget_search,
    ConsoleTab,
    ConsoleWidget,
    copy_to_user_clipboard,
    CopyBox,
    create_round_rectangle,
    default_pack,
    default_separator,
    default_vertical_pack,
    default_vertical_separator,
    DialerKeypad,
    EasySizegrip,
    enable_notebook_movement,
    ExampleTile,
    focus_next,
    FocusedToplevel,
    force_aspect,
    get_asset,
    get_bundled_themes_list,
    get_generated_font_image,
    get_generated_font_images_lookup,
    get_local_appdata_folder,
    get_themes_folder,
    KeypadButton,
    LabeledButton,
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
    LabeledPathEntry,
    LabeledProgressbar,
    LabeledRadiobutton,
    LabeledScale,
    Labeler,
    LauncherTab,
    ListWindow,
    MultiWidgetMixin,
    NoticeWindow,
    open_link,
    PasswordEntry,
    PasswordWindow,
    PromptWindow,
    recursive_widget_search,
    ResizableCanvas,
    run_cl,
    ScrolledCanvas,
    ScrolledEntry,
    ScrolledListBox,
    ScrolledText,
    ScrolledTree,
    SuperWidgetMixin,
    Tab,
    Table,
    TableTab,
    TiledCanvas,
    ToolTip,
    TreeTable,
    TreeTableTab,
    YesNoCancelWindow,
)

from .utils.color import (
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
)
from .utils.zip_packager import (
    package_folder,
    get_package_file,
    get_package_manifest,
    get_package_manifest_json,
)

from .mega_widgets.chat import ConversationsTab
from .mega_widgets.notes import NotesTab
from .mega_widgets.profile_manager import ProfilesWindow
from .mega_widgets.timecard_maker import TimecardTab, TimecardMaker
from .mega_widgets.wattage_calculator import WattageTab, WattageCalculator
from .mega_widgets.shopping_list import ShoppingListTab, ShoppingList
from .mega_widgets.tictactoe import TicTacToeTab, TicTacToe

from .app import App


if not check_if_module_installed("pillow"):
    PILLOW_AVAILABLE = False
    print("Pillow not detected, not importing pillow-only widgets")
else:
    PILLOW_AVAILABLE = True
    print("Pillow detected, importing pillow-only widgets")
    from .pillow_widgets.GifLoader import GifLoader, GifViewer
    from .pillow_widgets.ImageCore import load_tk_image_from_bytes_array
