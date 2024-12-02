label stage01:
    default stage02_unlocked = False
    scene bg room
    show eileen happy

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    $ stage02_unlocked = True  # Unlock stage02 after completing stage0

label stage02:
