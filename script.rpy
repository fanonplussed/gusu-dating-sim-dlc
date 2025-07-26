label start: ## this bit exists to help with playtesting

    ## jump start_real
    ## we can skip directly to start_real when shipping the game, or comment it out for playtesting

    "This let's us quickly skip to a specific point in the story"

    menu:
        "Lemme grab some points first.":
            jump points

        "Skip to the first arc":
            "Which scene in the first arc do you want to jump to?"

            menu:
                "the start of the game":
                    jump start_real

                "LXC_1":
                    jump LXC_1
        
                "LWJ_1":
                    jump LWJ_1
        
                "MY_1":
                    jump MY_1
                
                "WQ_1":
                    jump WQ_1
        
                "LWJ_2":
                    jump LWJ_2

                "XY_1":
                    jump XY_1
        
                "WQ_2":
                    jump WQ_2
        
                "LXC_2":
                    jump LXC_2

                "MY_2":
                    jump MY_2

        "Skip to the waterborne abyss arc":
            "Which scene in the waterborne abyss arc do you want to jump to?"

            menu:
                "WBA_start":
                    jump WBA_start
                
                "WBA_1":
                    jump WBA_1

                "WBA_2":
                    jump WBA_2
                
                "WBA_3":
                    jump WBA_3

                "LET_1":
                    jump LET_1

                "LET_2":
                    jump LET_2

                "GIFT_1":
                    jump GIFT_1
                
                "WBA_end":
                    jump WBA_end
        
        "Skip to the cold spring caves arc":
            "Which scene in the cold springs arc do you want to jump to?"

            menu:
                "CSC_1":
                    jump CSC_1
                
                "CSC_2":
                    jump CSC_2
                
                "CSC_MY":
                    jump CSC_MY
                
                "CSC_WQ":
                    jump CSC_WQ
                
                "CSC_NHS":
                    jump CSC_NHS

                "CSC_LXC":
                    jump CSC_LXC

                "CSC_JC":
                    jump CSC_JC

                "CSC_end":
                    jump CSC_end
        
        "Skip to the lantern scene":
            menu:
                "LT":
                    jump LT
                
                "LT_canon":
                    jump LT_canon
                
                "LT_NHS":
                    jump LT_NHS
                
                "LT_WQ":
                    jump LT_WQ
                
                "LT_LXC":
                    jump LT_LXC
                
                "LT_MY":
                    jump LT_MY
                
                "LT_NMJ":
                    jump LT_NMJ
        
        "Help mode?":
            menu:
                "help mode on":

                    $ helpmode = True

                    "Help mode turned on"

                    jump start

                "help mode off":

                    $ helpmode = False

                    "Help mode turned off"

                    jump start
    
    jump end

label points: ## this bit also exists to help with playtesting
    "Want some points? Get them here."

    menu:
        "What points can I get?":
            "Here are the available points, click them to get more!"

            menu:
                "wangxian":
                    $ wangxian += 1
                    "You got one wangxian point!"

                "sangcheng":
                    $ sangcheng += 1
                    "You got one sangcheng point!"
                
                "xicheng":
                    $ xicheng += 1
                    "You got one xicheng point!"
                
                "chengyao":
                    $ chengyao += 1
                    "You got one chengyao point!"
                
                "chengqing":
                    $ chengqing += 1
                    "You got one chengqing point!"
                
                "xiyao":
                    $ xiyao += 1
                    "You got one xiyao point!"
                
                "no thanks":
                    "No extra points for you!"

        "Can I check my current points?":
            "Current scores are"

            "Sangcheng points: [sangcheng] \n
            Xicheng points: [xicheng] \n
            Chengyao points: [chengyao] \n
            Chengqing points: [chengqing]"

            "Wangxian points: [wangxian] \n
            Xiyao points: [xiyao]"

            "That's everything so far!"

        "What about flags?":
            "These are the available flags. Click them to add a point."

            menu:
                "LXC_1_flag: 1 for JC saying he'll help NHS train, 2 for JC saying he'll protect NHS":
                    $ LXC_1_flag += 1
                    "Current LXC_1_flag is [LXC_1_flag]"
                
                "LWJ_talk_flag: +1 each time JC talks to LWJ":
                    $ LWJ_talk_flag += 1
                    "Current LWJ_talk_flag is [LWJ_talk_flag]"
                
                "WQ_1_flag: set it to true if JC has taught WN archery in WQ_1. only affects WQ_2":
                    $ WQ_1_flag = True
                    "Current WQ_1_flag is [WQ_1_flag]"
                
                "no thanks, lemme just check what they are":
                    "Current flags are"

                    "LXC_1_flag: [LXC_1_flag] \n
                    LWJ_talk_flag: [LWJ_talk_flag] \n
                    WQ_1_flag: [WQ_1_flag]"
        
        "I'm done, let's go back to the start":
            jump start
    
    jump points

## The game actually starts here.

label start_real:

    scene bg gusu
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun3.mp3" fadein 1.0

    "The Cloud Recesses lectures: a treasured opportunity for studious, dignified young cultivators to have a meeting of minds with their peers from other sects."

    "To learn from each other in an environment of serene, peaceful—"

    show JC left angy at left
    show WWX right at midright
    show NHS right at right

    JC "What the FUCK, Wei Wuxian! Why would I go on fucking dates!"

    show WWX talk
    
    WWX "As your shixiong, it's my sacred duty to make sure you don't die sad and alone—"

    show JC rage

    JC "{i}Who's sad and alone?{/i}"

    show WWX -talk

    WWX "Besides, you don't want to be the only one making a lantern all by yourself, right?"

    show JC angy

    JC "What lantern???"

    show NHS talk

    NHS "The Lans always hold a lantern lighting festival to mark the end of the lectures, since it coincides with Qixi."

    show WWX talk

    WWX "Honestly, I'm surprised that Qixi itself isn't against one of the three thousand Lan sect rules."
    
    WWX "Do Not Hold Festivals Celebrating Foolish Notions Of Romance, or something."

    show WWX blush
    
    WWX "Hmm, I wonder who Lan Zhan is going to light a lantern with..."

    menu:
        "Just admit you want it to be you.":
            $ wangxian += 1
            show JC angy

            JC "Ugh, Lan Zhan Lan Zhan Lan Zhan...Why are you always talking about him!"

            show JC hands

            JC "Do you secretly want to be his date for the lantern lighting festival or something?"

            show WWX wat

            WWX "What! No I don't! I do not!"

            show NHS fan

            NHS "You know, Wei-xiong, you really do talk about Lan-er-gongzi quite a bit..."

            show WWX blush

            WWX "That's...that's nonsense! Anyway, we're not talking about me! We're talking about Jiang Cheng!"

            show WWX -blush
            show NHS -fan

        "Who cares about Lan Wangji?":

            show JC angy

            JC "Ugh, Lan Zhan Lan Zhan Lan Zhan...Who cares about him, anyway?"

            show NHS fan

            NHS "I wonder if he'll just stand to one side like a statue and not even make anything."

            show WWX talk

            WWX "Man, that's just sad. Everyone should have a proper lantern for Qixi..."

            show WWX grin

            WWX "And that includes you, Jiang Cheng!"
    
    show WWX talk

    WWX "As I was saying! Jiang Cheng, I want to make sure you won't be the only loser lighting your lantern alone during the most romantic festival of the year—"

    show JC angy

    JC "You're the fucking loser!"

    show WWX grin

    WWX "—so Nie-xiong and I have decided to put our considerable intelligence and experience to the cause of helping you find a date!"

    show JC hands
    show WWX -grin

    JC "{i}What experience???{/i}"

    show NHS talkfan

    NHS "It's more fun to make a lantern with someone else, anyway, Jiang-xiong! Even if it's not really a date."

    show JC angy

    JC "...Why are {i}you{/i} helping Wei Wuxian with this dumb scheme of his?"

    show NHS fan

    NHS "Can't I just want you to be happy, Jiang-xiong?"

    show JC -angy

    JC "..."

    show NHS talkfan

    NHS "...Wei-xiong promised to help me cheat on all my tests so I won't fail, if I find someone who likes you enough to make a lantern with you."

    show JC rage

    JC "WHAT!"

    show NHS pout

    NHS "Come on, Jiang-xiong! I'm not asking you to {i}marry{/i} anyone! Or even date them! Just talk to people when I ask you to, that's all!"

    NHS "Help me out here, I don't want to fail again! Da-ge will make me stay in Gusu for the next ten years or something horrible like that!"

    menu:
        "No!":

            show JC angy
            
            JC "No! Maybe you should just study if you don't want to fail!"

            show JC hands
            
            JC "Look, what if I helped you study?"

            NHS "But studying is so hard..."

            show WWX grin

            WWX "...Finding someone who likes Jiang Cheng has got to be harder though..."

            show JC rage

            JC "Shut up, Wei Wuxian!"

            show NHS talkfan

            NHS "Look, Qixi is in two months. If you don't want to ask anyone to light a lantern with you by then, you don't have to!"
            
            NHS "Just, you know, talk to people a little? Ask them to make a lantern with you if you want?"

            show JC angy

            JC "This is stupid."

            show NHS fan

            NHS "Imagine how disappointed your sister will be if she finds out that you didn't even want to try making friends with the other guest disciples..."

            show WWX talk

            WWX "Oh, Shijie {i}would{/i} be so upset! I can already see her sad face in my mind!"

            show JC rage

            JC "You shut the hell up! You're the one who's always getting into trouble and upsetting A-jie!"

            show NHS talkfan

            NHS "She's such a lovely, caring person. You know, whenever I see her, she'll always ask me how her brothers are doing, and—"

            show JC hands

            JC "ARGH, alright, fine!"

            show JC angy

            JC "Who do you even want me to ask???"

            show NHS talk

            NHS "You don't have to ask anyone right now! Just talk to whoever I point out to you."

            show NHS fan

            NHS "As for asking someone to make a lantern with...You'll know when the time is right."


        "...Fine.":

            show JC angy
            
            JC "Ugh, fine. Stop wailing about your brother already."

            $ sangcheng += 1

            show NHS smile

            NHS "Yayyyy! Jiang-xiong, you're the best!"

            show WWX left talk

            WWX "Hey, I'm the one who's gonna help you with your tests, not Jiang Cheng!"

            show NHS talkfan

            NHS "You're the best too, Wei-xiong!"

            show WWX right
            show JC hands

            JC "I still think this is stupid. Who do you even want me to ask?"

            show NHS talkfan

            NHS "You don't have to ask anyone to make a lantern with you right now! Just talk to people when I point them out to you."

            show NHS fan

            NHS "As for asking someone to make a lantern with...You'll know when the time is right."

    jump LXC_1

label LXC_1:

    scene bg class
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun4.mp3" fadein 1.0

    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Fifty-nine days to Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)
    
    show JC left at midleft
    show NHS right at midright

    JC "—and of course Wei Wuxian got himself thrown out of class early again."

    show NHS talkfan

    NHS "I wonder if he's managed to sneak out of the librar—oh shit—"

    hide NHS with moveoutbottom
    play sound "audio/rustle.mp3"

    show NHS bush at center
    with moveinbottom

    show JC talk

    JC "...what are you doing? Why the hell are you hiding in the bushes—"

    show LXC left at left
    with moveinleft

    LXC "Good afternoon, Jiang-gongzi. How were your classes today?"

    show JC right rage at right
    with move 

    JC "GAH WHAT—"

    show JC right blush

    JC "Ahem. Good afternoon, Zewu-jun. Classes were, er, good. Educational."

    show LXC smile

    LXC "I'm glad to hear that."

    show LXC -smile

    LXC "Now, I wondered if Jiang-gongzi might happen to know where Nie-gongzi is?"

    hide NHS
    show bush_shake at center
    play sound "audio/rustle.mp3"

    show JC -blush

    JC "..."

    show JC talk

    JC "No...?"

    LXC "No? Ah, was he not in class with you today...?"

    hide bush_shake
    show bush_nod at center
    play sound "audio/rustle.mp3"

    show JC -talk

    JC "..."

    show JC talk

    JC "Er, he...was...? He was. In class."

    LXC "That's good to know. I was hoping to speak to him...But if Jiang-gongzi could spare me a moment of your time, I'd like to speak to you too."

    show bush_nod at center
    play sound "audio/rustle.mp3"

    JC "Oh, um, yes. Of course, Zewu-jun."

    show LXC talk

    LXC "I'm not sure if you're aware, but Nie-gongzi's older brother, Nie Mingjue, has been a good friend of mine since childhood."

    JC "Yes, he's...he's talked about his brother before, yes."

    show LXC smile

    LXC "Ah, of course he has. They care a lot for each other, as I'm sure you're aware."

    show JC -talk

    JC "...Ye-es. I'm sure they do."

    show LXC -smile

    LXC "Mingjue takes a great interest in Huaisang's education and well-being. And so, naturally, do I; I think of Huaisang as another younger brother, almost."

    show LXC talk

    LXC "So Jiang-gongzi, I hope you'll permit an older sibling's concerned interest. May I ask how you think Huaisang is doing in his studies?"

    menu:
        "He's doing okay?":
            show JC talk

            JC "He's, um, not doing too badly...?"

            $ sangcheng += 1

            show bush_nod at center
            play sound "audio/rustle.mp3"

            show LXC frown

            LXC "Hmm, is that so..."

            show LXC -frown

        "He's not doing so great.":
            show JC talk

            JC "He's, er, not doing that great, I guess."

            $ xicheng += 1

            hide bush_nod
            show bush_shakelots at center
            play sound "audio/rustle.mp3"

            show LXC smile

            LXC "Thank you for your honesty, Jiang-gongzi."

            show LXC -smile

    LXC "Will you walk with me, Jiang-gongzi?"

    hide LXC
    hide JC
    with moveoutright

    scene bg gusu
    with cutfast

    show LXC left at left
    show JC right at right

    LXC "I know these lectures can be rather uninteresting. And I'm sure much of the material that is covered can seem obscure and unimportant, isn't that so?"

    show JC talk

    JC "Not really."

    show LXC talk

    LXC "No?"

    JC "Well okay, I suppose back at Lotus Pier we don't really have lectures that go on for so long. And Old Man La—I mean, Lan-xiansheng's voice is really bor—"

    show JC blush
    
    JC "Wait, that's not what I—um, I just mean that I know the stuff we're learning is important."

    show JC talk
    
    JC "My parents say that the Gusu Lan's lectures are the best for building a strong foundation as a cultivator and a sect leader."

    show LXC smile

    LXC "Indeed. I have heard that Jiang-gongzi is doing rather well in class."

    show JC blush

    JC "...Ah, thank you, Zewu-jun. I try."

    LXC "Yes, you do seem like someone who does."

    show LXC frown

    LXC "Unfortunately, I only wish I could say the same of Huaisang..."

    show JC talk

    JC "But Huaisang's not going to be a sect leader anyway, right? And he always says that he doesn't want to go on night hunts, so I guess some of the things we learn really aren't important for him...?"

    show LXC talk

    LXC "Ah, perhaps."

    show LXC -talk

    LXC "I, too, wish that Huaisang can live as idyllic a life as he could hope for, that he can support Qinghe Nie only in the capacity in which he is best suited."

    show LXC frown

    LXC "However..."

    "Lan Xichen's eyes drift to a spot over Jiang Cheng's shoulder. Jiang Cheng turns, and sees Wen Qing walking down a distant corridor, her bright red robes immediately catching the eye."

    LXC "We may not have as peaceful an age as we could wish. Unforeseen combat and unexpected responsibilities may find him, even if he does not seek it out."

    LXC "Do you understand my concerns, Jiang-gongzi?"

    menu:
        "Yes, I'll make Huaisang train more.":
            JC "Yes. I'll try to make Huaisang train more if I can."

            show LXC smile

            LXC "I'm grateful for Jiang-gongzi's sincerity and dedication. And I'm sure Mingjue will be grateful too."

            $ xicheng += 1
            $ LXC_1_flag = 1

            show LXC -smile

        "Yes, I'll protect Huaisang.":
            JC "Yes. If anything happens, I'll do my best to protect Huaisang."

            show LXC -frown

            LXC "Hmm. Well, I'm glad Huaisang has a friend in you, Jiang-gongzi."

            $ LXC_1_flag = 2

        "Hopefully there's nothing to be concerned about.":
            JC "Yes. But hopefully everything will be okay, and there won't be anything to worry about."

            LXC "Hmm. Yes, I hope so too." 

    LXC "Well, thank you for indulging me today, Jiang-gongzi. I hope we'll have other opportunities to speak in the future."

    show JC smile

    JC "Oh, yes, um, me too. Thank you, Zewu-jun."

    scene bg dorm
    with cutfast

    show JC right talk at midright

    JC "I guess I should go back to look for Huai—"

    NHS "There you are!"

    show NHS right at right
    with moveinright
    
    show JC left rage at midright
    show JC rage at left
    with move

    JC "GAH WHAT—"

    show NHS talkfan

    NHS "I couldn't hear anything Xichen-ge said to you after you both walked away! What did he say?"

    show JC hands

    JC "I should have kicked you out of the bushes! Why the hell were you even hiding from Zewu-jun?"

    show NHS pout

    NHS "Jiang-xiong, have a heart! He's been bugging me about my studies, I bet Da-ge wrote him letters telling him to."

    show JC angy

    JC "Well this time he came to bug {i}me{/i} about your studies instead."

    if LXC_1_flag == 1:
        show JC talk
        
        JC "Look, maybe Zewu-jun is right and you should train more. I told him I'd try to get you to, anyway. I think he was worried about the Wens—"

        show NHS talk

        NHS "Ah, Xichen-ge worries too much. Why would I even need to train, I don't go night hunting or anything like that!"

        JC "I guess not, but what if you had to fight anyway?"

        show NHS talkfan

        NHS "Why would I have to? Da-ge is an incredible fighter, and Qinghe Nie has enough strong cultivators to defend the Unclean Realm without me."
        
        NHS "Besides, we don't have time to train today, we have to go rescue Wei-xiong from his punishment!"
    
    elif LXC_1_flag == 2:
        show JC talk

        JC "Look, maybe Zewu-jun is right and you should train more. I think he was worried about the Wens—"

        show NHS talk

        NHS "Ah, Xichen-ge worries too much. Why would I even need to train, I don't go night hunting or anything like that!"

        JC "I guess not, but what if you had to fight anyway? I told Zewu-jun that I'd try to protect you if anything happened, but it's not like I'm with you all the time."

        show NHS smile

        NHS "Aw, Jiang-xiong, that's sweet of you!"

        NHS "But there's nothing I need to be protected from, really! What dangers can there possibly be in the Cloud Recesses?"

        show NHS talkfan

        NHS "Other than dying of boredom."
        
        NHS "Which, speaking of, we have to go rescue Wei-xiong from his punishment!"
    
    else:
        show NHS talk
        
        NHS "Ah, Xichen-ge worries too much. The only thing anyone has to be worried about in the Cloud Recesses is dying of boredom."

        NHS "Which, speaking of, we have to go rescue Wei-xiong from his punishment!"

    jump LWJ_1

label LWJ_1:

    scene bg library
    with cutfast

    stop music fadeout 1.0
    play music "audio/fun2.mp3" fadein 1.0

    "The Library Pavilion: the heart of the Cloud Recesses. Shelves of ancient scrolls and educational texts adorn its walls, and low tables of white-robed young scholars fill its rooms."
    
    "One such young scholar is draped across his table in a posture of abject despair. He heaves a world-weary sigh, and cries out:"

    show WWX left talk at left
    show LWJ right at midleft
    with Dissolve(0.5)

    WWX "Lan Zhan. Lan {i}Zhan{/i}. Lan Zhaaaaaaaan."

    LWJ "..."

    show WWX grin

    WWX "Lan-xiong! Wang-xiong! Ji-xiong!"

    LWJ "..."

    "Two other white-robed scholars are peeking out from behind a nearby shelf, listening in on this riveting discussion between their peers."

    show NHS right fan at right
    show JC right at midright
    with moveinbottom

    NHS "We need a plan! Wei-xiong clearly needs rescuing!"

    show JC talk

    JC "Dunno about that, seems like he's having a great fucking time. Maybe we should just leave them alone."

    show NHS pout

    NHS "But then who will do my homework for me?"

    show JC -talk

    JC "..."

    show NHS talkfan

    NHS "I know! You should go talk to Lan-er-gongzi!"

    show JC left angy

    JC "{i}What?{/i}"

    show NHS talk

    NHS "Go talk to him! Didn't you agree to talk to whoever I asked you to?"

    show JC rage

    JC "Lan Wangji? You're telling me to talk to {i}Lan Wangji?{/i} You think I want that block of wood to light lanterns with me on Qixi???"

    NHS "SHHHHHH!"

    show NHS talkfan

    NHS "No, no, I know you wouldn't like someone like that."

    show JC angy

    JC "Of course not!"

    show NHS fan

    NHS "Also, Wei-xiong would probably stab you in the back for the chance..."

    show NHS talkfan

    NHS "But anyway, I'm not telling you to ask him out on a date! Just distract him with small talk! You could talk to him about...the weather...?"

    show NHS pout

    NHS "Come on, Jiang-xiong, you promised! Please?"

    menu:
        "Talk to Lan Wangji.":
            show JC hands

            JC "Argh, fine!"

            JC "But if he stabs me, you can explain to my mother why the Yunmeng Jiang sect is down a sect heir."

            show NHS smile

            NHS "No problem, I'm great at giving people bad news and then running away! Thanks, Jiang-xiong!"

            show JC right talk
            hide NHS
            with moveoutbottom

            JC "...this is stupid this is stupid this is stupid..."

            $ sangcheng += 1
            $ LWJ_talk_flag += 1

            show JC right:
                ease 0.25 xoffset -100
                ease 0.25 xoffset 0

            show JC -talk

            JC "Ahem."

            JC "Greetings, Lan-gongzi."

            show LWJ left

            LWJ "...Jiang-gongzi."

            show WWX talk

            WWX "Jiang Cheng! You're here! Aww, did you miss me?"

            show JC angy

            JC "Shut up, idiot, I'm not talking to you! Who'd miss you, anyway!"

            show WWX grin

            WWX "My dearest shidi would miss me, of course! Why else would you—"

            show WWX -grin

            WWX "Hmm."

            show WWX talk

            WWX "Oh, well, if you don't want to talk to me then I'll just go back to doing this essay."

            show JC -angy

            JC "Ahem. Anyway. Lan-gongzi."

            WWX "{size=-9}...I think I need a reference for the classifications of object possession."

            hide WWX with moveoutleft

            WWX "{size=-12}Now where would I find that scroll, oh I wonder, oh maybe that shelf all the way over there might have it..."

            show JC talk

            JC "So. The weather in Gusu is...quite warm, isn't it."

            LWJ "..."

            JC "I thought it would be colder. But it's not."

            LWJ "..."

            JC "Still, the weather isn't too bad."

            LWJ "..."

            show JC -talk

            JC "...Right. I'm going away now."

            hide JC with moveoutright

            LWJ "..."

            show LWJ right

            LWJ "...!"

            show LWJ angy

            LWJ "Where—"

            LWJ "...Wei Wuxian!"
        
        "Don't talk to Lan Wangji.":
            show JC hands

            JC "I did {i}not{/i} promise! And I certainly didn't promise to talk to Lan Wangji of all people!"

            NHS "Jiang-xioooooong..."

            show WWX talk

            WWX "Lan-xioooooong..."

            LWJ "..."

            show JC angy

            JC "Ugh, stop that! Look, I'll do your homework for you this one time, alright?"

            show NHS smile

            NHS "Okay, deal!"

            show WWX grin

            WWX "Laaaan Waaaang Jiiii—"

            LWJ "..."

            JC "Now let's leave already."
            
            JC "If I have to hear Wei Wuxian say Lan Wangji's name one more time, I'm going to stab myself in the ears, and then you can explain to my mother why the Yunmeng Jiang sect is down a sect heir."

            show NHS talkfan

            NHS "No problem! I'm great at giving people bad news and then running away!"

            JC "...Great. Okay let's go."

            hide JC
            hide NHS
            with moveoutright

            WWX "{size=-9}Lan Zhan-ge~{/size} {size=-12}Lan-ergege~{/size} {size=-18}Gege~"

            $ wangxian += 1
    
    jump MY_1

label MY_1:

    scene bg class
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun3.mp3" fadein 1.0

    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Fifty-one days to Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)

    show JC right at midright
    show WWX left at midleft
    show NHS left at left

    show WWX talk

    WWX "—class is {i}finally{/i} over, I swear the hours get longer and longer every day."

    show WWX grin
    
    WWX "Hey, do you think the Lans have some kind of time dilation array drawn around the lecture hall?"

    show JC talk

    JC "You're so full of nonsense. Even if they did, would you notice? You spent half that lecture asleep, and the other half bothering Lan Wangji."

    show NHS talk

    NHS "Hah, Wei-xiong, I can't believe you dared to—"

    MY "Er-gongzi, I've been waiting for you."

    show MY right at right
    with moveinright

    show JC left at center
    with move

    show NHS left fan:
        ease 0.1 yoffset -50
        ease 0.1 yoffset 0

    NHS "Oh, Meng Yao! What—what are you doing here!"

    show WWX -grin

    WWX "Oh hey, Meng Yao! Hi!"

    menu:
        "Hello, Meng Yao":
            show JC talk
            
            JC "Hello, Meng Yao."

            MY "Greetings, Wei-gongzi, Jiang-gongzi."

            $ MY_1_flag = True

        "Good afternoon, Meng-gongzi":
            show JC talk

            JC "Good afternoon, Meng-gongzi."

            show MY smile

            MY "Oh. A good afternoon to you too, Jiang-gongzi. And you as well, Wei-gongzi."

            $ chengyao += 1
    
    show MY talk

    MY "Er-gongzi, did your brother not write to tell you that I was coming?"

    show NHS pout

    NHS "He did, but I wrote back to say that he didn't have to send a babysitter! I promised him I wouldn't fail this year for sure! I told him I was studying so super hard!"

    show MY -talk

    MY "...Unfortunately, Er-gongzi was perhaps not convincing enough in his reassurances, because Zongzhu sent me anyway."

    show NHS talkfan

    NHS "Then I'll just have to send you back!"

    MY "I'm afraid I was given quite explicit instructions with regard to your continuing education here in Gusu, Er-gongzi."

    show MY talk
    
    MY "How about we move this discussion to your room, and after that we can review the materials from today's lecture together?"

    show NHS pout

    NHS "But you weren't even in the lecture! How do you know what I need to review?"

    show MY smile

    MY "Zewu-jun has been exceedingly kind, and taken the time to brief me on what I need to know."

    show MY -smile

    MY "Now, why don't we go to your rooms? Wei-gongzi, Jiang-gongzi, if you'll please excuse us?"

    show NHS pout

    NHS "No, but..."

    show WWX talk

    WWX "Oh, hey, I think I've got some of Nie-xiong's books with me. He probably needs them if he wants to study. Right, Nie-xiong?"

    show NHS pout

    NHS "What book—"

    show NHS fan
    
    NHS "Oh! Right, yes, the books. I should come get them from you. From your rooms."
    
    show WWX grin

    WWX "Yeah, from my rooms! We'll just head over to my rooms to get them. We'll come back right after!"

    show MY talk
    show WWX -grin

    MY "If you'll permit me to accompany you both—"

    show NHS left talkfan

    NHS "No need, no need! Wei-xiong's rooms are so far away, there's no need for you to trouble yourself, Meng Yao, really!"

    show NHS talk
    
    NHS "Look, why don't you just wait here with Jiang-xiong...Oh, yes, Jiang-xiong wants to talk to you, actually!"

    NHS "Isn't that right, Jiang-xiong?"

    menu:
        "...Sure.":
            show JC -talk
            
            JC "...Sure. Right."

            show NHS smile

            NHS "See? You two keep each other company, we'll be back real quick!"

            $ sangcheng += 1

            show WWX talk

            WWX "Yeah! We'll be back before you know it!"

            MY "Now, just a moment—"

            hide NHS
            hide WWX
            with moveoutleft

            show MY -talk

            MY "..."

            MY "Well. Jiang-gongzi."

            if MY_1_flag == True:
                JC "Yes, Meng Yao—I mean, Meng-gongzi?"

            else:
                JC "...Meng-gongzi."

            MY "Did you have something you'd like to talk to me about?"

            show JC talk

            JC "Er."

            show JC blush

            JC "So."

            JC "The weather in Gusu is...quite warm, isn't it."

        "What?":
            show JC right talk
            
            JC "What?"

            show NHS pout

            NHS "Jiang-xioooong..."
            
            show MY smile

            MY "I certainly look forward to becoming more closely acquainted with Jiang-gongzi in the future."
            
            MY "But am I right to say that Jiang-gongzi is not someone who's interested in making more mundane small talk than necessary?"

            show JC left talk

            JC "Er, I guess not."

            show MY talk

            MY "It was quite a journey, travelling back to Gusu from Qinghe, and given Nie-zongzhu's orders I really must speak to Nie-er-gongzi today. So I hope Wei-gongzi and Jiang-gongzi will forgive this interruption."

            JC "Oh, yeah. Of course. Um, I hope your journey wasn't too arduous."

            show MY smile

            MY "Not at all. Thank you for your concern, Jiang-gongzi."

            $ chengyao += 1

            show MY -smile

            MY "Now, if you'll excuse us, I'll just be seeing Nie-er-gongzi to his rooms."

            hide MY
            hide NHS
            with moveoutleft

            NHS "{size=-9}Nooooooooooooo...."
    
    jump WQ_1

