﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define audio.intro = "music/intro.mp3"
define fon1 = "fon1.png"
define mom = Character("Мама")
define k = DynamicCharacter("kuhmar_name")
define o = DynamicCharacter("olya_name")
define egor = DynamicCharacter("egor_name")
define sava = DynamicCharacter("saveliy_name")
define lyuba = Character("Люба")
define letov = Character("Егор Летов")
define miku = DynamicCharacter("miku_name")
define zhenya = DynamicCharacter("zhenya_name")
define Mi_Ku_root = 0
define Zhenya_root = 0
image black = "#000"
# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    jump prologue
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label intro:
    $ is_skipped = renpy.movie_cutscene("movies/intro.mpg")
    if is_skipped:
        o "НЕ СКИПАЙ КАТСЦЕНУ!!!!"
        jump intro
    jump prologue2

label prologue:
    $ kuhmar_name = "..."
    mom "Сынок, просыпайся! Нам пора!"
    k "Куда?"
    mom "Скоро узнаешь!"
    show bg bus
    "Меня привезли к ВДНХ, и мы с другими школьниками сели в автобус"
    "В автобусе я быстро уснул."
    $ olya_name = "???"
    scene bg a_front with fade
    show olga
    o "Просыпайся!"
    k "..."
    k "Где я?"
    o "Где-где? В МДКЦ! Самом технологичном лагере России!"
    jump intro
    
