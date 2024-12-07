style vpgrid_scrollbar is vscrollbar:
    xsize 24
    ysize 617
    xalign 0.91
    yalign 0.65
    base_bar "images/scrollbar/settings_scrollbar.png"
    thumb "images/scrollbar/ScrollBarThumb.png"

screen history_screen():

    tag menu

    modal True

    ## Avoid predicting this screen, as it can be very large.
    predict False
  
    frame:
        style_prefix "history"
        add ("images/settings_screen/history/history.png")
        background Transform("images/settings_screen/history/HistoryBG.png", alpha=0.0)

        imagebutton:
            xpos 1670 ypos 78
            auto "images/settings_screen/default_button/Back_%s.png"
            action Return(), Notify("BackButton Pressed")
            hover_sound "hover.mp3"

        vpgrid id "history_vpgrid":
            xsize 1450
            ysize 720
            xpos 130
            ypos 300
            cols 1
            draggable True
            mousewheel True

            for h in _history_list:

                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if h.who:

                        label h.who:
                            style "history_name"
                            substitute False

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

            if not _history_list:
                label _("The dialogue history is empty.")

    vbar:
        value YScrollValue("history_vpgrid")
        style "vpgrid_scrollbar" # Use the custom scrollbar style