label WQ_1:

    scene bg backhill
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun1.mp3" fadein 1.0

    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Forty-six days to Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)

    show NHS right at center
    show WWX right at midleft
    show JC left talk at left

    JC "Are you {i}sure{/i} we're allowed to be here?"

    show WWX talk

    WWX "Didn't you hear Old Man Lan? He said no one's allowed to enter the back hills without good reason...and our reasons are excellent!"

    WWX "We're going fishing!"

    show JC smile

    JC "Hah, I don't think he's going to accept \"trying to catch fish for dinner so we don't die of a meat deficiency\" as a good reason."

    show NHS talk

    NHS "It'll be fine as long as we don't get caught! It—"

    show NHS left fan

    NHS "Wait, is someone else here???"

    show WWX left -talk

    WWX "I think there's someone up ahead...?"

    show WWX at midright
    with move

    WWX "Oh, it's Wen Ning! I think he's practising his archery?"

    show NHS talkfan

    NHS "Phew, I thought it was Meng Yao trying to ambush me again..."

    show JC talk

    JC "Wen Ning? Huh, I didn't realise he's still here in the Cloud Recesses. Don't think I've seen him since the gift presentation ceremony."

    show NHS right talk

    NHS "He's too young to join us for the lectures and the classes, I guess? Lucky..."

    show WWX right
    
    WWX "Hmm, I wonder why the Wens bothered to bring him along at all. His sister, sure, but he's just a kid."

    JC "What?"

    show WWX talk

    WWX "Oh, you know, forcing the Lans to accept Wen Qing as a student so that everyone is reminded that the Wens can do whatever they want, it's an intimidation tactic, right? But Wen Ning's just a kid."

    show NHS fan

    NHS "Dunno, that kid seems pretty intimidating with a bow and arrow..."

    show JC -talk

    menu:

        "Not bad":

            JC "Yeah, he’s pretty good now when he’s shooting at rocks.  The real test is how he’ll do against something that will fight back."
            
        "The Wen sect’s archery skills are notoriously bad":

            show JC hands

            JC "The Jiang sect weapons training is clearly superior. Right, Wei Wuxian?"

            $ chengxian += 1

            show WWX grin

            WWX "Totally! Our Jiang sect forms are better for sure!"

        "Maybe in 100 years":

            JC "Eh, his form could use some work."

            show NHS right pout

            NHS "You say that about everyone!"
 
    show WWX left talk

    WWX "I'm gonna go show Wen Ning how it's done!"

    hide WWX with moveoutright

    show JC angy

    JC "Damn it, get back here, Wei Wuxian, that's not what I—"

    WN "{size=-9}Oh...oh! Wei...Wei-gongzi!"

    WWX "{size=-9}Hey, Wen Ning! Not bad with the bow! But you know how you could be better..."

    show NHS right pout

    NHS "I didn't escape to the back hills for more weapons training. Let's leave them to it."

    menu:
        "Leave with Nie Huaisang":
            $ sangcheng += 1

            show JC talk

            JC "Yeah, let's go. Wei Wuxian can catch up with us once he's done with his nonsense."

            show NHS smile

            NHS "Yes! Jiang-xiong, you're sure you can catch enough fish for the both of us, right?"

            menu: ## dialogue

                "Of course!":
                    pass

                "Attempt the impossible!":
                    pass

                "Just watch me break all of these fishes' legs!":
                    pass

            JC "Damn right—"
            
            JC "Wait, for both of us? Aren't you gonna catch some fish too?"

            show NHS talkfan

            NHS "Ah, Jiang-xiong, you know Qinghe has far more mountains than streams, I've never caught a fish for myself before..."

            show JC smile

            JC "I've been catching fish since I was a kid, I'll show you how. I was the one who first taught Wei Wuxian, you know?"

            show NHS smile

            NHS "I'm sure you're a fantastic fishing teacher, Jiang-xiong!"

            show NHS talk

            NHS "But if I don't manage to catch any, then..."

            menu: ## dialogue
            
                "Lucky for you, I'm the Grandmaster of River Fishing!":
                    pass

                "If it's Nie-xiong asking...":
                    pass

                "If I have to":
                    pass

            show JC blush

            JC "Fine, fine, I'll make sure to catch enough for you too."

            show NHS smile

            NHS "Fresh fish for dinner, mmmmmm...."

            show JC right:
                ease 0.4 xoffset -400

            show NHS right -smile at midleft
            with move

            show JC -blush

            JC "Right, let's find a good stream for—"

            show JC:
                ease 0.2 xoffset 600
            show NHS:
                ease 0.2 xoffset 600

            show WQ left at left
            with moveinleft

            show JC talk

            JC "Oh! Wen-guniang!"

            WQ "Jiang-gongzi. Nie-gongzi."

            show NHS talkfan

            NHS "Wen-guniang, greetings! Um, fancy seeing you here!"

            WQ "Indeed. Please excuse me."

            hide WQ with moveoutright
            show JC left
            show NHS left

            show JC talk

            JC "Huh, what's Wen-guniang doing here?"

            show NHS fan

            NHS "I don't know, but I wonder if she has as good a reason to be here as we do..."

            show JC -talk

            JC "...Do {i}we{/i} have a good reason to be here???"

            jump LWJ_2

        "Join Wei Wuxian and Wen Ning":

            show JC hands

            JC "Argh, I can't just—"

            hide JC with moveoutright

    scene bg backhill
    with cutfast

    show WN right at right
    show WWX left at midright
    with None

    show JC left angy at midleft zorder 3
    with moveinleft

    JC "Wei Wuxian!"

    show WN:
        ease 0.1 yoffset -50
        ease 0.1 yoffset 0

    show WWX right

    WN "Jiang...Jiang-gongzi! Greet...Greetings..."

    show NHS left pout at left
    with moveinleft

    NHS "{size=-9}...run…so…fast, Jiang-xiong!{/size} Wait up!"

    show WWX grin

    WWX "Oh, Nie-xiong! Are you here to teach Wen Ning too?"

    show NHS fan

    NHS "Who, me? Oh no, no, I can't possibly teach anyone anything."
    
    show WQ left hmm at left
    with moveinleft

    show NHS right:
        ease 0.1 xoffset 800

    show WWX right:
        ease 0.1 xoffset -300

    show JC right:
        ease 0.1 xoffset 50

    WQ "What is going on here???"

    $ WQ_1_flag = True

    show WN smile

    WN "Jie!"

    show JC blush

    JC "Oh, Wen-guniang! Greetings!"

    show WWX grin

    WWX "Wen-guniang, hi! We're teaching your brother archery!"

    WQ "A-Ning already knows how to use a bow."

    WN "Jie, Jiang-gongzi and Wei-gongzi said they'd teach me how to shoot better!"

    show WQ -hmm

    WQ "Hmm."

    show WQ sustalk

    WQ "I don't think our sect leader would appreciate you teaching him a different sect's technique." 

    show WN -smile

    WN "Jie!"

    menu:
        "Wen Ning has potential!":

            JC "Wen Ning has a lot of potential, but even he can't improve without some help." 

            $ chengqing += 1

            WQ "He has all of the help he needs from his family.  Good day, Jiang-gongzi.  Nie-gongzi."

        "Can't we all get along?":

            JC "You don't think that all of the sects can learn something from each other?  Isn't that the point of these lectures– to foster good relations between us?"

            $ chengqing += 1

            WQ "The Wens weren't even invited to participate in these lectures.  Don't pretend like you want to play nice.  Stay away from my brother."

        "But Wen Ning wants to learn from us.":

            JC "Don't you think you're interfering a little too much?  The kid wants to learn from us."

            WQ "Don't presume to tell me what is best for my family, Jiang-gongzi.  We can take care of ourselves."

            show NHS fan

            NHS "That much is apparent."

            WQ "Come on, A-Ning.  Let's go."

            show WQ right
            hide WQ with moveoutleft

            hide WN with moveoutleft

            WWX "Well, that went well."

            JC "Shut up, Wei Wuxian."

            jump LWJ_2

        "But your sect leader is Wen Rouhan…":

            JC "Fine! Your sect is all evil anyway!" 

            $ chengqing -= 2

            $ WenHate_flag = True

            WQ "I see.  If you'll excuse me, Jiang-gongzi.  I have to go do some evil on the other side of the mountain." 

            jump LWJ_2

    ##wrap up exchange for the good dialog options

    show WQ right
    hide WQ with moveoutleft

    WN "Oh. Oh, okay. Good...Goodbye, Jiang-gongzi, Wei-gongzi, Nie-gongzi."

    hide WN with moveoutleft

    show WWX talk

    WWX "...I guess it did get late, huh."

    show NHS left pout

    NHS "Oh no, does that mean we won't have time to catch fish for dinner???"

    jump LWJ_2

label LWJ_2:

    scene bg dormnight
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun4.mp3" fadein 1.0

    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Thirty-nine days to Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)

    show JC left at left
    show WWX right at right
    show NHS right talk at center

    NHS "Ahhh, it's so nice to finally have the chance to stretch our legs in Caiyi Town! And do a little shopping!"

    show JC talk

    JC "I'm telling you, Lotus Pier has everything Caiyi has and more! I bet they sell fans in Lotus Pier too."

    show NHS talkfan

    NHS "I'd love to look at them! Does that mean you'll take me around town if I visit?"

    show WWX grin

    WWX "Of course! Yunmeng is the best, and who better to show you than the two best cultivators of Yunmeng Jiang!"

    show JC smile

    JC "Yeah, of course we'll show you around."

    show WWX -grin

    WWX "Although when it comes to alcohol, Gusu is definitely a close second. Ahhh, having a bottle of Emperor's Smile is truly the best way to end the day, I can't wait!"

    show NHS talk

    NHS "Don't drink it now, Wei-xiong, let's get settled in your rooms first—"
    
    show NHS fan at midright
    with move
    show NHS:
        ease 0.1 yoffset 300

    NHS "Shit! Hide!"

    show WWX talk

    WWX "Oh, is that Lan Zhan?"

    NHS "{size=-9}SHHHHH, get down here!"

    show JC right at center
    with move
    show JC:
        ease 0.1 yoffset 300
    show WWX:
        ease 0.1 yoffset 300

    show LWJ left at left
    with moveinleft

    JC "{size=-9}What the hell is he doing out here? Is he on patrol?"

    WWX "{size=-9}Hah, I bet Lan Zhan patrols for fun!"

    show JC angy

    JC "{size=-9}Who the fuck patrols for {i}fun?{/i}"

    show NHS talk

    NHS "{size=-9}Maybe he's looking for Wei-xiong specifically..."

    show WWX grin

    WWX "{size=-9}Aww, you think he missed me?"

    show JC left angy

    JC "{size=-9}No, idiot, I bet he's figured out you're always up to some nonsense and is trying to stop you before you do something else."

    show NHS talkfan

    NHS "{size=-9}Jiang-xiong, go talk to him! Distract him!"

    JC "{size=-9}Why the hell do you keep making me talk to people as a distraction!"

    show NHS pout

    NHS "{size=-9}Come onnnn, Jiang-xiooooong..."

    menu:
        "Talk to Lan Wangji":

            if LWJ_talk_flag >= 1:
                JC "{size=-9}Damn it, fine, damn it, but this is the last time!"

            else:
                JC "{size=-9}Damn it, fine, damn it!"

            $ sangcheng += 1
            $ LWJ_talk_flag += 1

            show NHS -pout
            show JC right:
                ease 0.2 yoffset 0
                ease 0.3 xoffset -200

            JC "AHEM."

            show JC talk

            JC "Lan-er-gongzi."

            LWJ "..."

            LWJ "Jiang-gongzi."

            JC "So."
            
            JC "The weather in Gusu is...quite warm, isn't it."

            LWJ "..."

            show LWJ right
            hide LWJ with moveoutleft

            JC "I thought it would be colder—Hey! Where are you going!"

        "Throw Wei Wuxian at Lan Wangji":   
            show JC talk

            JC "{size=-9}Actually, I have a better idea."

            WWX "{size=-9}What—{/size}"

            show JC right at right
            with move

            show WWX left wat:
                ease 0.1 xoffset -800
            
            show WWX
            with hpunch
            with vpunch
            
            WWX "ARGH! JIANG—"

            show WWX right talk:
                ease 0.5 yoffset 0

            WWX "Oh, Lan Zhan! Hi!"

            LWJ "Wei Wuxian."

            show WWX grin

            WWX "Fancy meeting you out here! Why, you're not up to some funny business, are you?"

            LWJ "..."

            LWJ "Alcohol is forbidden in the Cloud Recesses."

            show WWX talk

            WWX "Alcohol? What alcoho—oh, this?"

            show WWX grin
            
            WWX "Ha. Haha! How did this get in my hands?"

            LWJ "Dispose of it."

            show WWX talk

            WWX "Surely wastefulness is also forbidden in—"

            play sound "audio/swords.mp3"

            show WWX wat

            WWX "Hey! Lan Zhan, why do you draw your sword over every little—WHOA."

            play sound "audio/swords.mp3"

            hide LWJ
            hide WWX
            with moveoutleft
            pause

            show JC:
                ease 0.2 yoffset 0
            show NHS:
                ease 0.2 yoffset 0

            show JC talk
            
            JC "Great, they're gone."

            show NHS pout

            NHS "But so is all our alcohol!"

            $ wangxian += 1

    jump XY_1

label XY_1:

    scene bg roof
    with cutslow

    stop music fadeout 1.0
    play music "audio/funny.mp3" fadein 1.0

    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Thirty days to Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)

    show JC left talk at midright
    show NHS right at right

    JC "Look, I don't know why you're so paranoid about being stalked—"

    show NHS pout

    NHS "It's not paranoia if I'm actually being ruthlessly, heartlessly hunted down, Jiang-xiong!"

    show JC hands

    JC "—but do we really have to sneak around across the rooftops any time we're not in class? Isn't this against the rules?"

    show NHS talk

    NHS "I've seen Lan-er-gongzi using the rooftops to travel through the Cloud Recesses."

    show JC talk

    JC "You have? When?"

    show NHS talkfan

    NHS "Just yesterday! So it's fine!"

    show JC angy

    JC "...You mean you saw him chase Wei Wuxian through the Cloud Recesses across the rooftops. Do you also want to be chased across the rooftops by Lan Wangji and locked up in the Library Pavilion???"

    JC "Anyway, I bet there's a rule that says you can climb whatever roofs you want if you're chasing down an idiot rule-breaker."

    show NHS talk

    NHS "Well, if I'm breaking the rules by being up here, then it's fine for you to be up here chasing me. And if {i}you're{/i} breaking the rules by being up here, then it's fine for {i}me{/i} to be up here chasing {i}you{/i}."

    show NHS smile

    NHS "So it's fine for both of us to be here!"

    show JC hands

    JC "Or we're both breaking the rules by being here! Which is what I said in the first place! You—"

    show NHS -smile:
        ease 0.2 yoffset 300

    NHS "SHHHH! {size=-9}"

    show NHS at center
    
    NHS "I see my oppressors!"

    show JC right talk

    JC "...Do you mean Zewu-jun and Meng-gongzi?"

    NHS "SHHHHHHHHH! {size=-9}Come here!"

    show JC:
        ease 0.2 yoffset 300

    NHS "{size=-9}Look at them! They're clearly talking about me!"
    
    JC "{size=-9}I dunno, it looks like a private, personal conversation. Very personal."

    NHS "{size=-9}I bet they're scheming about how to force me to study."

    JC "{size=-9}Zewu-jun doesn't seem like the scheming type to me..."

    show NHS fan

    NHS "{size=-9}But Meng Yao definitely is. Let's get closer."

    menu:
        "Agree to eavesdrop":
            show JC angy

            JC "{size=-9}Ugh, fine, but if they spot us, I'm telling Zewu-jun that you're the idiot rule-breaker that I'm chasing."

            show NHS left smile 

            NHS "{size=-9}I'm always happy to be caught if it's you chasing me, Jiang-xiong!"

            $ sangcheng += 1

            show NHS right

            NHS "{size=-9}Now let's see what they're up to..."

            show NHS:
                ease 0.2 xoffset -100

            show JC hands

            JC "{size=-9}Careful! Don't go so damn fast, these tiles are slippery!"

            LXC "...know Mingjue must be deeply missing Meng-gongzi's presence in Qinghe already. After all, if it was I who had the joy and privilege of being able to rely on Meng-gongzi's competence and diligence, I know I surely would feel the same."

            NHS "{size=-9}Gotta get closer to—{nw}"

            show NHS:
                ease 0.4 xoffset -200
                ease 0.05 yoffset 400
                ease 0.05 yoffset 300
            
            extend "WHOA!"

            show JC:
                ease 0.1 xoffset -50
                ease 0.1 xoffset 0

            JC "Careful!"

            MY "Zewu-jun is too kind. That's—"

            MY "Wait. Did you hear that?"

            NHS "..."

            show JC -angy

            JC "..."

            LXC "Hear what?"

            MY "I would have sworn..."

            MY "Hmm."

            MY "Zewu-jun, it's been so pleasantly warm in Gusu these last few days. Maybe we'd be more comfortable under the shade of that awning over there?"

            LXC "Of course, Meng-gongzi. Though perhaps we'd be more comfortable in my rooms."

            show NHS fan

            NHS "{size=-9}In his rooms? Oooh, did Zewu-jun just ask Meng Yao to his rooms?"

            show JC talk

            JC "{size=-9}I think he did???"
            
            LXC "If it's not too forward of me, I wonder if I could invite Meng-gongzi to continue our conversation over afternoon tea?"

            MY "Oh, that's..."

            NHS "{size=-9}Oho, we're here for the tea all right. Ah, if only Wei-xiong were here."

            JC "{size=-9}What? What do you need him for?"

            show NHS left

            NHS "{size=-9}That paper doll trick of his would make a great eavesd—{/size}"

            show MY left at left
            with moveinbottom

            MY "Er-gongzi. Jiang-gongzi."

            show NHS right fan:
                ease 0.2 yoffset 0

            NHS "Meng Yao!"

            show JC right blush:
                ease 0.5 yoffset 0

            JC "Meng...Meng-gongzi."

            LXC "Meng-gongzi, did I say something wrong? Why did you run for the roof—"

            show LXC right frown at right
            with moveinbottom
            
            LXC "Oh. Nie-gongzi, Jiang-gongzi!"

            show NHS left talkfan
            show JC left blush

            NHS "Zewu-jun!"

            JC "Ze...Zewu-jun!"

            show LXC talk

            LXC "What a pleasant surprise! What are we all doing up here?"

            show MY talk

            MY "A very good question. What {i}are{/i} we doing up here, Er-gongzi?"

            show NHS fan

            NHS "Oh, just. Enjoying the sunshine! On this beautiful, pleasantly warm Gusu day! Right, Jiang-xiong?"

            show JC blush

            JC "Right. Sunshine, yes."

            show MY -talk

            MY "Enjoying the sunshine. On this roof."

            show NHS talkfan

            NHS "Oh, but it's such a warm day, we had to drink so much water to stay well hydrated, and now I really have to pee, excuse me!"

            hide NHS with moveoutbottom

            JC "Er, me too. Hydration. Peeing. Excuse me, Meng-gongzi, Zewu-jun."

            hide JC with moveoutbottom

            MY "..."

            LXC "..."

            show LXC smile

            LXC "Well, at the speed they're going, it surely qualifies as training for Huaisang, wouldn't you say, Meng-gongzi?"

            show MY talk

            MY "...Indeed. At least Nie-zongzhu will be pleased."

        "Decline to eavesdrop":
            show JC hands

            JC "No, what if they spot us!"

            JC "Anyway, they look like they'll be talking for a long-ass time, so that means they won't be looking for you, right?"

            show NHS left talkfan

            NHS "Oh, good point! Maybe we can make a break for the back hills!"

            show JC angy

            JC "Sure, fine, but can we make a break for it on the {i}ground?{/i}"

            show NHS right talk

            NHS "Yes, but let's wait until they're distracted first before we get down."

            show JC -angy

            JC "...They're looking pretty deeply into each other's eyes, I think they're not going to notice us anyway."

            show JC talk
            
            JC "Not even if we land on top of them."

            NHS "Shh, just wait for it..."

            JC "Wait for what?"

            NHS "Just wait, wait until they—okay, they're bowing to each other! Go go go!"

            hide NHS with moveoutbottom
            hide JC with moveoutbottom

            $ xiyao += 1

    jump WQ_2

label WQ_2:

    scene bg backhill
    with cutfast

    stop music fadeout 1.0
    play music "audio/fun1.mp3" fadein 1.0

    show NHS left at midleft
    show JC right at midright

    NHS "Ahhh, thank goodness we got away! I—"

    play sound "audio/rustle.mp3"

    NHS "Someone's coming!"

    if sangcheng > 3:  ## hiding behind JC

        show NHS right fan at right
        with move

    NHS "If it's Meng Yao, you have to—"

    show WQ left at left
    with moveinleft

    show NHS talkfan

    NHS "Oh, phew, it's just you, Wen-guniang."

    show WQ hmm

    WQ "{i}Just{/i} me?"

    show JC blush

    JC "Wen-guniang! Ah, Nie Huaisang just means he's glad it's you, and not Zewu-jun or Meng-gongzi."

    show NHS left fan
    pause 0.5
    show NHS right fan
    pause 0.5

    NHS "SHHHH don't say their names so loudly!"

    WQ "...Are you expecting them to leap out of the trees and attack you?"

    NHS "YES."

    show JC -blush

    JC "No."

    NHS "WITH BOOKS."

    show WQ talk

    WQ "Ah. How...terrifying."

    NHS "They are! They might not look like it, but they're so scary when they're on a mission."

    show NHS talkfan

    NHS "Oh."

    if sangcheng <= 3:
        show NHS left fan
        pause 0.5
        show NHS right fan
        pause 0.5

    else:
        show NHS fan:
            ease 0.5 xoffset 100

    NHS "Ohh…."

    NHS "Speaking of {i}missions{/i}, I need to go… do a… thing.  Over there!"

    hide NHS with moveoutright

    show JC rage

    JC "Nie Huaisang!"

    show WQ hmm right
    pause 0.5
    show WQ hmm left
    pause 0.5

    show WQ sustalk left at midleft
    with move

    WQ "Actually, Jiang-gongzi, I wanted to speak with you anyway." 

    show JC -rage

    show WQ hmm

    JC "You did?"

    menu:
        "Of course you did":

            show JC smile

            JC "Yeah, I'm not surprised. I'm a pretty important person."

            $ chengqing -= 1
            
            show WQ sustalk left

            WQ "Charming."

            show WQ -talk

        "Is this a trick?":

            $ WenHate_flag = True

            show JC rage

            JC "Why, so you can involve me in whatever schemes you Wens are plotting?"

            $ chengqing = 0

            show WQ angy

            WQ "I see. Then you'll have no problem with staying away from my brother."

            JC "Gladly!"

            WQ "Excellent."

            jump LXC_2

        "Go on...":

            JC "Okay." 

            show JC smile

            JC "What did you need, Wen-guniang?"

            WQ "My brother tells me that you and Wei-gongzi have become quite friendly."

            menu:
                "We're friends!":
                    JC "Yeah, Wen Ning is pretty great." 
                    
                    $ chengqing =+1

                    show WQ smile
                    pause 0.5

                "He's okay.":

                    show JC talk
                    JC "We've talked with Wen Qionglin a couple of times."

                "I wish we weren't.":
                    show JC roll

                    JC "Yeah, he keeps hanging around us. It's pretty annoying."
                    $ chengqing -= 1

                    show WQ angy
                    pause 0.5

    show WQ sustalk

    WQ "That being the case, I'd like to ask you a favor."

    show WQ hmm

    WQ "Please stop."
                    
    show JC talk
                    
    JC "Stop what?"
                    
    show WQ sustalk
                    
    WQ "I don't know what you and Wei-gongzi think you're doing, but leave A-Ning out of it."

    JC "What makes you think we're {i}planning{/i} anything?"
                    
    JC "Wei Wuxian can't even plan how to get to class on time."

    show WQ angy

    WQ "I don't want my brother involved. Do you understand me?"

    show JC angy

    JC "Hey, you guys are the ones who brought him here. If anyone involved him in anything, it was you."

    WQ "I'm just trying to protect him."

    JC "From who? Us?"

    show WQ hmm right
    pause 0.5
    show WQ hmm left
    pause 0.5

    ## ?add WQ line or change sprite

    show JC hands

    JC "Why are you so suspicious anyway?  Did we really do anything to make you distrust us so much?"

    show WQ rage

    WQ "What have any of you done to make me {i}trust{/i} you?"

    show JC rage

    JC "I could say the same about you!  Why are you always creeping around in the back hills anyway!" 

    WQ "Who says I'm doing anything other than trying to get away from everyone whispering about us!"  

    WQ "Every time you've seen me in the back hills, it's because {i}you're there too{/i}. Now who's being overly suspicious!"  

    JC "You–!"
                    
    menu:
        "That's different!":
                            
            JC "You're a Wen!  We know that you're up to no good back here!"
                            
            $ WenHate_flag = True
            $ chengqing -= 1

            show WQ sustalk

            WQ "Prove it."

            WQ "Goodbye, Jiang-gongzi.  Remember to stay away from my brother."
                            
            hide WQ with moveoutleft

            show JC angy

            JC "Fuck."

            jump LXC_2

        "We were fishing!":

            show JC angy

            JC "We were just out here fishing, okay!"

            show WQ angy

            WQ "Which is against the rules of Cloud Recesses.  Whereas I was looking for medicinal herbs and took a wrong turn."

            show JC hands

            JC "You took a wrong turn?  The same one every day this week?!"

            show JC angy

            show WQ sustalk

            WQ "These mountain paths are very confusing.  It could happen to anyone."

            JC "Right."

            show WQ angy

            WQ "Anyway, my point still stands.  Please stay away from my brother and we'll stay away from you."

            WQ "Good day, Jiang-gongzi."
                                
            hide WQ with moveoutleft

        "Maybe you have a point…":

            show JC hands

            JC "Okay, I get it.  We're all breaking the rules, so we'll keep it quiet from Lan-xiansheng if you do the same."

            JC "The bruises on Wei Wuxian's knees will get bruises if he's made to kneel for any more punishments."
                                
            $ chengqing += 1

            show WQ smile
            pause 0.5
            show WQ sustalk

            WQ "Agreed.  As a doctor, I try to prevent others from feeling pain."

            WQ "Even if they are as troublesome as Wei-gongzi."

            show WQ hmm

            show JC smile
            pause 0.5
            show JC angy

            JC "Troublesome is one word for it.  Impossible is another."

            show WQ sustalk

            WQ "Indeed."

            WQ "Please remember what I said about not involving my brother in any of that trouble."

            show WQ hmm

            show JC -angy

            JC "Right…"

            WQ "Good day, Jiang-gongzi."

            hide WQ with moveoutleft

            ##collective ending for good and neutral paths##

    show NHS left at left
    with moveinleft

    NHS "Soooo….."

    show NHS fan

    NHS "How did it go?"

    show JC -angy

    JC "Why do you keep leaving me alone with people?  I'm not good at talking to strangers."

    NHS "All the more reason to practice!"

    show NHS -fan
                    
    NHS "Look.  No one is expecting you to negotiate peace terms with the Wen sect, but…"

    show NHS fan

    NHS "Do you at least know if you like her yet?"

    show JC blush

    JC "Well…"

    menu:
        "Yes!":
                                
            JC "She is pretty cute when she's angry."

            show NHS smile

            NHS "That sounds like a good start to me!"

        "Who knows…":

            JC "I barely know her…"

            show JC -blush

            JC "But at least it's better than having to watch Wei Wuxian flirt with Lan-er-gongzi."

            show NHS smile

            NHS "That sounds like a good start to me!"

        "Nope!":

            JC "To be honest, I'd rather hang out with you and Wei Wuxian."

            NHS "Aww, Jiang-xiong!  You do care!"

            show JC angy

            JC "Ugh, shut up."

            NHS "Let's not leave Wei-xiong waiting then!  Let's head back."

            ##WWX yelling from off screen##

    WWX "Jiang Cheng! Nie-xiong!  Did you know that the tips of Lan Zhan's ears blush red when he's embarrassed!"

    show NHS fan

    show WWX right grin at right
    with moveinright

    show JC left

    WWX "You should have seen his {i}face{/i} when I showed him that yellow book I borrowed from you, Nie-xiong!"

    jump LXC_2