label prologue2:
    "\"Что еще за МДКЦ?\""
    "\"Ладно, без паники, надо придумать, что ей ответить...\""
    menu:
    
        "Что еще за МДКЦ?":
            o "Всмысле? МДКЦ это Международный Детский Компьютерный Центр. Твои родители тебя сюда отправили. Пошли в корпус, соня!"
    
        "\[Хранить молчание\]":
            o "Ладно, пошли, соня!"

    "Мы вышли из автобуса, подошли к какому-то зданию и я увидел табличку на стене."
    scene bg c_front with fade
    show olga
    "\"Корпус C...\""

    $ olya_name = "Оля"
    o "Кстати меня зовут Ольга Хитрова, ну или просто Оля, я твой новый куратор."
    k "Это типа как в Синем Ките, да?"
    "Оля пропустила эту остроумную шутку мимо ушей."
    o "А кто ты?"

    $ kuhmar_name = renpy.input ("Меня зовут", "", length=20,)
    $ kuhmar_name = "Кухмарь"

    o "Слишком сложно. Будем называть тебя пио... Кухмарь!"

    "\"Кухмарей много, а я один...\""
    "\"Ну да ладно\""
    scene bg room_c_5 with fade
    show olga
    "Мы зашли в корпус и вошли в 13-ую комнату."
    "Там уже были 3 человека."    

    o "Познакомся с твоими новыми соседями: Женя..."

    "Дальше я не слушал, я был в шоке."
    "\"Я буду жить с еще тремя людьми? Какое варварство! Что это за МДКЦ вообще? Это как колония строгого режима, или может хуже?! Как Мама вообще на это согласилась?!\""
    o "Все понял?"
    k "Ага..."

    "На самом деле я ничего не понял, но я не хотел сейчас с кем-то вести диалог."
    o "Вот и хорошо! Располагайся, через полчаса будет раздача карточек и обход кафедр."
    hide olga with moveoutright
    "Оля ушла."

    "\"Что за дурдом...\""
    $ saveliy_name = "???"
    $ egor_name = "???"
    $ zhenya_name = "???"
    show zhenya at left
    show egor at center
    show sava at right
    with dissolve
    zhenya "Проходи, садись, давай знакомиться!"
    "Я сел на свою койку."
    sava "Намасте, кухмарь!"
    k "Что-что?"
    sava "Намасте, говорю!"
    k "Это что значит?"
    sava "Это \"Здравствуй\" по хинди. Кстати я заметил что ты не обратил внимания на речь Оли. "
    sava "Так что давай еще раз всех тебе представлю: меня зовут Савелий, я тут 3-ий раз, а этих зовут Женя и Егор. Егор, кстати, тут 8-ой раз."
    $ saveliy_name = "Савелий"
    $ egor_name = "Егор"
    $ zhenya_name = "Женя"
    o "C2, строимся у корпуса!!!!"
    "\"Теперь точно как в колонии...\""
    scene bg c_front with fade
    show olga
    "Я вышел на улицу."
    o "Строимся по парам!"
    "Это тотальное неуважение к личному пространству"
    menu:
        "Встать с Женей":
            $ Zhenya_root += 1
            hide olga with moveoutleft
            show zhenya
            with fade
            "\"Похоже у нас с Женей было много общего\""
            "\"Странно, что ее поселили в мужском крыле. Как я понял ей не хватило места.\""
            "Я встал в пару с Женей"

        "Встать с Егором":
            $ Mi_Ku_root += 1
            hide olga with moveoutleft
            show egor with fade
            "\"Егор вроде адекватный парниша, нужно побольше узнать об МДКЦ, чтобы было проще выживать\""

    scene bg a_front with fade
    "Оля посчитала людей и наш отряд отправился к корпусу А."
    scene bg english with fade
    "Мы поднялись на 2-ой этаж и вошли на кафедру Английского языка"
    lyuba "Всем хеллоу, меня зовут Люба, я жила в Ирландии и я преподаю Английский язык. Здесь вы научитесь говорить, читать и писать на Английском языке и узнаете какова жизнь на западе!"
    "Я подумал что это не для меня и захотел забить, но в итоге записался. Не знаю что на меня нашло."
    "На кафедру записался только Савелий и я."
    scene bg python_class with fade
    "Дальше была кафедра Python. Ее вел какой-то задрот. У задрота конечно было имя, но я его не слушал и дал ему кликуху \"Задрот\"."
    "Я записался на Питон, ибо хотел научиться хоть чему-то полезному в этой жизни."
    scene bg music_class with fade
    "Следующей кафедрой была Музыка. Мы зашли на кафедру и я удивился."
    sava "О! Егор снова ведет музыку!"
    show letov
    "МУЗЫКУ ВЁЛ ЕГОР ЛЕТОВ! ЛЕТОВ!!!!!"
    letov "Здравствуйте, меня зовут Егор и я препод музыки, здесь мы будем учить мои песни, возрождать коммунизм и не только!"
    "\"Он же мертв уже лет 10!\""
    k "Вы же умерли 10 лет назад! Как вы тут стоите?"
    letov "Всмысле?"
    k "Ладно..."
    "\"Что за дурдом...\""
    "На всякий случай я записался и на Музыку."
    scene bg a_second_floor
    "Следующей была кафедра C и Pascal. Но я был на такой стадии сознания, на котором я вообще не понимал, что происходит и соответственно ничего не запомнил."
    scene bg d_front
    "Потом мы пошли в корпус D. Там была столовка, танцы и 3D Графика."
    scene bg 3d
    "Я записался на 3D графику, ее вел Сасаткин"
    scene bg food
    "После обхода кафедр мы пошли ужинать."
    "Я сел за стол один ибо не хотел с кем либо говорить, но тут я услышал приятный, женский голос."
    show miku
    $ miku_name = "???"
    miku "Можно с тобой сесть пожалуйста?"
    k "Конечно..."
    "Я это сказал с неохотой ибо хотел посидеть один"
    $ miku_name = "Ми Ку"
    miku "Как тебя зовут? Меня - Ми Ку!"
    k "А меня Кухмарь... Стоп, что это за имя?"
    miku "Я школьница из Северной Кореи! Приехала в лагерь чтобы изучить русскую культуру!"
    "\"Стоп, а так можно было?\""
    k "Интересно..."
    "Я начал есть ужин. Там было картофельное пюре, котлета (похожая на подошву) и очень сладкий чай."
    miku "А что это такое?"
    "Она показала на пюре."
    k "Это картофельное пюре"
    miku "А что значит \"картофельное\"?"
    "\"Она прикалывается?\""
    menu:
        "Ты прикалываешся?":
            $ Zhenya_root += 1
            k "Ты прикалываешься?"
            miku "Пошел ты нахрен грязный капиталист!"
            "*Мне прилетел тяжелый коммунистический лещ*" with hpunch
        
        "Объяснить что такое картофель":
            $ Mi_Ku_root += 1
            k "Ну картофель это такой овощ... У вас что, картошки нет?"
            miku "Первый раз вижу!"
            "\"Она или отличный актер или в КНДР все реально плохо...\""
    scene bg c_front
    "Я закончил пожирать свою порцию биоматериала и пошел в корпус."
    scene bg room_c_5
    "\"Спать хочется пиздец...\""
    "Я вошел в свою комнату и упал на кровать."
    "Но прямо через 5 минут, Оля начала орать" with fade

    show olga
    with dissolve

    o "С2, СТРОИМСЯ НА ВЕЧЕРКУ!"
    "\"Это еще что?\""
    scene bg c_front
    "Я опять же вышел на улицу."
    scene bg d_front
    "Мы пошли в корпус D." 
    scene bg act_room
    "В корпусе мы вошли в подобие актового зала."
    "Внезапно Оля куда-то ушла"
    show olga
    "Через несколько минут заиграла попса и на сцену вышла Оля."
    o "Привет МДКЦ! Сегодня у нас очень важное событие! Прошу Ольгу Васильевну на сцену!"
    hide olga
    "Дальше я ни смотрел, ни слушал, ибо я был в полном афиге."
    "\"Шо тут происходит? Куда я попал? Надо позвонить маме!\""
    "Я достал телефон, но сети не было."
    "\"Бля...\""
    "Прошел где-то час полнейшего ахуевания и так называемая вечерка кончилась." with fade
    scene bg room_c_5
    "Я сразу же пошел в свою комнату и упал на кровать."
    "\"Что за дурдом...\""
    
