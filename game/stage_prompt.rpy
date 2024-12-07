# Initialize variables
default show_overlay = False
default current_stage_prompt = None  # Variable to hold the current stage prompt image
default target_label = None  # Variable to hold the target label for Jump

# Define the overlay screen
screen overlay_screen():
    modal True  # Makes this screen modal, blocking clicks outside of it
    
    if show_overlay and current_stage_prompt:  # Check if there's a prompt to show
        add current_stage_prompt at delayed_appearance align (0.5, 0.5)

        # Play button
        imagebutton:
            auto "images/chapter_screen/scene_prompt/play_button_%s.png"
            action [Hide("overlay_screen"), SetVariable("show_overlay", False), Start(target_label)]  # Jump to the target label
            at delayed_appearance
            hover_sound "hover.mp3"
            xpos 975
            ypos 615

        # Close button within the overlay screen
        imagebutton:
            auto "images/chapter_screen/scene_prompt/back_button_%s.png"
            action [Hide("overlay_screen", transition=dissolve), SetVariable("show_overlay", False)]
            at delayed_appearance
            hover_sound "hover.mp3"
            xpos 1550
            ypos 370  # Adjust position as needed

screen scenelock():
    modal True
    add "images/prompt_screen/scene_lock.png" xalign 0.5 yalign 0.5 at chapter_lock
    timer 0.7 action Hide("scenelock", transition=dissolve)

screen chapterlock():
    modal True
    add "images/prompt_screen/chapter_lock.png" xalign 0.5 yalign 0.5 at chapter_lock
    timer 0.7 action Hide("chapterlock", transition=dissolve)

screen reset_confirmed():
    modal True
    add "images/prompt_screen/reset_confirm.png" xalign 0.5 yalign 0.5 at chapter_lock
    timer 1.0 action Hide("reset_confirmed", transition=dissolve)

screen black_screen():
    modal True
    add "images/prompt_screen/black_screen.png"
    timer 0.3 action Hide("black_screen", transition=dissolve)

screen confirm_prompt():
    modal True
    add "images/prompt_screen/confirm_prompt.png"

    imagebutton:
        xpos 826
        ypos 580
        auto "images/prompt_screen/yes1_%s.png"
        hover_sound "hover.mp3"
        action Function(layer_unlock), Show("main_menu"), Hide("gamepause", transition=dissolve), Hide("confirm_prompt")

    imagebutton:
        xpos 1046
        ypos 580
        hover_sound "hover.mp3"
        auto "images/prompt_screen/no1_%s.png"
        action Hide("confirm_prompt")

screen confirm_reset():
    modal True
    add "images/prompt_screen/reset_prompt.png"

    imagebutton:
        xpos 826
        ypos 580
        auto "images/prompt_screen/yes1_%s.png"
        hover_sound "hover.mp3"
        action Function(reset_defaults), Hide("confirm_reset"), Show("reset_confirmed")

    imagebutton:
        xpos 1046
        ypos 580
        hover_sound "hover.mp3"
        auto "images/prompt_screen/no1_%s.png"
        action Hide("confirm_reset")


transform chapter_lock:
    alpha 0.0
    linear 0.1 alpha 1.0
    linear 0.05 alpha 0.0
    linear 0.1 alpha 1.0

transform delayed_appearance:
    alpha 0.0
    linear 0.2 alpha 0.0   # Start invisible
    linear 0.3 alpha 1.0  # Fade in effect

transform delayed_image:
    alpha 0.0
    linear 2.0 alpha 0.0
    linear 0.5 alpha 1.0