label LXC_2:

    scene bg indoors
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun3.mp3" fadein 1.0

    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Twenty-one days to Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)

    show JC right at midleft
    show NHS left pout at left

    NHS "Are you sure you won't do my homework for me, Jiang-xiong? I really need to paint this now, before my muse leaves me!"

    show JC hands

    JC "Tell your muse to wait! I barely have time to finish my own essays, let alone yours!"

    NHS "But Wei-xiong keeps getting dragged to the Library Pavilion by Lan Wangji! Maybe we should try to rescue him again..."

    if LWJ_talk_flag >= 1:
        show JC angy
        
        JC "No! I've had enough of trying to talk to that block of wood!"

        show NHS talk

        NHS "Hmm, maybe you need to call him 'Lan Zhan~' the way Wei-xiong does."

        show JC rage

        JC "BLEAGH! What the hell, don't say his name like that!"

        NHS "That's how Wei-xiong says it! And Lan Wangji seems to like it."

        show JC talk

        JC "Does he? How can you tell if he likes anything when he's only got the one expression???"

        show NHS talkfan

        NHS "Well, Wei-xiong's still alive, isn't he?"

        JC "That's because that idiot is harder to kill than a cockroach."
    
    else:
        show JC angy
       
        JC "No! I've had enough of Lan Wangji glaring at me!"
    
    JC "Besides, didn't you say that homework doesn't matter as long as you pass the tests?"

    show NHS pout

    NHS "I didn't think Da-ge would sic Meng Yao and Xichen-ge on me for not doing homework! All he said was that I wasn't allowed to fail again!"

    show JC talk

    JC "Well, either you do the work, or we have to keep sneaking around Cloud Recesses to avoid them, so take your pick."

    NHS "Hmm..."

    show NHS smile

    NHS "It's fun sneaking around when you're with someone else!"

    show NHS talk
    
    NHS "And anyway, I'm too busy to do any homework, this masterpiece isn't going to paint itself, you know."

    JC "Your—"

    play sound "audio/knock.mp3"

    show JC left

    JC "Huh, wonder who's that?"

    show JC left at midright
    with move

    NHS "No wait don't—"

    show LXC right at right
    with moveinright

    show JC talk

    JC "Oh! Zewu-jun! Good afternoon."

    LXC "Good afternoon, Jiang-gongzi. And Nie-gongzi, you're here as well! I thought you might be!"

    show NHS talkfan

    NHS "Ze...Zewu-jun, hi!"

    show NHS:
        ease 0.5 xoffset -100

    show NHS fan

    NHS "If you're here to talk to Jiang-xiong, I can go—"

    show LXC talk

    LXC "No, no, I was looking for you, actually, but you weren't in your rooms."

    LXC "And you weren't in the back hills either, despite a few of your classmates saying that you might be. I wonder how they came to that misapprehension..."

    NHS "...I don't know, I really don't know."

    show LXC -talk

    LXC "Well, I'm glad I found you. I don't mean to interrupt, but I've been hoping to have a quick chat, Huaisang, and check in on how you're doing."

    show NHS talkfan

    NHS "Oh, I'm doing great, Xichen-ge! Really great! In fact, you should tell Da-ge how great I'm doing!"
    
    NHS "Look, me and Jiang-xiong have been doing homework, we've been writing an essay about..."

    show NHS fan

    NHS "..."

    show JC right talk

    JC "{size=-9} Plant spirits."

    show NHS talkfan

    NHS "Plant spirits!"

    show LXC talk

    LXC "Ah, a complicated subject indeed. I hope you're not having any trouble? If you are, I'd be glad to be of assistance."

    NHS "Oh, no, no trouble at all, I'm so ready to go on all the night hunts and take down all the plant spirits!"

    show LXC -talk

    LXC "How wonderful! So you've both had no problems memorising the eleven classes of plant spirits and their respective elemental affinities and weaknesses?"

    show NHS fan

    NHS "Um...The eleven classes..."

    menu:
        "Make an attempt to list the eleven classes of plant spirits":

            show JC left talk

            JC "The eleven classes are Aromatics, Succulents, Evergreens..."

            show NHS talkfan

            NHS "Yes, those!"

            show JC blush

            JC "Er...herbal..."

            show LXC talk

            LXC "Ah, not quite. But that was a very good attempt, Jiang-gongzi."

            show LXC -talk     
        
        "Admit to having problems memorising the eleven classes of plant spirits":

            show JC left blush

            JC "I...I think I remember three classes? Maybe four. There's a lot to memorise about plant spirits."

            show LXC smile

            LXC "Indeed there is! But it's better to be aware of the gaps in one's knowledge than to be foolishly overconfident."

            show LXC -smile
            $ xicheng += 1

    LXC "I do find the way this topic is taught to be perhaps more obscure and dry than some of the others, so there's no shame in having some difficulty with it."

    LXC "Perhaps a mnemonic might help! I've often found that to be a valuable educational aid! In fact, I'd be happy to tutor you both for the rest of the afternoon!"

    LXC "And perhaps the next few afternoons as well—"

    show NHS fan

    NHS "NO no no no, I'm sure Xichen-ge is so very busy, you must have so many more important things to do with your time."

    show NHS talkfan

    NHS "In any case, studies aren't as important as...as what Jiang-xiong wants to talk to you about!"

    LXC "Oh? What does Jiang-gongzi want to talk to me about?"

    menu:
        "Actually, I wouldn't mind having some help with studying":
            show JC blush

            JC "Actually, I wouldn't mind having Zewu-jun's help with studying. If Zewu-jun doesn't mind."

            show NHS pout

            NHS "Nooooo, Jiang-xiong..."

            show LXC smile

            LXC "Not at all, I'm always glad to help! Besides, it is important to know one's limits and seek assistance when appropriate."

            $ xicheng += 1

            show LXC -smile

            LXC "Now, I came up with a mnemonic for the eleven classes of plant spirits, and another one for their elemental affinities. And another one for..."

            NHS "{size=-9}Nooooooooooooooooo...."

            scene bg class ## this is technically the start of MY_2
            with cutslow

            stop music fadeout 1.0
            play music "audio/fun4.mp3" fadein 1.0

            show bar
            show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Twenty days to Qixi{/color}{/font}" at truecenter
            with Dissolve(0.5)
            pause(2.0)
            hide text
            hide bar
            with Dissolve(0.5)

            show JC right angy at midright

            JC "Damn it, how did Nie Huaisang disappear after class so quickly? Did he already make it to Caiyi?"

        "Er. Something very important. Unrelated to studying":
            show JC left talk
            
            JC "Er. Something very important. Unrelated to studying."

            NHS "Yes! He was telling me about...about Lan-er-gongzi!"

            $ sangcheng += 1

            show LXC frown

            LXC "Oh? Has something happened with Wangji?"

            show NHS talk

            NHS "Oh, I don't know, I've barely spoken to Lan-er-gongzi since I got here. But Jiang-xiong has."

            if LWJ_talk_flag >= 1:
                show LXC -frown

                LXC "That's true, Wangji has mentioned this to me."

                JC "Wait, what? He has???"

                LXC "We have our evening meal together every day, and I always ask if he's making friends with the other guest cultivators."

                show LXC smile
                
                LXC "He's mentioned making conversation with Jiang-gongzi before, I remember being very pleased to hear it!"

                show JC angy

                JC "{i}Making conversation?{/i} Like hell that was—"

                show NHS talkfan

                NHS "Oh yes! Such conversation! When Jiang-xiong told me about it, I thought they both seemed to be...um...of the same mind!"

                show JC right

                JC "..."

            else:
                LXC "Hmm, I don't believe Wangji has mentioned speaking to Jiang-gongzi before."

                show NHS talkfan

                NHS "Oh, I'm sure they must have."
            
            NHS "In any case, Jiang-xiong was telling me about it, and I thought it sounded like Lan-er-gongzi was...Well..."

            show LXC right frown

            LXC "Wangji was what?"

            show NHS fan

            NHS "Interested in Wei-gongzi. I don't know, I don't really know Lan-er-gongzi that well, but after all Jiang-gongzi knows Wei-gongzi best, so I thought..."

            show LXC talk:
                ease 0.3 xoffset -800

            LXC "Oh? Yes? What did you think?"

            show NHS talkfan

            NHS "Well, just that Lan-er-gongzi seems awfully keen on dragging Wei-xiong off to be alone in the Library Pavilion all the time, right?"

            show JC right talk

            JC "What? But that's just because Wei Wuxian—"

            show LXC smile

            LXC "Yes! I thought so too!"

            NHS "In fact, I think they're both in the Library Pavilion right now! Alone!"            

            LXC "Oh! Well!"

            show LXC -smile

            LXC "Perhaps the two of them might also need some assistance learning about plant spirits."

            NHS "I bet they would! Wei-xiong's missed so much class because of all his punishments."

            LXC "Mn, it would be unfair to let him fall further behind in his studies because of this. Excuse me, gentlemen."

            show LXC left
            hide LXC with moveoutright
            show NHS pout:
                ease 0.5 xoffset 0

            NHS "Oh thank goodness, he's finally gone. Is nowhere in the Cloud Recesses safe..."

            show JC right talk

            JC "I guess next time you'll have to invent a talisman that teleports you from the doors of the lecture hall directly into Caiyi."

            scene bg class ## this is technically the start of MY_2
            with cutslow

            stop music fadeout 1.0
            play music "audio/fun4.mp3" fadein 1.0

            show bar
            show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Twenty days to Qixi{/color}{/font}" at truecenter
            with Dissolve(0.5)
            pause(2.0)
            hide text
            hide bar
            with Dissolve(0.5)

            show JC right angy at midright

            JC "Damn it, did Nie Huaisang actually find some way to teleport from the lecture hall to Caiyi? How did he disappear after class so quickly?"

            show JC hands

            JC "And how the hell did he manage to stuff this note into my sleeve without me noticing???"

    jump MY_2

label MY_2:
    show JC left at midright

    JC "Ugh, I need to finish my homework, but joining Huaisang in Caiyi for a bit would be pretty nice..."

    show MY left at midleft
    with moveinleft

    MY "Greetings, Jiang-gongzi."

    show JC right talk

    JC "Oh, Meng-gongzi. Greetings."

    show JC blush

    JC "If you're looking for Nie-gongzi, I have no idea where he is."

    MY "Hmm, I see."

    show MY talk

    MY "How fortunate that I was looking for you instead, Jiang-gongzi. Could you spare me a moment of your time?"

    menu:
        "Yes":

            show JC talk

            JC "Er, sure."

            $ chengyao += 1

            show MY smile

            MY "Jiang-gongzi is most gracious."

            JC "So, what is it?"

        "No":

            show JC talk

            JC "Sorry, I have to go, actually."

            show JC blush

            JC "To...my dorm. To do homework. {size=-9}Eventually."

            show MY -talk

            MY "I see."

            show JC talk

            JC "Okay, so I'll just be going then. Good bye."

            hide JC with moveoutright

            scene bg caiyi
            with cutfast

            show JC right at center

            JC "Right. Okay. Now, where on earth did Huaisang say he was going to be in Caiyi..."

            $ sangcheng += 1

            jump WBA_start
    
    show MY -smile

    MY "I've noticed that Jiang-gongzi has been spending a lot of time with Nie-er-gongzi. Could I venture that Jiang-gongzi would count himself a good friend of his?"

    ## scene changed from here on out

    menu: 
        "Yes":
            $ sangcheng += 1 ## seems a bit weird to get sangcheng points when NHS isn't around, but then NHS is probably hiding in a bush eavesdropping or something

            show JC blush

            JC "Er, yeah I hope so? We're...we're pretty good friends, I guess."

            if sangcheng >= 5:

                show MY smile

                MY "I believe Nie-er-gongzi feels the same."

            else:

                show MY smile

                MY "Indeed."

            show MY frowny

            MY "So I think he would take your advice, if you thought to give it. And I do believe he needs some, at least with regard to his studies."

        "No":
            show JC -talk

            JC "He hangs out with me and Wei Wuxian sometimes, I guess. And also other people."

            show MY -smile

            MY "Hmm, I see."

            show MY frowny

            MY "Still, I believe you are friends enough that he would listen to your advice. And I do believe he needs some, at least with regard to his studies."
    
    show JC talk

    JC "Oh, right, this is about his studies."

    show MY talk

    MY "Just so. I hear Jiang-gongzi is doing far better in his studies, and is also known for his good sense and diligence."

    menu:
        "Really?":
            
            show JC blush

            JC "Compared to Wei Wuxian and Nie Huaisang, sure, I got good sense."

        "Totally.":

            show JC roll

            JC "Oh, sure. Beacon of good sense and diligence, that's me."
    
    show MY smile

    MY "Quite. Don't you think Nie-er-gongzi could benefit from a little friendly encouragement towards good sense and diligence, as well?"

    menu:
        "I can try":

            show JC talk

            JC "So you want me to...what? Convince him to study? I mean, I can try. The Jiang sect motto {i}is{/i} attempt the impossible."

        "Pretty sure that's impossible":

            show JC talk

            JC "So you want me to...what? Convince him to study? Don't think anyone can earn enough friendship points to do {i}that.{/i}"

        "Sure, if you mean bribery":

            $ chengyao += 1

            show JC talk

            JC "So you want me to...what? Convince him to study? Won't you have better luck just bribing him?"

            show MY happy

            MY "Ah, I could never!"

            show MY smile

            MY "I mean that quite literally, unfortunately; his allowance is too substantial. Couldn't Jiang-gongzi attempt more traditional methods of persuasion first?"
    
    show JC hands

    JC "Look, I'll be honest, Meng-gongzi, I have to work hard because I'm the sect heir. But Nie Huaisang's not, he won't ever be the Nie sect leader."

    show MY happy

    MY "I certainly hope not. For his sake, and mine."

    show JC smile

    JC "Hah, yeah, sounds like a disaster for the Nie sect. And you."

    show JC hands
    
    JC "But that's why it's impossible to convince him to care about his studies. He doesn't need to care, not like I do."

    show MY smile

    MY "Hmm. I must say, the Jiang sect is fortunate to have a sect heir such as yourself, Jiang-gongzi."

    menu:
        "For sure!":
            
            show JC smile

            JC "Heh, thanks, I try my best. Gotta live up to the Jiang sect name!"

        "I guess...":

            show JC blush

            JC "I try my best, I guess. Um, thanks."

        "Wei Wuxian would be better":

            show JC blush

            JC "Eh, Wei Wuxian would probably be better."

            show MY frowny

            MY "Oh?"

            show MY talk

            MY "Please let me assure you, Jiang-gongzi, that from what I know of you both, that cannot possibly be further from the truth."

            show MY smile

            MY "While I've heard Wei-gongzi has a natural talent for cultivation, that is the least of the skills a sect leader must have. Surely a sense of duty and responsibility, like Jiang-gongzi has, is of far greater import."

            JC "If...if you say so. Thanks."

        "My sister would be better":

            show JC blush

            JC "Eh, my sister would probably be better."

            show MY frowny

            MY "Oh? Jiang-guniang? I've heard her cultivation is..."

            show JC hands

            JC "Cultivation isn't the most important thing about being sect leader, is it! She's good at organising things, and at diplomacy stuff! Heaps better than me!"

            show JC angy

            JC "She's great!!"

            $ chengyao += 1

            show MY smile

            MY "Yes, that does sound like she would make an excellent sect leader too. Though perhaps the fact that Jiang-gongzi recognises her skills speaks to his own capability as well."

            show JC blush

            JC "If...if you say so. Thanks."
        
    show MY talk
    
    MY "Well, in any case, thank you for taking the time to answer my questions, Jiang-gongzi."

    show JC talk

    JC "Right. Of course, Meng-gongzi."

    show MY smile

    MY "Now, if you'll excuse me..."

    show MY right smile
    hide MY with moveoutleft

    show JC -talk

    JC "Well."

    JC "That was..."

    show JC angy
    
    JC "Argh, damn it, Nie Huaisang this is your fault! Why am I talking to random people even when you're not around?"

    scene bg caiyi
    with Fade(0.1, 0.0, 0.2)

    show NHS left fan at center

    NHS "Achoo!"

    jump WBA_start

label WBA_start:

    scene bg gates
    with cutslow

    stop music fadeout 1.0
    play music "audio/WBA.mp3" fadein 1.0

    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Ten days to Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)

    show WQ right at right
    show JC left at left
    show WWX left talk at center
    
    WWX "You sure you really want to come with us, Wen-guniang?"

    show WQ talk

    WQ "I am. I'm sure it will be educational."

    WWX "Not sure why you need an education in eradicating water ghouls. Does Qishan even have any lakes?"

    show WQ hmm

    WQ "It has some."

    show JC talk

    JC "Let's not get ahead of ourselves. We don't even know if Zewu-jun will let us go along."

    show WWX grin

    WWX "I'm sure he can be convinced."

    scene bg gates
    with cutfast

    show LWJ left at left
    show LXC left at midleft
    with None
    
    WWX "There he is! Zewu-jun! Wangji-xiong!"
    
    show WQ right at right
    show WWX right at center
    show JC right at midright
    with moveinright

    show LXC talk

    LXC "Wei-gongzi. And Jiang-gongzi, Wen-guniang."

    show WWX talk

    WWX "Zewu-jun, we heard you're planning to head down to Biling Lake to deal with some water ghouls. Could we also come along? I'm sure it will be educational!"

    show JC talk

    JC "Wei Wuxian and I also have some experience eradicating water ghouls, since Yunmeng has many rivers and lakes. We might be able to be of assistance."

    LWJ "It's against the rules."

    show WWX -talk

    WWX "What's against the rules? Since Lan-xiansheng isn't here, none of us have classes for the next few days, so there's no reason why we can't go."

    LWJ "Unnecessary."

    show LXC right
    pause(1.0)
    show LXC left smile

    LXC "Ah, I see. Yes, perhaps Jiang-gongzi and Wei-gongzi could come along with us to Biling Lake."

    show LWJ angy

    LWJ "..."

    show WQ talk

    WQ "Zewu-jun, if I may, I too would like to join you all."

    show LXC frown

    LXC "Hmm."

    menu:
        "Speak up for Wen Qing, citing her insight and competence":
            JC "Zewu-jun, Wen-guniang's skills may lie mainly in the healing arts, but her cultivation is strong."

            JC "I'm sure she won't be a burden, and her knowledge and insight might even be of some help in this matter."

            show LXC talk

            LXC "Hm. Does Wen-guniang have much expertise with water spirits?"

            show WQ -talk

            WQ "I..."

            show WWX talk

            WWX "Even if she can't help with the water ghouls themselves, there might be some villagers in the area who could have been injured by the ghouls."

            WWX "She might be able to provide medical aid to them."

            show LXC -talk

            LXC "Hm. Very well, then perhaps Wen-guniang might join us as well."

            show WQ smile

            WQ "Thank you, Zewu-jun."

        "Speak up for Wen Qing, citing her ability to provide medical aid":
            JC "Zewu-jun, Wen-guniang is well-versed in the healing arts."

            JC "If one of us was injured during this night hunt, she might be of valuable assistance."

            show LXC -frown

            LXC "Hm. Very well, then perhaps Wen-guniang might join us as well."

            show WQ smile

            WQ "Thank you, Zewu-jun, Jiang-gongzi."

            $ chengqing += 1

        "Don't speak up":
            LXC "As I understand, Wen-guniang does not cultivate with the sword. Perhaps it will be safer if you stay behind."

            show WQ -talk

            WQ "I..."

            show WWX talk

            WWX "Zewu-jun, Wen-guniang's skills indeed lie with healing. Even if she can't help with the water ghoul themselves, there might be some villagers in the area who could have been injured by the ghouls."

            WWX "She might be able to provide medical aid to them."

            show LXC -frown

            LXC "Hm. Very well, then perhaps Wen-guniang might join us as well."

            show WQ smile

            WQ "Thank you, Zewu-jun."

    LXC "Now, let us head down the mountain."

    hide LWJ
    hide LXC
    hide JC
    hide WWX
    hide WQ
    with moveoutleft

    scene bg black
    with cutfast

    stop music fadeout 1.0
    play music "audio/funny.mp3" fadein 1.0

    NHS "WAAAAAAAAIT!"

    scene bg gates
    with Dissolve(0.5)

    show NHS right at midright
    with moveinright

    show LXC left at midleft
    show JC left at left
    with moveinleft

    LXC "Nie-gongzi?"

    show NHS talkfan

    NHS "HellohelloareweallgoingtoCaiyiI'llcomealongtoolet'sgolet'sgo!"

    LXC "...what was that?"

    show NHS talk:
        ease 0.2 xoffset -150

    NHS "LET'S GO TO CAIYI QUICK LET'S—"

    show MY right at right
    with moveinright

    MY "There you are."

    show MY talk

    MY "Er-gongzi, you—oh, Zewu-jun!"
    
    MY "And Jiang-gongzi, and...so many other people. May I ask why everyone is standing at the gates?"

    show LXC smile

    LXC "Meng-gongzi, what a pleasure to see you!"

    show LXC -smile
    
    LXC "We were just about to head down the mountain. There have been reports of water ghouls in Biling Lake, and we were about to head down to assess the situation."

    show NHS talkfan

    NHS "Great, sounds educational! I wanna go too!"

    LXC "Oh? I'm glad to hear that Nie-gongzi is taking an interest in his education!"

    show MY -talk

    MY "I do believe that Nie-er-gongzi's education would be better served by staying in the Cloud Recesses and studying."

    MY "Not to mention that water ghouls are no laughing matter, and might be too dangerous for Nie-er-gongzi to deal with, if you'll excuse my presumption for saying so."

    LXC "Ah, Meng-gongzi does have a point..."

    show NHS left pout

    NHS "You can't keep me here, Meng Yao! Everyone is going to Caiyi and I don't want to be left here all alone!"

    show MY talk

    MY "You won't be alone, Er-gongzi. I'll also be here."

    NHS "Yes, that's exactly the problem. You'll also be here. You and your scrolls."

    show NHS talkfan

    NHS "Anyway, I'm sure I'll be fine! There are so many strong cultivators here who'll look out for me, like...like Jiang-xiong! Right, Jiang-xiong?"

    menu:
        "Agree to stick with Huaisang":
            show JC talk

            JC "Yeah, I guess I can keep an eye out for Nie-gongzi if he comes to Caiyi with us."

            jump WBA_1
        
        "Don't stick with Huaisang":
            show JC talk

            JC "What? But aren't you always saying you don't want to go on night hunts anyway?"

            jump WBA_2

        "Stay in the Cloud Recesses":
            show JC talk

            JC "Look, what if I stay in the Cloud Recesses with you and Meng-gongzi?"

            jump WBA_3

    jump end

label WBA_1:

    show NHS right smile

    NHS "Yeah! Thanks, Jiang-xiong, you're the best!"

    $ sangcheng += 4
    show MY -talk

    MY "...Very well. If it's not too much trouble, I'd like to be permitted to come along as well."

    show NHS left talk

    NHS "You don't have to worry about me, Meng Yao, you and your scrolls can stay in the Cloud Recesses. Jiang-xiong won't let me get hurt."

    show NHS talkfan

    NHS "Besides, you haven't got much experience with night hunting either. I've got Jiang-xiong to protect me, but who will protect you?"

    MY "That's..."

    show LXC talk

    LXC "I will."

    show LXC -talk

    LXC "Not that Meng-gongzi will need any protection, I'm sure. But I will do everything in my power to make sure that no one coming along will be injured."

    show MY blush

    MY "Oh, that's...I wouldn't want to be a burden..."

    show LXC smile

    LXC "You could never be a burden, Meng-gongzi."
    
    LXC "Even if you're not the strongest in sword cultivation, Nie-zongzhu has said that you make up for it in combat in countless other ways. I'm confident you would be an asset to our hunt."

    show MY smile

    MY "You praise this undeserving one far too much, Zewu-jun."

    $ xiyao += 1

    show WWX left talk at midleft
    show LWJ left at left
    with moveinleft

    show JC right:
        ease 0.5 xoffset 650

    show LXC right:
        ease 0.5 xoffset 900
    
    show NHS right:
        ease 0.5 xoffset 0
    
    show MY right:
        ease 0.5 xoffset 150

    WWX "Soooo, I guess you're both coming along then. Cool! This is a real party now!"

    LWJ "...This is a night hunt."

    show WWX grin right

    WWX "That's what I said! I can tell how excited you are to have all of us along for the ride, Lan Zhan, don't try to hide it!"

    LWJ "..."

    JC "..."

    MY "..."

    show LXC smile

    LXC "Indeed! Shall we all head to Caiyi, then?"

    hide LXC
    hide WWX
    hide LWJ
    hide NHS
    hide MY
    hide JC
    with moveoutleft

    WN "Wait, A-jie! A-jie, can I come along too?"

    show WN right at midright
    with moveinright

    show LXC left frown at left
    show WQ left at midleft
    with Dissolve(0.5)

    LXC "..."

    scene bg caiyi
    with cutslow

    stop music fadeout 1.0
    play music "audio/sneaky.mp3" fadein 1.0

    show JC right at midleft

    NHS "Pssst Jiang-xiong, come here."

    show NHS right fan at center
    with moveinright

    show JC left

    JC "What?"

    show JC talk at center
    show NHS at midright
    with move
    
    JC "Why are you dragging me into this alley? We're going to get separated from the others."

    NHS "That's the plan."

    JC "What? Where are we going?"
    
    NHS "Away. I don't want to go to Biling Lake."

    show JC angy

    JC "{i}What?{/i}"

    show NHS talkfan

    NHS "There's so many more fun things to do in Caiyi than get rid of a few water ghouls! Safer, too!"

    JC "But—"

    show NHS talk

    NHS "I slipped a note into Zewu-jun's sleeve so he won't worry about us! I said we're going to go look at books and study materials! Come on!"

    show NHS left talk:
        ease 0.3 xoffset 150
        pause(0.3)

    show JC rage

    JC "You did what! I did {i}not{/i} agree to—"

    show NHS right talkfan

    NHS "You agreed to keep an eye on me in Caiyi though! And I'm not going to Biling Lake, so you'll have to follow me to keep an eye on me, won't you?"

    show NHS pout
    
    NHS "You won't go back on your word, right, Jiang-xiong?"
    
    show NHS talk

    NHS "Besides, didn't you say you're sick of the bland food in the Cloud Recesses? I'll buy you the most delicious dessert in all of Caiyi! It's to die for!"

    show JC angy

    JC "...It better be amazing, or you {i}will{/i} die for it."

    scene bg cornetto
    with cutfast

    show JC left smile at midleft
    show NHS right at midright
    
    JC "...Wow, it {i}is{/i} amazing."

    show NHS smile

    NHS "See? Isn't this the best frozen dessert you've ever had?"

    show NHS talk

    NHS "Caiyi's where you wanna go, for an ice-cold Cornetto~"

    show JC talk

    JC "...Are you getting paid by them or something?"

    show NHS fan

    NHS "No, no, I don't know what you mean."

    show NHS talkfan

    NHS "But see, isn't this better then going on some night hunt for water ghouls?"

    show NHS talk

    NHS "Why fight silly water ghouls, have an ice-cold Cornetto~"

    show JC -talk

    JC "..."

    JC "...You sure you're not getting paid for this?"

    jump WBA_end