label day1:
    "Меня разбудила громкая музыка. Я не понимал, что происходит, пока я не услышал этот голос."
    show olga
    o "Вставай, уже 9 утра!"
    "Это был голос из преисподней. Голос дьявола."
    "Я неспешно встал"
    o "А почему ты в одежде?"
    k "Не знаю…"
    "На самом деле я знал, почему я в одежде, но мне было лень объяснять что-либо."
    scene bg c_front
    "Я пошел на построение и увидел Женю и Ми Ку. Впереди был очень тяжелый выбор."
    menu:
        "Встать с Женей":
            $ Zhenya_root += 1
            show zhenya with fade
            "Я встал с Женей."
            "Не знаю почему для меня был так важен этот выбор ибо мне надо в 1-ую очередь выбраться. Похоже я уже начинаю привыкать к этой, новой жизни кухмаря…"
            zhenya "Доброе Утро!"
            k "Доброе..."
            "\“Нихрена оно не доброе\”"
            zhenya "Как спалось?"
            k "Нормально, а тебе?"
            "Я решил завести диалог."
            zhenya "Ты не представляешь что мне приснилось!"
            k "И что же?"
            zhenya "Ты!"
            k "?"
            k "И что же там было?"
            zhenya "Мы с тобой танцевали на дискотеке"
            "\“Она долбанутая какая-то\”"
            k "Ясно..."

        "Встать с Ми Ку":
            $ Mi_Ku_root += 1
            show miku with fade
            "Я пошел с Ми Ку."
            "Не знаю почему для меня был так важен этот выбор ибо мне надо в 1-ую очередь выбраться. Похоже я уже начинаю привыкать к этой, новой жизни кухмаря…"
            miku "Доброе Утро!"
            k "Доброе…"
            "\“Нихрена оно не доброе\”"
            miku "Как спалось?"
            k "Нормально, а тебе?"
            "Я решил завести диалог."
            miku "Ты не представляешь что мне приснилось!"
            k "И что же?"
            miku "Потом расскажу..."
            "\“Ну и хер с ним...\”"

        "Встать одному":
            "Я встал в полном одиночестве в конце строя."
            "\"Не стоит доверять этим людям...\""
    
    scene bg d_front
    "Тем временем мы пришли в корпус D"
    scene bg food
    "Мы дошли до столовой."
    "Я хотел помыть в раковине руки, но не было мыла, а вода вмиг отморозила мне руки. Я зашел в столовку и решил сесть за стол. Но с кем?"
    menu:
        "С кем сесть?"
    
        "С Ми Ку":
            $ Mi_Ku_root += 1
            "\“Женя и мои друзья по несчастью были какими-то не совсем нормальными. Поэтому я сел с Ми Ку. Она была более-менее нормальная.\”"
            show miku with fade
            
    
        "С Женей":
            $ Zhenya_root += 1
            "\“Ладно, сяду с Женей\”"
            show zhenya with fade

        "Сесть с сокомнатниками":
            "\"Сяду с сокомнатниками\""

    "Я ничего не говорил ибо был в тяжелейших раздумиях."
    scene bg d_front
    "Я вышел из столовой и направился к корпусу."
    "Но тут я увидел её…"
    show olga
    o "А куда это мы идем?"
    k "В корпус"
    o "А надо на кафедры!"
    k "Окей…"
    hide olga
    scene bg english
    "Я пошел на кафедры."
    "Первой кафедрой был Английский язык."
    # Показать Любу
    lyuba "Привет, Кухмарь!"
    k "Шалом"
    
    lyuba "Сегодня у нас изучение Английской культуры! Поэтому мы будем смотреть \“Стар против сил зла\”."
    "\"Я ненавижу эти мультики для маленьких детей, но ладно.\""
    "Мы посмотрели несколько серий и кафедра кончилась. Я пошел к выходу."
    lyuba "Стой, а как же баллы?"
    "Я не знал о чем она говорит и просто стоял в ступоре."
    lyuba "Карточку дай, говорю."
    "Я дал ей карточку и она в ней расписалась."
    lyuba "А теперь можешь идти."
    # Убрать Любу
    scene bg a_road
    with fade
    menu:
        "Далее я мог выбрать между 3D Графикой и Музыкой."
        "Пойти на 3D графику":
            scene bg 3d
            show zhenya
            with fade
            "Я пошёл на кафедру 3D и встретил там Женю."
            zhenya "Привет"
            k "Шалом!"
            "Мы с ней провели весь день на 3D. Мы даже не обращали внимания на препода и саму кафедру. Мы обсуждали наши жизни часами напролёт."
            "Я чувствовал какую-то связь между нами. Может быть это и называют искрой… Я не знаю. Я чувствовал не просто любовь, я чувствовал что мы были созданы друг для друга. Мы пропустили обед, полдник, ужин и даже вечерку."
            "Я был влюблён."
            $day1_choice = False
            
        "Пойти на Музыку":
            scene bg music_class
            show miku
            with fade
            "Я пошёл на кафедру Музыки и встретил там Ми Ку."
            miku "Привет!"
            k "Шалом!"
            "Мы с ней провели весь день на Музыке. Мы играли на гитаре Гражданскую оборону"
            "Я был влюблён."
            $day1_choice = True
            
    scene bg c_front
    if day1_choice:
        $ Mi_Ku_root += 1
        show miku at left
        show olga at right
        with fade
        o "Ну и где вы были?"
        k "На Музыке."
        o "Ладно, завтра разберёмся. А теперь идите спать!"
        "Мы зашли в комнату."
        scene bg room_c_5
        show egor
        with fade
    else:
        $ Zhenya_root += 1
        show zhenya at left
        show olga at right
        with fade
        o "Ну и где вы были?"
        k "На Музыке."
        o "Ладно, завтра разберёмся. А теперь идите спать!"
        "Мы зашли в комнату."
        scene bg room_c_5
        show egor
        with fade
    egor "Здарова, любовники!"
    "Он начал угарать над нами."
    "Я пошёл спать."
    jump day2

