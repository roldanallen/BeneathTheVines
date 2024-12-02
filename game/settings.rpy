style custom_volume_slider:
    xsize 1083  # Width of the slider (match your bar image width)
    ysize 48    # Height of the slider

    # Images for the slider
    base_bar Frame("images/settings_screen/music/slider_bar1.png")  # Background image
    thumb "images/settings_screen/music/slider_thumb.png"  # Movable thumb image

style vscrollbar1 is vscrollbar:
    xsize 24
    ysize 617
    xpos 1510
    base_bar "images/scrollbar/Scrollbar.png"
    thumb "images/scrollbar/ScrollBarThumb.png"

style text_slider:
    xsize 1023
    ysize 48
    base_bar "images/settings_screen/text/TextSlider.png"
    thumb "images/settings_screen/text/TSThumb.png"
#screen save_prompt():

screen screen_setting():
    zorder 100
    modal True
    add "images/settings_screen/display/Background_settings.png"

    # Back Button
    imagebutton:
        xpos 1712 ypos 110
        idle "images/settings_screen/default_button/Back_idle.png"
        action Hide("screen_setting", transition=dissolve), Notify("BackButton Pressed") 

    # Reset Button
    imagebutton:
        xpos 1714 ypos 963
        idle "images/settings_screen/default_button/Reset_idle.png"
        action Notify("Reset Pressed"), Function(reset_defaults)

    frame:
        xysize (1450, 720)
        xpos 235
        ypos 230
        background None

        viewport id "settings_viewport":
            #draggable True
            mousewheel True
            child_size(0, 1400)
            
            add "images/settings_screen/display/Display.png" xpos 69 ypos 35
            add "images/settings_screen/music/Audio.png" xpos 65 ypos 240
            add "images/settings_screen/skip/SkipText.png" xpos 65 ypos 850
            add "images/settings_screen/text/Text.png" xpos 65 ypos 1010

            imagebutton:
                xpos 234 ypos 125
                idle "images/settings_screen/display/Windowed_idle.png"
                action Notify("WindowedButton Pressed"), Preference("display", "window")

            imagebutton:
                xpos 604 ypos 125
                idle "images/settings_screen/display/Fscreen_idle.png"
                action Notify("FscreenButton Pressed"), Preference("display", "fullscreen")

            imagebutton:
                xpos 65 ypos 655
                idle "images/settings_screen/mute_button/MuteSoundOn_idle.png"
                action Notify("MuteButton Pressed")

            imagebutton:
                xpos 258 ypos 930
                idle "images/settings_screen/skip/UnseenText.png"
                action Preference("skip", "toggle"), Notify("SkipText Pressed")

            imagebutton:
                xpos 619 ypos 930
                idle "images/settings_screen/skip/AfterChoices.png"
                action Preference("after choices", "toggle"), Notify("SkipText Pressed")

            imagebutton:
                xpos 1019 ypos 930
                idle "images/settings_screen/skip/Transitions.png"
                action Notify("Transitions Pressed"), InvertSelected(Preference("transitions", "toggle"))

            bar:
                value Preference("music volume") # Binds slider to music volume
                style "custom_volume_slider"  # Apply the custom style
                xpos 230
                ypos 300

            bar:
                value Preference("sound volume") # Binds slider to music volume
                style "custom_volume_slider"  # Apply the custom style
                xpos 230
                ypos 430

            bar:
                value Preference("voice volume") # Binds slider to music volume
                style "custom_volume_slider"  # Apply the custom style
                xpos 230
                ypos 560

            bar:
                value Preference("text speed")# Binds slider to music volume
                style "text_slider"  # Apply the custom style
                xpos 210
                ypos 1100

            bar:
                value Preference("auto-forward time") # Binds slider to music volume
                style "text_slider"  # Apply the custom style
                xpos 210
                ypos 1260

            python:
                current_music_volume = preferences.get_volume("music")
                current_sound_volume = preferences.get_volume("sfx")
                current_system_volume = preferences.get_volume("voice")
                current_skip_text = preferences.skip_unseen
                current_after_text = preferences.skip_after_choices
                current_transitions = preferences.transitions
                current_fullscreen = preferences.fullscreen

            if current_music_volume == 0.0:
                add "images/settings_screen/music/VolumeMute1.png" xpos 1337 ypos 300
            else:
                add "images/settings_screen/music/VolumeMax1.png" xpos 1337 ypos 300

            # Check for sound volume
            if current_sound_volume == 0.0:
                add "images/settings_screen/music/VolumeMute1.png" xpos 1337 ypos 430
            else:
                add "images/settings_screen/music/VolumeMax1.png" xpos 1337 ypos 430
            # Check for system volume
            if current_system_volume == 0.0:
                add "images/settings_screen/music/VolumeMute1.png" xpos 1337 ypos 560
            else:
                add "images/settings_screen/music/VolumeMax1.png" xpos 1337 ypos 560

            if current_skip_text == True:
                add "images/settings_screen/skip/Indicator.png" xpos 500 ypos 942  # Reset state image

            if current_after_text == True:
                add "images/settings_screen/skip/Indicator.png" xpos 900 ypos 942

            if current_transitions == 2:
                add "images/settings_screen/skip/Indicator.png" xpos 1250 ypos 942
            
            if current_fullscreen == True:
                add "images/settings_screen/display/Indicator.png" xpos 853 ypos 138
            else:
                add "images/settings_screen/display/Indicator.png" xpos 469 ypos 138
            

                
                
        vbar:
            value YScrollValue("settings_viewport")
            style "vscrollbar1" # Use the custom scrollbar style

# Python function to reset preferences
init python:
    def reset_defaults():
        preferences.text_cps = config.default_text_cps
        preferences.afm_time = config.default_afm_time
        preferences.afm_enable = config.default_afm_enable
        preferences.set_volume('sfx', 0.7)
        preferences.set_volume('music', 0.7)
        preferences.set_volume('voice', 0.7)
        preferences.skip_unseen = False 
        preferences.skip_after_choices = False
        preferences.transitions = 2
        
        # Rerender the screen to reflect changes immediately
        renpy.restart_interaction()