label WBA_2:

    $ xicheng += 1

    show NHS right pout

    NHS "I know, but..."

    if LXC_1_flag == 2:
        JC "Water ghouls can be really dangerous if you're not ready to fight them. I can try to protect you, but it's safer if you're not there at all."

        NHS "I guess, but..."
    
    else:
        JC "Water ghouls can be really dangerous if you're not ready to fight them, and if you're not, you should just stay here."

        NHS "But..."
    
    show MY right smile

    MY "I entirely agree, Jiang-gongzi."

    show LXC smile
    
    LXC "Indeed. I do believe Jiang-gongzi is displaying a very sensible caution."

    show LXC -smile

    LXC "Nie-gongzi, please stay in the Cloud Recesses with Meng-gongzi. As for the rest, let us make haste for Biling."

    NHS "Nooooo..."

    hide MY
    hide NHS
    with moveoutright

    hide LXC
    hide JC
    with moveoutleft

    WN "Wait, A-jie! A-jie, can I come along too?"

    show WN right at midright
    with moveinright

    show LXC left frown at left
    show WQ left at midleft
    with Dissolve(0.5)

    LXC "..."

    scene bg biling
    with cutfast

    stop music fadeout 1.0
    play music "audio/biling.mp3" fadein 1.0

    "The cultivators reach the shore of Biling Lake. What was once a noisy gathering of merchant vessels coming and going from Caiyi is now empty of visible life."

    "Eerie silence stretches over still waters, beneath which unidentifiable shadows dart and quiver."

    show LXC right talk at right
    show WWX left at center
    show JC left at left
    with dissolve

    LXC "Everyone, I've rented these five boats from one of Caiyi's merchants. Once you've ensured that you have the talismans you'll need on hand, please ready yourselves and board the boats."

    hide LXC with moveoutright
    show WWX right talk

    WWX "Hey, Jiang Cheng, got any extra talisman paper?"

    show JC talk

    JC "Didn't you bring your own? Also, why the hell is Lan Wangji in one boat while all the other Lans are in another?"

    show WWX -talk

    WWX "What?"

    JC "And are Wen Qing and Wen Ning getting their own boat?"

    WWX "Huh? Why shouldn't they get their own boat?"

    show WWX grin
    
    WWX "Oh, nice, found a few pieces in my other sleeve!"

    show JC hands

    JC "Because Wen Qing doesn't have combat skills and her brother is a kid?"

    show WWX -grin

    WWX "I'm sure they'll be fine. Wen Qing's secretly scary as hell. The water ghouls'll leave her alone if they know what's good for 'em."

    show WWX talk
    
    WWX "You think these are too wrinkled to work?"

    show JC angy

    JC "What—Wei Wuxian, what the hell did you do to your talisman paper, eat it and shit it out again?"

    show JC hands

    JC "For fuck's sake, take some of mine."

    show WWX grin

    WWX "Awesome, thanks! Oh, look, there's two more boats empty, just enough for us to take one each!"

    hide WWX with moveoutleft

    show JC angy

    JC "Wait, but—"

    menu:
        "Ask Lan Xichen to consider rearranging everyone":
            $ xicheng += 1

            JC "Ugh, this is stupid."

            scene bg biling
            with cutfast

            show JC left at center
            with moveinleft

            show LXC right at right
            with Dissolve(0.5)

            show JC talk

            JC "Excuse me, Zewu-jun. Can I suggest we change who's on which boat?"

            show LXC talk

            LXC "Hmm? What do you mean?"

            JC "It's probably better for there to be two or three people to each boat. Those in the same boat can watch each other's backs, and if any given boat capsizes, all the others will have space to take additional passengers."

            show LXC smile

            LXC "Oh, an excellent idea! Jiang-gongzi must have great experience leading night hunts against water spirits."

            show JC blush

            JC "Oh, I... Well, not that much. But my father always puts me in charge of organising all the disciples."

            show LXC -smile

            LXC "I can see why Jiang-zongzhu would do so. I'm sure his faith in Jiang-gongzi's ability to take charge is well-founded."

            LXC "Now, how would you advise us to rearrange ourselves?"

            scene bg biling
            with cutfast

            "The group sets off after a quick reshuffle: Jiang Cheng now in the same boat as Wei Wuxian, Lan Xichen with Wen Qing and Wen Ning, and the other Lan cultivators split between the last two boats. Somehow, Lan Wangji still ends up alone."

            "The water ghouls turn out to be something far more sinister: a waterborne abyss. Thankfully, no one is injured during this surprise discovery, and the group of young cultivators return to Caiyi Town, soaking wet but triumphant."

            scene bg caiyi
            with cutfast

            stop music fadeout 1.0
            play music "audio/fun3.mp3" fadein 1.0

            show WWX right at midright
            show JC left at midleft

            WWX "Man, I thought it would be more fun than that."

            show JC talk

            JC "What, was splashing water at Lan Wangji not fun enough for you? Chattering his ear off the entire night hunt after he joined our boat not fun enough for you?"

            show WWX talk

            WWX "I figured we'd get to do more than just watch Zewu-jun do his thing. Though seeing what's-his-face flail in panic before Lan Zhan rescued him was kinda funny."

            JC "You mean Su She?"

            WWX "Dunno, I can never tell all the Lans apart, they all have the same white robes and judgey faces."

            show JC angy

            JC "{i}Lan Wangji{/i} has the same damn white robes and judgey face and you seem to be able to recognise him just fine!"

            show WWX grin

            WWX "Oh, speaking of, I think that's him over there!"

            hide WWX with moveoutleft
            
            WWX "Lan Zhan, hey Lan Zhan, d'you want a loquat..."

        "Ask Wen Qing if you can share a boat with her and Wen Ning": 

            $ chengqing += 1

            JC "Ugh, this is stupid."

            scene bg biling
            with cutfast

            show WN right at right
            show WQ right at midright
            with Dissolve (0.5)

            show JC left at midleft
            with moveinleft

            JC "Uh, excuse me, Wen-guniang. Can I share a boat with you and your brother?"

            show WQ talk

            WQ "Hm? There's still a spare boat, if Jiang-gongzi would prefer."

            show JC blush

            JC "Yes, I know. But just in case there's any trouble, if you and your brother need help..."

            show WQ -talk

            WQ "Ah, I see."

            show WQ smile
            
            WQ "Thank you, Jiang-gongzi, we'd appreciate it."

            scene bg biling
            with cutfast

            "Once everyone is ready, the group sets off onto the dark waters in their rented boats. As an unnatural mist rolls in, Wei Wuxian discovers that what they thought were water ghouls is actually something far more sinister: a waterborne abyss."

            "Jiang Cheng nearly gets injured, but Wen Qing's sharp eyes spot the attack before it lands. And so when Wen Ning suddenly takes ill—eyes filming over white and body going weak—Jiang Cheng easily carries him up to safety."
            
            "Lan Xichen finally eradicates the abyss, and the group of young cultivators return to Caiyi Town, soaking wet but triumphant."

            scene bg caiyi
            with cutfast

            stop music fadeout 1.0
            play music "audio/fun3.mp3" fadein 1.0

            show WWX right at midright
            show JC left at midleft

            WWX "Man, I thought it would be more fun than that."

            show JC talk

            JC "What, was splashing water at Lan Wangji not fun enough for you? Chattering his ear off the entire night hunt not fun enough for you?"

            show WWX talk

            WWX "At least {i}you{/i} got to play hero in front of Wen Qing and rescue her brother."

            show JC blush

            JC "I wasn't playing at anything! He was sick!"

            show WWX -talk

            WWX "Weird time to fall sick, huh?"
            
            WWX "Ah, I just figured we'd get to do more than watch Zewu-jun do his thing. Though seeing what's-his-face flail in panic before Lan Zhan rescued him was kinda funny."

            show JC talk

            JC "You mean Su She?"

            WWX "Dunno, I can never tell all the Lans apart, they all have the same white robes and judgey faces."

            show JC angy

            JC "{i}Lan Wangji{/i} has the same damn white robes and judgey face and you seem to be able to recognise him just fine!"

            show WWX grin

            WWX "Oh, speaking of, I think that's him over there!"

            hide WWX with moveoutleft
            
            WWX "Lan Zhan, hey Lan Zhan, d'you want a loquat..."
        
        "Take the last boat":
            $ wangxian += 2

            JC "Ugh, fine."

            scene bg biling
            with cutfast

            "Once everyone is ready, the group sets off onto the dark waters in their rented boats. As an unnatural mist rolls in, Wei Wuxian discovers that what they thought were water ghouls is actually something far more sinister: a waterborne abyss."
            
            "Jiang Cheng gets injured, and Lan Wangji has to enact a heroic rescue of Wen Ning, Su She, and Wei Wuxian."
            
            "Thankfully, Lan Xichen manages to eradicate the abyss, and the group of young cultivators finally return to Caiyi Town, soaking wet but triumphant."

            scene bg caiyi
            with cutfast

            stop music fadeout 1.0
            play music "audio/fun3.mp3" fadein 1.0

            show WWX left at center
            show JC right at right

            WWX "Ah, Jiang Cheng, that was fun, wasn't it?"

            show JC angy

            JC "Fun? What part of being attacked by a {i}surprise waterborne abyss{/i} was fun???"

            show WWX grin

            WWX "All of it! Too bad Nie-xiong didn't come along, aha I bet he'd have wet his pants!"

            show WWX right talk

            WWX "Hey, Lan Zhan! There you are!"

            show LWJ left at left
            with moveinleft
            
            WWX "Have a loquat!"

            show LWJ angy

            LWJ "...No."

            WWX "Ah, he really has no taste."

            show WWX left talk
            
            WWX "Here, Jiang Cheng, catch!"

            hide WWX
            hide JC
            with moveoutright

            LWJ "..."

            show LXC right at center
            with moveinright

            LXC "Wangji, if you want loquats, I can buy a basket back home."

            LWJ "No."

    jump WBA_end

label WBA_3:

    show MY smile

    MY "Yes, that would be very much appreciated, Jiang-gongzi."

    $ chengyao += 1

    show NHS pout

    NHS "I guess that's fine too..."

    scene bg library
    with cutfast

    stop music fadeout 1.0
    play music "audio/2fun.mp3" fadein 1.0

    show MY left at left
    show JC right at center
    show NHS right pout at right
    with dissolve

    MY "What is one possible sign that a restless spirit has had an unnatural death?"

    NHS "I don't know."

    show JC talk

    JC "An unusual collection of yin energy around its grave, which can manifest as unnatural cold."

    show MY talk

    MY "Correct. What about one possible sign that a restless spirit did {i}not{/i} have an unnatural death?"

    NHS "I don't knoooow."

    JC "The spirit not being particularly attached to its place of death."

    show MY -talk

    MY "Correct. Nie-er-gongzi, we've {i}just{/i} gone through this topic together, should we go through it again?"

    show NHS:
        ease 0.5 yoffset 300

    NHS "Noooo, I'll die of boredom and become a restless spirit myself."

    show MY talk
    
    MY "Might another approach be more helpful? I apologise if this isn't engaging enough."

    menu:
        "This is engaging enough":

            $ chengyao += 1

            JC "Nah, it's fine. This is way more engaging than how Old Man Lan teaches it, actually. Less painful."

            show MY smile

            MY "Well, high praise indeed. Thank you, Jiang-gongzi, let's continue"

        "A break might be more helpful":

            $ sangcheng += 1

            JC "Maybe a break would help. We've been studying for a shichen now."

            NHS "Yeah, a whole shichen! I'm about to keel over and turn into a restless spirit myself!"

            show MY -talk

            MY "I suppose a break can't hurt. But let's at least get to the end of this chapter."

    show NHS pout

    NHS "No, I need a break now! A...a pee break!"

    show MY -smile

    MY "Er-gongzi, you've just—"

    show NHS fan:
        ease 0.1 yoffset 0

    NHS "There's a waterborne abyss in my bladder, Meng Yao, I can't fight it, I'll be right back!"

    show NHS left at offscreenright
    show MY at right
    with ease

    MY "Er-gongzi, wait—"

    show JC left

    JC "You should just let him go."

    show MY right frowny

    MY "Oh? Should I?"

    menu:
        "He deserves a break":

            $ chengyao -= 1

            show JC smile

            JC "He's probably about to pass out or something. You made him study more today than he has in the whole of last month."

            JC "That's pretty damn good already, right?"

            show MY -frowny

            MY "Do you find it so, Jiang-gongzi? Somehow, I'm not sure that I agree."

        "You deserve a break":

            $ chengyao += 1

            show JC smile

            JC "You've got to be about to pass out or something. You made him study more today than he has in the whole of last month."

            JC "That's pretty damn good already, right?"

            show MY -frowny

            MY "Do you find it so, Jiang-gongzi? Somehow, I'm not sure that I agree."

        "He's going to pass anyway":

            show JC roll

            JC "He's going to pass anyway, so what's the point?"

            show MY -frowny

            MY "Is he? Not to cast doubt upon Nie-er-gongzi's many talents, but is Jiang-gongzi aware that Nie-er-gongzi has already failed three times?"

            show JC blush

            JC "Uh, yes, but..."

            menu:
                "He's working extra hard":

                    JC "He's. Actually. Working extra hard."

                    JC "Where you can't see."

                    $ chengyao -= 2

                    show MY frowny

                    MY "Oh?"

                    MY "I suppose I will have to take Jiang-gongzi's word for it, and keep my eyes peeled."

                "Just have faith":

                    JC "You should just have faith in him. He might surprise you."

                    JC "Very surprising person, that Nie Huaisang."

                    show MY frowny

                    MY "...I suppose I can't disagree with that."

                "He has a plan to cheat":

                    $ chengyao += 2

                    JC "He, um, has a plan to cheat."

                    MY "...Is that so."

                    show MY smile

                    MY "Well, thank you for your honesty, Jiang-gongzi. Let me be honest in return, and say that I'm relieved that he {i}has{/i} a plan at all."

                    show MY talk

                    MY "I don't suppose Jiang-gongzi knows the details of said plan...?"

                    show JC smile

                    JC "Sure I do. Wei Wuxian is going to make some kind of talisman that copies his answers to Nie Huaisang's scroll."

                    JC "It's the kind of stupidly ingenious thing that—"

                    show JC talk

                    JC "Er. Wait, you really don't care...?"

                    show MY smile
        
                    MY "Oh, I care, and I would be grateful if Jiang-gongzi could convince Wei-gongzi and Nie-er-gongzi to tell me about their plan in greater detail."

                    show MY happy

                    MY "Because I care so much about Nie-er-gongzi's academic success, as Jiang-gongzi is aware."

                    show JC smile

                    JC "Hah, sure, I'll tell them."

                    show MY smile

                    MY "I'm grateful for your assistance, Jiang-gongzi."
            
    show MY talk

    MY "Well, in any case, I suppose that we're free of restless spirits for today. What would you like to do now, Jiang-gongzi?"

    menu:
        "I'll go find the others in Caiyi":

            show JC talk

            JC "I guess I'll head to Caiyi, see how the others are doing with the water ghouls."

            show MY smile

            MY "How thoughtful of you, Jiang-gongzi, I'm sure your strength and skill has been sorely missed."

            show JC blush

            JC "I guess, sure..."

            show MY talk

            MY "Good day to you then, Jiang-gongzi, and good luck."

            show JC smile

            JC "Right, yes. Good day, Meng-gongzi"

            show MY left talk at offscreenright
            with ease
            pause 0.5

            scene bg caiyi ## edit music/bg later
            with cutfast

            stop music fadeout 1.0
            play music "audio/fun3.mp3" fadein 1.0

            show JC right at midright
            with moveinright

            JC "Guess they've already gone ahead to Biling. Maybe I can still catch up—"

            NHS "Jiang-xiong! Over here!"

            show NHS left talk at midleft
            with moveinleft

            NHS "You made it out of Meng Yao's clutches alive!"

            show JC angy

            JC "Have you been on pee break in Caiyi this whole time??"

            show NHS talkfan

            NHS "Well, it's much easier to go with the sound of water right outside your window, isn't it?"

            show JC rage

            JC "Next time you run away to take a 'break', I'm breaking your legs!!"

            jump LET_1

        "I'll go after Nie Huaisang":

            show JC talk

            JC "I guess I'll go after Nie Huaisang, see what he's up to."

            show MY -talk

            MY "Ah, of course, I'm sure I'd rather not know."

            show MY talk
            
            MY "I'd offer to accompany you, Jiang-gongzi, but somehow I suspect you'll have more luck without me."

            show JC blush

            JC "Er..."

            show MY smile

            MY "Good day to you then, Jiang-gongzi, and good luck."

            show JC talk

            JC "Right, yes. Good day, Meng-gongzi"

            show MY left
            hide MY with moveoutright
            pause 0.5

            scene bg dorm  ## edit music/bg later
            with cutfast

            stop music fadeout 1.0
            play music "audio/fun3.mp3" fadein 1.0

            show NHS bush at midleft
            with dissolve

            show JC left at center
            with moveinleft

            JC "Right, now where would he be hiding..."

            hide NHS
            with moveoutbottom

            show NHS left talk at midleft
            with moveinbottom

            NHS "You made it out of Meng Yao's clutches alive!"

            show JC right rage:
                ease 0.2 xoffset 400
            
            JC "GAH!"

            show JC hands

            JC "Where the hell did you come from! Have you been hiding this whole time?"

            show NHS talkfan

            NHS "No no, I just wanted to make sure Meng Yao wasn't following you. Did you talk him into giving up?"

            show JC roll

            JC "I didn't talk him into anything, but he sounds like he's given up on you alright."

            JC "At least for today."

            show NHS smile

            $ sangcheng += 1

            NHS "Great! See, Jiang-xiong, you really are the best at talking to people!"

            show JC angy

            JC "Next time you run away to take a 'break', I'm breaking your legs!!"

            jump LET_1

        "We could keep studying":

            $ chengyao += 1

            show JC talk

            JC "We could keep studying? You're pretty great at teaching things."

            show JC blush

            JC "Only if you want to! Not that Meng-gongzi has to teach anyone anything—except Nie Huaisang, maybe..."

            show MY smile

            MY "Jiang-gongzi is certainly the more apt pupil. It would be my pleasure."

            show MY talk

            MY "Now, where were we—"

        "What do you want to do?":

            $ chengyao += 2

            JC "What would {i}you{/i} like to do now, Meng-gongzi? You're always running after Nie Huaisang, but now that he's run away—"

            show JC angy

            JC "I mean, not to say you don't do anything else, or that you don't WANT to do anything else!"

            show JC hands

            JC "But if you DID want to do something else I'm just saying that you can! Not that you need my permission or anything!"

            show JC blush

            JC "Whatever. Do whatever you want."

            show MY blush

            MY "Perhaps I will, Jiang-gongzi."

            show MY talk

            MY "I'd like to spend more time here in the library, and Jiang-gongzi is very welcome to join me if—"

    show MY -talk

    show JC -blush

    show NPC1 at offscreenleft
    show NPC2 at offscreenleft
    
    NPC1 "{size=-9}Hey look, is that Jin-zongzhu's bastard hanging out with Jiang Wanyin?"

    show JC right

    NPC2 "{size=-9}Yeah, that's Meng Yao alright. That guy doesn't know his place."

    menu:
        "Yell at them":

            $ WBA3_yell = True

            jump .JCyell            

        "Ignore them":
            show JC left talk

            JC "Um, tell me more about, er, plant spirits."

        "Tell Meng Yao to ignore them":

            $ chengyao -= 1

            show JC left angy

            JC "UGH, ignore those assholes. Tell me about, er, plant spirits."

        "Ask Meng Yao about Jin Guangshan":

            $ chengyao -= 2

            show JC left talk

            JC "So, Jin Guangshan's your father?"

            show MY frowny

            MY "Yes."

            JC "That sucks."

            MY "You could say that."

            show MY -frowny

            MY "Though perhaps we could discuss more relevant academic topics instead?"

            show JC blush

            JC "Right. Yes. Tell me about, er, plant spirits."

    MY "Of course. There are various classifications of plant spirits, which can be—"
            
    NPC1 "{size=-9}Isn't he usually yapping after Nie Huaisang? Found some other master's boots to lick, hasn't he?"

    show JC right
    pause 0.5
    show JC left angy

    JC "SO. Those classifications."

    show MY talk

    MY "Yes. While they can be difficult to remember, in the field, the most pertinent thing to note is that—"

    show JC right angy
    show MY -talk

    NPC2 "{size=-9}Sure looks like it. Not like he can go crawling back to his father after all {i}that{/i}, heh."

    menu:
        "Keep ignoring them":

            show JC left angy

            JC "RIGHT. What is the pertinent thing about...whatever we're talking about?"

            show MY talk

            MY "Plant spirits. What's most pertinent in the field is whether they use airborne attacks, such as pollen that lowers inhibitions, or physical attacks, like vines that may function as spiritual whips or rope bindings."

            NPC1 "{size=-12}Guess he'll go crawling to any sect heir. I saw him pestering Lan Xichen too."

            NPC2 "{size=-18}Zewu-jun must know better than to associate with someone like that. I suppose Jiang Wanyin likes having his boots licked, hah!"

            show MY -talk

            MY "..."

            show JC hands

            JC "{i}Anyway!!{/i} How about those attacks!"

            show MY frowny

            MY "...They've left, Jiang-gongzi. You needn't keep up the pretense."

            menu:
                "What pretense?":

                    $ chengyao += 1 ## ehhh might remove this point

                    show JC angy

                    JC "Who's pretending anything! Maybe I want to learn about ropes and whips with you!"

                    show MY blush

                    MY "...I don't think that's in the curriculum."

                    show MY -blush

                "What the fuck is with them!":

                    show JC angy

                    JC "What the fuck is with them! Why the hell are they going around talking about you like that!"

                    MY "Ah, well, I'm sure I couldn't speculate."

                    JC "Actually, I bet you could!"

                    show MY -frowny

            MY "Ah, it doesn't matter. It's very kind of you to have spent the last shichen with me, Jiang-gongzi, but I'm sure you have other things that need your attention."

            jump .WBA3end

        "Yell at them":

            jump .JCyell

    label .JCyell:

        $ chengyao += 1

        show JC rage at left
        with move
            
        JC "HEY, WHAT THE HELL ARE YOU TWO TALKING ABOUT!"

        show NPC1 at midleft
        show NPC2 at left
        show JC at midright
        show MY at offscreenright
        with move

        NPC1 "What? What??"

        hide MY

        NPC2 "We weren't saying anything!"

        show JC angy

        JC "Weren't saying anything? Then what was that I heard you say about Meng-gongzi?"

        NPC1 "I...I said he was Jin-zongzhu's illegitimate son, that's all! Everyone knows that!"

        NPC2 "Yeah, maybe you didn't know that about Meng Yao, but it's true."

        NPC1 "And everyone also knows that his mother is a prostitute!"

        menu:
            "{i}Your{/i} mom is a prostitute":

                $ chengyao -= 2

                show JC rage

                JC "{i}Your{/i} mother is a prostitute! And {i}you{/i} should crawl back into the gutter she birthed you in!"

            "Don't talk about him like that":

                ## mid-arc romance splash screen here?

                show JC rage

                JC "How dare you talk about Meng-gongzi like that! You watch your mouth, or Sandu will watch it for you!"

            "Jin Guangshan sucks anyway":

                $ chengyao -= 1

                show JC rage

                JC "Jin Guangshan is a philandering low-life who no one wants as a father anyway! And you two are even lower than he is!!"

            "I don't care who his parents are":

                ## mid-arc romance splash screen here also? or only here? If it's only here might be a good idea to beef up the dialogue some more

                $ chengyao += 1

                show JC rage

                JC "I don't give a shit who his parents are! And I don't give a shit who {i}your{/i} parents are either, I can beat you up all the same!"

        show NPC1:
            ease 0.1 yoffset -100
            ease 0.1 yoffset 0
            pause 0.2
            ease 0.5 xoffset -200

        show NPC2:
            ease 0.1 yoffset -100
            ease 0.1 yoffset 0
            pause 0.2
            ease 0.5 xoffset -200

        NPC1 "Whoa, okay, chill out, Jiang-gongzi. Just thought you ought to know."

        NPC2 "Yeah, not trying to pick a fight or anything. We were just leaving anyway."

        JC "Good! Leave!"

        show NPC1 at offscreenleft
        show NPC2 at offscreenleft
        with move

        NPC1 "{size=-9}Man, what's wrong with that Jiang Wanyin."

        NPC2 "{size=-12}He's unstable. Guess it's not a surprise, with a mother like the Violet Spider."

        NPC1 "{size=-18}Hah, more like the Violent Spider. I hear she beats up her husband all the time!"

        show JC rage at midleft
        with ease

        JC "WHAT DID YOU SAY ABOUT MY MOTHER?!"

        MY "Jiang-gongzi, wait—"

        menu:
            "Wait":

                pass

            "Get their asses":

                JC "YOU TWO ASSHOLES GET BACK HERE!!"

                hide JC with moveoutleft
                
                show MY right at right
                with moveinright

                NPC1 "{size=-12}Stop! No...no running in the Cloud Recessess!"

                JC "{size=-18}THEN STAND STILL AND GET YOUR ASS KICKED!!"

                MY "..."

                jump LET_1

        $ chengyao += 1

        show MY right at right
        with moveinright

        show JC left rage

        JC "What!!"

        MY "Leave them be, Jiang-gongzi, it's not worth the trouble."

        show JC hands

        JC "Not worth the trouble?! Did you hear what they said??"

        show MY frowny

        MY "Of course I heard. But chasing them down will only stop them saying it in your hearing, Jiang-gongzi, and not out of it."

        show JC angy

        JC "That's still better than just letting them talk anywhere they want, any way they want!"

        show MY -frowny

        MY "Perhaps. But it's still best if they didn't talk at all."

        show JC -angy

        JC "..."

        show JC talk

        JC "Are you suggesting I kill them...?"

        JC "Not saying I'm opposed, exactly, but—"

        show MY happy

        MY "What? Haha, I'd never suggest anything like that!"

        show MY talk

        MY "At least, not for so minor an incident."

        show MY -talk

        MY "I just meant not giving people any reason to talk at all. That is to say, if you aren't seen with me, then there wouldn't have to be talk about you, Jiang-gongzi."

        jump .WBA3end

    label .WBA3end:

        show JC hands

        JC "What? Are you telling me to go?"

        show MY frowny

        MY "I..."

        show MY -frowny

        MY "Only if you want to."

        show JC blush
        
        JC "...What if I don't want to?"

        show MY blush

        MY "Please don't misunderstand, I truly have enjoyed Jiang-gongzi's company today. And I hope Jiang-gongzi has enjoyed mine."

        show MY -blush

        MY "But Jiang-gongzi must see that people will talk, if you're seen spending time with me."

        menu:
            "Who cares what they say":
                show JC angy

                JC "Who gives a shit about what people say!"

                show MY smile

                MY "...Who indeed."

            "They don't know you":

                $ chengyao += 2

                show JC angy

                JC "They don't know a damn thing about you, so who cares what they have to say! The people who really know you will know better!"

                show MY blush

                MY "And I suppose Jiang-gongzi knows better."

            "I can talk louder":

                $ chengyao += 1

                show JC angy

                JC "They're not the only ones who can talk!"

                JC "I can talk, and I bet I can talk louder!"

                show MY smile

                MY "Indeed. Why, when Jiang-gongzi talks, sometimes all of the Cloud Recesses listens."

        if WBA3_yell == True:

            show MY talk

            MY "Now, shall we get back to more important matters? I believe we were learning about restless spirits."

            MY "Let's move on to how to fight them."

            show JC smile

            JC "Finally! Now we're getting to the good part."

            jump LET_1
        
        show MY talk

        MY "Now, shall we get back to plant spirits? Firstly, how to combat their sex pollen in the field."

        show JC blush:
            ease 0.1 yoffset -100
            ease 0.1 yoffset 0

        JC "Sex pollen?! What the hell is sex pollen???"

        jump LET_1

label LET_1:

    ## edit bg and music and days to Qixi
    
    scene bg class
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun3.mp3" fadein 1.0

    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Ten days to Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)

    show JC left at left
    show NHS right smile at right
    show WWX left at center
    with dissolve

    NHS "It worked, it worked! I really might pass after all! Wei-xiong you're a life-saver and a genius!!!"

    show WWX talk

    WWX "Of course I am! Why would you ever doubt me?"

    menu:
        "Get over yourself":

            show JC angy

            JC "Ugh, get over yourself. The only thing you're a genius at is breaking the rules."

            show WWX right cheeky

            WWX "Aww Jiang Cheng, no need to be jealous! You're welcome to use my talisman if you need it during the final exam too."
        
        "Fine, you're a genius":

            $ chengxian += 1

            show JC roll

            JC "Fine, fine, you're a genius. A genius at {i}breaking the rules.{/i}"

            show WWX right grin

            WWX "Aw, Jiang Cheng, I know you're secretly very impressed by my talismans! Hey, if you wanna use them too—"

    show JC rage

    JC "I don't need your stupid cheating talisman!!"

    show NHS talkfan

    NHS "Well, I do! So I'm glad Wei-xiong very cleverly invented it so that I don't have to fail!"

    show JC hands

    JC "But that was just a quiz! What if Old Man Lan takes more precautions against cheating in the final exam?"

    show WWX talk

    WWX "Why would he? He didn't notice anything was wrong, we were super sneaky!"

    show NHS fan

    NHS "Super duper sneaky! And now we should super duper sneak our way out of the Cloud Recesses and into Caiyi town to celebrate!"

    show JC talk

    JC "Why do we have to sneak—oh, are Meng-gongzi and Zewu-jun looking for you again?"

    show NHS pout

    NHS "They're always trying to hunt me down! It's all Da-ge's fault, they—"

    show NHS talkfan:
        ease 0.15 yoffset -40
        ease 0.15 yoffset 0

    NHS "Wait! Jiang-xiong, you should talk to Da-ge for me!"

    show JC angy

    JC "Talk to {i}your Da-ge?{/i} Isn't he in Qinghe?! You want me to go {i}all the way to—{/i}"

    show NHS talk

    NHS "No no, just write him a letter!"

    show NHS fan

    NHS "Tell him how well I'm doing and that I'm totally gonna pass and that he should call off his spies—ahem, I mean he should tell Meng Yao and Xichen-ge that they can totally leave me alone!"

    show JC roll

    JC "Yeah, like he's gonna believe me over Meng-gongzi and Zewu-jun."

    show NHS talkfan

    NHS "Of course he will! You're so responsible and trustworthy!"

    show WWX cheeky

    WWX "Heh, you mean boring and too unimaginative to lie."

    show JC hands

    JC "{i}Who are you calling boring—{/i}"

    show WWX left grin

    WWX "Besides, Jiang Cheng's terrible at letter writing! Shijie always has to help him or it takes him all day. Bet he won't finish in time to join us in Caiyi."

    show JC rage

    JC "{i}WEI WUXIAN, I'LL SHOW YOU TERRIBLE—{/i}"

    show NHS pout

    NHS "I'm sure Jiang-xiong will write a great letter! Won't you, Jiang-xiong?"

    menu:
        "Write the letter":

            $ sangcheng += 1

            show JC hands

            JC "Damn right! I'll write a great fucking letter!"

            show NHS smile

            NHS "Yay! Thanks, Jiang-xiong, I'm sure Da-ge will be really impressed! And convinced about my diligence and academic prowess!"

            show JC roll

            JC "...I don't know if {i}anyone{/i} can write a letter that's {i}that{/i} good."

            show WWX right talk

            WWX "Good luck! Take breaks every hour or your hand will cramp up! Remember to eat and sleep and use the toilet! And if nobody sees you for the next three days, we'll know what you're doing."

            show JC angy

            JC "If nobody sees me, it'll be because I {i}smothered you in your sleep{/i} to get you to {i}shut up{/i} and had to go on the run!"

            show NHS talk

            NHS "Don't worry, Jiang-xiong! I'll help you hide the body!"

            show WWX left wat

            WWX "Hey, I thought I was your life-saver."

            show NHS smile

            NHS "You are, you are. Which is why I'll buy you four jars of Emperors Smile in Caiyi before Jiang-xiong kills you!"

            show WWX grin

            WWX "Sounds like a good way to go, I accept!"

            show JC hands

            JC "Ugh, both of you get lost already. I have a letter to write. Apparently."

            jump LET_2
        
        "Go to Caiyi":

            show JC hands

            JC "No! I'm not writing a great letter, or {i}any{/i} letter, to Chifeng-zun!"

            show NHS pout

            NHS "But Jiang-xiong..."

            show WWX left talk

            WWX "Yeah, better not. What if Jiang Cheng does such a bad job at it that your Da-ge comes down in person to make sure you study?"

            show JC angy

            JC "I would not!"

            show NHS talk

            NHS "Jiang-xiong would not!"

            show NHS fan

            NHS "...Would he?"

            show WWX cheeky

            WWX "Oh, he would, I'll get Shijie to show you some of his most appalling attempts—"

            show JC rage

            JC "WEI WUXIAN—"

            show WWX grin

            WWX "—But we said we were going to Caiyi! To celebrate! So why spoil a good day!"

            JC "I'LL SPOIL YOUR FACE—"

            jump GIFT_1

