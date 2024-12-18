
label start:
    "what suppppp"
    "yowwwww"
    return

label ch1_scene1: 
    scene flashlight_bk
    play music "hearbeat.mp3"
    pause 1.5
    play music "heartbeat.mp3"
    
    scene  scene1 at Static
    show blinking

    ivy "Where...."
    ivy"Where am i?"
    unknown "Where it all began… before you lost yourself completely."
    pause 0.5

    show Unknown Voice behind blinking at WhiteNoise :
        xpos 1150
        ypos 500
        zoom 0.5
    
    ivy "Who's there?"

    hide Unknown Voice
    pause 2.0

    show Unknown Voice behind blinking at WhiteNoise:
        xpos 270
        ypos -300
        zoom 3.5
    pause 
    scene flashlight_bk
   
    scene scene2

    ivy "what was that dream?"
    ivy "...."
    ivy "it felt real"
    ivy "Well.. anyways today's my wedding"
    ivy "I gotta go and prepare.."

    scene scene_3 with fade
    "knock knock!"

    ivy "Come in!"

    pause 0.5
    scene scene_3_1 with fade

    show Ivy smile at right with easeinright

    show Anna smile1 at left with easeinleft
    anna "Here comes the Bride!"
    anna "Oh, you look so beautiful."
    show Anna laugh at left with dissolve
    anna "And here I thought you'd grow old alone."
    show Anna smile2 at left with dissolve
    anna "Now look at you, in a wedding dress. "
    anna "I’m so happy for you, Vy!"
    menu:
    
        "Thank her sarcastically":
            show Ivy lipsmile at right with dissolve
            ivy"Thank you for your 'ungrateful' words"

            show Anna serious at left with dissolve
            anna"Hey, I don’t hand out compliments like this every day,"
            anna"so enjoy it while it lasts."

            show Ivy laugh at right with dissolve
            ivy"Alright, alright"

            show Ivy bashful at right with dissolve
            ivy "I’ll take it. Thanks, An."

        "Tease her back":
            show Ivy laugh at right with dissolve
            ivy "Aww, stop it, you’re going to make me blush!"

            show Anna smile1 at left with dissolve
            anna "Well, that’s a first! Look at you, all flustered."

            show Ivy lipsmile at right with dissolve
            ivy"I can’t help it, you're being too nice today."
            show Anna serious at left with dissolve
            anna"I’m just speaking the truth! But don’t get used to it though."

    show Ivy smile at right with dissolve
    ivy "So.."
    show Anna smile1 at left with dissolve
    ivy "What are you doing here?"
    
    show Anna smile2 at left with dissolve
    anna "Just checking on the bride and making sure you are as pretty as me"

    show Ivy lipsmile at right with dissolve
    ivy "Sounds like someone's a little jealous.."
    show Anna serious at left with dissolve
    anna "haha.. funny"
    anna "So..."
    anna "Is everything okay? you looked kind of uneasy"

    menu: 
        "Tell her about the dream":
            show Ivy serious at right with dissolve
            ivy"I had a weird dream last night."
            show Anna serious at left with dissolve
            anna "How weird? try me."
            ivy "I was in a forest. It was dark and..."
            ivy" I don’t know, everything just felt wrong. Like I shouldn’t have been there."
            ivy "There was this... voice. I don’t remember it clearly, but it said something about where it all began. And losing myself..."
            ivy "or something like that."

            anna "that sounds creepy. what else happened?"
            ivy "there was a shadow.  I don't even know if it was a person or..."
            ivy "something else. it was just standing there, next to a tree."
            ivy "Then suddenly, it moved or maybe it didn't. I don't know."
            ivy "It's all a blur, but it was right in front of me, and ..."
            ivy "then i woke up"
            
            anna "Well, that is weird…"
            show Anna smile2 at left with dissolve
            anna"but I’m sure it was nothing."
            show Anna laugh at left with dissolve
            anna "Dont't worry about it. You are marrying the man of your dreams after all"
            show Ivy smile at right with dissolve
            ivy "Thanks, An. I'll try not to overthink it"
            anna "Just making sure!"


        "Tell her you're okay":
            show Ivy smile at right with dissolve
            ivy "I’m fine… just wedding jitters."
            show Anna laugh at left with dissolve
            anna "That's totally normal!."
            anna "You're starting a whole new chapter of your life"
    
    show Anna smile1 at left with dissolve
    anna "Alrighty, I gotta go check on things outside"
    anna "And make sure my bestfriend gets married!"
    show Ivy laugh at right with dissolve
    ivy "Okay, see you  later"
    show Ivy bashful at right with dissolve

    scene  pictures with 
    pause 

    $ persistent.chapter1_scene2 = True
    jump  ch1_scene2
    #call screen chapter()

label ch1_scene2:

   
    $ persistent.chapter1_scene3 = True

    jump ch1_scene3



label ch1_scene3:
    scene scene_3 with fade
    "knock knock!"
    pause 1.0
    scene scene_3_1 with fade

    $ persistent.chapter2_unlock = True
    $ persistent.chapter2_scene1 = True

    return

label ch2_scene1:

    

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