label day2:
    scene bg room_c_5 with fade
    "Утром я опять проснулся от громкой музыки."
    " Я уже начинаю привыкать к этому."
    "Я оделся и вышел на улицу."
    if Mi_Ku_root == 5:
        jump MikuRoot
    elif Zhenya_root == 5:
        jump ZhenyaRoot
    else:
        jump BadassRoot
        
label ZhenyaRoot:
    scene bg food with fade
    "В столовую я пошел с Женей. Она самая милая и красивая девушка лагеря. Сел я тоже с ней."
    show zhenya with dissolve
    zhenya "А ты пойдешь на дискотеку?"
    k "А она будет?"
    "\"Я не знал что в таких местах бывают дискачи\""
    zhenya "Да, будет."
    k "Пойду конечно!"
    "Это был идеальный план. План для того чтобы признаться ей в любви."
    "Весь остальной день прошел незаметно. Я думал только о ней."
    scene bg d_night with fade
    "И вот настало время. Время дискотеки." 
    show zhenya with dissolve
    "Она началась. Играл всякий драйвовый шлак. И тут начался медляк. Это мой шанс."
    k "Давай станцуем?"
    zhenya "Я же не умею!"
    k "Я тебя научу!"
    "Я взял её за руку и мы начали кружиться в танце. Я чувствовал будто моё сердце сейчас разорвётся. Я решил сказать это."
    # Сделать кружение в танце
    k "Женя?"
    zhenya "Да?"
    k "Я… "
    zhenya "Что?"
    k "Я тебя люблю!"
    zhenya "Правда?"
    k "ДА!"
    # Звуки ломающейся спины
    "Тут я услышал как проломалась сцена. Я повернулся и увидел фонтан черной массы."
    "???" "Это же нефть!"
    "Раздался звук танков и вертолётов. Я услышал громкие приказы на английском."
    "Прилетели американцы. Они прилетели за нефтью. Я взял Женю за руку и мы побежали в лес."
    "Позади оставались ужасающие крики пионеров. Тут я увидел впереди американцев с автоматами. Я оглянулся и понял что мы окружены."
    zhenya "Я должен тебе кое что сказать…"
    k "Всмысле “должен”?"
    "И тут пришёл он. Наше спасение. Летов. С автоматом. Офигеть."
    show zhenya at left with move
    show minigun at center with dissolve
    letov "БЕГИТЕ ГЛУПЦЫ, Я ИХ ОТВЛЕКУ!"
    "Мы с Женей побежали"
    letov "ЗА КОММУНИЗМ! ЗА МДКЦ!"
    # Анимация смерти
    scene black with fade
    "Мы бежали где-то полчаса, пока не выдохлись."
    show bg forest night with fade
    show zhenya with dissolve
    k "Вроде пронесло…"
    zhenya "Да…"
    "Мы устроили что-то типа привала."
    k "Так что ты хотела сказать?"
    zhenya "Я.."
    k "Что?"
    zhenya "Я мальчик."
    "\"ЧТО?! Нет.. Не может быть! Может я ослышался?\""
    k "Что-что?"
    zhenya "Я не девочка, я мальчик."
    "\"Нет… Нет…\""
    k "Господи…"
    "Тут я услышал шелест кустов."
    "Из кустов появился Савелий с Егором."
    show zhenya at left
    with move
    show sava at center
    show egor at right
    with dissolve
    sava "Я думал вы уже оба покинули этот мир…. В натуре!"
    k "Лучше бы сдох…"
    zhenya "Слава богу вы пришли!"
    egor "Мы нашли выход отсюда! Пошли!"
    k "Куда?"
    sava "К автобусу. Нам его армия подогнала."
    k "Ладно…"
    scene black with fade
    "Мы пошли сквозь лес и удивительно быстро добрались до остановки, где стоял автобус. В автобусе не было водителя, но это никого не волновало."
    scene bg bus ending with fade
    "Мы вошли в автобус и автобус поехал. Не знаю как, но после американцев и трапов мне было все равно."
    "Мы ехали, ехали, и тут я заметил. Егора с Женей нет. Они исчезли. Остался только Савелий."
    show sava with dissolve
    k "Сава, где все?"
    sava "Ты уходишь из этого мира, а они остаются здесь."
    k "Всмысле?"
    sava "Ты же понимаешь что все эти американцы, Летов, нефть. Это всё нереально. Ты все это время был в другой вселенной вне времени и пространства."
    "\"Нихрена себе...\""
    k "И кто меня сюда отправил?"
    sava "Не знаю. Тебя сюда отправили чтобы ты исправил свою жизнь."
    k "Ясно… И что же произойдёт когда мы доедем?"
    sava "Ты вернёшься к своей жизни, в свою вселенную."
    k "Ясно…"
    "\"Нифига не ясно, но ладно. Я хочу домой.\""
    "Тут меня начало клонить в сон и я уснул."
    scene bg bus home with fade
    "Проснулся я в автобусе. В городском. Он стоял на остановке рядом с моим домом."
    scene black with fade
    "После этого путешествия я будто начал новую жизнь."
    "У меня появились друзья, увлечения, личная жизнь." 
    "Я в первый раз поехал в МДКЦ. Я там провел много смен. Потом стал ассистентом, потом педагогом."
    "Он конечно отличался от МДКЦ в той вселенной, но он был даже лучше."
    jump end