label LET_2:

    scene bg indoors
    with cutslow

    ## music double-check later

    stop music fadeout 1.0  
    play music "audio/fun3.mp3" fadein 1.0

    show JC left angy at center
    with moveinleft

    JC "—of course I can write a fucking letter, I can write a great fucking letter—"

    show JC:
        ease 0.5 yoffset 100

    JC "—I'll start right fucking now and catch up with them in Caiyi and—"

    show JC -angy

    JC "Wait."

    show JC angy

    JC "I need paper! Where the hell's my paper!"

    show JC angy:
        ease 0.2 yoffset 0
        ease 0.5 xoffset 500
        ease 0.5 xoffset 0

    JC "And my ink!"

    show JC right angy:
        ease 0.5 xoffset -500
        ease 0.5 xoffset 0

    JC "And brush! And seal! And paper—no, wait, I already have—{nw}"

    show JC right hands:
        ease 0.1 yoffset -100
        ease 0.1 yoffset 0

    extend "{i}SHIT ow shit paper cut!{/i}"

    show JC rage

    JC "FUCK THIS STUPID LETTER, LET'S FINISH IT ALREADY!!"

    scene bg letter

    JC "...how the hell do letters start??"

    menu:
        "To the esteemed Chifeng-zun,":

            JC "I remember A-jie said to always address the other person politely, so..."

            $ let1 = "To the esteemed Chifeng-zun,"
        
        "To Nie-zongzhu":

            $ mingcheng += 1

            JC "Can't go wrong calling him Nie-zongzhu, not like Nie-zongzhu could ever be anyone else..."

            $ let1 = "To Nie-zongzhu,"

        "To Nie Mingjue,":

            JC "That...is his name, isn't it...? Damn it, no one ever calls him by name, how do you even write it..."

            $ let1 = "To {s}Nie Minjue{/s} {s}Nie Mingju{/s} Nie Mingjue,"

        "To Nie Huaisang's Da-ge,":

            $ mingcheng += 1

            JC "If Nie Huaisang wants me to write to his Da-ge, then I damn well will."

            $ let1 = "To Nie Huaisang's Da-ge,"

        "Dear Da-ge,":

            JC "Fuck, this is stupid, letters are stupid, Nie Huaisang should write it his damn self!"

            JC "Ah, fuck, I'll just go whatever Nie Huaisang would say, that can't be wrong...right??"

            $ let1 = "Dear Da-ge,"
    
    let "[let1]" ## this nvl shit needs fixing the spacing is weird, but also wait for actual bg letter before you start on that

    JC "Now some kind of opening paragraph...thing..."

    menu:
        "Talk about the weather":

            $ let_weather = True

            JC "Ah, fuck, can't go wrong with the weather."

            $ let2 = "The weather in Gusu is quite warm. I thought it would be colder, but it's not."

        "Ask after his health":

            JC "Ah, fuck, I'll just ask about his health, he can't have a problem with that."

            $ let2 = "How has your health been? I'm sure there's nothing wrong with your health."

        "Write about the lectures":

            JC "He keeps sending Nie Huaisang here for the lectures, clearly he must give a shit about it."

            $ let2 = "The Cloud Recesses lectures are happening right now. There are classes almost every day."

        "Skip the opening pargraph":

            $ mingcheng += 1

            JC "Ah, fuck, who cares about the opening, I always skip reading it anyway."

            $ let2 = "Greetings.{p=0.1}{p=0.1}"
    
    nvl clear
    scene bg letter

    let """

    [let1]

    [let2]

    """

    JC "Hmph. Needs more...something."

    menu:
        "Talk more about the weather" if let_weather == True:

            JC "...More...weather...?"

            $ let3 = "Still, the weather isn't too bad. Not as good as the weather in Yunmeng though. How is the weather in Qinghe?"
        
        "Talk about the weather" if let_weather == False:

            $ let_weather = True

            JC "Can't go wrong with the weather."

            if let2 == "Greetings.{p=0.1}{p=0.1}":
                $ let3 = "The weather in Gusu is quite warm. I thought it would be colder, but it's not."
            else:
                $ let3 = "Also, the weather in Gusu is quite warm. I thought it would be colder, but it's not."

        "Talk about Lan Xichen":

            $ let_LXC = True
            $ mingcheng += 1

            JC "Oh, he knows Zewu-jun, I guess I could talk about him."

            if xicheng >= 3: ## come back to work on point totals, and also on what JC would say based on prev points
                $ let3 = "Zewu-jun has been here in the Cloud Recesses. He's kind. And nice. And tall. You probably knew that."
            else:                
                $ let3 = "Zewu-jun has been here in the Cloud Recesses. He lives here. You probably knew that."

        "Talk about Meng Yao":

            $ let_MY = True
            $ mingcheng += 1

            JC "Oh, he knows Meng Yao, I guess I could talk about him."

            if chengyao >= 3: ## come back to work on point totals, and also on what JC would say based on prev points
                $ let3 = "Meng-gongzi arrived safely at the Cloud Recesses. He smiles a lot. It's a nice smile. You probably knew that."            
            else:                
                $ let3 = "Meng-gongzi arrived safely at the Cloud Recesses. You probably knew that. Since he's probably writing to you too."
        
        "Talk about Lan Qiren":

            JC "I guess he knows Old Man Lan? I could talk about him...?"

            $ let3 = "Lan-xiansheng is still teaching here. You probably knew that. Everyone and their grandfathers probably knew that. I bet Lan-xiansheng lectured them too."

    nvl clear
    scene bg letter
    let """

    [let1] {nw}

    [let2] {w}[let3]

    """

    JC "GOOD ENOUGH. Time to get to the point."

    menu:
        "Nie Huaisang is doing great":

            $ mingcheng -= 1
            $ NHS_let_flag = True

            JC "Nie Huaisang you better thank me for this..."

            $ let4 = "Nie Huaisang is doing really well in his studies. I know, because I have been studying with him."

        "Nie Huaisang is doing fine":

            $ mingcheng += 1
            $ NHS_let_flag = True

            JC "As if he'd believe Nie Huaisang is doing great."

            $ let4 = "Nie Huaisang is doing fine. Not great, but not terrible. I know, because I have been studying with him."

        "Nie Huaisang is...doing...":

            JC "Better not lie to Chifeng-zun..."

            $ let4 = "Nie Huaisang is doing. Stuff. Like calligraphy, which is one of the four great arts. Also painting. Which is another of the four great arts."
    
    nvl clear
    scene bg letter
    let """

    [let1] {nw}

    [let2] [let3]

    [let4]

    """

    JC "...Damn it! Why the fuck is there still so much paper?!"

    menu:
        "Talk about the weather" if let_weather == False:

            $ let_weather = True

            JC "Guess I can always talk about the weather."

            $ let5 = "By the way, did you know the weather in Gusu is quite warm? I thought it would be colder, but it's not."
        
        "Talk about Lan Xichen" if let_LXC == False:

            $ let_LXC = True
            $ mingcheng += 1

            JC "Oh, he knows Zewu-jun, I guess I could talk about him."

            if xicheng >= 3: ## come back to work on point totals, and also on what JC would say based on prev points
                $ let5 = "By the way, did you know Zewu-jun has been here in the Cloud Recesses? He's kind. And nice. And tall. You probably knew that."
            else:                
                $ let5 = "By the way, did you know Zewu-jun has been here in the Cloud Recesses? He lives here. You probably knew that."
        
        "Talk about Meng Yao" if let_MY == False:

            $ let_MY = True
            $ mingcheng += 1

            JC "Oh, he knows Meng Yao, I guess I could talk about him."

            if chengyao >= 3: ## come back to work on point totals, and also on what JC would say based on prev points
                $ let5 = "By the way, did you know Meng Yao arrived safely at the Cloud Recesses? He smiles a lot. It's a nice smile. You probably knew that."            
            else:                
                $ let5 = "By the way, did you know Meng Yao arrived safely at the Cloud Recesses? You probably knew that. Since he's probably writing to you too."
        
        "Talk more about Nie Huaisang":

            $ let_NHS = True
            $ mingcheng += 1
            $ NHS_let_flag = True

            JC "Eh, he's probably happy to keep hearing about Nie Huaisang. Or at least, to hear about this one thing."

            $ let5 = "Don't worry about him. He'll pass his exams this year."

        "Talk about Wen Qing":

            $ let_WQ = True
            $ mingcheng -= 1

            JC "I guess...he might also know...Wen Qing...?"

            $ let5 = "By the way, did you know Wen Qing is also here in the Cloud Recesses? Her brother, Wen Ning, is also with us. Her cousin, Wen Chao, was here at first, but is thankfully no longer with us. {w}I mean he left, not that he's dead."

        "Skip the closing paragraph":

            $ mingcheng += 1

            JC "Eh, no one wants to read more than they have to, anyway."

            $ let5 = "Regards, Jiang Wanyin of Yunmeng Jiang"
        
    nvl clear
    scene bg letter
    let """

    [let1] {nw}

    [let2] [let3] {nw}

    [let4]

    [let5]

    """
    scene bg indoors 
    with cutfast

    show JC left hands
    with dissolve

    JC "...In addition—OW, HAND CRAMP!"

    show JC angy

    JC "Fuck this! I'm done!!"

    show JC left angy
    pause 0.5
    show JC rage

    JC "...HOW HAS IT BEEN A SHICHEN ALREADY??"

    if NHS_let_flag == True:
        $ sangcheng += 1

    jump WBA_end

label GIFT_1:

    scene bg caiyi
    with cutslow

    ## music double-check later

    stop music fadeout 1.0  
    play music "audio/fun3.mp3" fadein 1.0            

    show WWX right at right
    show JC right at center
    show NHS right at left
    with moveinright
    pause 0.5

    show NHS talk

    NHS "...and this one's so elegant! I'll have this fan too, thanks!"

    show JC hands

    JC "Your haul is already twice your weight! How are you planning to carry it back up the mountain?!"

    show NHS left talkfan

    NHS "I'm sure my very good friends Wei-xiong and Jiang-xiong will help me carry it all, right?"

    show WWX talk

    WWX "I have my own haul to carry, but Jiang Cheng can help you! He hasn't bought anything at all."

    show JC left angy

    JC "The only thing {i}you've{/i} bought is two jars of Emperor's Smile!"

    show WWX grin

    WWX "They're very heavy jars!"

    show WWX cheeky

    WWX "And if Lan Zhan spots us on the way back, I have to be prepared to run very fast."

    show NHS talk

    NHS "Are you really not going to buy anything, Jiang-xiong? Look, they're selling so many different things here!"

    scene bg shop
    with cutfast

    JC "What's this random pile of junk! I don't want any of this!"

    SHOPK "What are you calling junk, you little wretch?!"

    WWX "Sorry about him, Uncle, he was raised by dogs."
    
    NHS "{size=-9}Now you {i}really{/i} have to buy something, Jiang-xiong. Look, maybe you could get a gift for someone else?"

    label giftshop:

        call screen shopping
    
        label gift_MYgd:

            if seen_MYgd == False:

                $ seen_MYgd = True

                WWX "What about this chonky jade bangle—whoa, it's heavy!"

                JC "Who the hell would wear a bangle this big? You could knock someone out with this thing!"

                WWX "Well, it's fancy jewellery, so bigger is better, right?"

                NHS "Don't be such a size queen, Wei-xiong. {i}Greener{/i} is better, not bigger."
                
                WWX "It {i}is{/i} very green...Oh, but it's got a crack in it."

                JC "Tch, no wonder it's not selling for much, it's broken crap."

                SHOPK "CRAP?! It might have a crack, but it's still made of the finest Dragonstone jade!"

                NHS "{size=-9}Hmm, the jade {i}is{/i} high quality. He might have to sell it at a markdown because of the crack, but a person with good business sense could cut beads from it instead and sell {i}that{/i} for far more."

                WWX "{size=-9}But why would anyone want a present they're supposed to break apart and sell?"

                NHS "{size=-9}I guess it depends on the person."
            
            NHS "So, Jiang-xiong, do you want to buy this jade bangle?"

            menu:
                "Yes":

                    $ giftbought = "MYgd"

                    jump giftbought

                "No":

                    NHS "Let's see what else there is."

                    jump giftshop

        label gift_WQgd:

            if seen_WQgd == False:

                $ seen_WQgd = True

                NHS "Chatter chatter chatter about the present here"  ## placeholder text!!
            
            NHS "So, Jiang-xiong, do you want to buy this thing WQ will like?" ## change the thing to the actual thing!!

            menu:
                "Yes":

                    $ giftbought = "WQgd"

                    jump giftbought

                "No":

                    NHS "Let's see what else there is."

                    jump giftshop

        label gift_LXCgd:

            if seen_LXCgd == False:

                $ seen_LXCgd = True

                NHS "Chatter chatter chatter about the present here"  ## placeholder text!!
            
            NHS "So, Jiang-xiong, do you want to buy this thing LXC will like?" ## change the thing to the actual thing!!

            menu:
                "Yes":

                    $ giftbought = "LXCgd"

                    jump giftbought

                "No":

                    NHS "Let's see what else there is."

                    jump giftshop

        label gift_LWJgd:

            if seen_LWJgd == False:

                $ seen_LWJgd = True

                WWX "Is this a textbook? 'The Definitive Guide to the Anatomy, Behaviour, and Habitat Use of Leporidae'."

                NHS "What are Lepeordi...Leperidi...those? Some kind of yao?"

                JC "No idea. There's no diagrams or illustrations or anything."

                WWX "{i}'Leporids ferment fiber in the cecum and then expel the contents as cecotropes, which are reingested. The cecotropes are then absorbed in the small intestine to utilize the nutrients. The dental formula of leporids is—'{/i}"

                NHS "Noooo, stop before I fall asleep, Wei-xiong."

                JC "At least you could use it as a pillow if you fall asleep reading it, it's thick enough..."

                WWX "You could also cut a hole in the pages and hide a {i}different{/i} book in it, it's thick enough for that too!"

                JC "Why the hell would anyone do that!"

                NHS "Ohhhhh, you could! Hmm..."
            
            NHS "So, Jiang-xiong, do you want to buy The Definitive Guide to the Anatomy, Behaviour, and Habitat Use of Leporidae?"

            menu:
                "Yes":

                    $ giftbought = "LWJgd"

                    jump giftbought

                "No":

                    NHS "Let's see what else there is."

                    jump giftshop

        label gift_MYbad:

            if seen_MYbad == False:

                $ seen_MYbad = True

                NHS "Oh look, here's a book that's nice and thin!"

                WWX "'The Illustrated Classics of Filial Piety'...looks like it's for kids."

                JC "Ugh, sounds boring. Put it back"

                SHOPK "Boring?! Did your parents not raise you right, young man, filial piety is one of the highest virtues!"

                JC "I know that! I didn't mean that filial piety is boring, I meant this book is—"

                WWX "{i}What my shidi means!{/i} Is that all the {i}rest{/i} of your goods are so exciting that this one pales just a little in comparison..."

                NHS "Actually, it's quite good! The illustrations are really well drawn!"

                SHOPK "Hah! Now {i}that{/i} is a young man of taste and virtue."

                NHS "...I wonder if the artist takes commissions for works that {i}aren't{/i} for kids..."
            
            NHS "So, Jiang-xiong, do you want to buy 'The Illustrated Classics of Filial Piety'?"

            menu:
                "Yes":

                    $ giftbought = "MYbad"

                    jump giftbought

                "No":

                    NHS "Let's see what else there is."

                    jump giftshop

        label gift_WQbad:

            if seen_WQbad == False:

                $ seen_WQbad = True

                NHS "chatter"
            
            NHS "So, Jiang-xiong, do you want to buy the thing WQ will hate?"

            menu:
                "Yes":

                    $ giftbought = "WQbad"

                    jump giftbought

                "No":

                    NHS "Let's see what else there is."

                    jump giftshop

        label gift_LXCbad:

            if seen_LXCbad == False:

                $ seen_LXCbad = True

                NHS "chatter"
            
            NHS "So, Jiang-xiong, do you want to buy the thing LXC will hate?"

            menu:
                "Yes":

                    $ giftbought = "LXCbad"

                    jump giftbought

                "No":

                    NHS "Let's see what else there is."

                    jump giftshop

        label gift_LWJbad:

            if seen_LWJbad == False:

                $ seen_LWJbad = True

                JC "There's a book here...'The Regret of Chunshan', wonder what that's—GAAAAH!!"

                NHS "Oooh, it's the illustrated version, I have a copy at home! It's good, I thought the artist picked the best, most dramatic scenes to draw!"

                WWX "Whoa, surely no one's heavenly pillar is that...dramatic..."

                JC "I'm not buying porn out here in broad daylight!!"

                SHOPK "Hmph, well the shop's open until late evening, so if you prissy young masters want to sneak back after sunset, you can."

                JC "THAT'S NOT WHAT I—"

                NHS "{size=-9}Shhh not so loud! Now everyone's looking!"
            
            NHS "So, Jiang-xiong, do you want to buy The Regret of Chunshan?"

            menu:
                "Yes":

                    $ giftbought = "LWJbad"

                    jump giftbought

                "No":

                    NHS "Let's see what else there is."

                    jump giftshop
           
        label giftbought:

            NHS "Great! I'm sure someone will like this!"

            WWX "{size=-9}And now we don't have to duel this uncle for the honour of his shop before he lets Jiang Cheng leave."

            jump GIFT_2

label GIFT_2:

    scene bg gusu
    with cutfast

    ## change music or keep the same?    

    show NHS right at right
    show WWX right at center
    show JC right angy at left
    with moveinright

    JC "...still think it was all overpriced rubbish!"

    show WWX talk

    WWX "That's the price you pay for having no manners."

    show NHS fan

    NHS "At least we got away safely. Jiang-xiong, I really thought that shopkeeper was going to beat you up even after you paid him."

    show JC left hands

    JC "It's your fault! If you hadn't forced me to look at his shop, I wouldn't have insulted his goods in the first place!"

    show NHS talkfan

    NHS "Well, you've already paid for it. If you don't want to keep it, why not give it to someone else?"

    menu:
        "Give it to Lan Xichen": ## edit this text later

            jump GIFT_LXC

        "Give it to Wen Qing": ## edit this text later

            jump GIFT_WQ

        "Give it to Meng Yao": 
            
            show JC blush

            JC "Maybe I'll give it to Meng-gongzi..."

            show WWX cheeky

            WWX "Oho, Meng-gongzi, is it? Soooo, do you like him? Is he your type?"

            show JC angy

            JC "What? What type—I don't—"

            WWX "But you want to give him a present! You want him to know you thought of him!"

            show JC hands

            JC "It's just a gift, I don't want him to know any damn thing—"

            show WWX left cheeky

            WWX "Did you hear that, Nie-xiong? Jiang Cheng wants to give Meng Yao a gift—a courting gift!"

            show JC rage

            JC "{i}It's not a courting gift! No courts involved!! BOTH OF YOU SHUT UP!!{/i}"

            show JC right rage at offscreenleft
            with ease

            show NHS pout

            NHS "I didn't even say anything..."

            jump GIFT_MY

        "Give it to Nie Huaisang":

            show JC left hands:
                ease 0.1 xoffset 100
                ease 0.1 xoffset 0

            JC "Fine! Nie Huaisang, you take it!"

            show NHS smile

            NHS "Aww, for me? Thanks, Jiang-xiong!"

            show NHS fan

            NHS "I'll make sure to give it to someone who'll really appreciate this...and maybe get something in return..."

            jump WBA_end

        "Give it to Wei Wuxian":

            show JC left hands:
                ease 0.1 xoffset 100
                ease 0.1 xoffset 0

            JC "Wei Wuxian, you deal with this!"

            show WWX wat

            WWX "What am I supposed to do with—"

            show WWX cheeky

            WWX "Oh! I could give it to Lan Zhan!"

            show JC angy

            JC "Is there nothing in your brain but Lan Wangji?! Why would you give something like this to him!"

            if giftbought == "LWJgd":
                show WWX right talk

            else:
                show NHS fan

                NHS "Yeah, Wei-xiong, I'm not sure Lan-er-gongzi will like it..."

                show WWX left cheeky

            WWX "Hey, it's the thought that counts, right?"

            show WWX left
            hide WWX with easeoutright

            show JC hands

            JC "That's the problem, dumbass! There {i}was{/i} no thought!! YOU NEVER HAVE THOUGHTS!!"

            jump GIFT_LWJ

        "Keep it":

            show JC angy

            JC "I already paid through my nose for this, I'm damn well keeping it!"

            show WWX cheeky

            WWX "Good idea! Next time you piss someone off, you'll have a present on hand to appease them."

            show NHS fan

            NHS "I don't know, I feel like this present might piss some people off even more..."

            show WWX talk

            WWX "That's true. Maybe you should give it to Shijie, at least she'll love you no matter what."

    jump WBA_end

label GIFT_LXC: ## edit everything including bg and music!

    scene bg library
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun3.mp3" fadein 1.0

    show LXC left at midleft
    with None

    show JC right at midright
    with moveinright

    JC "Hi Zewu-jun, here have [giftbought] as a present"

    jump WBA_end

label GIFT_WQ: ## edit everything including bg and music!

    scene bg backhill
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun3.mp3" fadein 1.0

    show WQ left at midleft
    with None

    show JC right at midright
    with moveinright

    JC "Hi Wen Qing, here have [giftbought] as a present"

    jump WBA_end

label GIFT_MY: ## edit music and maybe bg?

    scene bg class
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun3.mp3" fadein 1.0

    show MY left at midleft
    with dissolve

    show JC right talk at midright
    with easeinright

    JC "Meng-gongzi, there you are."

    show MY talk

    MY "Jiang-gongzi, greetings. Were you looking for me?"

    show JC blush

    JC "No. Yes. It's not—"

    show JC hands:
        ease 0.1 xoffset -100
        ease 0.1 xoffset -100

    JC "JUST TAKE THIS, ALRIGHT?! IT'S NOT A COURTING GIFT JUST A REGULAR GIFT!"

    if giftbought == "MYgd":

        $ chengyao += 2

        show MY frowny:
            ease 0.1 yoffset -100
            ease 0.1 yoffset 0
        
        MY "It's...a jade bangle? For me?"

        show JC angy

        JC "It's too big for you! And it's got a crack in it!"

        MY "I...see."

        show JC hands

        JC "Nie Huaisang said you could get it cut into beads and sell it for more money cause the jade is high quality!"

        show JC angy

        JC "ARGH look, I'm bad at presents, but you seem like a practical person so I thought maybe you could sell this off and buy yourself something nice! If you want!!"

        show JC hands

        JC "And if you don't want, then you can use it as a weapon and throw it at someone's head or something, I don't know!!"

        show MY talk

        MY "...I suppose no one would suspect that a jade bangle could be a murder weapon. And it doesn't take blood stains."

        show JC blush

        JC "Right! Exactly! Good!"

        show MY blush

        MY "It {i}is{/i} good, Jiang-gongzi, thank you."

        MY "I always appreciate your honesty and forthrightness. And as you say, I'm a practical person."

        show MY smile
        
        MY "That you tried to give me something I could use to help myself...well, that's worth more to me than the best jade in the world."

    elif giftbought == "MYbad":

        $ chengyao -= 2

        show MY frowny:
            ease 0.1 yoffset -100
            ease 0.1 yoffset 0
        
        MY "A gift?"

        MY "'The Illustrated Classics of Filial Piety'...ah. A children's book. To teach them about filial piety."

        show MY -frowny

        MY "..."

        show JC angy

        JC "Look, you like books, right? Books that teach people things? You're always carrying them around!"

        show MY frowny

        MY "...I am indeed often carrying textbooks around for Nie-er-gongzi's benefit, yes."

        show JC hands

        JC "Right! So I figured you'd want to have some of your own, instead of borrowing from the Lan sect library all the time. And this one's about filial piety, that's always good, right?"

        MY "...So it is said, yes. That's...a thoughtful...thought."

        show JC blush

        JC "Great. So, enjoy reading it. Hope you, um, learn something."

        show MY -frowny

        MY "..."

        show MY happy

        MY "Yes, I'm sure this children's book will be both entertaining and educational. How gracious of Jiang-gongzi, to think of me when he saw this."

        MY "Now, if you'll excuse me, Jiang-gongzi, I really cannot wait to crack into it."

        show MY right
        hide MY with moveoutleft

        show JC talk

        JC "Great. That went well. Right?"

        JC "...Right?"

    else:

        $ chengyao += 1

        show MY frowny:
            ease 0.1 yoffset -100
            ease 0.1 yoffset 0

        MY "Oh! Oh? Oh..."

        show MY -frowny

        MY "Ah, thank you, Jiang-gongzi. This is...very kind of you."

        show MY talk

        MY "I'll just...keep this. Thank you. Again."

        show JC blush

        JC "Good! You do that!"

        JC "Goodbye."

        show JC left blush
        hide JC with easeoutright

        show MY -talk

        MY "But why...?"

    jump WBA_end

label GIFT_LWJ: ## edit music and maybe bg? also needs new audio clip!

    scene bg library
    with cutslow

    stop music fadeout 1.0
    play music "audio/fun3.mp3" fadein 1.0

    show LWJ left at midleft
    with dissolve

    show WWX right talk at midright
    with easeinright

    WWX "Hey Lan Zhan, Lan Zhan!"

    LWJ "..."

    show WWX at center
    with ease

    WWX "Guess what! I got you a present!"

    show LWJ:
        ease 0.5 xoffset -100

    LWJ "...No."

    show WWX cheeky

    WWX "Here, look!"

    if giftbought == "LWJbad": 

        $ wangxian -= 1

        WWX "It's a book! You like books, right?"

        LWJ "...Mn. The Regret of Chunshan...?"

        show LWJ angy:
            ease 0.1 yoffset -100
            ease 0.1 yoffset 0
        
        LWJ "?!?"

        show WWX grin

        WWX "Ahahah! Great book, right? Lots of illustrative diagrams and everything!"

        LWJ "You—!!"

        play sound "audio/swords.mp3"
        ## play sound "audio/paperslashed.mp3" ## need to find this audio clip for this scene

        show WWX wat:
            ease 0.1 xoffset 300
        
        WWX "WHOA!"

        show WWX cheeky

        WWX "Really, Lan Zhan, ruining another book? I'm starting to think you hate reading!"

        WWX "Is that it? Do you secretly hate books? You can tell me, I promise to keep it a secret from Old Man Lan—"

        show LWJ right angy
        hide LWJ with moveoutleft
    
    elif giftbought == "LWJgd": 

        $ wangxian += 1

        show WWX talk

        WWX "It's a book! You like books, right?"

        LWJ "...Mn. The Definitive Guide to the Anatomy, Behaviour, and Habitat Use of Leporidae...?"
        
        LWJ "..."

        LWJ "Ah."

        show WWX grin

        WWX "Yeah, it's a book about bunnies!"
        
        show WWX cheeky
        
        WWX "Except written in the most boring, stuffy, Lan way possible. Which I figure makes it perfect for you!"

        LWJ "Hmm."

        show WWX talk:
            ease 0.3 xoffset -100

        WWX "You like it, don't you?"

        LWJ "..."

        show WWX grin

        WWX "You do! I knew you would, you like my present sooooo much! Is it 'cause of the bunnies, or 'cause it's the most boring textbook I've ever read? I bet it's both, it takes a real talented writer to make even bunnies boring, you know, and..."        

    else:
        LWJ "..."

        LWJ "I decline."

        show LWJ right at offscreenleft
        with move

        show WWX grin

        WWX "Awww, hate to see you leave, love to watch you go!"

    jump WBA_end

