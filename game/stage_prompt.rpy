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
            idle "images/chapter_screen/button2_idle.png"
            hover "images/chapter_screen/button2_hover.png"
            action [Hide("overlay_screen"), SetVariable("show_overlay", False), Jump(target_label)]  # Jump to the target label
            at delayed_appearance
            xpos 975
            ypos 615

        # Close button within the overlay screen
        imagebutton:
            idle "images/chapter_screen/arrow.png"
            action [Hide("overlay_screen"), SetVariable("show_overlay", False)]
            at delayed_appearance
            xpos 1550
            ypos 370  # Adjust position as needed

# Define the delayed appearance as a transform
transform delayed_appearance:
    alpha 0.0
    linear 0.2 alpha 0.0   # Start invisible
    linear 0.3 alpha 1.0  # Fade in effect

transform delayed_image:
    alpha 0.0
    linear 2.0 alpha 0.0
    linear 0.5 alpha 1.0