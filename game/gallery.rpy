#init python:
    #gallery = Gallery()

    #gallery.button("red") 
    #gallery.unlock_image("imagesnew/Gallery/CG_red") 

    #gallery.button("blue") 
    #gallery.image("imagesnew/Gallery/CG_blue")
    #gallery.condition("persistent.blue_unlocked") 

    #gallery.button("green_and_orange")
    #gallery.unlock_image("CG_green")
    #gallery.unlock_image("CG_orange") 

    #gallery.button("green_and_orange2") 
    #gallery.condition("persistent.green_unlocked and persistent.orange_unlocked") 
    #gallery.image("imagesnew/Gallery/CG_green")
    #gallery.image("imagesnew/Gallery/CG_orange") 
    #gallery.image("imagesnew/Gallery/CG_pink") 
    #gallery.condition("persistent.pink_unlocked") 

init python:
    g = Gallery()

    g.button("1")
    g.condition("persistent.blue_unlocked")
    g.transition = dissolve
    g.image("images/gallery_screen/epitaph.jpg") 
    #g.unlock_image("imagesnew/Gallery/image1_unlocked.png")

    g.button("2")
    g.condition("persistent.blue_unlocked")

    g.button("3")
    g.condition("persistent.blue_unlocked")

    g.button("4")
    g.condition("persistent.blue_unlocked")

screen album:
    tag menu

    frame:
        xsize 1720
        ysize 800
        align (0.5, 0.5)
        #background None

        vpgrid:
            cols 2
            vscrollbar_xoffset 400
            viewport_xsize 800
            mousewheel True
            scrollbars "vertical"
            xalign 0.5
            yalign 0.5

            add g.make_button(name="1", unlocked = "images/gallery_screen/image1_unlocked.png", locked = "images/gallery_screen/Locked.png")
            add g.make_button(name="2", unlocked = "images/gallery_screen/image1_unlocked.png", locked = "images/gallery_screen/Locked.png")
            add g.make_button(name="3", unlocked = "images/gallery_screen/image1_unlocked.png", locked = "images/gallery_screen/Locked.png")
            add g.make_button(name="4", unlocked = "images/gallery_screen/image1_unlocked.png", locked = "images/gallery_screen/Locked.png")
            add g.make_button(name="1", unlocked = "images/gallery_screen/image1_unlocked.png", locked = "images/gallery_screen/Locked.png")
            add g.make_button(name="2", unlocked = "images/gallery_screen/image1_unlocked.png", locked = "images/gallery_screen/Locked.png")
            add g.make_button(name="3", unlocked = "images/gallery_screen/image1_unlocked.png", locked = "images/gallery_screen/Locked.png")
            add g.make_button(name="4", unlocked = "images/gallery_screen/image1_unlocked.png", locked = "images/gallery_screen/Locked.png")

            yspacing 30
            xspacing 30

        #vbar:
            #xalign 1.0
            #yalign 0.5
            #value YScrollValue("gallery")
            #style "vscrollbar1" # Use the custom scrollbar style


    textbutton "Return" action Return()