label WBA_end:

    scene bg dormnight
    with timepass

    stop music fadeout 1.0
    play music "audio/fun2.mp3" fadein 1.0

    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Seven days to Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)

    let "{vspace=200}As the weeks of lectures pass and the final exam looms ever closer, some students discover new depths to their wells of diligence; their dormitory windows stay lit well into the night as they bury their noses further into their scrolls and tomes."

    let "Some other students, however, are staying up past sunset for slightly different reasons..."

    scene bg indoorsnight
    with cutfast

    show NHS right at right
    show WWX right at center
    show JC left at left
    with dissolve

    show WWX talk

    WWX "Since we're in Gusu, we have to drink Emperor's Smile!"

    WWX "Its scent is subtle, yet the flavour is rich. Pure, yet smooth. Strong, yet not overwhelming. Ahhh."

    show JC talk

    JC "Just drink if you're gonna drink. You sound like you're talking about a person, sheesh."

    show NHS talk

    NHS "Y'know, Jiang-xiong, I do believe Wei-xiong's described it perfectly! After all, as the poets say, a fine wine is as a beautiful woman."

    show WWX grin

    WWX "Cheers to that!"

    JC "Riiiight, well if that's the case, you two might as well follow the smell of liquor to track down your future partners."

    show WWX talk

    WWX "Well, we can't all have our future partners vetted and gift-wrapped for us by the experts, unlike you."

    show JC angy

    JC "What?"

    show WWX left talk

    WWX "Sooo, how goes the search for Jiang Cheng's future partner, Nie-xiong?"

    if chengyao >= 3 and xicheng >= 3:
        show NHS smile

        NHS "It's going so smoothly, Wei-xiong. Just like this wine!"

        WWX "I can't believe I missed a few of his dates! Nie-xiong, tell your fellow wingman about them!"

        show JC rage

        JC "There were no dates! And no wingman-ing!"

        show NHS talkfan

        NHS "Oh, Jiang-xiong has been chatting up practically everyone in the Cloud Recesses."

        show JC hands

        JC "Just chatting! Not chatting {i}up!{/i}"

        show NHS talk

        NHS "Why, I overheard Xichen-ge and Meng Yao talking about how wonderful they thought Jiang-xiong was."

        if chengqing >= 3:

            NHS "And even Wen-guniang smiled at him when she walked by, just the other day!"
        
    
    elif xicheng >= 3 and chengqing >= 3:
        show NHS smile

        NHS "It's going so smoothly, Wei-xiong. Just like this wine!"

        WWX "I can't believe I missed a few of his dates! Nie-xiong, tell your fellow wingman about them!"

        show JC rage

        JC "There were no dates! And no wingman-ing!"

        show NHS talkfan

        NHS "Oh, Jiang-xiong has been chatting up practically everyone in the Cloud Recesses."

        show JC hands

        JC "Just chatting! Not chatting {i}up!{/i}"

        show NHS talk

        NHS "Why, I overheard Zewu-jun telling Lan-er-gongzi how diligent and responsible he thought Jiang-xiong was."

        NHS "And even Wen-guniang smiled at him when she walked by, just the other day!"
        
    elif chengyao >= 3 and chengqing >= 3:
        show NHS smile

        NHS "It's going so smoothly, Wei-xiong. Just like this wine!"

        WWX "I can't believe I missed a few of his dates! Nie-xiong, tell your fellow wingman about them!"

        show JC rage

        JC "There were no dates! And no wingman-ing!"

        show NHS talkfan

        NHS "Oh, Jiang-xiong has been chatting up practically everyone in the Cloud Recesses."

        show JC hands

        JC "Just chatting! Not chatting {i}up!{/i}"

        show NHS talk

        NHS "Why, Meng Yao was telling me that I should learn from Jiang-xiong's good example, because Jiang-xiong was so polite and sensible."

        NHS "And even Wen-guniang smiled at him when she walked by, just the other day!"
    
    elif sangcheng >= 6 and chengyao <= 2 and chengqing <= 2 and xicheng <= 2:

        jump WBA_end_B

    elif sangcheng >= 6:
        show NHS smile

        NHS "It's going so smoothly, Wei-xiong. Just like this wine!"

        WWX "I can't believe I missed a few of his dates! Nie-xiong, tell your fellow wingman about them!"

        show JC rage

        JC "There were no dates! And no wingman-ing!"

        show NHS talkfan

        NHS "Oh, Jiang-xiong has been chatting up practically everyone in the Cloud Recesses. He's talked to Zewu-jun, and Wen-guniang, and even Meng Yao!"

        show JC hands

        JC "Just chatting! Not chatting {i}up!{/i}"

    else:
        jump WBA_end_B

    show WWX right

    WWX "Wow, I could never have imagined my shidi could be so suave! So charming! So, who do you like best?"

    menu:
        "Wen Qing" if chengqing >= 3:
            
            $ chengqing += 2

            show JC blush

            JC "That's...I guess Wen-guniang is..."

            show WWX talk

            WWX "I guess Wen-guniang does meet some of your requirements, huh? She's a natural beauty for sure."

            show NHS talkfan

            NHS "What requirements? Why wasn't I told about these requirements?"

            show WWX left grin

            WWX "Oho, Nie-xiong, I'll have you know my shidi came up with a stringent list of requirements for a partner back when he was only ten!"

            show JC angy

            JC "Shut up, Wei Wuxian!  We're not talking about that!"

            show WWX talk

            WWX "This person had to be beautiful, and gentle, and kind. Which, I dunno, Wen-guniang has a real unkind glare she's always using on me—"

            show JC rage

            JC "WEI WUXIAN! SHUT UP!"

            WWX "Oh, and they've gotta be thrifty, and good with housework. Which, who knows, maybe Wen-guniang is; she's good at making medicines, does that mean she's good at cooking—ACK—"

            play sound "punch.mp3"

            show JC rage at center
            with move
            with hpunch
            with vpunch

            show WWX:
                ease 0.1 yoffset 1000

            show NHS fan:
                ease 0.5 xoffset 100

            NHS "Jiang-xiong, don't kill him—"
            
        "Lan Xichen" if xicheng >= 3:

            $ xicheng += 2

            show JC blush

            JC "That's...I guess Zewu-jun is..."

            show WWX talk

            WWX "I guess Zewu-jun does meet some of your requirements, huh? He's very good-looking! Not as good-looking as Lan Zhan, of course, but still!"

            show NHS talkfan

            NHS "Wait, what requirements? Why wasn't I told about these requirements?"

            show WWX left grin

            WWX "Oho, Nie-xiong, I'll have you know my shidi came up with a stringent list of requirements for a partner back when he was only ten!"

            show JC angy

            JC "Shut up, Wei Wuxian! We're not talking about that!"

            show WWX talk

            WWX "This person had to be beautiful, and gentle, and kind. Which I suppose Zewu-jun is, that's true—"

            show JC rage

            JC "WEI WUXIAN! SHUT UP!"

            WWX "Oh, and they've gotta be from a reputable family. Which, I suppose the Lan sect has a good reputation, but can you imagine being related to Old Man Lan—ACK—"

            play sound "punch.mp3"

            show JC rage at center
            with move
            with hpunch
            with vpunch

            show WWX:
                ease 0.1 yoffset 1000

            show NHS fan:
                ease 0.5 xoffset 100

            NHS "Jiang-xiong, don't kill him—"

        "Meng Yao" if chengyao >= 3:
            $ chengyao += 2

            show JC blush

            JC "That's...I guess Meng-gongzi is..."

            show WWX talk

            WWX "I guess Meng-gongzi does meet some of your requirements, huh? He's pretty enough—though not as good-looking as Lan Zhan, of course!"

            show NHS talkfan

            NHS "Wait, what requirements? Why wasn't I told about these requirements?"

            show WWX left grin

            WWX "Oho, Nie-xiong, I'll have you know my shidi came up with a stringent list of requirements for a partner back when he was only ten!"

            show JC angy

            JC "Shut up! We're not talking about that!"

            show WWX talk

            WWX "This person had to be beautiful, and gentle, and thrifty. Which, I dunno Meng-gongzi that well, maybe he is?"

            show NHS talk

            NHS "Oh he definitely is. He's in charge of the Qinghe's budget and Da-ge is always complaining about how Meng Yao doesn't let him buy more sabres for the disciples."

            show JC rage

            JC "BOTH OF YOU SHUT UP!"

            WWX "What else is on the list? Oh yes, has to be good with housework, and from a reputable family—"

            show NHS smile

            NHS "Meng Yao belongs to us Qinghe Nie, and we're very reputable!"

            show WWX right

            WWX "Yeah, but he's also related to that snake Jin Guangshan. And the peacock too! Ugh, no, Jiang Cheng, you should reconsider—ACK—"

            play sound "punch.mp3"

            show JC rage at center
            with move
            with hpunch
            with vpunch

            show WWX:
                ease 0.1 yoffset 1000

            show NHS fan:
                ease 0.5 xoffset 100

            NHS "Jiang-xiong, don't kill him—"
            
        "None of them":

            show JC angy

            JC "No one! I don't like any of them! Shut up and drink!"

            if sangcheng >= 6:

                show NHS smile

                NHS "Well that's okay! At least you like us, right?"

                $ sangcheng += 4

                show JC blush

                JC "Ugh, you guys are fine. I guess. At least, you are."

                show JC hands
                
                JC "Wei Wuxian is another matter."

                show WWX talk

                WWX "Aww, Jiang Cheng, don't be like that! After all, who else in the whole world knows you best but your best shixiong?"

                show WWX grin

                WWX "Who else knows about your List Of Requirements For A Partner?"

            else:
                show NHS pout
                
                NHS "No one? But I've been trying so hard...Jiang-xiong, is no one in the Cloud Recesses to your taste?"

                show WWX left grin
            
                WWX "Ah, I should have warned you, Nie-xiong, my shidi has a stringent list of requirements for a partner. In fact, he came up with it when he was only ten!"

            show NHS talkfan

            NHS "Wait, what requirements? Why wasn't I told about these requirements?"

            show JC angy

            JC "Shut up, Wei Wuxian! We're not talking about that!"

            show WWX talk

            WWX "His partner has to be beautiful, and gentle, and kind, and thrifty—"

            show JC rage

            JC "WEI WUXIAN! SHUT UP!"

            WWX "—and not talk too much, and be from a reputable family, and—ACK—"

            play sound "punch.mp3"

            show JC rage at center
            with move
            with hpunch
            with vpunch

            show WWX:
                ease 0.1 yoffset 1000

            show NHS fan:
                ease 0.5 xoffset 100

            NHS "Jiang-xiong, don't kill him—"

    jump WBA_end_C

label WBA_end_B: 

    if chengyao >= 3:
        $ chengyao += 2

        show NHS pout

        NHS "Ah, I've been trying my best to get Jiang-xiong to talk to people, but it seems like the only one he gets along with is Meng Yao."

        show NHS talkfan

        NHS "Meng Yao's pretty good at getting along with everyone, but I do think he's making an extra effort for Jiang-xiong."

        show JC blush

        JC "That's...I guess Meng-gongzi is..."

        show WWX right talk

        WWX "I guess Meng-gongzi does meet some of your requirements, huh? He's pretty enough—though not as good-looking as Lan Zhan, of course!"

        show NHS talkfan

        NHS "Wait, what requirements? Why wasn't I told about these requirements?"

        show WWX left grin

        WWX "Oho, Nie-xiong, I'll have you know my shidi came up with a stringent list of requirements for a partner back when he was only ten!"

        show JC angy

        JC "Shut up! We're not talking about that!"

        show WWX talk

        WWX "This person had to be beautiful, and gentle, and thrifty. Which, I dunno Meng-gongzi that well, maybe he is?"

        show NHS talk

        NHS "Oh he definitely is. He's in charge of the Qinghe's budget and Da-ge is always complaining about how Meng Yao doesn't let him buy more sabres for the disciples."

        show JC rage

        JC "BOTH OF YOU SHUT UP!"

        WWX "What else is on the list? Oh yes, has to be good with housework, and from a reputable family—"

        show NHS smile

        NHS "Meng Yao belongs to us Qinghe Nie, and we're very reputable!"

        show WWX right

        WWX "Yeah, but he's also related to that snake Jin Guangshan. And the peacock too! Ugh, no, Jiang Cheng, you should reconsider—ACK—"

        play sound "punch.mp3"

        show JC rage at center
        with move
        with hpunch
        with vpunch

        show WWX:
            ease 0.1 yoffset 1000

        show NHS fan:
            ease 0.5 xoffset 100

        NHS "Jiang-xiong, don't kill him—"
    
    elif xicheng >= 3:
        $ xicheng += 2

        show NHS pout

        NHS "Ah, I've been trying my best to get Jiang-xiong to talk to people, but it seems like the only one he likes is Zewu-jun."

        show NHS talkfan

        NHS "Which makes sense, I suppose. Everyone likes Zewu-jun."

        show JC blush

        JC "That's...I guess Zewu-jun is..."

        show WWX right talk

        WWX "I guess Zewu-jun does meet some of your requirements, huh? He's very good-looking! Not as good-looking as Lan Zhan, of course, but still!"

        show NHS talkfan

        NHS "Wait, what requirements? Why wasn't I told about these requirements?"

        show WWX left grin

        WWX "Oho, Nie-xiong, I'll have you know my shidi came up with a stringent list of requirements for a partner back when he was only ten!"
        
        show JC angy

        JC "Shut up, Wei Wuxian! We're not talking about that!"

        show WWX talk

        WWX "This person had to be beautiful, and gentle, and kind. Which I suppose Zewu-jun is, that's true—"

        show JC rage

        JC "WEI WUXIAN! SHUT UP!"

        WWX "Oh, and they've gotta be thrifty, and from a reputable family. Which, I suppose the Lan sect has a good reputation, but can you imagine being related to Old Man Lan—ACK—"

        play sound "punch.mp3"

        show JC rage at center
        with move
        with hpunch
        with vpunch

        show WWX:
            ease 0.1 yoffset 1000

        show NHS fan:
            ease 0.5 xoffset 100

        NHS "Jiang-xiong, don't kill him—"

    elif chengqing >= 3:
        $ chengqing += 2

        show NHS pout

        NHS "Ah, I've been trying my best to get Jiang-xiong to talk to people, but it seems like he only has eyes for Wen-guniang."

        show NHS talkfan

        NHS "But at least Wen-guniang also seems to have eyes for him too."

        show JC blush

        JC "That's...I guess Wen-guniang is..."

        show WWX right talk

        WWX "I guess Wen-guniang does meet some of your requirements, huh? She's a natural beauty for sure."

        show NHS talkfan

        NHS "What requirements? Why wasn't I told about these requirements?"

        show WWX left grin

        WWX "Oho, Nie-xiong, I'll have you know my shidi came up with a stringent list of requirements for a partner back when he was only ten!"

        show JC angy

        JC "Shut up, Wei Wuxian!  We're not talking about that!"

        show WWX talk

        WWX "This person had to be beautiful, and gentle, and kind. Which, I dunno, Wen-guniang has a real unkind glare she's always using on me—"

        show JC rage

        JC "WEI WUXIAN! SHUT UP!"

        WWX "Oh, and they've gotta be thrifty, and good with housework. Which, who knows, maybe Wen-guniang is; she's good at making medicines, does that mean she's good at cooking—ACK—"

        play sound "punch.mp3"

        show JC rage at center
        with move
        with hpunch
        with vpunch

        show WWX:
            ease 0.1 yoffset 1000

        show NHS fan:
            ease 0.5 xoffset 100

        NHS "Jiang-xiong, don't kill him—"
    
    elif sangcheng >= 6:
        $ sangcheng += 4

        show NHS talk

        NHS "Ah, I've been trying my best to get Jiang-xiong to talk to people, but he doesn't ever want to talk to anyone but us."

        show NHS smile

        NHS "Well, to me, I suppose! Since you're always stuck in the Library Pavilion with Lan-er-gongzi, Wei-xiong."
        
        show JC hands

        JC "I wouldn't want to talk to him anyway."

        show WWX right talk

        WWX "Aww, Jiang Cheng, don't be like that! After all, who else in the whole world knows you best but your best shixiong?"

        show WWX grin

        WWX "Who else knows about your List Of Requirements For A Partner?"

        show NHS talkfan

        NHS "What requirements? Why wasn't I told about these requirements?"

        show JC angy

        JC "Wei Wuxian—"

        show WWX left talk

        WWX "Nie-xiong, didn't you know that Jiang Cheng came up with a whole list of requirements for a partner when he was the tender age of ten? This person has to be beautiful—"

        show JC hands

        JC "Shut up! We're not talking about that!"

        WWX "—and gentle, and kind, and thrifty—"

        show JC rage

        JC "SHUT UP! DON'T YOU DARE—"

        WWX "—and not talk to much, and be from a reputable family, and—ACK—"

        play sound "punch.mp3"

        show JC rage at center
        with move
        with hpunch
        with vpunch

        show WWX:
            ease 0.1 yoffset 1000

        show NHS fan:
            ease 0.5 xoffset 100

        NHS "Jiang-xiong, don't kill him—"
    
    else:
        show NHS pout

        NHS "Ah, I've been trying my best to get Jiang-xiong to talk to people, but he doesn't ever want to talk to anyone but us."

        show WWX right talk

        WWX "See, Jiang Cheng, I told you you were going to die sad and alone without our help."

        show JC angy

        JC "I'll show YOU dying sad and alone—"

        show WWX grin

        WWX "Ah, I know what the problem is! I forgot about your List of Requirements For A Partner!"

        show NHS talkfan

        NHS "What requirements?"

        JC "Wei Wuxian—"

        show WWX left talk

        WWX "Nie-xiong, didn't you know that Jiang Cheng came up with a whole list of requirements for a partner when he was the tender age of ten? This person has to be beautiful—"

        show JC hands

        JC "Shut up! We're not talking about that!"

        WWX "—and gentle, and kind, and thrifty—"

        show JC rage

        JC "SHUT UP! DON'T YOU DARE—"

        WWX "—and not talk to much, and be from a reputable family, and—ACK—"

        play sound "punch.mp3"

        show JC rage at center
        with move
        with hpunch
        with vpunch

        show WWX:
            ease 0.1 yoffset 1000

        show NHS fan:
            ease 0.5 xoffset 100

        NHS "Jiang-xiong, don't kill him—"
    
    jump WBA_end_C

label WBA_end_C:

    play sound "audio/dooropen.mp3"
    pause(1.0)

    LWJ "What are you doing."

    show LWJ left at left
    with moveinleft

    show NHS right fan:
        ease 0.1 yoffset -100
        ease 0.1 yoffset 0

    show JC right angy:
        ease 0.1 yoffset -100
        ease 0.1 yoffset 0

    NHS "YAH!"

    JC "URK—"

    show WWX right at midright
    show WWX:
        ease 0.5 yoffset 0

    WWX "What—oh, Lan Zhan!"

    show WWX grin

    WWX "Oh, haha! You're here! What perfect timing! Come sit down and have a drink with us!"

    show JC left

    JC "..."

    show NHS fan:
        ease 0.5 xoffset 150

    NHS "..."

    show LWJ angy

    LWJ "..."    

    LWJ "Alcohol is forbidden in the Cloud Recesses."

    LWJ "Report to the Discipline Hall at once."

    show WWX talk

    WWX "Ah, look at them both Lan Zhan, they're so drunk, how can they go anywhere right now?"

    NHS "What...what hall? Urk, oh, I feel sick..."

    show JC right blush

    JC "Oh. Urk. Me too, so sick..."

    NHS "I'm...I think I'm gonna throw up. Outside."
    
    hide NHS with moveoutleft

    JC "Yes, me too."

    hide JC with moveoutleft

    show LWJ right angy

    LWJ "You—"

    scene bg dormnight
    with cutfast
    
    show JC right angy at midright
    show NHS left pout at midleft

    JC "Argh, I can't believe that Lan Wangji! Why the hell did he suddenly show up!"

    NHS "*Huff* Did he *huff* follow us?"

    show JC left
    pause(0.5)
    show JC right

    JC "Doesn't look like it."

    show JC talk

    JC "Huh, wonder why he didn't."

    show NHS talkfan

    NHS "I don't know, maybe Wei-xiong convinced him not to."

    JC "...Yeah, I can't imagine how."
    
    JC "I have a feeling that idiot is somehow getting into more trouble now, not less. Maybe we should go back to check..."

    show NHS pout

    NHS "What, no! How could Wei-xiong possibly get into more trouble, anyway? Look, why don't we hide out in my rooms, and ask him about it tomorrow?"

    jump CSC_1

label CSC_1:
    scene bg indoors
    with timepass2

    stop music fadeout 1.0
    play music "audio/CSC_1.mp3" fadein 1.0

    scene bg indoors
    with timepass2

    stop music fadeout 1.0
    play music "audio/CSC_1.mp3" fadein 1.0

    let "{vspace=260}It is, of course, entirely possible for Wei Wuxian to get into more trouble, and so the next day finds these four young masters hauled up for punishment. Thankfully, they have the day after the punishment set aside for rest and reflection."

    scene bg indoors
    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} Five days to Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)

    show NHS left pout at center
    
    NHS "...Ow, this sucks, ow, this sucks, ow..."

    play sound "audio/dooropen.mp3"
    pause(1.0)

    show JC left rage at left
    with moveinleft 

    JC "WEI WUXIAN!!"

    show NHS right pout:
        ease 0.1 yoffset -100
        ease 0.1 yoffset 0

    NHS "YAH! Jiang-xiong, what—"

    show JC angy

    JC "He's not here?"
    
    NHS "No, why would he be here in my rooms? After he got three hundred strokes yesterday, shouldn't he still be lying in bed?"

    NHS "We only got fifty strokes, and now I can barely turn over..."
    
    JC "You haven't seen him at all today? Or yesterday, after our punishment?"

    NHS "No, why would I have? Wait, what's happening?"

    show JC hands

    JC "He's gone missing, is what! He didn't come back to our rooms last night, and he wasn't with A-jie, or any of the other Jiang disciples, and when I went to check the cold springs no one's there either, and A-jie started to get worried since he didn't leave a note so I thought I'd come here to ask—"

    NHS "Whoa, whoa, slow down. Did you say he's missing?"

    show JC rage

    JC "Yes! And he better show up before I find him for myself and {i}break his legs!{/i}"

    show JC right angy

    JC "Anyway, I gotta go, if he's not here then—"

    show NHS fan

    NHS "Wait wait wait! So the last time you saw him, he was going to...the cold springs?"

    show JC left hands

    JC "Yes, Zewu-jun said there are cold springs in the back hills that's good for healing, and Lan Wangji was probably already there, so Wei Wuxian said he'd go too, and no one's seen him after that—"
    
    show NHS talkfan

    NHS "Does that mean the last one to see him might have been Lan Wangji? Have you spoken to him?"

    JC "No, I...Right, yeah, I should go ask him."

    show NHS talk

    NHS "I know where his rooms are, let's go."

    hide NHS
    hide JC
    with moveoutleft

    scene bg library
    with cutfast

    if xiyao >= 1:

        show LXC left at midleft
        show MY left at left
        show JC right at midright
        show NHS right at right

        JC "...and no one answered the door, which is why we came to check the Library Pavilion, Zewu-jun."

        show NHS talk

        NHS "And ran into you and Meng Yao! And I thought maybe we should tell you about it."

        show LXC talk

        LXC "Yes, thank you both. It is indeed unusual for Wangji not to be in his rooms, at the lecture hall, or here in the library."

        show MY talk

        MY "But for him and Wei-gongzi to both be missing..."

        MY "Lan-er-gongzi might not have answered his door, but is there a chance he might nevertheless be inside? Or might he have left a note?"

        show LXC right smile

        LXC "Yes, good thought, Meng-gongzi. Perhaps we have no cause for alarm."

        show LXC left

        LXC "Please wait here, all of you. I will check Wangji's rooms again."

        show LXC right
        hide LXC with moveoutleft

        scene bg library
        with cutfast
        
        show JC right at center
        show MY right at midright
        show NHS right at right
        with None

        show LXC left frown at midleft
        with moveinleft

        LXC "Wangji was not in his rooms, nor did he leave a note. I have informed Shufu, and he has begun to organise the search party."

        show JC hands

        JC "So what do we do now?"

    else:

        show LXC left at midleft
        show JC right at midright
        show NHS right at right

        JC "...and no one answered the door, which is why we came to check the Library Pavilion, Zewu-jun."

        show LXC talk

        LXC "Yes, I see. It is indeed unusual for Wangji not to be in his rooms, at the lecture hall, or here in the library."

        LXC "Please wait here, Nie-gongzi, Jiang-gongzi. I will check Wangji's rooms again. Perhaps he's left a note, and there is no cause for alarm."

        show LXC right
        hide LXC with moveoutleft

        scene bg library
        with cutfast
        
        show NHS right at right
        show JC right at midright
        with None

        show MY left at midleft
        show LXC left frown at center
        with moveinleft

        LXC "Wangji was not in his rooms, nor did he leave a note. I have informed Shufu, and he has begun to organise the search party."

        LXC "I met Meng-gongzi coming to the library, and he has also offered his help."

        MY "Zewu-jun has appraised me of the situation. It sounds troubling."

        show JC hands

        JC "So what do we do now?"
    
    show MY talk
    
    MY "I suggest that we—"

    show WQ left at left
    with moveinleft

    WQ "Zewu-jun, I'm glad I've found you."

    show LXC right
    show MY right
    show JC right
    show NHS right

    WQ "Jiang-gongzi, Nie-gongzi, Meng-gongzi."

    LXC "Wen-guniang, is there something I can assist you with?"

    show WQ talk

    WQ "No, I was hoping {i}I{/i} could assist {i}you.{/i}"

    WQ "I hear lectures today are cancelled because Wei-gongzi and Lan-er-gongzi have gone missing, is that true?"

    show LXC frown

    LXC "Unfortunately, that is so."

    show WQ -talk

    WQ "I see. I...I thought I should mention that yesterday evening, as I was taking some fresh air in the back hills, I noticed a pair of shoes left unattended next to a small spring."

    WQ "I wondered why the owner had wandered off, and didn't think much of it otherwise. But now..."

    show MY talk

    MY "Hm, Wen-guniang, do you happen to remember where the spring is? We should check if the shoes are still there."

    show NHS talkfan

    NHS "It might be the cold springs that Jiang-xiong said they both went to yesterday!"

    show LXC talk

    LXC "Those springs are nearly impossible to find without directions. I'd be surprised if Wen-guniang stumbled upon them."

    show WQ blush

    WQ "Well, that's..."

    MY "Or perhaps it's a different spring, and the shoes belong to someone else? Regardless, I'm sure we must thank Wen-guniang for informing us of this."

    show LXC frown

    LXC "Indeed. Let us go at once to clarify this situation. If Wen-guniang will lead the way?"

    hide LXC
    hide MY
    hide NHS
    hide JC
    hide WQ
    with moveoutleft

    jump CSC_2

label CSC_2:

    scene bg springs
    with cutfast

    show NHS left at left
    show LXC left at midleft
    show MY right at right
    show WQ right at midright
    show JC right at center

    show LXC frown

    LXC "So it {i}was{/i} these cold springs that Wen-guniang...stumbled...across."

    show JC hands

    JC "And those are definitely Wei Wuxian's shoes."

    show NHS talk

    NHS "Maybe he wandered off to take a nap nearby? He can't have gone far barefoot, right?"

    show JC angy

    JC "A nap??? If he's really made us all run around like headless chickens because he's fucking {i}napping{/i}, I—"

    show LXC frown

    LXC "That would not explain where Wangji has gone. I find it doubtful that he is also napping."
    
    show MY talk

    MY "Nie-er-gongzi has a point, however. It is likely that they—or at least Wei-gongzi—is nearby. He would not have planned to go far without shoes."

    MY "Perhaps we should split up to check the surrounding area."

    show MY -talk

    MY "I haven't been in the back hills before and don't know this area well, so perhaps I'll search along the path from here to the Cloud Recesses."

    if chengyao >= 5:      
        MY "Perhaps Jiang-gongzi could join me?"
    
    show WQ talk

    WQ "Ah, I don't know the back hills very well either. Maybe I could—"

    LXC "I'd prefer if Wen-guniang didn't stray too far from this area. And it would be best if you were partnered up with someone else."

    if chengqing >= 5:
        show WQ -talk

        WQ "...Of course. Ah, Jiang-gongzi, would you accompany me then?"
    
    else:
        show WQ hmm

        WQ "...Of course."
    
    show NHS talkfan

    NHS "What about the area downstream of here? Or deeper into the back hills?"

    if sangcheng >= 10:
        NHS "Jiang-xiong and I could search one of those places together, maybe?"

    show LXC talk
    
    LXC "Hmm, I do believe I know the area deeper into the back hills best, so I should be the one to search there."

    if xicheng >= 5:
        LXC "I'd appreciate it if Jiang-gongzi could accompany me."

    show JC talk

    JC "In that case, I'll..."
    
    menu:
        "Join Meng Yao" if chengyao >= 5:
            JC "Okay, I'll search along the path to Cloud Recesses with Meng-gongzi."

            $ chengyao += 3

            jump CSC_MY
        
        "Join Wen Qing" if chengqing >= 5:
            JC "Okay, I'll search this area with Wen-guniang."

            $ chengqing += 3

            jump CSC_WQ
        
        "Join Nie Huaisang" if sangcheng >= 10:
            JC "Okay, I'll search the area downstream with Nie-gongzi."

            $ sangcheng += 4

            jump CSC_NHS
        
        "Join Lan Xichen" if xicheng >= 5:
            JC "Okay, I'll search the deeper part of the back hills with Zewu-jun."

            $ xicheng += 3

            jump CSC_LXC

        "Head back to the Cloud Recesses":
            pass
    
    JC "Maybe I should go back to the Cloud Recesses and see if Lan-xiansheng's search party has found anything."

    jump CSC_JC

label CSC_MY:

    show MY smile

    MY "Thank you, Jiang-gongzi."

    show LXC talk

    LXC "In that case, perhaps Nie-gongzi could stay with Wen-guniang to search this area. And I will go deeper into the back hills to see if there's any trace of them."

    LXC "Let us meet back here in a shichen, and hopefully one of us will have good news to share."

    hide MY
    hide JC
    with moveoutleft

    hide LXC
    hide NHS
    hide WQ
    with moveoutright

    scene bg hillnight
    with cutfast

    stop music fadeout 1.0
    play music "audio/search.mp3" fadein 1.0

    "The path from the cold springs to the Cloud Recesses is long and winding, passing many a peaceful grove of trees that one could enter to enjoy the quiet. After all, for those who seek the cold springs for healing, a solitary, meditative walk could be just as restorative as cool waters..."

    show JC angy right at midleft
    show MY right at midright
    with dissolve

    JC "This endless fucking path is driving me up a fucking wall!"

    show JC rage

    JC "Wei Wuxian! Show your fucking face before I punch a fucking tree! Wei Wuxian!!"

    show MY talk

    MY "If he {i}was{/i} napping, he certainly couldn't be now."

    show JC left angy

    JC "Do you really think Wei Wuxian's around here somewhere? Without his fucking shoes, the fucking idiot..."

    show MY smile

    MY "I do. I find it unlikely he would have left the back hills without his footwear, and if either of them had gone back to the Cloud Recesses, they would already have been found."

    show JC hands

    JC "Could they be...You don't think they had an accident or something, do you?"

    show MY talk

    MY "It's possible. But the back hills aren't dangerous, so if they've had an accident it's likely a minor one. And Lan-er-gongzi was raised here and surely knows these hills well. They're both strong and resourceful; if they're together, they surely can't be in too much trouble."

    show JC talk

    JC "Right. Yeah. You're right. You're right, they're probably fine."

    show MY smile

    MY "Most likely Wei-gongzi involved Lan-er-gongzi in a bit of...mischief, let's say, and they lost track of time."

    JC "Ugh, yeah, you're right. That's probably it. That idiot."

    show JC blush

    JC "Thanks."

    show MY smile

    MY "Not at all."
    
    MY "Feel free to keep shouting though, Jiang-gongzi. In case they {i}are{/i} caught up in something and need to be interrupted." 

    show JC smile

    JC "Hah, yeah, I will."

    show JC right angy

    JC "WEI WUXIAN! I'M FUCKING COMING FOR YOU! A-JIE IS WORRIED ABOUT YOU, ASSHOLE!"

    show MY talk

    MY "You and Jiang-guniang must be very close to Wei-gongzi, to be so worried about him."

    show JC left talk

    JC "Yeah. I mean, we're family. Unfortunately."

    show MY -talk

    MY "Ah, I thought...That is, my understanding is that Wei-gongzi is unrelated to you and Jiang-guniang...?"

    JC "What? Oh, no, he's not related by blood. But we all grew up together, more or less."

    show MY smile

    MY "I see. How fortunate for him, to be able to count someone as stalwart and capable as yourself as family, even without blood ties."

    show JC blush

    JC "Oh, uh, I—"

    show JC talk

    JC "I, I mean, blood isn't everything, right? Like you're technically related to—"

    show JC blush

    JC "Shit. Sorry, I didn't mean—um."

    show MY -smile

    MY "No, no need for apologies. I {i}am{/i} technically related to Jin-zongzhu, as everyone knows."

    show JC hands

    JC "Right, well, who cares about him. I mean, you're clearly better than the peacock—than Jin Zixuan—in every way, and if he can't see that, that's his loss."

    show MY blush

    MY "Ah. That..."

    MY "Thank you, Jiang-gongzi, I...I appreciate you saying so."

    show MY smile

    MY "Now, let's get back to our search, shall we?"

    show JC blush

    JC "Right, yes, of course."

    show JC right rage

    JC "WEI WUXIAN YOU LITTLE SHIT, SHOW YOURSELF!"

    jump CSC_end

