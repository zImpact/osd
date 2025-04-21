screen osd_achievements():
    modal True

    key "K_F1":
        action NullAction()
    
    if not osd_main_menu_var: 
        add "osd_main_menu_frame"
        
        text "Достижения":
            font osd_link_font
            size 70
            xalign 0.5
            ypos 33
            antialias True
            kerning 2

        add OSD_GUI_PATH + "achievements/frame.png" xalign 0.5 ypos 240

        $ osd_achievements_buttons = {
            "osd_our_world": {
                "hover": "osd_our_world_hover",
                "idle": "osd_our_world_idle",
                "xalign": 0.35, 
                "ypos": 290
            },

            "osd_old_story": {
                "hover": "osd_old_story_hover",
                "idle": "osd_old_story_idle",
                "xalign": 0.65,
                "ypos": 290
            },

            "osd_as_before": {
                "hover": "osd_as_before_hover",
                "idle": "osd_as_before_idle",
                "xalign": 0.35, 
                "ypos": 490
            },

            "osd_perfect_gear": {
                "hover": "osd_perfect_gear_hover",
                "idle": "osd_perfect_gear_idle", 
                "xalign": 0.65, 
                "ypos": 490
            },

            "osd_wind_of_changes": {
                "hover": "osd_wind_of_changes_hover",
                "idle": "osd_wind_of_changes_idle",
                "xalign": 0.35, 
                "ypos": 690
            },

            "osd_calm": {
                "hover": "osd_calm_hover",
                "idle": "osd_calm_idle",
                "xalign": 0.65, 
                "ypos": 690
            },
        }

        for achievement, buttons_info in osd_achievements_buttons.items():
            if persistent.osd_achievements.get(achievement, False):
                add buttons_info["hover"] xalign buttons_info["xalign"] ypos buttons_info["ypos"]

                imagebutton:
                    idle buttons_info["idle"]
                    xalign buttons_info["xalign"]
                    ypos buttons_info["ypos"]
                    at osd_buttons_transition
                    action ShowMenu("osd_achievement_description", achievement=achievement)
            else:
                add "osd_locked" xalign buttons_info["xalign"] ypos buttons_info["ypos"]
                
        textbutton "[osd_return_text]":
            style "osd_log_button" 
            text_style "osd_settings_link_main_menu_preferences" 
            xalign 0.1
            ypos 970
            action [Hide("osd_achievements"), ShowMenu("osd_extra")]

screen osd_achievement_description(achievement):
    $ osd_achievements_info = {
        "osd_old_story": {
            "name": "Старая история",
            "background": "osd/images/bg/osd_int_dining_hall_sunset.png",
            "text": "В мире лагерей и вечных повторов сложно держаться\nза что-то материальное, поэтому культура Пионеров\nбыстро обросла своими правилами, суевериями и праздниками.\n\nПионеры обожают испытывать друг друга и\nсоревноваться в боях, музыке и даже в готовке."
        },

        "osd_our_world": {
            "name": "Наш мир",
            "background": "osd/images/bg/osd_ext_camp_plain_sight.png",
            "text": "Лагерь использует крайне сложную систему «замка», проверки на выход. Сложно понять все его правила, но главное — каждый настоящий Пионер должен быть\nуверен, что выйти возможно. Довериться другим таким\nже, как он.\n\n{i}И, если это произойдет, они вырвутся из замкнутой\nпетли{/i}. А единственными в лагере останутся лишь две сильнейшие куклы."
        },

        "osd_perfect_gear": {
            "name": "Идеальная шестерёнка",
            "background": "osd/images/bg/osd_stars_anim/osd_stars_1.png",
            "text": "Сначала считалось, что куклы глупы и заскриптованы,\nкак, например, все девушки из лагеря. Но никто и\nподумать не мог, что марионетки могут быть едва ли не сложнее самых изобретательных Пионеров.\n\nДаже если Пионеры выберутся, будет ли это\nпоражением лагеря?"
        },

        "osd_as_before": {
            "name": "Как раньше",
            "background": "images/bg/int_library_night2.jpg",
            "text": "Вечная жизнь имеет свои недостатки, но так же и свои\nплюсы. Пионеры могут бесконечно пробовать и\nразвиваться. Но никакая человеческая память не\nспособна вместить тысячи тысяч однообразных недель\nи самые старые пионеры в один день очнутся\n«новичками». Хоть многие и считают это проклятьем, но вечность без страха и смерти, когда её принять, дарит настоящее счастье."
        },

        "osd_wind_of_changes": {
            "name": "Ветер перемен",
            "background": "images/bg/ext_road_day.jpg",
            "text": "Чтобы разрушить Лагерь, нужно понять, как он работает, каким он был и каковы его пределы.\n\nВряд ли это просто, или даже возможно, но, быть может, удастся его расшатать?",
        },

        "osd_calm": {
            "name": "Штиль",
            "background": "bg osd_ext_camp_entrance_anim",
            "text": "Мир лагерей огромен, хоть и не кажется таковым.\nЭто система, прошедшая тысячи лет и сотни тысяч\nиспытаний.\n\nНесмотря ни на что, она выполняла свою цель.\nНиточник не первый, кто захотел с ней покончить.\n\n{i}И он никогда не справится один.{/i}"
        }
    }

    modal True

    add osd_achievements_info[achievement]["background"]

    add "osd_main_menu_frame"

    text osd_achievements_info[achievement]["name"]:
        font osd_link_font
        size 70
        xalign 0.5
        ypos 33
        antialias True
        kerning 2

    text osd_achievements_info[achievement]["text"]:
        font osd_link_font
        size 60
        xpos 130
        ypos 140

    textbutton "[osd_return_text]":
        style "osd_log_button" 
        text_style "osd_settings_link_main_menu_preferences" 
        xalign 0.1
        ypos 970
        action [
            Hide("osd_achievement_description"),
            ShowMenu("osd_achievements")
        ]