screen osd_main_menu():
    tag menu 
    modal True

    key "game_menu":
        action NullAction()
        
    key "K_F1":
        action NullAction()

    add "osd_main_menu_atl"
    
    if osd_main_menu_var:
        add "osd_logo"
            
        textbutton ["Начать игру"] at osd_buttons_atl():
            style "osd_main_menu"
            text_style "osd_main_menu"
            xalign 0.5
            ypos 292
            action [Hide("osd_main_menu", Dissolve(1.5)), SetVariable("osd_lock_quit_game_main_menu_var", False), Start("osd_main_scenario")]
                
        textbutton "[osd_load_text]" at osd_buttons_atl():
            style "osd_main_menu"
            text_style "osd_main_menu"
            xalign 0.5
            ypos 415
            action [SetVariable("osd_main_menu_var", False), ShowMenu("osd_load_main_menu")]

        textbutton "[osd_extra_text]" at osd_buttons_atl():
            style "osd_main_menu"
            text_style "osd_main_menu"
            xalign 0.5
            ypos 538
            action [SetVariable("osd_main_menu_var", False), ShowMenu("osd_extra")]
            
        textbutton "[osd_preferences_text]" at osd_buttons_atl():
            style "osd_main_menu"
            text_style "osd_main_menu"
            xalign 0.5
            ypos 662
            action [SetVariable("osd_main_menu_var", False), ShowMenu("osd_preferences_main_menu")]
                
        textbutton ["Выход"] at osd_buttons_atl():
            style "osd_main_menu"
            text_style "osd_main_menu"
            xalign 0.5
            ypos 785
            action [SetVariable("osd_main_menu_var", False), ShowMenu("osd_quit_main_menu")]
            
        imagebutton:
            auto "osd_logowhite_%s"
            xpos 1520
            ypos 800
            action OpenURL("https://vk.com/public176281709")
        
screen osd_quit_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not osd_main_menu_var:
        add "osd_main_menu_frame"
        
        text "Вы действительно хотите выйти?":
            font osd_link_font
            size 80
            text_align 0.5
            xalign 0.5
            yalign 0.33
            antialias True
            kerning 2
            
        textbutton "[osd_yes_text]":
            style "osd_settings_header_main_menu_quit"
            text_style "osd_settings_header_main_menu_quit"
            xpos 493
            ypos 600
            action [Hide("osd_quit_main_menu"), (Function(osd_screens_diact)), ShowMenu("main_menu")]
            
        textbutton "[osd_no_text]":
            style "osd_settings_header_main_menu_quit"
            text_style "osd_settings_header_main_menu_quit"
            xpos 1230
            ypos 600
            action [SetVariable("osd_main_menu_var", True), Hide("osd_quit_main_menu"), ShowMenu("osd_main_menu")]
        
screen osd_preferences_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not osd_main_menu_var:
        add "osd_main_menu_frame"
        
        text "[osd_preferences_text]":
            font osd_link_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        text "[osd_display_preferences_text]":
            font osd_header_font
            size 60
            xalign 0.5
            ypos 200
            
        textbutton "[osd_display_preferences_fullscreen_text]":
            style "osd_button_none"
            text_style "osd_settings_header_main_menu_preferences"
            xalign 0.15
            ypos 280
            action Preference("display", "fullscreen")
            
        textbutton "[osd_display_preferences_window_text]":
            style "osd_button_none"
            text_style "osd_settings_header_main_menu_preferences"
            xalign 0.85
            ypos 280

            if not _preferences.fullscreen:
                text_style "osd_settings_header_main_menu_preferences_inverse"

            else:
                text_style "osd_settings_header_main_menu_preferences"

            action Preference("display", "window")

        text "[osd_font_size_preferences_text]":
            font osd_header_font
            size 60
            xalign 0.5
            ypos 360
                
        textbutton "[osd_font_size_preferences_small_text]":
            style "osd_button_none"
            text_style "osd_settings_header_main_menu_preferences"
            xalign 0.15
            ypos 440
            action SetField(persistent, "font_size", "small")
                
        textbutton "[osd_font_size_preferences_large_text]":
            style "osd_button_none"
            text_style "osd_settings_header_main_menu_preferences"
            xalign 0.85
            ypos 440
            action SetField(persistent, "font_size", "large")
                
        text "[osd_skip_preferences_text]":
            font osd_header_font
            size 60
            xalign 0.5
            ypos 520

        if not _preferences.skip_unseen:
            textbutton "[osd_skip_preferences_seen_text]":
                style "osd_button_none"
                text_style "osd_settings_header_main_menu_preferences"
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "[osd_skip_preferences_all_text]":
                style "osd_button_none"
                text_style "osd_settings_header_main_menu_preferences"
                xalign 0.85
                ypos 600
                action Preference("skip", "all")
                            
        if _preferences.skip_unseen:
            textbutton "[osd_skip_preferences_seen_text]":
                style "osd_button_none"
                text_style "osd_settings_header_main_menu_preferences"
                xalign 0.15
                ypos 600
                action Preference("skip", "seen")

            textbutton "[osd_skip_preferences_all_text]":
                style "osd_button_none"
                text_style "osd_settings_header_main_menu_preferences"
                xalign 0.85
                ypos 600
                action Preference("skip", "all")    
            
        text ["Громкость музыки"]:
            font osd_header_font
            size 60
            xpos 430
            ypos 820

        bar:
            value Preference("music volume")
            right_bar "osd_main_menu_bar_null"
            left_bar "osd_main_menu_bar_full"
            thumb "osd_main_menu_thumb"
            xpos 975
            ypos 813
            xmaximum 400
            ymaximum 85

        textbutton "[osd_return_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [SetVariable("osd_main_menu_var", True), Hide("osd_preferences_main_menu"), ShowMenu("osd_main_menu")]
        
screen osd_load_main_menu():
    modal True
    
    key "K_F1":
        action NullAction()
    
    if not osd_main_menu_var:
        add "osd_main_menu_frame"
        
        text "[osd_loading_text]":
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
            action [SetVariable("osd_main_menu_var", True), Hide("osd_load_main_menu"), ShowMenu("osd_main_menu")]
                    
        textbutton "[osd_load_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.5
            ypos 970
            action (OsdFunctionCallback(osd_on_load_callback, selected_slot), FileLoad(selected_slot, confirm=False))
                 
        textbutton "[osd_delete_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.9
            ypos 970
            action FileDelete(selected_slot, confirm=False)
            
        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True

            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "osd_save_load_button_main_menu"

                        fixed:
                            text ("%s." % i + FileTime(i, format=" %d.%m.%y, %H:%M", empty=OSD_SAVE_LOAD_SLOT_LABEL) + "\n" + FileSaveName(i)):
                                style "osd_text_save_load_main_menu"
                                xpos 15
                                ypos 15
        
screen osd_extra():
    modal True

    key "K_F1":
        action NullAction()
    
    if not osd_main_menu_var: 
        add "osd_main_menu_frame"
        
        text "[osd_extra_text]":
            font osd_link_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        textbutton ["Музыка"]:
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.5
            yalign 0.3
            action [Hide("osd_extra"), ShowMenu("osd_music_room")]

        textbutton ["Галерея"]:
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.5
            yalign 0.5
            action [Hide("osd_extra"), ShowMenu("osd_background_gallery")]

        textbutton ["Достижения"]:
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.5
            yalign 0.7
            action [Hide("osd_extra"), ShowMenu("osd_achievements")]

        textbutton "[osd_return_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [SetVariable("osd_main_menu_var", True), Hide("osd_extra"), ShowMenu("osd_main_menu")]
