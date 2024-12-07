## including images!
image forest_back_t = "images/chapter_screen/forest_back_t.png"
image forest_front_t = "forest_front_t.jpg"
#For popup screen as additionals

init python:
    # Define a Stage class
    class Stage:
        def __init__(self, x_stage, y_stage, x_imagesize, y_imagesize):
            # Initialize stage location and image size
            self.x_stage = x_stage
            self.y_stage = y_stage
            self.x_imagesize = x_imagesize
            self.y_imagesize = y_imagesize
            
            # Calculate the center of the stage box
            self.x_center = self.x_stage + (self.x_imagesize / 2)
            self.y_center = self.y_stage + (self.y_imagesize / 2)
            
            # Center screen based on stage box center
            self.w_screen = self.x_center - (1130 / 1.5)
            self.h_screen = self.y_center - (610 / 2)
        
        # Optional: method to retrieve the screen offset values
        def get_screen_offset(self):
            return self.w_screen, self.h_screen

    # Create stage instances with specific parameters
    stage1 = Stage(279, 324, 215, 117) # stage_name(xposition, yposition, image_size in width/x, image_size in height/y)
    stage2 = Stage(773, 252, 215, 117)
    stage3 = Stage(1318, 369, 215, 117)
    stage4 = Stage(1650, 450, 215, 117)


default auto_scroll_forest = False
default show_return_button = None

default current_frame = "chapter1"

screen chapter():
    tag menu
    modal True

#---------FOR CHANGING BACKGROUNDS EACH CHAPTERS----------------#
    if current_frame == "chapter1":
        add "images/chapter_screen/chapters/ChapterStory1(1).png"
    elif current_frame == "chapter2":
        add "images/chapter_screen/chapters/ChapterStory2(1).png"
    elif current_frame == "chapter3":
        add "images/chapter_screen/chapters/ChapterStory3.png"
    elif current_frame == "chapter4":
        add "images/chapter_screen/chapters/ChapterStory4.png"

#------------------FOR SIDEBAR CHAPTERS------------------------#
    #imagebutton:
    #    xpos 1700
    #    ypos 103
    #    auto "images/chapter_screen/chapters/Return_%s.png"
    #    action Hide("chapter", transition=dissolve)

    add "images/chapter_screen/chapters/game_menu.png" xpos 1446 ypos 109

    imagebutton:
        xpos 1771
        ypos 92
        auto "images/chapter_screen/chapters/gamepause_%s.png"
        action ShowMenu("gamepause")
        hover_sound "hover.mp3"

    imagebutton:
        xpos 75
        ypos 200
        auto "images/chapter_screen/chapters/Chapter1_%s.png"

        if current_frame != "chapter1":
            action SetVariable("current_frame", "chapter1"), Show("black_screen", transition=dissolve)
        else:
            action SetVariable("current_frame", "chapter1")

        hover_sound "hover.mp3"
        #activate_sound "clicked.mp3"

    imagebutton:
        xpos 75
        ypos 400
        idle ConditionSwitch(
            "persistent.chapter2_unlock", "images/chapter_screen/chapters/Chapter2_idle.png",
            "not persistent.chapter2_unlock", "images/chapter_screen/chapters/Chapter2_locked_idle.png")

        hover ConditionSwitch(
            "persistent.chapter2_unlock", "images/chapter_screen/chapters/Chapter2_hover.png", 
            "not persistent.chapter2_unlock", "images/chapter_screen/chapters/Chapter2_locked_idle.png")

        if persistent.chapter2_unlock:
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"
            if current_frame != "chapter2":
                action [SetVariable("current_frame", "chapter2"), Show("black_screen", transition=dissolve)]

            else:
                action [SetVariable("current_frame", "chapter2")]
        
        else:
            activate_sound "error.mp3"
            action Show("chapterlock")

    imagebutton:
        xpos 75
        ypos 600
        idle ConditionSwitch(
            "persistent.chapter3_unlock", "images/chapter_screen/chapters/Chapter3_idle.png",
            "not persistent.chapter3_unlock", "images/chapter_screen/chapters/Chapter3_locked_idle.png")

        hover ConditionSwitch(
            "persistent.chapter3_unlock", "images/chapter_screen/chapters/Chapter3_hover.png", 
            "not persistent.chapter3_unlock", "images/chapter_screen/chapters/Chapter3_locked_idle.png")
        
        if persistent.chapter3_unlock:
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"
            if current_frame != "chapter3":
                action [SetVariable("current_frame", "chapter3"), Show("black_screen", transition=dissolve)]

            else:
                action [SetVariable("current_frame", "chapter3")]
        
        else:
            activate_sound "error.mp3"
            action Show("chapterlock")

    imagebutton:
        xpos 75
        ypos 800
        idle ConditionSwitch(
            "persistent.chapter4_unlock", "images/chapter_screen/chapters/Chapter4_idle.png",
            "not persistent.chapter4_unlock", "images/chapter_screen/chapters/Chapter4_locked_idle.png")

        hover ConditionSwitch(
            "persistent.chapter4_unlock", "images/chapter_screen/chapters/Chapter4_hover.png", 
            "not persistent.chapter4_unlock", "images/chapter_screen/chapters/Chapter4_locked_idle.png")
        
        if persistent.chapter4_unlock:
            hover_sound "hover.mp3"
            #activate_sound "clicked.mp3"
            if current_frame != "chapter4":
                action [SetVariable("current_frame", "chapter4"), Show("black_screen", transition=dissolve)]

            else:
                action [SetVariable("current_frame", "chapter4")]
        
        else:
            activate_sound "error.mp3"
            action Show("chapterlock")