label CSC_WQ:

    show WQ smile

    WQ "Thank you, Jiang-gongzi."

    show LXC talk

    LXC "In that case, perhaps Meng-gongzi and I will search the rest of the back hills."

    show MY smile

    MY "Of course, Zewu-jun."
    
    LXC "And Nie-gongzi could go back to the Cloud Recesses for now. Maybe Shufu's search party has found something."

    show NHS talk

    NHS "Sure, Zewu-jun, I'll go back to check!"

    LXC "Alright then. Let us meet back here in a shichen, and hopefully one of us will have good news to share."

    $ xiyao += 1

    hide WQ
    hide JC
    with moveoutleft

    hide LXC
    hide NHS
    hide MY
    with moveoutright

    scene bg hillnight
    with cutfast

    stop music fadeout 1.0
    play music "audio/search.mp3" fadein 1.0

    "The cold springs are serene and restful, with many a quiet, shaded corner tucked away around it where a person could let the soft melody of burbling water and rustling leaves lull them into gentle slumber..."

    show JC angy right at midleft
    show WQ right at midright
    with dissolve

    JC "Wei Wuxian! If you're asleep, you better wake the fuck up right now!!"

    show WQ talk

    WQ "If he {i}was{/i} napping, he certainly couldn't be now."

    show JC left hands

    JC "Do you really think Wei Wuxian's around here somewhere?"

    WQ "I can't imagine where he would go without his shoes."
    
    WQ "Then again, Jiang-guniang was just telling me a story about him running around Lotus Pier barefoot and with no pants on, so..."

    show JC smile

    JC "Hah, A-jie says she's never going to stop telling that story. She'll tell it to her children. Her grandchildren."

    show WQ smile

    WQ "Of course she is, it's the prerogative of older siblings. I have several stories like that about A-Ning myself."

    show JC talk

    JC "Do you? Like what?"

    show WQ talk

    WQ "Well now, there was the time he spat up on the back of Wen Chao's robes, and Wen Chao didn't notice for an entire day."

    show JC smile

    JC "Hah, serves that asshole right, bet he was swaggering around with—"

    show JC blush
    
    JC "Not that he's...I mean, he {i}is{/i} an asshole, but he's your cousin, and I...I just mean that..."
    
    JC "Hey, so, did you know Wei Wuxian threw up on three sect leaders once? Did A-jie tell you about that?"

    show WQ -talk

    WQ "She did, yes. Quite a remarkable storyteller, your sister."

    show JC smile

    JC "Yeah, she's great. She used to tell us so many stories when we were younger, especially when she wasn't feeling well and had to stay in bed..."

    show JC blush

    JC "Thank you for looking out for her, by the way. She says you've been making her medicine and checking up on her health."

    show WQ smile

    WQ "No thanks necessary. It's my duty as a physician."

    JC "I suppose. Well, it wasn't your duty to let us know that you found Wei Wuxian's shoes out here, but I'm...I'm very grateful you did so anyway. Thank you, Wen-guniang."

    show WQ blush

    WQ "Ah. No thanks necessary for that too, it's my duty as...as a sibling."

    show JC talk

    JC "Wen-guniang seems like someone who takes her duties very seriously."

    JC "And look, I don't know why your asshole cousin wanted you here in the Cloud Recesses in the first place—Wei Wuxian thinks you're up to something in the back hills—but if there's something I can help with, I..."

    show JC blush

    JC "I mean, I can't promise I'll help, but I'll—"

    show WQ right

    WQ "Don't."

    show JC talk

    JC "What?"

    WQ "Don't promise to help. Not with that."

    show WQ left hmm
    
    WQ "I won't tell you more, and my duty is to my sect, of course, but I..."

    show JC -talk

    JC "Can't turn your back on your sect even if they're assholes, right? Yeah, I get it. You just have to do your best to honour your family name anyway."

    show WQ right

    WQ "...To honour my family name? Hm. Yes, I ought try my best to do that, shouldn't I. Jiang-gongzi is quite right."

    show JC blush

    JC "Um, yes? Yes."

    show JC smile
    
    JC "Anyway, I won't ask about that, but if you did need help with something else, for yourself—or for your brother—then I'll try my best."

    show WQ smile

    WQ "I see. In that case, thank you, Jiang-gongzi."

    WQ "Now, let's get back to our search, shall we?"

    JC "Right, yes, of course."

    show JC right angy

    JC "WEI WUXIAN YOU LITTLE SHIT, SHOW YOURSELF!"

    jump CSC_end

label CSC_NHS:

    show NHS smile

    NHS "Great! We'll search so hard together!"

    show LXC talk

    LXC "In that case, perhaps Jiang-gongzi and Nie-gongzi could also search this area. And Meng-gongzi and I will search the rest of the back hills, while Wen-guniang goes back to the Cloud Recesses. Maybe Shufu's search party has found something."

    show WQ hmm
    $ xiyao += 1

    WQ "Ah. Very well, I can go back to check."

    LXC "Alright then. Let us meet back here in a shichen, and hopefully one of us will have good news to share."

    hide NHS
    hide JC
    with moveoutleft

    hide LXC
    hide WQ
    hide MY
    with moveoutright

    $ xiyao += 1

    scene bg hillnight
    with cutfast

    stop music fadeout 1.0
    play music "audio/search.mp3" fadein 1.0
    
    "The cold springs flow downstream in a gently burbling ribbon, winding past many a peaceful grove of trees that one could enter to enjoy the quiet. After all, for those who seek healing, a solitary, meditative walk after could be just as restorative as cool waters..."

    show JC angy right at midleft
    show NHS right at midright
    with dissolve

    JC "This endless fucking path is driving me up a fucking wall!"

    show JC rage

    JC "Wei Wuxian! Show your fucking face before I punch a fucking tree! Wei Wuxian!!"

    show NHS talkfan

    NHS "No way he can nap through all this, that's for sure."

    show JC left hands

    JC "Do you really think Wei Wuxian's around here somewhere? Napping or whatever?"

    NHS "I don't know, but Wei-xiong wouldn't have left without his shoes, right? No way he'd have gone off to Caiyi or something without his shoes."

    show JC angy

    JC "Yeah, true..."

    show JC hands
    
    JC "Could he have...You don't think they might have had an accident? Or gotten lost?"

    show NHS -talkfan

    NHS "But why wouldn't they have sent word back? You know Wei-xiong has talismans for that, and I bet Lan-er-gongzi has too. Besides, I bet Lan-er-gongzi knows these hills as well as he knows the library, no way he'd get lost."

    show JC talk

    JC "Right. Yeah. You're right. You're right, they're probably fine."

    show NHS fan

    NHS "Maybe Wei-xiong showed Lan-er-gongzi another one of my yellow books and they both got, y'know. Distracted."

    show JC angy

    JC "What do you me—NO."

    NHS "When Wei-xiong bought more copies from me, he said he was really excited to show it to Lan-er-gongzi again, and I thought—"

    show JC rage

    JC "No no no! Don't think!"
    
    show JC right rage

    JC "Damn it! Wei Wuxian!!"

    show NHS talkfan

    NHS "See, I bet there's nothing to be worried about, really."

    show JC left angy

    JC "Nothing except whether I'm going to BREAK BOTH HIS FUCKING LEGS when we eventually find him."

    show NHS talk

    NHS "Ah, what a shame, I thought it would be nice to travel with you guys for a bit after the lectures are over. But if Wei-xiong's legs are broken, we'll just have to leave him behind."

    show JC hands

    JC "Damn right. We'll leave his ass in Gusu and travel together without him."

    show JC talk

    JC "...actually, that does sound kinda nice."

    show NHS smile

    NHS "I think so too! I'm really glad you came to the lectures this year, Jiang-xiong."

    show JC blush

    JC "Yeah, I. Yeah, me too."

    show JC smile

    JC "It's been...I was expecting it to be boring and stressful, but honestly it's been pretty fun."

    show NHS -smile

    NHS "You can always count on me if you're looking to have fun!"

    JC "And you don't get into half as much trouble as Wei Wuxian either."

    show NHS talkfan

    NHS "Hehe, I'm much better at not getting caught. Especially when I have your serious face to distract people with!"

    JC "Ugh, don't I know it."

    show NHS smile

    NHS "We make a good team!"

    show NHS talk

    NHS "And with our excellent teamwork, I bet we'll find Wei-xiong and Lan-er-gongzi in no time at all!"

    JC "Damn right, we will."

    show JC right angy

    JC "WEI WUXIAN YOU LITTLE SHIT, SHOW YOURSELF!"

    jump CSC_end

label CSC_LXC:

    show LXC smile

    LXC "Thank you, Jiang-gongzi."

    show LXC -smile

    LXC "In that case, perhaps Nie-gongzi and Meng-gongzi could search this area as well as the path towards the Cloud Recesses. And Jiang-gongzi and I will search the rest of the back hills."

    LXC "And Wen-guniang could go back to the Cloud Recesses for now. Maybe Shufu's search party has found something."

    show WQ hmm

    WQ "Ah. Very well, I can go back to check."

    LXC "Alright then. Let us meet back here in a shichen, and hopefully one of us will have good news to share."

    hide LXC
    hide JC
    with moveoutleft

    hide MY
    hide NHS
    hide WQ
    with moveoutright

    scene bg hillnight
    with cutfast

    stop music fadeout 1.0
    play music "audio/search.mp3" fadein 1.0

    "The path leading deeper into the back hills is long and winding, passing many a peaceful grove of trees that one could enter to enjoy the quiet. After all, for those who seek the cold springs for healing, a solitary, meditative walk could be just as restorative as cool waters..."

    show JC angy right at midleft
    show LXC right at midright
    with dissolve

    JC "This endless fucking path is driving me up a fucking wall!"

    show JC rage

    JC "Wei Wuxian! Show your fucking face before I punch a fucking tree! Wei Wuxian!!"

    LXC "Perhaps you {i}should{/i} punch a tree or two, if it'll help you feel better."

    show JC left blush

    JC "What? Oh, uh, sorry, Zewu-jun, I wouldn't actually—"

    LXC "Please don't apologise, Jiang-gongzi. I meant that sincerely."

    LXC "If you're worried about Wei-gongzi, and punching a tree would make you feel better, why not?"

    show JC talk

    JC "You think I should...actually punch a tree...?"

    show LXC talk

    LXC "Your cultivation is strong enough to keep you from getting hurt, and if you should fell one, another would grow in its place, would it not?"

    show JC blush

    JC "Er. I guess so. Well, if you say so—"

    play sound "audio/punch.mp3"
    show JC right rage at left
    with move
    with hpunch
    with vpunch

    JC "—HYAH!"

    show JC left talk

    JC "Huh, guess I do feel better."

    show JC left at midleft
    with move

    show LXC smile

    LXC "I'm glad."
    
    show JC smile

    JC "Maybe you should punch your own tree, Zewu-jun. Might help you feel better too."

    show LXC talk

    LXC "Ah. I'm feeling fine, thank you."

    show JC talk

    JC "Really? I mean, you've got to be at least as worried about them as I am."

    show LXC frown

    LXC "I..."

    LXC "..."

    show JC blush

    JC "Er, was that not—sorry, if that's—"

    show LXC -frown

    LXC "No, you're entirely correct, Jiang-gongzi."

    show LXC talk

    LXC "I {i}am{/i} worried about Wangji."

    LXC "I'm always worried about Wangji, even though he's no longer a child. Even though he insists he doesn't need anyone worrying about him. I still worry."

    show JC talk

    JC "Yeah, it's the curse of having a brother."

    show LXC smile

    LXC "Yes. Yes, quite."

    show LXC -smile

    LXC "Do you know, Jiang-gongzi, you rather remind me of Mingjue."

    JC "What? Chifeng-zun?"

    LXC "Yes. He's said something similar about Huaisang before."

    show JC smile

    JC "Hah!"

    show LXC smile

    LXC "And you're both very capable, responsible, straight-forward people. You're a credit to your sect, Jiang-gongzi."

    show JC blush

    JC "Oh, uh, I..."

    show LXC -smile

    LXC "Though perhaps more tolerant of the foibles of your brother than Mingjue is of his."

    show JC angy

    JC "Ugh, no one could tolerate Wei Wuxian. Maybe Lan-er-gongzi threw him off a cliff."    

    show LXC talk

    LXC "Oh? That would be a surprise, considering how much Wangji has warmed up to Wei-gongzi."

    show JC hands

    JC "{i}Warmed up?{/i} Lan Wang—I mean, you think your brother has warmed up to Wei Wuxian???"

    show LXC -talk

    LXC "Mn. There's not many people who can keep Wangji's attention the way Wei-gongzi has."

    show JC smile

    JC "Hah, if there's one thing Wei Wuxian is good at, it's making people pay attention to him whether they want to or not."

    show JC talk

    JC "I guess he {i}has{/i} been spending a lot of time with Lan-er-gongzi lately, because of all his punishments. And he hasn't been complaining nearly as much as I thought he would about it."

    show LXC smile

    LXC "Well, then. Perhaps the both of them aren't so much missing, as not yet ready to be found."

    show JC angy

    JC "Well too damn bad, if they didn't want people looking, they should have left a note!"

    show JC right rage

    JC "WEI WUXIAN, I'M COMING FOR YOU, JUST YOU WAIT!"

    jump CSC_end

label CSC_JC:
    LXC "In that case, perhaps Nie-gongzi could stay with Wen-guniang to search this area for now. Meng-gongzi, please follow me."

    $ xiyao += 1

    LXC "Jiang-gongzi, please hurry back and inform us if Shufu has any news."

    JC "I will, Zewu-jun."

    hide JC
    with moveoutleft

    hide LXC
    hide MY
    hide NHS
    hide WQ
    with moveoutright

    jump CSC_end

label CSC_end:
    scene bg gatesDESAT
    with cutfast

    centered "While these cultivators search the back hills, the Cloud Recesses itself is in a state of restrained not-quite-uproar. Many white-robed cultivators walk with haste—though not so hastily that it could be called running—through its hallways and rooms, searching for the two missing young men. \n {p}Thankfully, they show up just before the shichen is up, tumbling out from a hidden place in the back hills onto the grass, with wet robes and bright eyes and a dark secret entrusted to their care. \n {p}They do not speak of that secret, or explain their mysterious disappearance, to any of their fellow students. Fortunately, their peers quickly become preoccupied with more important matters: their examinations begin the very next day."
    
    centered "And even after the examinations are over, this mystery is the last thing on anyone's minds. Because finally, the lectures are over.\n {p}It is the Qixi lantern lighting festival, the last day of the Gusu Lectures; a celebration of months of hard work that have finally come to a close."

    jump LT

label LT:
    scene bg lantern1
    with cutslow

    stop music fadeout 1.0
    play music "audio/lantern1.mp3" fadein 1.0

    show bar
    show text "{size=+10}{font=PrincessSofia.ttf}{color=#610000} The evening of Qixi{/color}{/font}" at truecenter
    with Dissolve(0.5)
    pause(2.0)
    hide text
    hide bar
    with Dissolve(0.5)

    show NHS right at right
    show WWX right at midright
    show JC left at midleft
    with dissolve

    show WWX talk

    WWX "YAAAAH I can't believe we're finally done with these boring lectures and even more boring tests!"

    show JC angy

    JC "As if you didn't get thrown out of half of those lectures."

    show NHS smile

    NHS "I can't believe I passed! Finally!"

    show WWX left grin

    WWX "Hah, told you you had nothing to worry about."

    show NHS pout

    NHS "Tell that to my Da-ge."

    if mingcheng >= 4:

        show WWX left talk

        WWX "Speaking of your Da-ge, doesn't that look like him over there?"

        show NHS left talkfan

        NHS "Hah, why would Da-ge even be—"

        show NHS fan
        
        NHS "Wait! That's him! Why is he—"

        show NHS fan:
            ease 0.1 yoffset -100
            ease 0.1 yoffset 0

        NHS "He's looking this way!"

        hide NHS with moveoutbottom

        show NHS bush at center
        with moveinbottom

        NHS "{size=-9}I was never here, I am one with the bushes, I do not exist..."

        show NMJ right pissed at right
        with moveinright

        show WWX at midleft
        show JC at left
        with move

        NMJ "...I swear I saw Huaisang around here—"

        show WWX left:
            ease 0.3 yoffset 100
            ease 0.3 yoffset 0

        show JC left talk:
            ease 0.3 yoffset 100
            ease 0.3 yoffset 0

        WWX "Wei Wuxian of Yunmeng Jiang greets Chifeng-zun." ## maybe do this in unison with JC?

        JC "Jiang Wanyin of Yunmeng Jiang greets Chifeng-zun."

        show NMJ talk

        NMJ "Yes, greetings, Jiang-gongzi, Wei-gongzi. Just the man I wanted to meet."

        show WWX grin

        WWX "Me, really?"

        show WWX wat

        NMJ "No. I meant Jiang-gongzi. Let's talk, Jiang-gongzi, walk with me."

        menu:
            "Yes, sir":

                JC "Of course, Chifeng-zun."

                NMJ "Good. Come." ## there is a funny sex joke to be made by WWX after this i think??

                show NMJ left
                hide NMJ with moveoutright
                hide JC with moveoutright

            "...May I respectfully decline, sir":

                show JC blush

                JC "Of course, Chifeng-zun. Only, the lantern lighting—"

                NMJ "Don't worry about that, I won't take long. Come."

                show NMJ left
                hide NMJ with moveoutright
                hide JC with moveoutright
        
        ## edit scene/music

        scene bg gusu
        with cutfast

        stop music fadeout 1.0
        play music "audio/lantern1.mp3" fadein 1.0

        show NMJ left talk at midleft
        show JC right at midright
        with dissolve

        NMJ "Jiang-gongzi, I'll be frank, I was surprised to receive a letter from you."

        NMJ "Tell me, did Huaisang put you up to it?"

        menu:
            "Yes":

                show JC blush

                JC "He...did ask me to."

                show JC angy

                JC "But I was the one who decided what to write! He didn't write it for me!"

                show NMJ smile

                NMJ "I didn't think so. Huaisang writes better."

                NMJ "But I liked your letter anyway. Appreciated the honesty."

                NMJ "And the brevity."

                show JC blush

                JC "You liked my letter?? But no one ever—I mean, thank you, Chifeng-zun."

                show NMJ talk

                NMJ "Speaking of honesty, and brevity, let me get right to the point."

                NMJ "What do you think of Huaisang?"

                show JC angy

                JC "...What do I think of Nie Huaisang??"

                menu:
                    "He's a good friend" if sangcheng >= 10: ## fix all these points!

                        $ mingcheng += 1

                        JC "He's fine!"

                        NMJ "Fine?"

                        show JC hands

                        JC "Not like—"
                        
                        JC "I mean he's okay! Good! A...a good friend, good company."
                        
                        show JC angy

                        JC "Would be better company if he didn't keep making me keep {i}other people{/i} company—"

                        show NMJ smile

                        NMJ "Hah! Well, that's something. I was told he passed his exams this year somehow, it must have been Jiang-gongzi's good influence."

                        show NMJ pissed

                        NMJ "Not that he hasn't given Xichen and Meng Yao more than enough trouble, or so I've been told."
            
                    "He's fun":

                        JC "He's fine!"

                        NMJ "Fine?"

                        show JC hands

                        JC "Not like—"
                        
                        JC "I mean he's okay! Fun! He drags us down to Caiyi to shop sometimes, or to the back hills to fish, or—"

                        show NMJ pissed

                        NMJ "That layabout, I already warned him that I'd send him back again next year if—"

                        show JC blush:
                            ease 0.1 yoffset -100
                            ease 0.1 yoffset 0

                        JC "But he passed the exams! Which is a very important thing I think about Nie Huaisang too!"

                        NMJ "Did he now. Then perhaps I won't have to inflict him on Xichen and Wangji again next year."

                    "He's bad at studying":

                        JC "He's fine!"

                        NMJ "Fine?"

                        show JC hands

                        JC "Not like—"
                        
                        JC "I mean he's okay! I mean, he's bad at studying, and training with the sword, but he's pretty good at fishing and—"

                        show NMJ pissed

                        NMJ "That layabout, I already warned him that I'd send him back again next year if—"

                        show JC blush:
                            ease 0.1 yoffset -100
                            ease 0.1 yoffset 0

                        JC "But he passed the exams! Which is a very important thing I think about Nie Huaisang too!"

                        NMJ "Did he now. Then perhaps I won't have to inflict him on Xichen and Wangji again next year."

                    "He keeps making me talk to people":

                        $ mingcheng += 1

                        JC "He's fine!"

                        NMJ "Fine?"

                        show JC hands

                        JC "Not like—"
                        
                        JC "I mean he's okay! Likes to talk to people too much, likes to make {i}me{/i} talk to other people too damn much, but he's okay! An okay person!"

                        show NMJ smile

                        NMJ "Hah, sounds like Huaisang alright. I was told he passed his exams this year somehow, it must have been Jiang-gongzi's good influence."

                        show NMJ pissed

                        NMJ "Not that he hasn't given Xichen and Meng Yao more than enough trouble, or so I've been told."

                NMJ "I should go find him now, see what he has to say for himself."

            "No":

                show JC blush

                JC "No, he, uh. I heard him talk so much about you that I...couldn't stop myself from writing to you."

                $ mingcheng -= 1

                show NMJ pissed

                NMJ "Next time, stop."

                NMJ "Forget it. I'll find him and shake some answers out of him myself."

            "Maybe?":

                show JC blush

                JC "Er, maybe. I...can't remember, I don't know."

                $ mingcheng -= 1

                show NMJ pissed

                NMJ "Now you even sound like him."
        
                NMJ "Forget it. I'll find him and shake some answers out of him myself."
            
        menu:
            "Suggest he look for Lan Xichen":

                $ NMJ_gusu = "3zun"

                show JC talk

                JC "Maybe Chifeng-zun could ask Zewu-jun about Nie Huaisang too...?"

                show NMJ talk

                NMJ "Yes, good point, I'm sure Xichen will have something more to say about how Huaisang has been doing."

                if xiyao >= 2: ## fix points

                    NMJ "Instead of just talking about how great Meng Yao is all the damn time...like I don't already know how great Meng Yao is, tch."

                JC "He—"

                show NMJ talk

                NMJ "Right, good talk, Jiang-gongzi."

                show NMJ right
                hide NMJ with moveoutleft
            
            "Suggest he look for Meng Yao":

                $ NMJ_gusu = "3zun"

                show JC talk

                JC "Maybe Chifeng-zun could ask Meng-gongzi about Nie Huaisang too...?"

                show NMJ talk

                NMJ "Yes, good point, I'm sure Meng Yao will have something more to say about how Huaisang has been doing."

                if xiyao >= 2: ## fix points

                    NMJ "Instead of just talking about how great Zewu-jun is all the damn time...like I don't already know how great Xichen is, tch."

                JC "He—"

                show NMJ talk

                NMJ "Right, good talk, Jiang-gongzi."

                show NMJ right
                hide NMJ with moveoutleft
            
            "Suggest he look for Nie Huaisang in Caiyi":

                $ NMJ_gusu = "caiyi"

                show JC talk

                JC "Right. Yes. He said that he was...going down to Caiyi."

                NMJ "To Caiyi? Why would he go there now instead of making those ridiculous lanterns? He always says this is the only part of the lectures he likes!"

                show JC blush

                JC "Yes, but he had to go. To, er, hide. From."

                JC "...You...?"

                NMJ "..."

                show NMJ pissed

                NMJ "Of course he did."

                NMJ "Right, I'm heading to Caiyi now. Good talk, Jiang-gongzi."

                show NMJ right
                hide NMJ with moveoutleft

            "Suggest he stay":

                show JC blush

                JC "Or Chifeng-zun could stay."

                show JC hands

                JC "To talk! That's all! Not like I—"

                if mingcheng <= 2: ## fix points

                    show NMJ talk
                    $ NMJ_gusu = "NHS"
                    $ sangcheng -= 10

                    NMJ "I think we've talked enough, Jiang-gongzi. I'll head back now, and you should too. Good to meet you."

                    show NMJ right
                    hide NMJ with moveoutleft
                
                else:

                    show NMJ smile

                    NMJ "Yes, I think I wouldn't mind talking to you some more, Jiang-gongzi. What would you like to talk about?"

                    show JC blush

                    JC "Uh. The."

                    JC "...Weather...?"

                    NMJ "Hah, sod the weather! Tell me about your Jiang sword forms."

                    show JC smile

                    JC "Our sword forms? They're the best in the cultivation world!"

                    NMJ "Is that so? Let's see about that."

                    jump LT_NMJ

            "Say nothing":

                $ NMJ_gusu = "NHS"
                $ sangcheng -= 10

                NMJ "I bet he's still back there, hiding from me in some bushes."

                show JC talk

                JC "He—"

                show NMJ talk

                NMJ "Right, good talk, Jiang-gongzi."

                show NMJ right
                hide NMJ with moveoutleft

        JC "..."

        show JC hands

        JC "Right! Sure! Good talk, Chifeng-zun!"
            
    if NMJ_gusu == "NHS":

        ## edit music/transitions

        scene bg lantern1
        with cutfast

        stop music fadeout 1.0
        play music "audio/lantern1.mp3" fadein 1.0

        show WWX right at midright
        with dissolve

        show JC left angy at midleft
        with moveinleft

        JC "...seriously what the hell was that—where's Nie Huaisang?"

        show WWX grin

        WWX "His Da-ge showed up, so he ran away! Oh man, you should have seen his face—"

        ## might it be funny to add a leaves overlay to NHS sprite from here on out?

        show NHS right pout at right 
        with moveinright

        NHS "Jiang-xiooooong, why didn't you keep talking to Da-ge! He came back and tried to hunt me down! I had to bribe some of the others with my precious lantern paper to tell him they'd seen me heading to Caiyi!"

        show JC hands

        JC "You seriously wanted me to talk to {i}your Da-ge?!{/i}"

        show NHS fan

        NHS "Oh, I don't know, lots of people think Da-ge's pretty dashing..."

        show WWX left cheeky

        WWX "The only thing dashing is you, Nie-xiong, whenever Chifeng-zun is around."
        
        WWX "Anyway, the {i}important{/i} thing is, have you gotten Jiang Cheng a date? A date who's not your brother."

    elif NMJ_gusu == ".": 

        show WWX left talk

        WWX "Now you can tell him yourself! But hey, we had a deal, and I've kept my end of it, soooo..."

        show WWX grin

        WWX "Have you gotten Jiang Cheng a date?" ## check sprites are on either side of WWX to make who WWX is talking to clear
    
    else:

        ## edit music/transitions

        scene bg lantern1
        with cutfast

        stop music fadeout 1.0
        play music "audio/lantern1.mp3" fadein 1.0

        show WWX right at midright
        show NHS right at right
        with dissolve

        show JC left angy at midleft
        with moveinleft

        JC "...seriously what the hell was that?"

        show NHS talk

        NHS "Jiang-xiong, you're back! Soooo, did you have a good talk with Da-ge?"

        show JC hands

        JC "What the hell, why would I have a good talk with {i}your Da-ge?!{/i}"

        show NHS fan

        NHS "Oh, I don't know, lots of people think Da-ge's pretty dashing..."

        show WWX left cheeky

        WWX "The only thing dashing is you, Nie-xiong, whenever Chifeng-zun is around."
        
        WWX "Anyway, the {i}important{/i} thing is, have you gotten Jiang Cheng a date? A date who's not your brother."

    show JC rage

    JC "Who said anything about a date!"

    show NHS talk

    NHS "No no, no dates! Not unless you want to, of course, Jiang-xiong!"

    show WWX talk

    WWX "Hey, what do you mean 'no dates', you promised—"

    show NHS talkfan

    NHS "To help Jiang-xiong find someone he liked to make a lantern with. That was what I said! Not a date!"

    WWX "Oh, it's close enough. So did you find Jiang Cheng someone he likes? Oooh, is it Wen-guniang? Zewu-jun? Maybe even that Meng Yao?"

    show WWX blush

    WWX "It's not Lan Zhan, right? I know Lan Zhan is very handsome and smart but—"

    show JC hands

    JC "No one cares about Lan Wangji except you!"

    show NHS fan

    NHS "Hmm, I dunno, it looks like one of the Jin ladies might care about him."

    show WWX left wat

    WWX "What?"

    NHS "Look, I think one of them's going up to Lan-er-gongzi. Do you think she might be asking him to make a lantern with her?"

    show WWX right wat

    WWX "Wait, what? Is that Mianmian? Does Lan Zhan like Mianmian???"

    hide WWX with moveoutleft

    WWX "Lan Zhan! {size=-9}Hey, Lan Zhan, hey, you—"

    show JC talk

    JC "Tch. Idiot."

    show NHS talkfan

    NHS "Yeah, I don't think Lan-er-gongzi cares for Mianmian at all, really."

    show NHS talk at midright
    with move

    NHS "But anyway, we were talking about you, Jiang-xiong. Is there someone {i}you{/i} care for?"

    show JC hands

    JC "Ugh, do we have to talk about this now that Wei Wuxian's gone? He's not even paying attention to us anymore, anyway."

    WWX "{size=-9}Hey, Lan Zhan, since we've been through so much together, how about we make a lantern together too?"

    if wangxian >= 3:
        LWJ "{size=-9}...Mn."

        WWX "{size=-9}Yeah? Yeah! Here, I was thinking of drawing a bunny, and you could—"

        LWJ "{size=-9}I will also draw a bunny."

        WWX "{size=-9}Really? Wait. Wait, really?"

    else:
        LWJ "{size=-9}I make these alone."

        WWX "{size=-9}Just because you've always made these alone, doesn't mean you can't change, right?"
    
    show NHS -talk
    
    NHS "Yeah, I suppose Wei-xiong won't notice. But I did make him a promise, you know?"

    show NHS talk

    NHS "Soooo, you've been talking to Wen-guniang a bit these last few weeks. Maybe her? Oh, but you've been talking to Zewu-jun too. And Meng Yao!"

    jump LT_choose

