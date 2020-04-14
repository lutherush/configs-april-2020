##### IMPORTS #####
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

##### DEFINING SOME VARIABLES #####
mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "st"                                    # My terminal of choice
myConfig = "/home/lutherus/.config/qtile/config.py"    # The Qtile config file location

##### KEYBINDINGS #####
keys = [
         ### The essentials
         Key(
             [mod], "Return",
             lazy.spawn(myTerm)                      # Open terminal
             ),
         Key(
             [mod], "v",              # Dmenu Run Launcher
             lazy.spawn("dmenu_run -p 'Run: '")
             ),
         Key(
             [mod], "Tab",
             lazy.next_layout()                      # Toggle through layouts
             ),
         Key(
             [mod, "shift"], "c",
             lazy.window.kill()                      # Kill active window
             ),
         Key(
             [mod, "shift"], "r",
             lazy.restart()                          # Restart Qtile
             ),
         Key(
             [mod, "shift"], "q",
             lazy.shutdown()                         # Shutdown Qtile
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0)                       # Keyboard focus to screen(0)
             ),
         Key([mod], "e",
             lazy.to_screen(1)                       # Keyboard focus to screen(1)
             ),
         Key([mod], "r",
             lazy.to_screen(2)                       # Keyboard focus to screen(2)
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen()                      # Move monitor focus to next screen
             ),
         Key([mod], "comma",
             lazy.prev_screen()                      # Move monitor focus to prev screen
             ),
         ### Treetab controls
         Key([mod, "control"], "k",
             lazy.layout.section_up()                # Move up a section in treetab
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down()              # Move down a section in treetab
             ),
         ### Window controls
         Key(
             [mod], "k",
             lazy.layout.down()                      # Switch between windows in current stack pane
             ),
         Key(
             [mod], "j",
             lazy.layout.up()                        # Switch between windows in current stack pane
             ),
         Key(
             [mod, "shift"], "k",
             lazy.layout.shuffle_down()              # Move windows down in current stack
             ),
         Key(
             [mod, "shift"], "j",
             lazy.layout.shuffle_up()                # Move windows up in current stack
             ),
         Key(
             [mod], "h",
             lazy.layout.grow(),                     # Grow size of current window (XmonadTall)
             lazy.layout.increase_nmaster(),         # Increase number in master pane (Tile)
             ),
         Key(
             [mod], "l",
             lazy.layout.shrink(),                   # Shrink size of current window (XmonadTall)
             lazy.layout.decrease_nmaster(),         # Decrease number in master pane (Tile)
             ),
         Key(
             [mod], "n",
             lazy.layout.normalize()                 # Restore all windows to default size ratios 
             ),
         Key(
             [mod], "m",
             lazy.layout.maximize()                  # Toggle a window between minimum and maximum sizes
             ),
         Key(
             [mod, "shift"], "f",
             lazy.window.toggle_floating()           # Toggle floating
             ),
         ### Stack controls
         Key(
             [mod, "shift"], "space",
             lazy.layout.rotate(),                   # Swap panes of split stack (Stack)
             lazy.layout.flip()                      # Switch which side main pane occupies (XmonadTall)
             ),
         Key(
             [mod], "space",
             lazy.layout.next()                      # Switch window focus to other pane(s) of stack
             ),
         Key(
             [mod, "control"], "Return",
             lazy.layout.toggle_split()              # Toggle between split and unsplit sides of stack
             ),
         ### Dmenu scripts launched with ALT + CTRL + KEY
         Key(
             ["mod1", "control"], "e",
             lazy.spawn("./.dmenu/dmenu-edit-configs.sh")
             ),
         Key(
             ["mod1", "control"], "m",
             lazy.spawn("./.dmenu/dmenu-sysmon.sh")
             ),
         Key(
             ["mod1", "control"], "p",
             lazy.spawn("passmenu")
             ),
         Key(
             ["mod1", "control"], "r",
             lazy.spawn("./.dmenu/dmenu-reddio.sh")
             ),
         Key(
             ["mod1", "control"], "s",
             lazy.spawn("./.dmenu/dmenu-surfraw.sh")
             ),
         Key(
             ["mod1", "control"], "t",
             lazy.spawn("./.dmenu/dmenu-trading.sh")
             ),
         Key(
             ["mod1", "control"], "i",
             lazy.spawn("./.dmenu/dmenu-scrot.sh")
             ),
         ### My applications launched with SUPER + ALT + KEY
         Key(
             [mod, "mod1"], "l",
             lazy.spawn(myTerm+" -e w3m lutherush.github.io")
             ),
         Key(
             [mod, "mod1"], "n",
             lazy.spawn(myTerm+" -e newsboat")
             ),
         Key(
             [mod, "mod1"], "r",
             lazy.spawn(myTerm+" -e rtv")
             ),
]

##### GROUPS #####
group_names = [("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               (" ", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group	

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "2e3440",
                "border_normal": "1D2330"
                }

##### THE LAYOUTS #####
layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
     layout.Floating(**layout_theme)
]

##### COLORS #####
colors = [["#434c5e", "#434c5e"], # panel background
          ["#4c566a", "#4c566a"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#4c566a", "#4c566a"], # border line color for other tab and odd widgets
          ["#5e81ac", "#5e81ac"], # color for the even widgets
          ["#e5e9f0", "#e5e9f0"]] # window name

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####

def init_widgets_list():
    widgets_list = [
               widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.GroupBox(font="Ubuntu Bold",
                        fontsize = 9,
                        margin_y = 1,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[3],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.Prompt(
                        prompt=prompt,
                        font="Ubuntu Mono",
                        padding=10,
                        foreground = colors[3],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 40,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.WindowName(
                        foreground = colors[6],
                        background = colors[0],
                        padding = 0
                        ),
               widget.TextBox(
                        text='',
                        background = colors[0],
                        foreground = colors[4],
                        padding=0,
                        fontsize=37
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=37
                        ),
               widget.TextBox(
                        text=" 🌡",
                        padding = 2,
                        foreground=colors[2],
                        background=colors[5],
                        fontsize=11
                        ),
               widget.ThermalSensor(
                        foreground=colors[2],
                        background=colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=0,
                        fontsize=37
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=37
                        ),
               widget.TextBox(
                        text=" 🖬",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 0,
                        fontsize=14
                        ),
               widget.Memory(
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=0,
                        fontsize=37
                        ),
               widget.Net(
                        interface = "wlp3s0",
                        foreground = colors[2],
                        background = colors[4],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=37
                        ),
               widget.TextBox(
                       text=" Vol:",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 0
                        ),
               widget.Volume(
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=0,
                        fontsize=37
                        ),
               widget.CurrentLayoutIcon(
                        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                        foreground = colors[0],
                        background = colors[4],
                        padding = 0,
                        scale=0.7
                        ),
               widget.CurrentLayout(
                        foreground = colors[2],
                        background = colors[4],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=37
                        ),
               widget.Clock(
                        foreground = colors[2],
                        background = colors[5],
                        format="%A, %B %d - [ %H:%M ]"
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[0],
                        background = colors[5]
                        ),
               widget.Systray(
                        background=colors[0],
                        padding = 5
                        ),
              ]
    return widgets_list

##### SCREENS ##### (TRIPLE MONITOR SETUP)

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.95, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

