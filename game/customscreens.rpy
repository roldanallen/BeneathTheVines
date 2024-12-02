
# clickable doors
screen test():

    imagemap:
        
        auto "door_%s.png"
        hotspot (737, 379, 158, 514):
            if turns < 5:
                action [SetVariable("turns", turns + 1),SetVariable("events",If(events < 2, events +1 , 0)) , If(isUnlocked,movePlayer("room 1"), Function(renpy.call_in_new_context, "warning") )]
            else:
                action NullAction() 
        
        hotspot (1710, 168, 193, 694):
            if turns < 5:
                action [SetVariable("turns", turns + 1),SetVariable("events",If(events <=4, events +1 , 0)) ,movePlayer("room 2")]
            else:
                action NullAction() 

        hotspot (1282, 480, 166, 175):
            if turns < 5:
                action [SetVariable("turns", turns + 1),SetVariable("events",If(events <=4, events +1 ,0)) , movePlayer("room 3")]
            else:
                action NullAction() 
      
#return to previous room
screen returnbutton():
   
    imagebutton:
        focus_mask None
        xalign 0.0
        yalign 0.0
        yoffset 40
        xoffset 35
        auto "return_%s.png"
        
        if turns < 5:
            action [SetVariable("turns", turns + 1),SetVariable("events",If(events <=4, events + 1 , 0)) , movePlayer("hallway")]
        else:
            action NullAction()

#turn
screen turnstext():
    
    frame:
        textbutton ("Skip Turn") action [SetVariable("events",If(events <=4, events + 1, 0)), movePlayer(location_user, isSkip =True)]

        xalign 1.0
    
    frame:
        text "Turns: [turns] / 5"
        xalign 0.9
    frame:
        text "Event: [events]"

    #frame:
        #text "The Stranger is in the [location_stranger]"
        #xalign 1.5



screen inventory():
    
    modal True
    imagemap:
        
        auto "inventory_%s.png" 
        
        hotspot(179, 143, 88, 95) action Jump("start")

        hotspot(179, 261, 88, 88) action Jump("start")

        hotspot(180, 371, 87, 95) action Jump("start")

        hotspot(179, 485, 86, 92) action Jump("start")

        hotspot (126, 325, 34, 65) action Hide("inventory", transition=moveoutright)
        xalign 1.0 yoffset 50 xoffset 200
    
    draggroup :
    
        if len(inventory.items) == 0:
            pass
        else:
            drag:
                drag_name "key"
                child [inventory.items[0].image]
                xpos 1798
                ypos 196
                drag_offscreen True
                dragged dragged_key
                mouse_drop True 
                tooltip "key"
            if location_user =="hallway":
                drag:
                    drag_name "door"
                    idle_child "invisibleDoor_idle.png"
                    hover_child "invisibleDoor_hover.png"
                    xpos 745
                    ypos 379
                    dragged dragged_key
                    clicked door_clicked
                    drag_offscreen True
            

screen getkey():

    imagebutton:
        focus_mask None
        auto "key_%s.png" 

        action [Function(inventory.add, key1),Function(renpy.notify, "Key acquired"), Hide("getkey")]
        
        xalign 1.0 yalign 1.5 xoffset -60 yoffset 230

    
screen gameover():
    modal True
    frame:
        xsize 800
        ysize 300
        text "YOU HAVE CAUGHT. GAME OVER!" xalign 1.5 yalign 1.5
        textbutton("Try Again") action [SetVariable("turns", 0), SetVariable("events", 0),  Jump("start")] xalign 1.5 yalign 1.0 yoffset -40
        xalign 1.5 yalign 1.5

screen iconInventory():

    imagebutton:
        focus_mask None
        xalign 1.0
        yalign 0.0
        yoffset 50
        auto "inventoryIcon_%s.png" action Show ("inventory", transition=wipeleft)
        

# Fireflies animation overlay, used in the main menu
image fireflies:
    "fireflies/frame1.png" with Dissolve(1.5)
    pause 1.5
    "fireflies/transparent.png" with Dissolve(1.5)
    pause 1.5
    "fireflies/frame2.png" with Dissolve(1.5)
    pause 1.5
    "fireflies/transparent.png" with Dissolve(1.5)
    pause 1.5 
    "fireflies/frame3.png" with Dissolve(1.5)
    pause 1.5
    "fireflies/transparent.png" with Dissolve(1.5)
    pause 1.5
    "fireflies/frame4.png" with Dissolve(1.5)
    pause 1.5
    "fireflies/transparent.png" with Dissolve(1.5)
    pause 1.5
    "fireflies/frame5.png" with Dissolve(1.5)
    pause 1.5
    "fireflies/transparent.png" with Dissolve(1.5)
    pause 1.5
    repeat