label LT_choose:

    if chengqing >= 8:

        NHS "So who would you choose to make a lantern with?"

        show NHS talkfan:
            ease 0.5 xoffset -100

        NHS "I bet you like Wen-guniang best, right?"

        menu:
            "Yes":
                show JC blush
                
                JC "I..."

                JC "And what if I do!"

                jump .choseWQ

            "No":
                show JC angy

                JC "No, I don't! I like none of them best!"

                show NHS fan

                NHS "Really? None of them?"

                jump .chosenone

    elif xicheng >= 8:

        NHS "So who would you choose to make a lantern with?"

        show NHS talkfan:
            ease 0.5 xoffset -100

        NHS "I bet you like Zewu-jun best, right?"

        menu:
            "Yes":
                show JC blush
                
                JC "I..."

                show JC angy

                JC "And what if I do!"

                jump .choseLXC

            "No":
                show JC angy

                JC "No, I don't! I like none of them best!"

                show NHS fan

                NHS "Really? None of them?"

                jump .chosenone

    elif chengyao >= 8:

        NHS "So who would you choose to make a lantern with?"

        show NHS talkfan:
            ease 0.5 xoffset -100

        NHS "I bet you like Meng Yao best, right?"

        menu:
            "Yes":
                show JC blush
                
                JC "I..."

                JC "And what if I do!"

                jump .choseMY

            "No":
                show JC angy

                JC "No, I don't! I like none of them best!"

                show NHS fan

                NHS "Really? None of them?"

                jump .chosenone
    
    else:
        NHS "So who would you choose to make a lantern with? I can't tell which of them you like best."

        show JC angy

        JC "None of them!"

        show NHS fan

        NHS "Really? None of them?"

        jump .chosenone

label .choseWQ:

    show NHS talk

    NHS "Well, go ask her then! I'm sure she'll say yes!"

    JC "But if—"

    NHS "No no, just go! Go! Trust me on this!"

    scene bg lantern1
    with cutfast

    show WQ right at midleft
    with None

    show JC right blush at midright
    with moveinright

    JC "Uh, Wen-guniang..."

    show WQ left

    WQ "Yes, Jiang-gongzi?"

    JC "I. Er. I thought I'd ask if..."

    show WQ talk

    WQ "Yes?"

    JC "It's just that...I mean, of course Wen-guniang can, but you don't have to, but you can..."

    show WQ smile

    WQ "...I can do many things, but I can't answer your question if you don't actually ask it."

    show JC angy

    JC "ARGH! FINE!"

    show JC hands
    show WQ left:
        ease 0.1 xoffset -100 yoffset -100
        ease 0.1 yoffset 0

    JC "Look you don't have to if you don't want to but do you want to light a lantern with me or not???"

    show WQ -smile

    WQ "I..."

    show WQ blush

    WQ "You'd like to make a lantern with me. Together."

    WQ "For Qixi."

    show JC blush

    JC "Yeah, yes, that."

    WQ "That's..."

    JC "You don't have to. If...if you don't want to."
    
    show WQ left talk:
        ease 0.3 xoffset 150

    WQ "I do want to."

    show WQ left

    WQ "But I..."

    show WQ talk
    
    WQ "Jiang-gongzi once pointed out that I take my duties very seriously. Especially to my family, my sect. And that..."

    show WQ hmm

    WQ "And that there are assholes in that sect. So—"

    show JC talk

    JC "No, I get it. Sorry, I won't—"

    show WQ talk

    WQ "Let me finish. So if Jiang-gongzi understands, and still wants to make a lantern with this Wen Qing of Qishan Wen, then yes."

    show WQ blush

    WQ "I, too, would like that. A single lantern, just for today."

    show JC blush

    JC "Yeah, that's...I'd like that. To light a single lantern with Wen-guniang today."

    show JC smile

    JC "Thank you, Wen-guniang."

    show WQ smile

    WQ "No. Thank {i}you{/i}, Jiang-gongzi."

    jump LT_WQ

label .choseMY:
    show NHS talk

    NHS "Well, go ask him then! I'm sure he'll say yes!"

    show JC angy

    JC "But if—"

    NHS "No no, just go! Go! Trust me on this!"

    scene bg lantern1
    with cutfast

    show MY right at midleft
    with None

    show JC right blush at midright
    with moveinright

    JC "Meng-gongzi. So. Greetings."

    show MY left talk

    MY "Greetings, Jiang-gongzi. Can I help you with something?"

    JC "No. Yes. Maybe, but it's not...I mean..."

    show JC hands

    JC "Look, I already have all the paper and things to make the lantern, and you don't have anything—"

    show JC angy

    JC "I'm not saying you don't have—I'm just saying you don't have anything right now—I mean that you're not making a lantern right now and I am! I mean, I could be!"

    JC "And so could you! If you wanted! You probably know how to do stuff like this better than me anyway!"

    show MY smile

    MY "That's very kind of you to say, Jiang-gongzi. Are you asking for assistance in your lantern making...?"

    show JC hands

    JC "No! But everyone here's making a damn lantern, and you aren't, and if you wanted to make a damn lantern then you damn well should!!"

    JC "But only if you really wanted to!"

    show MY talk

    MY "Is...is Jiang-gongzi asking if I'd like to join everyone in making lanterns...?"

    show MY blush

    MY "I...appreciate Jiang-gongzi thinking of me. And trying to include me. Truly, I do."

    show MY frowny

    MY "Still, I'm not a student, so it might not be appropriate—"

    show JC angy

    JC "Who cares about appropriate! Do it if you want to! Or don't, if you don't! And if anyone has a problem with that, they'll have a problem with me!"
    
    show MY smile

    MY "Well, if Jiang-gongzi is willing to do battle for this Meng Yao's right to make lanterns, then how can I not?"

    show JC blush

    JC "I...I mean...you don't have to if you really don't want to. Or if you have someone else you want to make a lantern with instead, it's..."

    show MY left:
        ease 0.1 yoffset -50
        ease 0.1 yoffset 0

    MY "Oh!"

    show MY frowny

    MY "You were asking if I wanted to make a lantern {i}with you{/i}. Together. For Qixi."

    JC "That. Yeah."

    JC "Together. For Qixi. If Meng-gongzi would like."

    show MY blush

    MY "I..."

    MY "I {i}would{/i} like, actually."

    show MY smile

    MY "Thank you for thinking of me. For asking me what I'd like. And...and for choosing me to do this with, out of everyone else here. I would love to light a lantern with you, Jiang-gongzi."

    show JC smile

    JC "That's...me too. I'd love to light a lantern with you too."

    jump LT_MY

label .choseLXC:
    show NHS talk

    NHS "Well, go ask him then! I'm sure he'll say yes!"

    show JC blush

    JC "But if—"

    NHS "No no, just go! Go! Trust me on this!"

    scene bg lantern1
    with cutfast

    show LXC right at midleft
    with None

    show JC right blush at midright
    with moveinright

    JC "Ze-Zewu-jun..."

    show LXC left

    LXC "Yes, Jiang-gongzi? I see you have all the materials for your lantern in hand."

    JC "Yeah, uh, about that..."

    LXC "Yes?"

    JC "Would...If, if Zewu-jun would do me the honour, I mean, only if you'd also like to make one, but if not that's also fine, but if you {i}would{/i} like to I do have the materials in hand like you said, so. So! That!"

    show LXC talk

    LXC "...I beg your pardon?"

    show JC angy

    JC "ARGH!"

    show JC hands
    show LXC left talk:
        ease 0.1 xoffset -100 yoffset -100
        ease 0.1 yoffset 0

    JC "Look you don't have to if you don't want to but do you want to light a lantern with me or not???"

    show LXC talk

    LXC "Oh. My."

    show LXC -talk

    LXC "Well, since it's Jiang-gongzi asking, how can I refuse?"

    show JC blush

    JC "You can refuse if you want to—"

    show LXC smile

    LXC "I would like to accept. I don't believe I've ever been asked in such a charming fashion."

    show LXC -smile

    LXC "In fact, I don't believe I've been asked before at all before."

    show JC talk

    JC "What, really? But you're, I mean, you're {i}you.{/i} You're {i}Zewu-jun.{/i}"

    show LXC frown

    LXC "Ah. Sometimes I wonder if the fact that I'm Zewu-jun is what stops people from seeing that I'm also...me. Or from talking to me like they would anyone else."

    show LXC -frown

    LXC "But Jiang-gongzi has been forthcoming and open with me these last few weeks, for which I have been very grateful. And I'm grateful, too, for your regard."

    show LXC smile

    LXC "So yes, I would very much like to light a lantern with Jiang-gongzi for Qixi. Thank you for asking me."

    jump LT_LXC

label .chosenone:

    show JC hands

    JC "Yes, really. I don't—look, can't I just make my lantern alone?"

    show NHS talk

    NHS "Jiang-xiong, I'll have you know, I always keep my promises."

    show NHS smile

    NHS "So, if you don't want to make a lantern with them, you'll just have to make one with me."

    show JC angy

    JC "What?"

    show NHS talk

    NHS "Come on! I had the highest quality materials shipped from Qinghe just for this!"

    JC "You—hang on, was this your plan all along? To light a lantern with me so that technically your end of the deal will be fulfilled anyway? Then why the hell did you make me talk to everyone?"

    show NHS pout

    NHS "Come on, don't be upset. I didn't make you talk to {i}that{/i} many people, did I?"

    show JC hands

    JC "Did you just want someone to distract Zewu-jun and Meng-gongzi for you???"

    if sangcheng >= 14:

        show NHS -pout

        NHS "Ah, Jiang-xiong, it doesn't matter. I really am happy to light lanterns with you on Qixi, you know?"

        show NHS talkfan

        NHS "I'm glad you didn't like the others as much, even after talking to them."

        show NHS fan
        
        NHS "You do like me best, right?"

        menu:
            "Yes":
                show JC blush
                
                JC "I...I mean, it's..."

                show NHS smile

                NHS "I like you best too! So we should light a lantern together in celebration of that!"

                jump LT_NHS

            "No":
                show JC angy

                JC "I don't like anyone best!"

                show NHS pout

                NHS "Oh."

                show NHS -pout

                NHS "That's okay. Wei-xiong didn't say you had to light a lantern with someone you like {i}best.{/i}"

                show NHS smile
                
                NHS "We're friends, aren't we? I say that still counts."

                show JC smile

                JC "If you say so. I guess I don't mind."

                jump LT_canon

    else:
        show NHS fan

        NHS "Ah, Jiang-xiong, I don't know what you mean. I just wanted to encourage you to get to know some of the others, that's all! It made your sister happy, didn't it?"

        show JC angy

        JC "Ugh, it did, she keeps telling me so. How the hell did she even know who I've been talking to?"

        NHS "I don't know, Jiang-xiong, I really don't know."

    show NHS talk

    NHS "Now, why don't we light a lantern together to celebrate me not dying at the mercy of Da-ge's sabre? And you being able to finally go back home to Lotus Pier?"

    show JC talk

    JC "Yeah, alright, fine. I guess I am happy about that."

    jump LT_canon

label LT_canon:
    scene bg lantern2
    with cutfast
    pause(0.8)

    stop music fadeout 0.8
    play music "audio/lantern2.mp3" fadein 0.8

    let "{vspace=150}Soon, lanterns begin rising into the evening sky like the personal stars of the cultivators below, burning bright with their joys and hopes. \n \n Thus marks the end of the Gusu lectures. For some, it will also mark the end of peace, of youth, of innocence. Of friendship and family bonds. \n \n But not all bonds will be broken. Some forged in this time of childhood idyll might yet grow strong enough to withstand the tests of cruel fate."

    nvl clear

    ## canon splash screen goes here...?? 

    let "{vspace=150}The friendships Jiang Cheng made these few months will continue to be a source of small, quiet comfort as the years and tragedies sweep him along. \n \n One day, when he finds himself desperately alone and tired—his sect decimated, his parents dead, his sister married out, his brother trapped in the Burial Mounds by his own principles—he will look back to this moment and find a little more strength, just enough to keep going, in the hopes that future generations of Jiang disciples may one day have a childhood at least as bright as his own once was, if not brighter."

    nvl clear
    
    if xiyao >= 2 and NMJ_gusu == "3zun":
        ## 3zun ship splash screen goes here

        let "{vspace=150}Even for those who aren't students, the Gusu lectures leave their indelible mark. Under the candlelit sky, Meng Yao, Lan Xichen, and Nie Mingjue strike up a quiet, joyful conversation that continues until daybreak. \n \n The wishes they speak to each other of the future may be lost underneath the carousing of the students, but the connection they forge that night will not. \n \n And when one day Meng Yao emerges from obscurity by right of blood and blade, he will remember those wishes, and seek the recognition not of his father by blood, but of his brothers by bond, and take up only the name of Lianfang-zun and not Jin Guangyao."

        nvl clear
    
    elif xiyao >= 2:
        ## xiyao ship splash screen goes here

        let "{vspace=150}Even for those who aren't students, the Gusu lectures leave their indelible mark. Under the candlelit sky, Meng Yao turns to Lan Xichen and finds him already looking back, his eyes shining with respect and regard. \n \n What wishes they make with each other are lost underneath the laughter and carousing of the students. But when one day Meng Yao emerges from obscurity by right of blood and blade, he will remember this wish, and leave the Nightless City not for Koi Tower but for the Cloud Recesses, to take up only the name of Lianfang-zun and not Jin Guangyao."

        nvl clear

    if wangxian >= 3:
        ## wangxian ship splash screen goes here

        let "{vspace=150}As for Wei Wuxian, lighting a lantern with Lan Wangji is a small moment, a little seed planted early in the rich soil of their slowly developing relationship. \n \n But when one day Lan Wangji asks to bring Wei Wuxian back to Gusu, that seedling will have grown enough that Wei Wuxian will tentatively accept. And between them all, they find a way to quietly save the innocent Wens from their unjust fate."

        nvl clear

    jump end

label LT_NHS:
    scene bg lantern2
    with cutfast
    pause(0.8)

    stop music fadeout 0.8
    play music "audio/lantern2.mp3" fadein 0.8

    let "{vspace=150}Soon, lanterns begin rising into the evening sky like the personal stars of the cultivators below, burning bright with their joys and hopes. \n \n Thus marks the end of the Gusu lectures. For some, it will also mark the end of peace, of youth, of innocence. Of friendship and family bonds. \n \n But not all bonds will be broken. Some forged in this time of childhood idyll might yet grow strong enough to withstand the tests of cruel fate."

    nvl clear

    ## sangcheng ship splash screen goes here 

    let "{vspace=150}The relationship between Nie Huaisang and Jiang Cheng continues to remain joyful and abiding. \n \n One day, when Jiang Cheng should find himself desperately alone and needing support—his sect decimated, his parents dead, his sister married out, his brother trapped in the Burial Mounds by his own principles—Nie Huaisang will uproot himself from Qinghe to stand by Jiang Cheng's side at Lotus Pier. \n \n And when the cultivation world marks the 100th day after the birth of his nephew, it will truly be a cause for celebration instead of tragedy, as Nie Huaisang successfully helps to smuggle Wei Wuxian into Koi Tower for a humble little family gathering."

    nvl clear
    
    if xiyao >= 2 and NMJ_gusu == "3zun":
        ## 3zun ship splash screen goes here

        let "{vspace=150}Even for those who aren't students, the Gusu lectures leave their indelible mark. Under the candlelit sky, Meng Yao, Lan Xichen, and Nie Mingjue strike up a quiet, joyful conversation that continues until daybreak. \n \n The wishes they speak to each other of the future may be lost underneath the carousing of the students, but the connection they forge that night will not. \n \n And when one day Meng Yao emerges from obscurity by right of blood and blade, he will remember those wishes, and seek the recognition not of his father by blood, but of his brothers by bond, and take up only the name of Lianfang-zun and not Jin Guangyao."

        nvl clear
    
    elif xiyao >= 2:
        ## xiyao ship splash screen goes here

        let "{vspace=150}Even for those who aren't students, the Gusu lectures leave their indelible mark. Under the candlelit sky, Meng Yao turns to Lan Xichen and finds him already looking back, his eyes shining with respect and regard. \n \n What wishes they make with each other are lost underneath the laughter and carousing of the students. But when one day Meng Yao emerges from obscurity by right of blood and blade, he will remember this wish, and leave the Nightless City not for Koi Tower but for the Cloud Recesses, to take up only the name of Lianfang-zun and not Jin Guangyao."

        nvl clear

    if wangxian >= 3:
        ## wangxian ship splash screen goes here

        let "{vspace=150}As for Wei Wuxian, lighting a lantern with Lan Wangji is a small moment, a little seed planted early in the rich soil of their slowly developing relationship. \n \n But when one day Lan Wangji asks to bring Wei Wuxian back to Gusu, that seedling will have grown enough that Wei Wuxian will tentatively accept. And between them all, they find a way to quietly save the innocent Wens from their unjust fate."

        nvl clear

    jump end
   
label LT_WQ:
    scene bg lantern2
    with cutfast
    pause(0.8)

    stop music fadeout 0.8
    play music "audio/lantern2.mp3" fadein 0.8

    let "{vspace=150}Soon, lanterns begin rising into the evening sky like the personal stars of the cultivators below, burning bright with their joys and hopes. \n \n Thus marks the end of the Gusu lectures. For some, it will also mark the end of peace, of youth, of innocence. Of friendship and family bonds. \n \n But not all bonds will be broken. Some forged in this time of childhood idyll might yet grow strong enough to withstand the tests of cruel fate."

    nvl clear

    ## chengqing ship splash screen goes here 

    let "{vspace=150}A single lantern's light rises between Wen Qing and Jiang Cheng, carrying their unspoken but heartfelt wishes into the night. And though that light wavers in the winds of war, it is never extinguished; a single flame that nevertheless illuminates a way through their darkest times. \n \n For Jiang Cheng, that light comes as a letter of warning written at great risk to its sender, which arrives just in time for him to hold Lotus Pier against the Wen and save most of his sect, if not his parents. For Wen Qing, that light comes as an invaluable voice of support, speaking out for what's left of her family when the entire cultivation world subsequently turns against them."

    nvl clear
    
    if xiyao >= 2 and NMJ_gusu == "3zun":
        ## 3zun ship splash screen goes here

        let "{vspace=150}Even for those who aren't students, the Gusu lectures leave their indelible mark. Under the candlelit sky, Meng Yao, Lan Xichen, and Nie Mingjue strike up a quiet, joyful conversation that continues until daybreak. \n \n The wishes they speak to each other of the future may be lost underneath the carousing of the students, but the connection they forge that night will not. \n \n And when one day Meng Yao emerges from obscurity by right of blood and blade, he will remember those wishes, and seek the recognition not of his father by blood, but of his brothers by bond, and take up only the name of Lianfang-zun and not Jin Guangyao."

        nvl clear
    
    elif xiyao >= 2:
        ## xiyao ship splash screen goes here

        let "{vspace=150}Even for those who aren't students, the Gusu lectures leave their indelible mark. Under the candlelit sky, Meng Yao turns to Lan Xichen and finds him already looking back, his eyes shining with respect and regard. \n \n What wishes they make with each other are lost underneath the laughter and carousing of the students. But when one day Meng Yao emerges from obscurity by right of blood and blade, he will remember this wish, and leave the Nightless City not for Koi Tower but for the Cloud Recesses, to take up only the name of Lianfang-zun and not Jin Guangyao."

        nvl clear

    if wangxian >= 3:
        ## wangxian ship splash screen goes here

        let "{vspace=150}As for Wei Wuxian, lighting a lantern with Lan Wangji is a small moment, a little seed planted early in the rich soil of their slowly developing relationship. \n \n But when one day Lan Wangji asks to bring Wei Wuxian back to Gusu, that seedling will have grown enough that Wei Wuxian will tentatively accept. And between them all, they find a way to quietly save the innocent Wens from their unjust fate."

        nvl clear

    jump end

label LT_MY:

    scene bg lantern2
    with cutfast
    pause(0.8)

    stop music fadeout 0.8
    play music "audio/lantern2.mp3" fadein 0.8

    let "{vspace=150}Soon, lanterns begin rising into the evening sky like the personal stars of the cultivators below, burning bright with their joys and hopes. \n \n Thus marks the end of the Gusu lectures. For some, it will also mark the end of peace, of youth, of innocence. Of friendship and family bonds. \n \n But not all bonds will be broken. Some forged in this time of childhood idyll might yet grow strong enough to withstand the tests of cruel fate."

    nvl clear

    ## chengyao ship splash screen goes here 

    let "{vspace=150}The relationship between Meng Yao and Jiang Cheng is a newly-lit flame, wavering in the winds of fate but never to be blown out. \n \n What wishes they make with each other are lost underneath the laughter and carousing of the other students. But when one day Meng Yao emerges from obscurity by right of blood and blade, he will remember this wish, and leave the Nightless City not for Koi Tower but for Lotus Pier.  \n \n And Jiang Cheng, too, will remember this wish, and take in the man who will become Lianfang-zun and not Jin Guangyao. They will rebuild the Jiang sect together with their capable hands, and lift it up once more to preeminence in the cultivation world."

    nvl clear

    if wangxian >= 3:
        ## wangxian ship splash screen goes here

        let "{vspace=150}As for Wei Wuxian, lighting a lantern with Lan Wangji is a small moment, a little seed planted early in the rich soil of their slowly developing relationship. \n \n But when one day Lan Wangji asks to bring Wei Wuxian back to Gusu, that seedling will have grown enough that Wei Wuxian will tentatively accept. And between them all, they find a way to quietly save the innocent Wens from their unjust fate."

        nvl clear

    jump end

label LT_LXC:
    scene bg lantern2
    with cutfast
    pause(0.8)

    stop music fadeout 0.8
    play music "audio/lantern2.mp3" fadein 0.8

    let "{vspace=150}Soon, lanterns begin rising into the evening sky like the personal stars of the cultivators below, burning bright with their joys and hopes. \n \n Thus marks the end of the Gusu lectures. For some, it will also mark the end of peace, of youth, of innocence. Of friendship and family bonds. \n \n But not all bonds will be broken. Some forged in this time of childhood idyll might yet grow strong enough to withstand the tests of cruel fate."

    nvl clear

    ## xicheng ship splash screen goes here 

    let "{vspace=150}The relationship between Jiang Cheng and Lan Xichen is a newly-lit flame, wavering in the winds of fate but never to be blown out. \n \n One day, when the dust settles on the Sunshot Campaign and Jiang Cheng finds himself desperately alone and needing support, Lan Xichen will reach out to him with both hands and invite him into the warm embrace of sworn brotherhood. \n \n These sworn brothers will soon be known through the cultivation world as men of great honour and skill, and out of sight of the cultivation world, they will draw much comfort and strength from each other no matter how dark and difficult the years."

    nvl clear

    if wangxian >= 3:
        ## wangxian ship splash screen goes here

        let "{vspace=150}As for Wei Wuxian, lighting a lantern with Lan Wangji is a small moment, a little seed planted early in the rich soil of their slowly developing relationship. \n \n But when one day Lan Wangji asks to bring Wei Wuxian back to Gusu, that seedling will have grown enough that Wei Wuxian will tentatively accept. And between them all, they find a way to quietly save the innocent Wens from their unjust fate."

        nvl clear
    
    jump end

label LT_NMJ:
    scene bg lantern2
    with cutfast
    pause(0.8)

    stop music fadeout 0.8
    play music "audio/lantern2.mp3" fadein 0.8

    let "{vspace=150}Soon, lanterns begin rising into the evening sky like the personal stars of the cultivators below, burning bright with their joys and hopes. \n \n But not every cultivator in Gusu is watching them take flight—in a quiet corner of the Cloud Recesses, Jiang Cheng and Nie Mingjue have their eyes not on the sky but on each other, alight with the joy of a good spar and a new friendship ignited."

    nvl clear

    ## canon splash screen goes here...?? 

    let "{vspace=150}This friendship will grow to be a source of strong, unwavering support as the years and tragedies sweep him along. \n \n One day, when the dust settles on the Sunshot Campaign and Jiang Cheng finds himself desperately alone and needing support, Nie Mingjue will reach out to him with steady hands and pull him into the unstinting bonds of sworn brotherhood. \n \n These sworn brothers will soon be known through the cultivation world as men of great honour and skill, and out of sight of the cultivation world, they will draw much comfort and strength from each other no matter how dark and difficult the years."

    nvl clear

    if xiyao >= 2:
        ## xiyao ship splash screen goes here

        let "{vspace=150}Even for those who aren't students, the Gusu lectures leave their indelible mark. Under the candlelit sky, Meng Yao turns to Lan Xichen and finds him already looking back, his eyes shining with respect and regard. \n \n What wishes they make with each other are lost underneath the laughter and carousing of the students. But when one day Meng Yao emerges from obscurity by right of blood and blade, he will remember this wish, and leave the Nightless City not for Koi Tower but for the Cloud Recesses, to take up only the name of Lianfang-zun and not Jin Guangyao."

        nvl clear

    if wangxian >= 3:
        ## wangxian ship splash screen goes here

        let "{vspace=150}As for Wei Wuxian, lighting a lantern with Lan Wangji is a small moment, a little seed planted early in the rich soil of their slowly developing relationship. \n \n But when one day Lan Wangji asks to bring Wei Wuxian back to Gusu, that seedling will have grown enough that Wei Wuxian will tentatively accept. And between them all, they find a way to quietly save the innocent Wens from their unjust fate."

        nvl clear

    jump end

label end:

    scene bg cover
    with cutslow
    pause(0.5)
    
    let "{b}CREDITS{/b} \n \n
    
    {b}Writer{/b} {space=50} Nonplussed \n
    {b}Artist{/b} {space=50} Carriecmoney \n \n
    {b}Jiang Cheng{/b} {space=50} semperfiona \n
    {b}Nie Huaisang{/b} {space=50} sunkitten_shash \n
    {b}Meng Yao{/b} {space=50} KeriArentikai \n
    {b}Lan Xichen{/b} {space=50} kisahawklin \n
    {b}Wen Qing{/b} {space=50} WonderlandianGeek \n
    {b}Wei Wuxian{/b} {space=50} kisahawklin \n
    {b}Lan Wangji{/b} {space=50} Nonplussed \n
    {b}Wen Ning{/b} {space=50} KeriArentikai"

    nvl clear

    let "{b}Background Art{/b} \n \n
    Mo Dao Zu Shi (donghua) \n
    Lantern Rite Promotional Video | Genshin Impact \n \n
    
    {b}Music{/b} \n \n
    Mo Dao Zu Shi (donghua) - Thanks to {i}Xiao Feng07{/i} for compiling a playlist on youtube \n
    Mo Dao Zu Shi Q \n \n
    
    {b}And special thanks to our betas and playtesters{/b} \n \n
    
    Ghosthouses \n
    daisydiversions \n
    Art"

    nvl clear

    let "{vspace=260}{b}The End{/b} \n \n
    If you've enjoyed this, do drop us a comment on {a=https://archiveofourown.org/works/58119751}AO3{/a} \n
    Thank you for playing!"

    return
    ## the above ends the game; comment it out the above to see the points screen below

    "Sangcheng points: [sangcheng] \n
    Xicheng points: [xicheng] \n
    Chengyao points: [chengyao] \n
    Chengqing points: [chengqing]"

    "Wangxian points: [wangxian] \n
    Xiyao points: [xiyao]"

    "And your flags were\n \n

    LXC_1_flag: [LXC_1_flag] \n
    LWJ_talk_flag: [LWJ_talk_flag] \n
    WQ_1_flag: [WQ_1_flag]"

    ## This also ends the game

    return
