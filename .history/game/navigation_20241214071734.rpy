init python:
     config.game_menu_action = [ShowMenu("gamepause")]

screen gamepause():
    #zorder 100
    modal True
    key "game_menu" action Return()

    add "images/navigation/navigation.png"
    
    imagebutton:
        xpos 136
        ypos 880
        auto "images/navigation/Return_%s.png"
        hover_sound "hover.mp3"
        #activate_sound "clicked.mp3"  
        action Return()

    imagebutton:
        xpos 136
        ypos 395
        auto "images/navigation/Settings_%s.png"
        hover_sound "hover.mp3"
        #activate_sound "clicked.mp3"  
        action Show("screen_setting", transition=dissolve)

    imagebutton:
        xpos 136
        ypos 665
        auto "images/navigation/MainMenu_%s.png"
        hover_sound "hover.mp3"
        #activate_sound "clicked.mp3"  
        action Show("confirm_prompt")

    imagebutton:
        xpos 136
        ypos 485
        auto "images/navigation/Gallery_%s.png"
        hover_sound "hover.mp3"
        #activate_sound "clicked.mp3"  
        action Show("album", transition=dissolve)
    #imagebutton:
    #    xpos 136
    #    ypos 340
    #    auto "images/navigation/StoryChapter_%s.png"
    #    action SetVariable("show_return_buttom", "navigation"), ShowMenu("chapter")
    
    if main_menu:
        
        imagebutton:
            xpos 136
            ypos 880
            auto "images/navigation/Return_%s.png"
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"  
            action Hide("gamepause", transition=dissolve)
        
        imagebutton:
            xpos 136
            ypos 485
            auto "images/navigation/Gallery_%s.png"
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"  
            action Show("album", transition=dissolve)
        
        imagebutton:
            xpos 136
            ypos 575
            auto "images/navigation/Load_%s.png"
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"  
            #action Hide("gamepause", transition=dissolve), Show("save")
            action Show("load", transition=dissolve)
        
    else:
        imagebutton:
            xpos 136
            ypos 575
            auto "images/navigation/Save_%s.png"
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"  
            action Show("save", transition=dissolve)



    