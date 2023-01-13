# Lily base config: https://github.com/KMKfw/kmk_firmware/blob/master/boards/lily58/main.py
# Base key reference: https://github.com/KMKfw/kmk_firmware/blob/a309aa52f3b09309aa989f92de3ccc3537b996c8/kmk/keys.py
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.modules.split import Split, SplitSide, SplitType
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
# oled
oled_ext = Oled(OledData(corner_one={0:OledReactionType.STATIC,1:["layer:"]},corner_two={0:OledReactionType.LAYER,1:["1","2","3","4","5","6","7","8"]},corner_three={0:OledReactionType.LAYER,1:["base","raise","lower","adjust","5","6","7","8"]},corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","shifted","leds","5","6","7","8"]}),toDisplay=OledDisplayMode.TXT,flip=False)
# oled
keyboard.extensions.append(oled_ext)
# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255]],split=True,rightSide=False,disable_auto_write=True)
# ledmap
keyboard.extensions.append(rgb_ext)
# KMK uses the final character in the name of the drive (luluL or luluR) to determine the side.
split = Split(use_pio=True)
keyboard.modules.append(split)

LOWER = KC.MO(1)
RAISE = KC.MO(2)
DLFT = KC.LCTL(KC.LEFT) # Desktop left
DRGT = KC.LCTL(KC.RIGHT) # Desktop right
# keymap
keyboard.keymap = [ 
        [# qwerty
            KC.TAB,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                     KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.GRAVE,
            KC.LALT, KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                      KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.MINUS,
            KC.ESC,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                      KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOTE,
            KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.TAB,  KC.RBRC, KC.N,    KC.M,    KC.COMM,  KC.DOT,  KC.SLSH, KC.RSFT, 
                                       LOWER,   KC.LCTL, KC.LGUI, KC.ENT  ,KC.SPC,  KC.BSPC, RAISE,   KC.RGUI
        ], 

        [ # lower
            KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,                     KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
            KC.TILD, KC.TRNS, KC.UP,   KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.PIPE, KC.EQUAL,KC.TRNS,
            KC.TRNS, KC.LEFT, KC.DOWN, KC.RIGHT,KC.TRNS, KC.TRNS,                   KC.LEFT, KC.UP,   KC.DOWN, KC.RIGHT,KC.TRNS, KC.TRNS,
            KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, DLFT,    KC.TRNS, KC.TRNS, DRGT,    KC.TRNS, KC.TRNS,
                                       KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.DEL,  KC.TRNS
        ], 

       [ # raise
           KC.N2,   KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC,                   KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.TILD, 
           KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.PLUS, KC.UNDS, 
           KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.COLN, KC.DQUO, KC.TRNS, KC.TRNS, 
           KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LCBR, KC.RCBR, KC.TRNS, KC.KP_1, KC.LABK, KC.RABK, KC.QUES, KC.TRNS, KC.LGUI, KC.TRNS,
                                      KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.RCBR, KC.RCBR, KC.RCBR 
       ], 

[KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS], 
[KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS], 
[KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS], 
[KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS], 
[KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS] ] 
# keymap
if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)
