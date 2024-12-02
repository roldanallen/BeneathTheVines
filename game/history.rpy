style vpgrid_scrollbar is vscrollbar:
    xsize 24
    ysize 617
    xalign 0.91
    yalign 0.5
    base_bar "images/scrollBar/Scrollbar.png"
    thumb "images/scrollBar/ScrollBarThumb.png"

screen history_screen():

    tag menu

    modal True

    ## Avoid predicting this screen, as it can be very large.
    predict False
  
    frame:
        style_prefix "history"
        add ("images/settings_screen/history/frame.png")
        background Transform("images/settings_screen/history/HistoryBG.png", alpha=0.7)

        imagebutton:
            xpos 1670 ypos 90
            idle "images/settings_screen/history/Back_idle.png"
            action Return(), Notify("BackButton Pressed") 

        vpgrid id "history_vpgrid":
            xsize 1450
            ysize 720
            xpos 130
            ypos 235
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