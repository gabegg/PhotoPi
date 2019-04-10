"""
Constants for the program

.. py:data:: SCREEN_H,SCREEN_W
    Dimensions in pixels of the screen attached (will be used to compute layout)
.. py:data:: EFFECT_PARAMETERS
    A dict of dict data structure to tune acquisition parameters for each snap effct
.. py:data:: SOFTWARE_BUTTONS
    A dict of dict data structure to tune software buttons (in case of no hardware buttons)
.. py:data:: HARDWARE_BUTTONS
    configuration of the hardware buttons' GPIO pins, pull_up_down state and active state
.. py:data:: EMAIL_BUTTON_IMG  
    'send_email' button icon
.. py:data:: OAUTH2_REFRESH_PERIOD
    interval between two OAuth2 token refresh (ms)
.. py:data:: HARDWARE_POLL_PERIOD = 100
    polling interval to detect hardware buttons change (ms)

.. py:data:: CONFIGURATION_FILE
    name of the configuration file (relative to scripts/ directory)
.. py:data:: APP_ID_FILE
    name of the 'application_secret' file downloaded from console.developers.google.com (relative to scripts/ directory)
.. py:data:: CREDENTIALS_STORE_FILE
    name of the automaticaly generated credentials store (relative to scripts/ directory)

"""
import os

# Obsolete: This will be autodetected at runtime
SCREEN_W = 800 ## raspi touch
SCREEN_H = 480 ## raspi touch

# Parameters for the three main effects
# None: simple shot
# Four: Collage of four shots
# Animation : animated gif
v2_full_size = (3280,2464)
v2_half_size = (1640,1232)
v2_quarter_size = (820,616)

v1_full_size = (2592,1944)
v1_half_size = (1296,972)
v1_quarter_size = (648,486)

EFFECTS_PARAMETERS = {
    "None": {
        'snap_size' : v2_full_size, #(width, height) => preferably use integer division of camera resolution
        'logo_size' : 128,         # height in pixels of the logo (will be thumbnailed to this size)
        'logo_padding' : 32        # bottom and right padding of the logo (pixels)
    },
    "Four": { 
        'snap_size' : v2_half_size,                       #(width, height) of each shots of the 2x2 collage
        'foreground_image' : "collage_four_square.png" # Overlay image on top of the collage
    },
    "Animation": {
        'snap_size' : (500, 500),   
        'frame_number' : 10,        
        'snap_period_millis' : 200, 
        'gif_period_millis' : 50    
    }
}


SOFTWARE_BUTTONS = {
    "None": {
        "icon" : os.path.join("ressources","ic_photo.png")
        },
    "Four": {
        "icon" : os.path.join("ressources","ic_portrait.png")
        },
    "Animation": {
        "icon" : os.path.join("ressources","ic_anim.png")
        }
}


EFFECTS_THUMB_DIR = os.path.join("ressources","effects")
IMAGE_EFFECTS_LIST = [
    "none",
    "colorswap1",
    "colorswap0",
    "negative",

    "oilpaint",
    "pastel",
    "gpen",
    "sketch",

    "cartoon",
    "posterise",
    "watercolor1",
    "colorpoint1"
]

IMAGE_EFFECTS = {
    "none": {
        "effect_name":"none",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_none.png")
    },
   
    "solarize": { 
        "effect_name":"solarize",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_solarize.png")
    },
    "oilpaint": {
        "effect_name":"oilpaint",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_oilpaint.png")
    },
    "cartoon": {
        "effect_name":"cartoon",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_cartoon.png")
    },
    "colorswap0": {
        "effect_name":"colorswap",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_colorswap.png"),
        "effect_params" : 0 # green faces
    },
    "colorswap1": {
        "effect_name":"colorswap",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_colorswap1.png"),
        "effect_params" : 1  # purple faces
    },
    "negative": {
        "effect_name":"negative",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_negative.png")
    },
    "pastel": {
        "effect_name":"pastel",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_pastel.png")
    },
    "posterise": {
        "effect_name":"posterise",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_posterise.png"),
        "effect_params" : 8
    },
    "gpen": {
        "effect_name":"gpen",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_gpen.png")
    },
    "sketch": {
        "effect_name":"sketch",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_sketch.png")
    },
    "watercolor1": {
        "effect_name" : "watercolor",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_watercolor_170_25.png"),
        "effect_params" : (170,25) # cyan
    },
    "colorpoint1": {
        "effect_name" : "colorpoint",
        "effect_icon": os.path.join(EFFECTS_THUMB_DIR,"eff_colorpoint1.png"),
        "effect_params" : 1 
    }
}


HARDWARE_BUTTONS = {
    "button_pins": [10,8,12], 
    "pull_up_down": "pull_down",        
    "active_state": 1        
}


ACTIONS_KEYS_MAPPING = {
    "snap_None": ["s","S","<F1>"],
    "snap_Four": ["f","F","<F2>"],
    "snap_Animation": ["a","A","<F3>"],
    "send_email":["e","@"],
    "configure":["<Escape>"]
    
}


COUNTDOWN_OVERLAY_IMAGES=[
    os.path.join("ressources","count_down_1.png"),
    os.path.join("ressources","count_down_2.png"),
    os.path.join("ressources","count_down_3.png"),
    os.path.join("ressources","count_down_4.png"),
    os.path.join("ressources","count_down_5.png"),
    os.path.join("ressources","count_down_ready.png")]
# this defines the height ratio of the countdown images wrt. the preview size
COUNTDOWN_IMAGE_MAX_HEIGHT_RATIO = 0.2 #[0. - 1.] range

# Path to button icon ressources
EMAIL_BUTTON_IMG  = os.path.join("ressources","ic_email.png")
PRINT_BUTTON_IMG  = os.path.join("ressources","ic_print.png")
EFFECTS_BUTTON_IMG = os.path.join("ressources","ic_effects.png")


OAUTH2_REFRESH_PERIOD = 1800000 # interval between two OAuth2 token refresh (ms)


HARDWARE_POLL_PERIOD = 100


CONFIGURATION_FILE = "configuration.json"
APP_ID_FILE        = "google_client_id.json"
CREDENTIALS_STORE_FILE = "google_credentials.dat"
EMAILS_LOG_FILE = os.path.join("..","sendmail.log") 
