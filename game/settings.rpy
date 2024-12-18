
style custom_volume_slider:
    xsize 1083  # Width of the slider (match your bar image width)
    ysize 42    # Height of the slider

    # Images for the slider
    base_bar "images/settings_screen/music/VolumeBar.png"  # Background image
    thumb "images/settings_screen/music/VolumeThumb.png"  # Movable thumb image

style vscrollbar1 is vscrollbar:
    xsize 24
    ysize 617
    xpos 1510
    base_bar "images/scrollbar/settings_scrollbar.png"
    thumb "images/scrollbar/ScrollBarThumb.png"

style text_slider:
    xsize 947
    ysize 48
    base_bar "images/settings_screen/text/TextSlider.png"
    thumb "images/settings_screen/text/TSThumb.png"
#screen save_prompt():

screen screen_setting():

    python:
        current_music_volume = preferences.get_volume("music")
        current_sound_volume = preferences.get_volume("sfx")
        current_system_volume = preferences.get_volume("voice")
        current_skip_text = preferences.skip_unseen
        current_after_text = preferences.skip_after_choices
        current_transitions = preferences.transitions
        current_fullscreen = preferences.fullscreen
        current_mute = preferences.set_mute
    #zorder 100
    modal True
    add "images/settings_screen/display/Background_settings.png"

    # Back Button
    imagebutton:
        xpos 1712 ypos 110
        auto "images/settings_screen/default_button/Back_%s.png"
        action Hide("screen_setting", transition=dissolve)#, Notify("BackButton Pressed") 
        hover_sound "hover.mp3"

    # Reset Button
    imagebutton:
        xpos 1714 ypos 963
        auto "images/settings_screen/default_button/Reset_%s.png"
        action Show("confirm_reset")
        hover_sound "hover.mp3"

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
            add "images/settings_screen/skip/Skip.png" xpos 65 ypos 850
            add "images/settings_screen/text/Text.png" xpos 65 ypos 1010

            imagebutton:
                xpos 234 ypos 125
                auto "images/settings_screen/display/Windowed_%s.png"
                action Preference("display", "window")#, Notify("WindowedButton Pressed")
                hover_sound "hover.mp3"

            imagebutton:
                xpos 604 ypos 125
                auto "images/settings_screen/display/Fscreen_%s.png"
                action Preference("display", "fullscreen")#,  Notify("FscreenButton Pressed")
                hover_sound "hover.mp3"

            imagebutton:
                xpos 65 ypos 655

                if preferences.get_mute('main'):
                    auto "images/settings_screen/mute_button/MuteSoundOff_%s.png"
                else:
                    auto "images/settings_screen/mute_button/MuteSoundOn_%s.png"
                action Preference("all mute", "toggle")
                hover_sound "hover.mp3"

            imagebutton:
                xpos 258 ypos 930
                auto "images/settings_screen/skip/UnseenText_%s.png"
                action Preference("skip", "toggle")#, Notify("SkipText Pressed")
                hover_sound "hover.mp3"

            imagebutton:
                xpos 619 ypos 930
                auto "images/settings_screen/skip/AfterChoices_%s.png"
                action Preference("after choices", "toggle")#, Notify("SkipText Pressed")
                hover_sound "hover.mp3"

            imagebutton:
                xpos 1019 ypos 930
                auto "images/settings_screen/skip/Transitions_%s.png"
                action InvertSelected(Preference("transitions", "toggle"))#, Notify("Transitions Pressed")
                hover_sound "hover.mp3"

            if not preferences.get_mute('main'):
                add "images/settings_screen/music/Audio.png" xpos 65 ypos 240
                bar:
                    value Preference("music volume") # Binds slider to music volume
                    style "custom_volume_slider"  # Apply the custom style
                    xpos 230
                    ypos 312

                bar:
                    value Preference("sound volume") # Binds slider to music volume
                    style "custom_volume_slider"  # Apply the custom style
                    xpos 230
                    ypos 442

                bar:
                    value Preference("voice volume") # Binds slider to music volume
                    style "custom_volume_slider"  # Apply the custom style
                    xpos 230
                    ypos 572
                
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

            else:
                add "images/settings_screen/music/music_muted.png" xpos 65 ypos 240

            bar:
                value Preference("text speed")# Binds slider to music volume
                style "text_slider"  # Apply the custom style
                xpos 244
                ypos 1100

            bar:
                value Preference("auto-forward time") # Binds slider to music volume
                style "text_slider"  # Apply the custom style
                xpos 244
                ypos 1260

            if current_skip_text == True:
                add "images/settings_screen/skip/Indicator.png" xpos 504 ypos 942  # Reset state image

            if current_after_text == True:
                add "images/settings_screen/skip/Indicator.png" xpos 904 ypos 942

            if current_transitions == 0:
                add "images/settings_screen/skip/Indicator.png" xpos 1258 ypos 942
            
            if current_fullscreen == True:
                add "images/settings_screen/display/Indicator.png" xpos 879 ypos 138
            else:
                add "images/settings_screen/display/Indicator.png" xpos 503 ypos 138                
                
        vbar:
            value YScrollValue("settings_viewport")
            style "vscrollbar1" # Use the custom scrollbar style

init python:
    def reset_defaults():
        preferences.text_cps = config.default_text_cps
        preferences.afm_time = config.default_afm_time
        preferences.afm_enable = config.default_afm_enable
        preferences.set_volume('sfx', 0.7)
        preferences.set_volume('music', 0.7)
        preferences.set_volume('voice', 0.7)
        preferences.skip_unseen = False 
        preferences.skip_after_choices = True
        preferences.transitions = 2
        preferences.set_mute("main", False)

        renpy.restart_interaction()
        
    def toggle_mute():
        # Toggle the mute state for all mixers
        renpy.run(Preference("all mute", "toggle"))
        # Restart interaction to update any UI changes
        renpy.restart_interaction()
        # Rerender the screen to reflect changes immediately

    def restart_screen():
        renpy.restart_interaction()