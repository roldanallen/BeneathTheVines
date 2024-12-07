define e = Character("Eileen")
image background = ("images/chapter_screen/forest_front_t.jpg")

# The game starts here.

label start:
    "what suppppp"
    "yowwwww"
    return

label ch1_scene1:

    show bg room
    show Eileen happy

    "You are in scene1!"
    "you will proceed to scene2 after completing this!"

    $ persistent.chapter1_scene2 = True

    return

    call screen chapter()

label ch1_scene2:

    show bg room

    show Eileen happy at left

    "Scene 2!!"
    "Finish this to proceed to Scene3"

    $ persistent.chapter1_scene3 = True

    return


label ch1_scene3:

    show bg room

    show Eileen happy at right

    "Scene 2!!"
    "Finish this to proceed to Scene3"

    $ persistent.chapter2_unlock = True
    $ persistent.chapter2_scene1 = True

    return

label ch2_scene1:

    show bg room

    "Chapter 2!!"
    "Finish this to proceed to Scene2"

    $ persistent.chapter2_scene2 = True

label ch2_scene2:

    show bg room

    "Scene 3 of Chapter 2!!"
    "Finish this to proceed to Chapter 3!!!"

    $ persistent.chapter2_scene3 = True


label ch2_scene3:

    show bg room

    "Scene 3 of Chapter 2!!"
    "Finish this to proceed to Chapter 3!!!"

    $ persistent.chapter3_unlock = True
    $ persistent.chapter3_scene1 = True


label ch3_scene1:

    show bg room

    "Chapter 2!!"
    "Finish this to proceed to Scene2"
