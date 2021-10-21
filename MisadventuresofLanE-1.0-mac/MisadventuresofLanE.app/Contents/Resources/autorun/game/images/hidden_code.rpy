init python:
    sc_thing = False
    class registerClick(Action):
        def __call__(self):
            global num_clicks
            num_clicks += 1
            renpy.restart_interaction()


    class getHint(Action):
        def __call__(self):
            global num_hints
            num_hints -= 1
            for index,i in enumerate(hidden_items):
                if i.found == False and i.hint == False:
                    i.hint = True
                    break
            renpy.restart_interaction()

        def get_sensitive(self):
            global num_hints
            return num_hints > 0

    class SetItem(Action):

        def __init__(self, object, field, value):
            self.object = object
            self.field = field
            self.value = value

        def __call__(self):
            setattr(self.object, self.field, self.value)
            renpy.restart_interaction()

        def get_selected(self):
            return getattr(self.object, "hint") == True

    class Item:
        def __init__(self, name, x,y,w,h,hint=False):
            self.name = name
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.found = False
            self.hint = hint

    showitems = False
    def display_items_overlay():
        if showitems:
            ui.frame(id="obj_list")
            ui.vbox(id="display_vbox",spacing=10)
            ui.text("Hints: %d" % (num_hints))
            ui.text("Items:" )
            for index,i in enumerate(hidden_items):
                inventory_prefix = ""
                inventory_suffix = ""
                item_name = i.name
                item_state = i.found
                if item_state == True:
                    inventory_prefix = "{s}"
                    inventory_suffix = "{/s}"
                item_text = inventory_prefix+item_name+inventory_suffix
                item_index = "object_%d" % (index)
                ui.text(item_text,id=item_index)
            ui.close()
    config.overlay_functions.append(display_items_overlay)

    # def run_sc_thing():
    #     global sc_thing
    #     if (sc_thing == False):
    #
    #
    #     sc_thing = True
    #
    # def rmv_sc_thing():
    #     global sc_thing
    #     if (sc_thing == True):
    #         sc_thing = False
    #         config.overlay_functions.remove(display_items_overlay)

    def is_all_found():
        for i in hidden_items:
            if i.found == False:
                return False
        return True

    def resetItems(in_items):
        for i in in_items:
            i.found = False

screen hidden_object:
    tag hidden

    imagemap:
        auto hidden_files
        # $ global sc_thing = False
        # $ run_sc_thing()
        cache False
        imagebutton auto "empty_%s.png" action registerClick()
        textbutton "Hint" xalign 1.0 yalign 0.0 action getHint()
        for index, item in enumerate(hidden_items):
            hotspot (item.x,item.y,item.w,item.h) action If(hidden_items[index].found==False, SetItem(hidden_items[index],"found",True), None)
        if is_all_found():
            textbutton "Objects found!" xalign 0.5 yalign 0.5 action Return("All Found!")
