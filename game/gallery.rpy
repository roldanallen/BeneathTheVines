init python:
    g = Gallery()

    g.button("1")
    g.condition("persistent.blue_unlocked")
    g.transition = dissolve
    g.image("images/prologue/scene 2/Scene2.png") 
    g.unlock_image("imagesnew/Gallery/image1_unlocked.png")

    g.button("2")
    g.condition("persistent.blue_unlocked")

    g.button("3")
    g.condition("persistent.blue_unlocked")

    g.button("4")
    g.condition("persistent.blue_unlocked")

default current_gallery = "chapter1"

screen album:
    modal True
    #tag menu

    add "images/gallery_screen/Gallery.png"

    if current_gallery == "chapter1":
        add "images/gallery_screen/Chapter1.png" xpos 1550 ypos 135
    elif current_gallery == "chapter2":
        add "images/gallery_screen/Chapter2.png" xpos 1550 ypos 135
    elif current_gallery == "chapter3":
        add "images/gallery_screen/Chapter3.png" xpos 1550 ypos 135
    elif current_gallery == "chapter4":
        add "images/gallery_screen/Chapter4.png" xpos 1550 ypos 135
    elif current_gallery == "chapter5":
        add "images/gallery_screen/Chapter5.png" xpos 1550 ypos 135


    imagebutton:
        xpos 136
        ypos 936
        auto "images/gallery_screen/Return_%s.png"
        action Notify("Return pressed"), Hide("album", transition=dissolve)
        hover_sound "hover.mp3"
        #activate_sound "clicked.mp3"

    imagebutton:
        xpos 75
        ypos 300
        auto "images/gallery_screen/Chapter1_%s.png"
        action SetVariable("current_gallery", "chapter1")
        hover_sound "hover.mp3"
        #activate_sound "clicked.mp3"

    imagebutton:
        xpos 75
        ypos 400
        idle ConditionSwitch(
            "persistent.chapter2_unlock", "images/gallery_screen/Chapter2_idle.png",
            "not persistent.chapter2_unlock", "images/gallery_screen/Chapter2_locked_idle.png")
        hover ConditionSwitch(
            "persistent.chapter2_unlock", "images/gallery_screen/Chapter2_hover.png",
            "not persistent.chapter2_unlock", "images/gallery_screen/Chapter2_locked_idle.png")

        if persistent.chapter2_unlock:
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"
            action [SetVariable("current_gallery", "chapter2")]
        
        else:
            activate_sound "error.mp3"
            action Show("chapterlock")

    imagebutton:
        xpos 75
        ypos 500
        idle ConditionSwitch(
            "persistent.chapter3_unlock", "images/gallery_screen/Chapter3_idle.png",
            "not persistent.chapter3_unlock", "images/gallery_screen/Chapter3_locked_idle.png")
        hover ConditionSwitch(
            "persistent.chapter3_unlock", "images/gallery_screen/Chapter3_hover.png",
            "not persistent.chapter3_unlock", "images/gallery_screen/Chapter3_locked_idle.png")

        if persistent.chapter3_unlock:
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"
            action [SetVariable("current_gallery", "chapter3")]
        
        else:
            activate_sound "error.mp3"
            action Show("chapterlock")

    imagebutton:
        xpos 75
        ypos 600
        idle ConditionSwitch(
            "persistent.chapter4_unlock", "images/gallery_screen/Chapter4_idle.png",
            "not persistent.chapter4_unlock", "images/gallery_screen/Chapter4_locked_idle.png")
        hover ConditionSwitch(
            "persistent.chapter4_unlock", "images/gallery_screen/Chapter4_hover.png",
            "not persistent.chapter4_unlock", "images/gallery_screen/Chapter4_locked_idle.png")

        if persistent.chapter4_unlock:
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"
            action [SetVariable("current_gallery", "chapter4")]
        
        else:
            activate_sound "error.mp3"
            action Show("chapterlock")

    imagebutton:
        xpos 75
        ypos 700
        idle ConditionSwitch(
            "persistent.chapter5_unlock", "images/gallery_screen/Chapter5_idle.png",
            "not persistent.chapter5_unlock", "images/gallery_screen/Chapter5_locked_idle.png")
        hover ConditionSwitch(
            "persistent.chapter5_unlock", "images/gallery_screen/Chapter5_hover.png",
            "not persistent.chapter5_unlock", "images/gallery_screen/Chapter5_locked_idle.png")

        if persistent.chapter5_unlock:
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"
            action [SetVariable("current_gallery", "chapter5")]
        
        else:
            activate_sound "error.mp3"
            action Show("chapterlock")

                
    
    if current_gallery == "chapter1":
        frame:
            xsize 1260
            ysize 737
            xpos 530
            ypos 236
            background None
        
            viewport:
                draggable True
                mousewheel True
                child_size(0, 1080)

                add g.make_button(name="1", unlocked = "images/prologue/scene 2/gal.png", locked = "images/gallery_screen/image_locked.png") xpos 130 ypos 60
                add g.make_button(name="2", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 680 ypos 60
                add g.make_button(name="3", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 130 ypos 420
                add g.make_button(name="4", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 680 ypos 420


    elif current_gallery == "chapter2":
        frame:
            xsize 1260
            ysize 737
            xpos 530
            ypos 236
            background None

            viewport:
                draggable True
                mousewheel True
                child_size(0, 1200)

                add g.make_button(name="1", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 130 ypos 60
                add g.make_button(name="2", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 680 ypos 60
                add g.make_button(name="3", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 130 ypos 420
                add g.make_button(name="4", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 680 ypos 420
            

    elif current_gallery == "chapter3":
        frame:
            xsize 1260
            ysize 737
            xpos 530
            ypos 236
            background None

            viewport:
                draggable True
                mousewheel True
                child_size(0, 1200)

                add g.make_button(name="1", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 130 ypos 60
                add g.make_button(name="2", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 680 ypos 60
                add g.make_button(name="3", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 130 ypos 420
                add g.make_button(name="4", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 680 ypos 420
        
    elif current_gallery == "chapter4":
        frame:
            xsize 1260
            ysize 737
            xpos 530
            ypos 236
            background None

            viewport:
                draggable True
                mousewheel True
                child_size(0, 1200)

                add g.make_button(name="1", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 130 ypos 60
                add g.make_button(name="2", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 680 ypos 60
                add g.make_button(name="3", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 130 ypos 420
                add g.make_button(name="4", unlocked = "images/gallery_screen/image_Frame.png", locked = "images/gallery_screen/image_locked.png") xpos 680 ypos 420
        
