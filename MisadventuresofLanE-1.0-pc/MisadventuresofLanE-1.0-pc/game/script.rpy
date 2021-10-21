# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define super = Character("Human Supervisor")
define super2 = Character("Human Supervisor")
define l = Character('Lan-E', color="#F7D762")
define n = Character('Narrator', color="#1EC8F1")
define ch = Character('Child')
define m = Character("Mother")
define ib = Character("Fun Fact")
define man_queue = Character("Man in queue")
define garbage_crew = Character("Garbage crew")
define sci1 = Character("Scientist 1")
define sci2 = Character("Scientist 1")
define pres = Character("President")
define pcs = Character("Peach Corp Security")
define pbot = Character("Peachbots")
define pb1 = Character("Passerby1")
define pb2 = Character("Passerby2")
define pb1 = Character("Passerby")
default pressed = False
default code_attempts = 0
default code = 0
# default sc_thing = False
# The game starts here.

# init python:
#     config.screen_width = 2360
#     config.screen_height = 1640

label start:

    $ renpy.suspend_rollback(True)

    scene s1b1

    n "In the distant future, Peach Corp., the largest manufacturer of anything electronic, has made millions of robots to mine metals out of ores to meet the demand for the “new” and “top-of-the-line” smartphones that the corporation released every week."

    scene s1b2
    show lanemining
    l "REE is what we mine, to help the world feel fine! Metal ores are what we take, to replace the phones that break!"
    hide lanemining

    ib "REEs, or rare earth elements, are elements 57 to 71 on the periodic table. Although scientists believe that there are plenty of REEs on the Earth’s crust, the ores from which they are extracted are hard to find, which is the reason why they are referred to as being rare."

    "Help Lan-E identify the REE!"
    label element_game:
        call screen element_game

    label incorrect:
        n "Looks like you've mixed up your elements! Give it another go, and make sure you remeber that F, H and C are not rare!"
        call element_game from _call_element_game

    label correct:
        n "Nice work! Neodymium is an example of an REE!"



    screen element_game():
        add "s1b2"
        modal True

        imagebutton auto "la_%s":
            focus_mask True
            # hover SetVariable("screen_tooltip", "La")
            # unhovered SetVariable("screen_tooltip", "")
            # action la_ckd
            action Jump ("incorrect")


        imagebutton auto "c_%s":
            focus_mask True
            # hover SetVariable("screen_tooltip", "C")
            # unhovered SetVariable("screen_tooltip", "")
            # action c_ckd
            action Jump ("correct")

        imagebutton auto "nd_%s":
            focus_mask True
            # hover SetVariable("screen_tooltip", "C")
            # unhovered SetVariable("screen_tooltip", "")
            # action c_ckd
            action Jump ("incorrect")

        imagebutton auto "f_%s":
            focus_mask True
            # hover SetVariable("screen_tooltip", "C")
            # unhovered SetVariable("screen_tooltip", "")
            # action c_ckd
            action Jump ("incorrect")

    show s1super
    super "Robots! Form a single file line and go to Mine 5771! I repeat, form a single file line and go to Mine 5771!"
    hide s1super
    show s1lane2
    n "Just as Lan-E was merging into the line, he hits his positioning chip and it falls to the ground."


    #Scene 2
    scene s1b1
    show lanereprogram
    n "Without his positioning chip, Lan-E misread the coordinates and stumbled upon the hustle and bustle of Neopolis."
    hide lanereprogram

    show lanequestionmark
    ch "Look mom! It’s a mining robot!"
    m "Oh, you’re right! I wonder what it’s doing here?"
    man_queue "Can’t wait to get the Peach 17! The Peach 16 from a month ago doesn’t have all the new features."
    hide lanequestionmark
    show lanereedetected
    l "*detects REE in man in queue’s Peach 17* REE detected. Ore found and ready for extraction!"
    hide lanereedetected
    #Scene 3
    show s3f1
    man_queue "Finally, the latest Peach 17! Goodbye, last month’s Peach 16. You will not be missed."
    hide s3f1
    show s2lane
    n "Lan-E zoomed right past dozens of customers to get to the man’s REE-filled phone. In the trash, he found hundreds of discarded units, and all of the REEs that come along with them!"

    ib "53.6 million tonnes of e-waste dumped globally last year and just 17.4\% of the world’s discarded electronics was recycled."
    n "Guess the stat! Guess the right statistic about electronic waste recycling."
    label mg2:
        menu:
            "Every year, an estimated _______ worth of high-value metals such as gold, silver, copper, platinum, and REEs are just dumped or burned rather than recycled and reused."

            "$57 billion":
                "Spot on! Nice work!"

            "$5,000":
                "Not quite, try again!"
                call mg2 from _call_mg2

            "$500 million":
                "Not quite, try again!"
                call mg2 from _call_mg2_1

            "$500 gazillion":
                "Not quite, try again!"
                call mg2 from _call_mg2_2

    label mg3:
        menu:
            "By 2030, how many tonnes of e-waste will have been dumped globally in a year?"

            "500 billion tonnes":
                "Not quite, try again!"
                call mg3 from _call_mg3

            "10 million tonnes":
                "Not quite, try again!"
                call mg3 from _call_mg3_1

            "74 million tonnes":
                "Right on! Great work!"

            "500 kg":
                "Not quite, try again!"
                call mg3 from _call_mg3_2

    hide s2lane
    show laneinbin
    n "As Lan-E reached down the trash bin, he fell in and got stuck!"
    hide laneinbin
    show laneintruck
    garbage_crew "This one’s ready! Dump this one in!"
    hide laneintruck

    #Scene 4
    scene s4b1
    n "Lan-E found itself in a mountain of garbage, where trash from all of Neopolis gets dumped."
    show lanereedetected
    scene lfbg
    l "Detecting multiple REE ores. Sample collection mode: initiated."

    ib "Landfills are areas that are dedicated to be a place where garbage gets disposed. Typically, trash collected by a city is first sent to a processing centre, where they are separated into different types on conveyor belts. The ones that are not in a category are collected and sent to the landfill as garbage."


    init python:
        locker_items = []
        locker_items.append(Item("Purple Rock", 801,266,54,70))
        locker_items.append(Item("Golden Rock", 974,486,81,62))
        locker_items.append(Item("Purple Rock 2", 876,788,71,72))
        locker_items.append(Item("Circuit Board",939,907,96,70))
        # locker_items.append(Item("mirror",528,73,91,129))
        # locker_items.append(Item("photo",515,296,98,99))
        # locker_items.append(Item("pencil case",380,153,109,134))
        # locker_items.append(Item("book",346,0,80,83))
        # locker_items.append(Item("card",648,159,83,61))
        # locker_items.append(Item("flower",295,238,43,48))

    label ree_finding:
        $ start = renpy.time.time()
        # this sets all the items back to not found
        $ resetItems(locker_items)
        # which image set to use
        $ hidden_files = "locker_%s.png"
        # randomize the list and pick 5 items
        $ hidden_items = renpy.random.sample(locker_items,4)
        # set number of hints
        $ num_hints = 3
        # set number of extra clicks
        $ num_clicks = 0


        show locker_empty
        "Get ready to find the items!"

        $ showitems = True
        call screen hidden_object

        show locker_empty
        $ elapsed = round(renpy.time.time() - start)
        "Result: [_return] in [elapsed] seconds with [num_clicks] extra clicks!"

    $ showitems = False

    # $ ui.close()

    hide lanereedetected
    scene s1b2
    show lanesamplecollected
    l "Sample collection complete. Reinitializing positioning system. Route set for: Mine 5771."
    hide lanesamplecollected

    #Scene 5
    show newmineright
    l "I have detected ore samples for your analysis. Recommendation: Convert Landfill 1775 to a new mine"
    show s5super
    super2 "These are discarded electronics, and these are useless! Why do you want Peach Corp to waste our capital on a useless suggestion?"
    l "Unidentified ores have significantly higher REE content than regular ores. Converting the landfill into a mine is projected to lead to a 15\% increase in overall profit margins."
    super2 "Nonsense! Hey, you! *gestures to other Lan-E units* Bring this defective bot to the Reprogrammer."

    #Scene 6
    scene reprogramming_background
    n "Lan-E was brought to the Reprogrammer, a facility that wipes out and reinstalls the program on all defective Peach Corp robots."
    l "New directive: Relay suggestion to Peach Corp. Research and Development department"
    hide lanenewmine
    hide s5super
    # Game: Help Lan-E escape! Input the code to the door of the Reprogrammer. Hint will be given after 3 incorrect tries.
    # $ ca = 0
    while (code != "1577"):
        if code_attempts > 3:
            "Try 1577!"
        $ code = renpy.input("Help Lan-E escape! Input the code to the door of the Reprogrammer.", allow="1234567890", length = 4)
        if (code != "1577"):
            "Opps! Try again!"
        $ code_attempts += 1

    "Nice work! That was the code!"

    #Scene 7
    scene scib
    show f_sci
    sci1 "Oh, what’s a mining bot doing here?"
    show newmineright
    l "I have detected ore samples for your analysis. Recommendation: Convert Landfill 1775 to a new mine. Unidentified ores have significantly higher REE content than regular ores. Mining of new ores is projected to lead to a 15\% increase in overall profit margins."
    sci1 "Oh, wow! Changing our feedstream will also decrease our greenhouse gas emissions, but I don’t know by how much."

    ib "Greenhouse gases are gases in the atmosphere that absorb and reemits energy, thus causing the greenhouse effect, which warms the planet and makes life possible."
    ib "These gases act like a blanket and keep the whole planet warm, but too much of these, like carbon dioxide and methane, can make the planet hotter and cause the climate to change drastically. Our carbon footprint is a measure of the total amount of greenhouse gases that are produced from what we do."
    n "EnviroStats. Help the scientist make a case for recovering REE from electronic waste by choosing the right numbers."
    label mg4:
        menu:
            "How much carbon footprint is made when mining 1 kg neodymium oxide?"

            "12 kg CO2-Eq to 66 kg CO2-Eq":
                "Perfect!"

            "1 g CO2-Eq":
                "Not quite, try again!"
                call mg4 from _call_mg4_1

            "10,000 kg CO2-Eq to 100,000 kg CO2-Eq":
                "Not quite, try again!"
                call mg4 from _call_mg4

            "1,550,000 kg":
                "Not quite, try again!"
                call mg4 from _call_mg4_2

    label mg5:
        menu:
            "How much does neodymium sell for?"

            "$1000/kg":
                "Not quite, try again!"
                call mg5 from _call_mg5

            "$0.26/kg":
                "Not quite, try again!"
                call mg5 from _call_mg5_1

            "$470/g":
                "Not quite, try again!"
                call mg5 from _call_mg5_2

            "$95/kg":
                "Right on! Great work!"

    label mg6:
        menu:
            "How much does gadolinium sell for?"

            "$100/tonne":
                "Not quite, try again!"
                call mg6 from _call_mg6

            "$1/g":
                "Not quite, try again!"
                call mg6 from _call_mg6_1

            "$20,010/kg":
                "Right on! Great work!"

            "$65.59/kg":
                "Not quite, try again!"
                call mg6 from _call_mg6_2

    sci1 "Great! I can bring this up to the Peach Corp. President, and I am sure that he will give us the green light to fast track this suggestion."

    #Scene 8
    scene presbg
    show pres
    show sci
    sci2 "Mr. President, I believe we have something that could slowly make our operations more sustainable if we shift our mining source."
    hide sci
    pres "What are you proposing exactly?"
    show sci
    sci2 "If we recover the REEs from our phones instead of constantly having to mine them from the Earth, we would decrease our carbon footprint substantially!"
    hide sci
    pres "That is absolutely pointless. The way we make money now is the way we have made money since then."
    show sci
    sci2 "But, Sir! If we keep doing what we do, we will run out of REEs to mine!"
    hide sci
    pres "And that’s exactly why we can charge them even more in the future! Why do you think we make such easily breakable phones?"
    show sci
    sci2 "But --"
    hide sci
    pres "Silence! This madness ends here. If you tell another soul about this, you know what’s waiting for you."

    #Scene 9

    scene s2b1
    show sci
    n "Despite the President’s threats, the scientist was still determined to let the world know of the better alternative to Peach Corp.’s operations."
    sci2 "This discovery is too good to be kept in the shadows… Lan-E, I need you to pass this on to the people. Oh, you’ll also need some of these upgrades, so they can see that what we’re doing is possible!"
    hide sci

    ib "To help Lan-E detect and extract REEs from e-waste, the scientist implanted a lanmodulin core inside Lan-E. Lanmodulin is a special protein that can bind to REEs."
    ib "It essentially has three, very small hands that can catch the REEs from e-waste, which is important since e-waste has different types of materials in it, and we only want to get REEs!"
    ib "Proteins are special molecules made up of building blocks called amino acids. There are 20 different amino acids that you can mix and match, and the shapes that proteins take depends on what amino acids they are made out of!"
    # show p1
    # ib "Primary structure is the order in which the amino acids are connected. That’s right, the order of the amino acids matters!"
    # hide p1
    # show p2
    # ib "Secondary structure comes from the interactions in the protein backbone, and they come as either alpha helices and beta sheets."
    # hide p2
    # show p3
    # ib "Tertiary structure is the 3-D structure of the protein that comes from interactions of the side chains in the amino acids."
    # hide p3
    # show p4
    # ib "Quaternary structure is the structure that is made from two or more protein chains."
    # hide p4
    #
    # ib "Let's test what we just learned! Which of the following pictures is the primary structure?"
    #
    # label protein:
    #     call screen protein
    #
    # label pincorrect:
    #     n "Looks like you mixed up your protein structures, remember, the primary structure is just the sequence of amino acids!"
    #     call protein# from _call_protein
    #
    # label pcorrect:
    #     n "Nice work!"
    #
    # screen protein():
    #     add "s1b2"
    #     modal True
    #
    #     imagebutton auto "gp1_%s":
    #         focus_mask True
    #         # hover SetVariable("screen_tooltip", "La")
    #         # unhovered SetVariable("screen_tooltip", "")
    #         # action la_ckd
    #         action Jump ("pcorrect")
    #
    #
    #     imagebutton auto "gp3_%s":
    #         focus_mask True
    #         # hover SetVariable("screen_tooltip", "C")
    #         # unhovered SetVariable("screen_tooltip", "")
    #         # action c_ckd
    #         action Jump ("pincorrect")

    show laneinstall
    n "With Lan-E fully equipped, it is ready to inform the public and face whatever the Peach Corp. President throws in its way!"
    hide laneinstall
    #Scene 10

    show laneav
    l "Audiovisual device, located! Preparing for port connection and video transmission."
    hide laneav
    show s1super
    pcs "There it is! Get them, Peachbots!"
    hide s1super
    show 3bots
    pbot "Target: located. Lock on!"
    hide 3bots

    ######
    show bot_l
    show laneav
    l "Connecting to audiovisual device."
    show scipres
    sci2 "Everyone! The Peach Corp. President is trying to shut down a greener and cheaper alternative for making easily replaceable Peach phones, so he can make more money off of you! If you don’t believe me, you’ll believe him!"
##########
    scene s2b1
    show pb
    pb1 "What?! So that’s why my Peach 16 is worn out just after 2 weeks!"
    pb2 "Me, too! And they release the Peach 17 with “added features” to solve problems that shouldn’t exist in the first place!"
    pb1 "We should all boycott Peach Corp!"
    pb2 "Yeah! Boycott Peach Corp!"
    scene s4b1
    # show locker_empty
    show lanemining
    n "With public opinion pressuring Peach Corp., the President stepped down from his position. The board of directors then appointed the scientist as the new president, and Peach Corp. ushered a new era of sustainability with the release of NeoPeach, a phone made from recycled materials."

    scene lanecredits
    n "Thank you for playing our game! We hope you had fun following LanE through his adventures! :)"
    $ MainMenu(confirm=False)()
