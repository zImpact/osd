init python:
    osd_music_box = {
        "God Is An Astronaut — All Is Violent, All Is Bright": osd_god_is_an_astronaut_all_is_violent_all_is_bright,
        "OSD — Escape From Reality": osd_escape_from_reality,
        "Nova: Covert Ops — Loading Screen": osd_novaco_loading,
        "Hearthstone — Boomsday": osd_boomsday,
        "Heroes Might and Magick 4 — Combat Theme": osd_heroes_of_might_and_magic_4_combat_theme_III,
        "OSD — Fireplace": osd_fireplace,
        "Painkiller — Forest": osd_painkiller_forest,
        "Skyrim — Tundra": osd_skyrim_tundra,
        "AlexRoma — Academy of Honor Guitar Cover": osd_academy_of_honor_guitar_cover,
        "April Rain — Soulmate": osd_soulmate,
        "Haimin — Mistakes": osd_haimin_mistakes,
        "OSD — Socialism": osd_socialism,
        "April Rain — In Spite Of": osd_having_lived,
        "God Is An Astronaut — When Everything Dies": osd_god_is_an_astronaut_when_everything_dies,
        "OSD — The Ancients": osd_the_ancients
    }

    osd_music_room = MusicRoom(fadeout=1.0)

    for music_name in osd_music_box.values():
        osd_music_room.add(music_name)

screen osd_music_room():
    modal True

    if not osd_main_menu_var:
        add "osd_music_room_frame"

        frame background "osd_main_menu_frame":
            side "c r":
                area (0.15, 0.22, 0.79, 0.73)

                viewport:
                    id "osd_music_box"
                    draggable True
                    mousewheel True
                    scrollbars None
                    
                    grid 1 len(osd_music_box):
                        for name, track in sorted(osd_music_box.iteritems()):
                            $ osd_music_room_label_text = name if osd_music_room.is_unlocked(track) else "???"
                            textbutton osd_music_room_label_text:
                                style "osd_button_none"
                                text_style "music_link"
                                xalign 0.5
                                action osd_mr.Play(track)

                vbar:
                    value YScrollValue("osd_music_box")
                    bottom_bar "osd_main_menu_vbar_null"
                    top_bar "osd_main_menu_vbar_full"
                    thumb "images/misc/none.png"
                    xmaximum 52

        text "Музыка":
            font osd_link_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton "[osd_return_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [
                Hide("osd_music_room"),
                ShowMenu("osd_extra")
            ]

        on "replaced" action Play("music", osd_god_is_an_astronaut_all_is_violent_all_is_bright)