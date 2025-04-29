init python:
    mods["osd_start"] = u"{font=[osd_link_font]}{size=40}Один украденный день{/font}{/size}"

    try:
        modsImages["osd_start"] = (OSD_GUI_PATH + "misc/osd_tabular_list_preview.png", False)

    except:
        pass

label osd_start:
    $ osd_set_time(OSD_TIMEOFDAY_PROLOGUE)
    $ osd_onload("lock")
    $ osd_set_dynamic_cursor("main_menu")
    $ osd_screens_save_act()
    scene bg black with Dissolve(2)
    $ renpy.pause(0.5, hard=True)
    scene osd_sky_day
    show osd_intro_logo at truecenter
    show osd_blank_skip
    with Dissolve(2)
    $ renpy.pause(0.5, hard=True) 
    play sound osd_intro_sample
    $ renpy.pause(8, hard=True)
    scene bg black with Dissolve(2)
    $ renpy.pause(0.5, hard=True)
    $ osd_set_mode_adv()

    label osd_after_intro:
        $ osd_onload("unlock")
        stop sound
        $ renpy.transition(Dissolve(2))