label MikuRoot:
    scene bg food with fade
    "В столовую я пошел с Ми Ку. Она самая милая и красивая девушка лагеря. Сел я тоже с ней."
    show miku with dissolve
    miku "А ты пойдешь на дискотеку?"
    k "А она будет?"
    "\"Я не знал что в таких местах бывают дискачи\""
    miku "Да, будет."
    k "Пойду конечно!"
    "Это был идеальный план. План для того чтобы признаться ей в любви."
    "Весь остальной день прошел незаметно. Я думал только о ней."
    scene bg d_night with fade
    "И вот настало время. Время дискотеки." 
    show miku with dissolve
    "Она началась. Играл всякий драйвовый шлак. И тут начался медляк. Это мой шанс."
    k "Давай станцуем?"
    miku "Я же не умею!"
    k "Я тебя научу!"
    "Я взял её за руку и мы начали кружиться в танце. Я чувствовал будто моё сердце сейчас разорвётся. Я решил сказать это."
    k "Женя?"
    miku "Да?"
    k "Я… "
    miku "Что?"
    k "Я тебя люблю!"
    miku "Правда?"
    k "ДА!"
    "Тут я услышал как проломалась сцена. Я повернулся и увидел фонтан черной массы."
    "???" "Это же нефть!"
    "Раздался звук танков и вертолётов. Я услышал громкие приказы на английском."
    "Прилетели американцы. Они прилетели за нефтью. Я взял Ми Ку за руку и мы побежали в лес."
    "Позади оставались ужасающие крики пионеров. Тут я увидел впереди американцев с автоматами. Я оглянулся и понял что мы окружены."
    "Я должна тебе кое что сказать…"
    "И тут пришёл он. Наше спасение. Летов. С автоматом. Офигеть."
    show zhenya at left with move
    show letov minigun at center with dissolve
    letov "БЕГИТЕ ГЛУПЦЫ, Я ИХ ОТВЛЕКУ!"
    "Мы с Ми Ку побежали"
    letov "ЗА КОММУНИЗМ! ЗА МДКЦ!"
    scene black with fade
    "Мы бежали где-то полчаса, пока не выдохлись."
    show bg forest night with fade
    show miku with dissolve
    k "Вроде пронесло…"
    miku "Да…"
    "Мы устроили что-то типа привала."
    k "Так что ты хотела сказать?"
    miku "Я.."
    k "Что?"
    miku "Я тоже люблю тебя!"
    "Тут я услышал шелест кустов."
    "Из кустов появился Савелий с Егором."
    show miku at left
    with move
    show sava at center
    show egor at right
    with dissolve
    sava "Я думал вы уже оба покинули этот мир…. В натуре!"
    k "Аллелуя!"
    miku "Слава богу вы пришли!"
    egor "Мы нашли выход отсюда! Пошли!"
    k "Куда?"
    sava "К автобусу. Нам его армия подогнала."
    k "Ладно…"
    scene black with fade
    "Мы пошли сквозь лес и удивительно быстро добрались до остановки, где стоял автобус. В автобусе не было водителя, но это никого не волновало."
    scene bg bus ending with fade
    "Мы вошли в автобус и автобус поехал. Не знаю как, но после американцев и трапов мне было все равно."
    "Мы ехали, ехали, и тут я заметил. Егора с Ми Ку нет. Они исчезли. Остался только Савелий."
    show sava with dissolve
    k "Сава, где все?"
    sava "Ты уходишь из этого мира, а они остаются здесь."
    k "Всмысле?"
    sava "Ты же понимаешь что все эти американцы, Летов, нефть. Это всё нереально. Ты все это время был в другой вселенной вне времени и пространства."
    "\"Нихрена себе...\""
    k "И кто меня сюда отправил?"
    sava "Не знаю. Тебя сюда отправили чтобы ты исправил свою жизнь."
    k "Ясно… И что же произойдёт когда мы доедем?"
    sava "Ты вернёшься к своей жизни, в свою вселенную."
    k "Ясно…"
    "\"Нифига не ясно, но ладно. Я хочу домой.\""
    "Тут меня начало клонить в сон и я уснул."
    scene bg bus home with fade
    "Проснулся я в автобусе. В городском. Он стоял на остановке рядом с моим домом."
    scene black with fade
    "После этого путешествия я будто начал новую жизнь. У меня появились друзья, увлечения, личная жизнь."
    "Я в первый раз поехал в МДКЦ. Я там провел много смен. Потом стал ассистентом, потом педагогом."
    "Потом я встретил Ми Ку. Она была студенткой в ЯРГУ. Она меня не помнила. Ну и ладно."
    jump end

