define ivy = Character("Ivy", color="#ffff")
define anna = Character("Anna", color="#a118a1ff")
define andre = Character("Andre")
define unknown = Character("Unknown Voice")
#define background_ch2s1 = ("images/characters/bgch1_s1.png")

image Unknown Voice:
    "shadow.png"

image Ivy smile:
    "images/character_sprite/Ivy/3-4view/ivy_3 smile.png"

image Ivy bashful:
    "images/character_sprite/Ivy/3-4view/ivy_3 bashful.png"

image Ivy lipsmile:
   "images/character_sprite/Ivy/3-4view/ivy_3 lipsmile.png"

image Ivy laugh:
   "images/character_sprite/Ivy/3-4view/ivy_3 laugh.png"

image Ivy serious:
    "images/character_sprite/Ivy/3-4view/ivy_3 serious.png"

image Anna smile1:
    "images/character_sprite/Anna/anna_3 smile1.png"

image Anna smile2:
    "images/character_sprite/Anna/anna_3 smile2.png"

image Anna laugh:
    "images/character_sprite/Anna/anna_3 laugh.png"

image Anna serious: 
    "images/character_sprite/Anna/anna_3 serious.png"


image blinking:
    "flashlight.png"
    pause 2.0
    "flashlight_bk.png" with dissolve
    pause 1.0
    "flashlight.png" with dissolve
    pause 0.5
    repeat