#--------------------------FOR SCENES(N) IN CHAPTER(N) --------------------------------#
    if current_frame == "chapter1":
        vbox:
            #align (0.5, 0.5)
            ## Here's another viewport, which scrolls horizontally. It has some
            ## buttons on each parallax layer which scroll with the layer itself.
            parallax_viewport:
                draggable True
                #xysize (int(config.screen_width), int(config.screen_height))
                xysize (1446, 610)
                xpos 437
                ypos 235

                id "parallax_vp_ex2"
                ## Important!! This line is required just before you add your layers.
                has fixed style "vparallax_fixed"

#-----------------------------------CHAPTER 1-----------------------------------------------

                fixed:
                    fit_first True
                    add "images/chapter_screen/forest_back_t1.png"
                    add "images/chapter_screen/chapter1/chapter1_vector.png" xpos 494 ypos 319
                    #add "images/chapter_screen/arrow.png" xpos 370 ypos 555

                    imagebutton: #Scene1
                        idle "images/chapter_screen/chapter1/scene1_idle.png"
                        hover "images/chapter_screen/chapter1/scene2_hover.png"

                        focus_mask True
            
                        action [                          
                            AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=0, y_position=0, delay=0.5, warper="ease"),
                            SetVariable("current_stage_prompt", "images/chapter_screen/scene_prompt/scene_prompt1.png"),  # Set prompt for Button1
                            SetVariable("target_label", "ch1_scene1"),  # Set target label for Button1
                            SetVariable("show_overlay", True),
                            Show("overlay_screen")
                        ]
                        #hover_sound "hover.mp3"
                        activate_sound "clicked.mp3"
                
                        xpos stage1.x_stage
                        ypos stage1.y_stage

                    imagebutton: #Scene2
                        idle ConditionSwitch("persistent.chapter1_scene2", "images/chapter_screen/chapter1/scene2_idle.png", 
                                            "not persistent.chapter1_scene2", "images/chapter_screen/chapter1/screen_locked2_idle.png")
                        hover ConditionSwitch("persistent.chapter1_scene2", "images/chapter_screen/chapter1/scene2_hover.png", 
                                            "not persistent.chapter1_scene2", "images/chapter_screen/chapter1/screen_locked2_idle.png")
                        focus_mask True
                        
                        if persistent.chapter1_scene2:
                            action [
                                #Notify("Button2"),
                                AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage2.w_screen, y_position=stage2.h_screen, delay=0.5, warper="ease"),
                                SetVariable("current_stage_prompt", "images/chapter_screen/scene_prompt/scene_prompt2.png"),  # Set prompt for Button1
                                SetVariable("target_label", "ch1_scene2"),  # Set target label for Button1
                                SetVariable("show_overlay", True),
                                Show("overlay_screen") 
                            ]
                            #hover_sound "hover.mp3"
                            activate_sound "clicked.mp3"
                             
                                                  
                        elif not persistent.chapter1_scene2:
                            action [
                            Show("scenelock"),
                            AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage2.w_screen, y_position=stage2.h_screen, delay=0.5, warper="ease")
                            ]

                            activate_sound "error.mp3" 

                        xpos stage2.x_stage 
                        ypos stage2.y_stage

                    imagebutton: #Scene3
                        idle ConditionSwitch("persistent.chapter1_scene3", "images/chapter_screen/chapter1/scene3_idle.png", 
                                            "not persistent.chapter1_scene3", "images/chapter_screen/chapter1/screen_locked3_idle.png")
                        hover ConditionSwitch("persistent.chapter1_scene3", "images/chapter_screen/chapter1/scene2_hover.png", 
                                            "not persistent.chapter1_scene3", "images/chapter_screen/chapter1/screen_locked3_idle.png")
                        focus_mask True
            
                        if persistent.chapter1_scene3:
                            action [
                                #Notify("Button3"),
                                AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage3.w_screen, y_position=stage3.h_screen, delay=0.5, warper="ease"),
                                SetVariable("current_stage_prompt", "images/chapter_screen/scene_prompt/scene_prompt1.png"),  # Set prompt for Button1
                                SetVariable("target_label", "ch1_scene3"),  # Set target label for Button1
                                SetVariable("show_overlay", True),
                                Show("overlay_screen") 
                            ]
                            #hover_sound "hover.mp3"
                            activate_sound "clicked.mp3"

                        else:
                            action [
                                Show("scenelock"),
                                AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage3.w_screen, y_position=stage3.h_screen, delay=0.5, warper="ease")]
                            activate_sound "error.mp3"
                        xpos stage3.x_stage 
                        ypos stage3.y_stage
                
#-----------------------CHAPTER 2-------------------------------------#

    elif current_frame == "chapter2":
        vbox:
            #align (0.5, 0.5)
            ## Here's another viewport, which scrolls horizontally. It has some
            ## buttons on each parallax layer which scroll with the layer itself.
            parallax_viewport:
                draggable True
                #xysize (int(config.screen_width), int(config.screen_height))
                xysize (1446, 610)
                xpos 437
                ypos 235

                id "parallax_vp_ex2"
                ## Important!! This line is required just before you add your layers.
                has fixed style "vparallax_fixed"

                fixed:
                    fit_first True
                    add "images/chapter_screen/forest_back_t1.png"
                    add "images/chapter_screen/chapter1/chapter1_vector.png" xpos 494 ypos 319
                    #add "images/chapter_screen/arrow.png" xpos 370 ypos 555

                    imagebutton: #Scene1
                        idle "images/chapter_screen/chapter1/scene1_idle.png"
                        hover "images/chapter_screen/chapter1/scene2_hover.png"

                        focus_mask True
            
                        action [                          
                            AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=0, y_position=0, delay=0.5, warper="ease"),
                            SetVariable("current_stage_prompt", "images/chapter_screen/stageprompt3.png"),  # Set prompt for Button1
                            SetVariable("target_label", "ch2_scene1"),  # Set target label for Button1
                            SetVariable("show_overlay", True),
                            Show("overlay_screen")
                        ]
                        #hover_sound "hover.mp3"
                        activate_sound "clicked.mp3"
                        xpos stage1.x_stage
                        ypos stage1.y_stage

                    imagebutton: #Scene2
                        idle ConditionSwitch("persistent.chapter2_scene2", "images/chapter_screen/chapter1/scene2_idle.png", 
                                            "not persistent.chapter2_scene2", "images/chapter_screen/chapter1/screen_locked2_idle.png")
                        hover ConditionSwitch("persistent.chapter2_scene2", "images/chapter_screen/chapter1/scene2_hover.png", 
                                            "not persistent.chapter2_scene2", "images/chapter_screen/chapter1/screen_locked2_idle.png")
                        focus_mask True
                        
                        if persistent.chapter2_scene2:
                            action [
                                #Notify("Button2"),
                                AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage2.w_screen, y_position=stage2.h_screen, delay=0.5, warper="ease"),
                                SetVariable("current_stage_prompt", "images/chapter_screen/stageprompt3.png"),  # Set prompt for Button1
                                SetVariable("target_label", "ch2_scene2"),  # Set target label for Button1
                                SetVariable("show_overlay", True),
                                Show("overlay_screen") 
                            ] 
                            #hover_sound "hover.mp3"
                            activate_sound "clicked.mp3"                     
                        else:
                            action [
                            Show("scenelock"),
                            AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage2.w_screen, y_position=stage2.h_screen, delay=0.5, warper="ease")
                            ]
                            activate_sound "error.mp3"
                        xpos stage2.x_stage 
                        ypos stage2.y_stage

                    imagebutton: #Scene3
                        idle ConditionSwitch("persistent.chapter2_scene3", "images/chapter_screen/chapter1/scene3_idle.png", 
                                            "not persistent.chapter2_scene3", "images/chapter_screen/chapter1/screen_locked3_idle.png")
                        hover ConditionSwitch("persistent.chapter2_scene3", "images/chapter_screen/chapter1/scene2_hover.png", 
                                            "not persistent.chapter2_scene3", "images/chapter_screen/chapter1/screen_locked3_idle.png")
                        focus_mask True
            
                        if persistent.chapter2_scene3:
                            action [
                                #Notify("Button3"),
                                AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage3.w_screen, y_position=stage3.h_screen, delay=0.5, warper="ease"),
                                SetVariable("current_stage_prompt", "images/chapter_screen/stageprompt3.png"),  # Set prompt for Button1
                                SetVariable("target_label", "ch2_scene3"),  # Set target label for Button1
                                SetVariable("show_overlay", True),
                                Show("overlay_screen") 
                            ]
                            #hover_sound "hover.mp3"
                            activate_sound "clicked.mp3"  

                        else:
                            action [
                                Show("scenelock"),
                                AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage3.w_screen, y_position=stage3.h_screen, delay=0.5, warper="ease")]
                            activate_sound "error.mp3"

                        xpos stage3.x_stage 
                        ypos stage3.y_stage

    elif current_frame == "chapter3":
        vbox:
            #align (0.5, 0.5)
            ## Here's another viewport, which scrolls horizontally. It has some
            ## buttons on each parallax layer which scroll with the layer itself.
            parallax_viewport:
                draggable True
                #xysize (int(config.screen_width), int(config.screen_height))
                xysize (1446, 610)
                xpos 437
                ypos 235

                id "parallax_vp_ex2"
                ## Important!! This line is required just before you add your layers.
                has fixed style "vparallax_fixed"

#-----------------------------------CHAPTER 1-----------------------------------------------

                fixed:
                    fit_first True
                    add "images/chapter_screen/forest_back_t1.png"
                    add "images/chapter_screen/chapter1/chapter1_vector.png" xpos 494 ypos 319

                    imagebutton: #Scene1
                        idle "images/chapter_screen/chapter1/scene1_idle.png"
                        hover "images/chapter_screen/chapter1/scene2_hover.png"

                        focus_mask True
            
                        action [                          
                            AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=0, y_position=0, delay=0.5, warper="ease"),
                            SetVariable("current_stage_prompt", "images/chapter_screen/stageprompt3.png"),  # Set prompt for Button1
                            SetVariable("target_label", "ch2_scene1"),  # Set target label for Button1
                            SetVariable("show_overlay", True),
                            Show("overlay_screen")
                        ]
                        #hover_sound "hover.mp3"
                        activate_sound "clicked.mp3"

                        xpos stage1.x_stage
                        ypos stage1.y_stage
                