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
            self.w_screen = self.x_center - (config.screen_width / 2)
            self.h_screen = self.y_center - (config.screen_height / 2)
        
        # Optional: method to retrieve the screen offset values
        def get_screen_offset(self):
            return self.w_screen, self.h_screen

    # Create stage instances with specific parameters
    stage1 = Stage(350, 485, 215, 117) # stage_name(xposition, yposition, image_size in width/x, image_size in height/y)
    stage2 = Stage(800, 505, 215, 117)
    stage3 = Stage(1250, 485, 215, 117)
    stage4 = Stage(1650, 550, 215, 117)

default auto_scroll_forest = False

screen test_parallax_screen():
    modal True
    vbox:
        align (0.0, 0.5)
        ## Here's another viewport, which scrolls horizontally. It has some
        ## buttons on each parallax layer which scroll with the layer itself.
        parallax_viewport:
            draggable True
            xysize (int(config.screen_width), int(config.screen_height))
            id "parallax_vp_ex2"
            ## Important!! This line is required just before you add your layers.
            has fixed style "vparallax_fixed"

            fixed:
                fit_first True
                add "images/chapter_screen/forest_back_t.png"
                add "images/chapter_screen/arrow.png" xpos 370 ypos 555
                #add Movie(play="images/Vines.webm", mask="images/Vines_mask.webm", framedrop=False, loop=False) xpos 1000 ypos 515

                imagebutton:
                    idle ("images/chapter_screen/stage01_idle.png")
                    hover ("images/chapter_screen/stage01_hover.png")
                    focus_mask True
                    action [
                        Notify("Button1"),
                        AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=0, y_position=0, delay=0.5, warper="ease"),
                        SetVariable("current_stage_prompt", "images/chapter_screen/stageprompt3.png"),  # Set prompt for Button1
                        SetVariable("target_label", "chapter1"),  # Set target label for Button1
                        SetVariable("show_overlay", True),
                        Show("overlay_screen")
                    ]
                    xpos stage1.x_stage
                    ypos stage1.y_stage

                imagebutton:
                    idle ("images/chapter_screen/stage02_idle.png")
                    hover ("images/chapter_screen/stage02_hover.png")
                    focus_mask True
                    action [
                        Notify("Button2"),
                        AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage2.w_screen, y_position=stage2.h_screen, delay=0.5, warper="ease"),
                        SetVariable("current_stage_prompt", "images/chapter_screen/stageprompt3.png"),  # Set prompt for Button1
                        SetVariable("target_label", "chapter2"),  # Set target label for Button1
                        SetVariable("show_overlay", True),
                        Show("overlay_screen") 
                    ]
                    xpos stage2.x_stage 
                    ypos stage2.y_stage

                imagebutton:
                    idle ("images/chapter_screen/stage03_idle.png")
                    hover ("images/chapter_screen/stage03_hover.png")
                    focus_mask True
                    action [
                        Notify("Button3"),
                        AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage3.w_screen, y_position=stage3.h_screen, delay=0.5, warper="ease"),
                        SetVariable("current_stage_prompt", "images/chapter_screen/stageprompt3.png"),  # Set prompt for Button1
                        SetVariable("target_label", "chapter3"),  # Set target label for Button1
                        SetVariable("show_overlay", True),
                        Show("overlay_screen") 
                    ]
                    xpos stage3.x_stage 
                    ypos stage3.y_stage

                imagebutton:
                    idle ("images/chapter_screen/stage04_idle.png")
                    hover ("images/chapter_screen/stage04_hover.png")
                    focus_mask True
                    action [
                        Notify("Button4"),
                        AnimateScroll("parallax_vp_ex2", "horizontal increase", x_position=stage4.w_screen, y_position=stage4.h_screen, delay=0.5, warper="ease"),
                        SetVariable("current_stage_prompt", "images/chapter_screen/stageprompt3.png"),  # Set prompt for Button1
                        SetVariable("target_label", "chapter4"),  # Set target label for Button1
                        SetVariable("show_overlay", True),
                        Show("overlay_screen") 
                    ]
                    xpos stage4.x_stage 
                    ypos stage4.y_stage

    textbutton _("Return") action Return()