label BadassRoot:
    scene bg food with fade
    "Я пошел в столовую один. Мне все не нравились."
    "Так и прошел весь день. И на дискач я пошёл один."
    scene bg d_night with fade
    "Я танцевал, танцевал и я услышал как проломилась цена. Я повернулся и увидел темный фонтан."
    "???" "Это же нефть!"
    "Раздался звук танков и вертолётов. Я услышал громкие приказы на английском."
    "Прилетели американцы. Они прилетели за нефтью. Я как настоящий трус убежал." 
    "Позади оставались ужасающие крики пионеров. Тут я увидел впереди американцев с автоматами. Я оглянулся и понял что я окружён." 
    "И тут пришёл он. Моё спасение. Летов. С автоматом. Офигеть."
    show minigun with dissolve
    letov "БЕГИ ГЛУПЕЦ, Я ИХ ОТВЛЕКУ!"
    "Я побежал."
    letov "ЗА КОММУНИЗМ! ЗА МДКЦ!"
    scene black with fade
    "Я бежал где-то полчаса, пока не выдохся." 
    scene bg forest night
    k "Вроде пронесло…"
    "Я устроил что-то типа привала."
    "Тут я услышал шелест кустов."
    "Из кустов появился Савелий с Егором."
    show sava at center
    show egor at right
    with dissolve
    sava "Я думал ты уже покинул этот мир…. В натуре!"
    k "Аллелуя!"
    egor "Мы нашли выход отсюда! Пошли!"
    k "Куда?"
    sava "К автобусу. Нам его армия подогнала."
    k "Класс!"
    scene black with fade
    "Мы пошли сквозь лес и удивительно быстро добрались до остановки, где стоял автобус. В автобусе не было водителя, но это никого не волновало."
    scene bg bus ending with fade
    "Мы вошли в автобус и автобус поехал. Не знаю как, но после американцев и Летова мне было все равно."
    "Мы ехали, ехали, и тут я заметил. Егора с Женей нет. Они исчезли. Остался только Савелий."
    show sava with dissolve
    k "Сава, где все?"
    sava "Ты должен уходить из этого мира, а они остаться здесь."
    k "Всмысле?"
    sava "Ты же понимаешь что все эти американцы, Летов, нефть. Это всё нереально. Ты все это время был в другой вселенной вне времени и пространства."
    "\"Нихрена себе...\""
    k "И кто меня сюда отправил?"
    sava "Не знаю. Тебя сюда отправили чтобы ты исправил свою жизнь."
    k "Ясно… И что же произойдёт когда мы доедем?"
    sava "Ты не доедешь."
    k "Почему?"
    sava "Ты не исправился."
    scene black with fade
    "Тут меня начало клонить в сон и я уснул."
    $ Mi_Ku_root = 0
    $ Zhenya_root = 0
    jump prologue

label end:
    pass
