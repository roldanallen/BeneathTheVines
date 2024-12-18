init -1 python:
    # This runs very early during the game's startup
    persistent.chapter_layer_unlock = False

init python:
    # List of initial values for unlock states
    def layer_unlock():
        persistent.chapter_layer_unlock = False
    
    def layer_lock():
        persistent.chapter_layer_unlock = True

    if not hasattr(persistent, "chapter1_scene2"):
        persistent.chapter1_scene2 = False

    chapter_defaults = {
        "chapter1_unlock": True,
        "chapter2_unlock": False,
        "chapter3_unlock": False,
        "chapter4_unlock": False,
        "chapter5_unlock": False,
        "chapter_layer_unlock": False
    }

    # Handle scene states
    scene_defaults = {
        "chapter1_scene1": True,
        "chapter1_scene2": False,
        "chapter1_scene3": False,
        "chapter2_scene1": False,
        "chapter2_scene2": False,
        "chapter2_scene3": False,
    }

    # Ensure each default is mapped into persistent storage only if not already saved
    for key, value in chapter_defaults.items():
        if not hasattr(persistent, key):
            setattr(persistent, key, value)

    for key, value in scene_defaults.items():
        if not hasattr(persistent, key):
            setattr(persistent, key, value)