init python:
    build.classify("**01_parallax_viewport.rpy", None)
    build.classify("**01_parallax_viewport.rpyc", "archive")
################################################################################
python early:

    class ParallaxVP(Viewport):
        """
        A special viewport that will scroll its children in parallax based
        on their sizes. Inherits from the built-in Viewport.
        """
        def render(self, width, height, st, at):
            self.width = width
            self.height = height

            child_width = self.child_width or width
            child_height = self.child_height or height

            surf = renpy.render(self.child, child_width, child_height, st, at)

            cw, ch = surf.get_size()
            cxo, cyo, width, height = self.update_offsets(cw, ch, st)

            self.offsets = [(cxo, cyo)]

            rv = renpy.Render(width, height)

            # Adjust child layers in relation to scroll percentage
            for child in self.child.children:
                child_render = child.render(width, height, st, at)
                pct_xscrolled = self.xadjustment.value / max(self.xadjustment.range, 1.0)
                pct_yscrolled = self.yadjustment.value / max(self.yadjustment.range, 1.0)
                child_w, child_h = child_render.get_size()

                # Offset positions based on scroll percentages
                new_xo = ((width - child_w) * pct_xscrolled)
                new_yo = ((height - child_h) * pct_yscrolled)

                # Set child rendering and clipping for focus handling
                child_render.xclipping = False
                child_render.yclipping = False

                # Keep the smaller layers on-screen and add focus at full dimensions
                rv.blit(child_render, (new_xo, new_yo))

            # Ensure full screen clipping and focus, which may affect button focus detection
            rv = rv.subsurface((0, 0, width, height), focus=True)

            if self.draggable or self.arrowkeys:
                rv.add_focus(self, None, 0, 0, width, height)

            return rv


    renpy.register_sl_displayable("parallax_viewport", ParallaxVP, 'viewport', 1,
        replaces=True, pass_context=True,
    ).add_property("child_size"
    ).add_property("mousewheel"
    ).add_property("arrowkeys"
    ).add_property("pagekeys"
    ).add_property("draggable"
    ).add_property("edgescroll"
    ).add_property("xadjustment"
    ).add_property("yadjustment"
    ).add_property("xinitial"
    ).add_property("yinitial"
    ).add_property("scrollbars"
    ).add_property("spacing"
    ).add_property("transpose"
    ).add_property("xminimum"
    ).add_property("yminimum"
    ).add_property_group("position",
    ).add_property_group("ui",
    )

init python:

    class AnimateScroll(Scroll):
        def __init__(self, id, direction, amount="step", delay=0.0, warper="ease", x_position=None, y_position=None):
            try:
                super(AnimateScroll, self).__init__(id, direction, amount, delay)
            except TypeError:
                super(AnimateScroll, self).__init__(id, direction, amount)
                self.delay = 0.0
            self.warper = warper
            self.x_position = x_position  # Fixed x-position scroll
            self.y_position = y_position  # Fixed y-position scroll

        def __call__(self):
            # Get the current horizontal adjustment
            adjustment = renpy.get_widget(None, self.id).xadjustment

            # Set fixed x-position scroll amount if specified
            if self.x_position is not None:
                x_amount = self.x_position - adjustment.value  # Move directly to x_position
            else:
                x_amount = adjustment.step  # Use the default step if x_position isn't set

            # Initialize y_adjustment if y_position is specified
            if self.y_position is not None:
                y_adjustment = renpy.get_widget(None, self.id).yadjustment
                y_amount = self.y_position - y_adjustment.value  # Move directly to y_position
            else:
                y_adjustment = None

            # Apply the x and y changes
            if self.delay == 0.0:
                adjustment.change(x_amount)
                if y_adjustment is not None:
                    y_adjustment.change(y_amount)
            else:
                adjustment.animate(x_amount, self.delay, renpy.atl.warpers[self.warper])
                if y_adjustment is not None:
                    y_adjustment.animate(y_amount, self.delay, renpy.atl.warpers[self.warper])


style vparallax_fixed:
    xfit True yfit True