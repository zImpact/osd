init python:
    osd_gallery = Gallery()
    osd_gallery_page = 0
    osd_gallery.transition = fade
    osd_gallery.locked_button = OSD_GUI_PATH + "save_load/main_menu/thumbnail_idle.png"
    osd_gallery.navigation = False

    osd_rows = 4
    osd_cols = 3
    osd_cells  = osd_rows * osd_cols

    def osd_page_counter(n, k):
        l = float(n) / float(k)
        
        if l - int(l) > 0:
            return int(l) + 1

        else:
            return l

    osd_gallery_bg_list = [
        "osd_int_dining_hall_damaged",
        "osd_int_clubs_male_night_light",
        "osd_ext_music_club_night",
        "osd_ext_no_bus_pioneers",
        "osd_ext_bus_pioneers",
        "osd_int_bus_pioneers",
        "osd_int_dining_hall_sunset",
        "osd_ext_camp_plain_sight",
        "osd_ext_sky",
        "osd_nit_third_fight"
    ]

    for bg in osd_gallery_bg_list:
        osd_gallery.button(bg)
        osd_gallery.image("bg " + bg)
        osd_gallery.unlock("bg " + bg)

screen osd_background_gallery():
    modal True

    if not osd_main_menu_var:
        add "osd_main_menu_frame"

        $ osd_gallery_table = osd_gallery_bg_list

        $ osd_len_table = len(osd_gallery_bg_list)

        text "Галерея":
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
                Hide("osd_background_gallery"),
                ShowMenu("osd_extra")
            ]

        grid osd_rows osd_cols xpos 0.09 ypos 0.18:
            $ osd_bg_displayed = 0
            $ osd_next_page = osd_page + 1

            if osd_next_page > int(osd_len_table / osd_cells):
                $ osd_next_page = 0

            for n in range(osd_len_table):
                if n < (osd_page + 1) * osd_cells and n >= osd_page * osd_cells:
                    $ _osd_t = im.Crop(
                        "osd/images/bg/" + osd_gallery_table[n][len(OSD_PREFIX):] + ".png",
                        (0, 0, 1920, 1080)
                    )
                            
                    $ _osd_img_scaled = im.Scale(_osd_t, 320, 180)

                    $ osd_img = im.Composite(
                        (336, 196),
                        (8, 8),
                        im.Alpha(_osd_img_scaled, 0.9),
                        (0, 0),
                        im.Image(OSD_GUI_PATH + "save_load/main_menu/thumbnail_idle.png")
                    )

                    $ osd_imgh = im.Composite(
                        (336, 196),
                        (8, 8),
                        _osd_img_scaled,
                        (0, 0),
                        im.Image(OSD_GUI_PATH + "save_load/main_menu/thumbnail_hover.png")
                    )

                    add osd_g.make_button(
                        osd_gallery_table[n],
                        get_image("gui/gallery/blank.png"),
                        None,
                        osd_imgh,
                        osd_img,
                        style="blank_button",
                        bottom_margin=50,
                        right_margin=50
                    )

                    $ osd_bg_displayed += 1

                    if n + 1 == osd_len_table:
                        $ osd_next_page = 0

            for j in range(0, osd_cells - osd_bg_displayed):
                null

        if osd_page != 0:
            imagebutton:
                auto "osd_gallery_previous_%s"
                yalign 0.5 
                xalign 0.04 
                action [
                    SetVariable("osd_page", osd_page - 1),
                    ShowMenu("osd_background_gallery")
                ]

        if osd_page != int(osd_page_counter(osd_len_table, osd_cells)) - 1:
            imagebutton: 
                auto "osd_gallery_next_%s"
                yalign 0.5 
                xalign 0.96 
                action [
                    SetVariable("osd_page", osd_next_page),
                    ShowMenu("osd_background_gallery")
                ]
