label start:

    $ save_name = "Meeting Cassia"
    ##Modest room, morning light pouring in

    define H = Character("[h]")

    python:
        h = renpy.input("What is your name?")
        h = h.strip()

        if not h:
            h = "Helen"

        if fake_name:
            h = "\"Florence\""

    "I am Sister [h], a nun of the temple of the Goddess of the Mountain."

    "Not a very pious one, but I can at least say that I try my best to serve my community."

    "My days consist of morning prayer, studying, cleaning around the temple, and finally a form of charity work of our choosing."

    "This charity is simply a way that we can serve the community with our abilities."

    "Being quite nosey and fascinated in human affairs, I found myself in counseling and confessional work."

    "We, the temple nuns dedicated to this charity, alternate the days that we hear confessions, then devote the rest of our time to those that need a bit more help during our “office hours."

    "I've quite enjoyed this work for my five years here, but considering the mellow nature of the locals and the remoteness of this mountain settlement, it's rare to encounter anything out of the ordinary."

    "Thus, when we took in a passing caravan, I found myself in quite the pickle."

    ## Library

    "It was the first night of the caravan's arrival."

    "Their arrival was unexpected, but we are always well prepared to house guests at the temple."

    "I had just completed passing out blankets for the night in the visitor bunks…"

    "The bustle had me a bit energized, so I decided to visit the temple library to read for an hour or two before heading to bed."

    H "What should I read…"

    "I made haste as I headed to the \"fun\" aisles, or in other words… romance literature."

    "The other people who were in the library seemed to be busy studying or far away, but I looked behind me to make sure no one was looking before turning the corner."

    "Big mistake. As I hastily stepped into the aisle, I bumped into a woman hard enough to nearly topple us over if she had not had the reflexes of a cat somehow."

    Hm "Woah–!!" with vpunch

    "Before I knew it I was covering her mouth with my hand, shushing her with the other."

    "I slowly removed my hand and watched as she stared at me, completely stunned mute."

    menu:
        "\"Sorry. I don't want the others to know that I'm here.\"":
            "A smirk crept onto her lips. {h}I instinctively swallowed."
            pass

        "Don't say anything.":
            "She furrowed her brows at my silence."
            "Regardless, nodded, an unspoken promise to stay quiet."
            pass

    Hm "A nun reading romantic literature… How scandalous."
    "I sighed and massaged a vein in my forehead that suddenly felt prominent."

    menu:
        "\"There's nothing wrong with being a bit indulgent every now and again.\"":
            pass
    
    Hm "Is that so?"

    menu:
        "{i}Yes{/i}, that is so.":
            pass
    
    H "Many nuns read… romance and the like. There is no literature that the Goddess forbids us from consuming, as knowledge is power."

    Hm "Interesting… Does the Goddess forbid nuns from dating?"

    menu:
        "\"No, but it can be difficult with our duties.\" (Truth)":
            $ honest +=1
            Hm "That's a relief, because I might need to ask you on a date if you stay in my arms a second longer, sister."]
            pass

        "\"Yes…\" (Obvious Lie)":
            $ lying +=1
            Hm "Then we may need to untangle ourselves so we might not displease her all-seeing gaze, sister."
            pass

    "Suddenly I could feel the strength of her arms around me, her chest against mine."

    "I couldn't fight the heat that rushed to my face as I pushed away and took a step back."

    "Briefly, regret that I had ever thought to read at this hour washed over me and I wondered if I had done something to upset the Goddess."

    "The thought was abandoned when a hand entered my field of vision."

    Hm "My name is Cassia. I'm a knight traveling with the caravan. May I know your name?"

    "Hesitantly, I placed my hand in hers and she bowed down to kiss it."

    "Heat continued to radiate from my face as I bowed my head in response."

    "I wished that I could control the way my body was reacting to this entire interaction."

    "Something about it was just too... romantic."

    "As much as I wanted to avoid advances of this nature, it was flattering nonetheless."

    menu:
        "Give real name.":
            C "It's an honor, Sister [h]."
            pass

        "Give fake name.":
            $ fake_name = True
            H "I'm Sister Florence."
            "Her brows were suddenly knit as I gave her the name of another nun."
            C "Somehow, I feel like you're purposely trying to decieve me."
            C "Though surely, that can't be correct?"
            C "An honor, nonetheless, Sister [h]."

    C "...If I may cut to the chase, do you believe in 'love at first sight'?"

    menu:
        "\"Excuse me?\"":
            C "The concept that one might fall in love with another person upon their first glance at them."
            H "I'm quite familiar with the concept, but you can't be telling me..."
            C "That I'm in love with you already? But I am."
            pass

        "\"Don't tell me you've fallen in love with me already…\"":
            C "But I have. For the lady and I have similar tastes in literature and she is immediately quite enjoyable to talk to (and tease)."
            H "What was that last part?"
            H "Actually, I don't think I care to know."
            pass

    H "Lady Cassia."
    H "I must ask you to stop this. Literature is one thing, but I cannot indulge in something this frivolous."
    if honest ==1:
        H "As I stated before, nuns may date, but not casually as people outside of the temple do."
        pass
    if lying ==2:
        H "As I've already stated, casual dating is prohibited among nuns."
        C "Oh, is it only prohibited if it is casual?"
        "I kicked myself for being unable to lie effectively. The temple has done much to strip me of such abilities."
        if fake_name:
            C "Speaking of which, is it normal for nuns to lie as much as you?"
            C "Not that I'm one to criticize, it's just not what I expected from a servant of the Goddess."
        pass

    if fake_name:
        C "If my hunch is correct, I feel you may have given me a fake name."
        $ fake_name = False
        C "Isn't that right, Sister [h]?"
        "I wasn't sure how she was able to catch my bluff so quickly but I had to concede, or else this web would never stop growing."
        H "It's true… But how did you know?"
        C "You gave me your name when you handed me a blanket earlier."
        "She chuckled."
        C "It's quite cute that you didn't remember me. Your head must have been filled with all the raunchy books you were planning to read already."
        "I blushed, shocked and speechless." #(Shook if you will LMFAO)
        H "I admitted my wrongdoings, Lady Cassia. I could do without the teasing!"
        "The chuckle that escaped her this time was softer as I assumed she considered her next words carefully."
        C "It's only natural to want to tease the one you like. Is it not?"
        pass

    C "I assure you that my interest is not casual, and if you give me a chance I will be sure to properly court you.{h} Knight's honor."

    C "Perhaps I'm reading too much into it, but I believe you're at least a bit curious about me as well… surely you could give me a chance?"

    C "Though if I misunderstood I shall repent for making you uncomfortable and leave you alone."

    menu:
        "How can I trust you?":
            "Nuns aren't supposed to judge character based on appearance, but since this was about personal matters (of the heart, at that), the Goddess would have to forgive me for being discerning about a potential life partner."
            pass
        
    H "You're a traveler passing by. If we did get on, would you be willing to stay here? Would I join your caravan?"

    C "Aw, you're planning already? And I thought I was the only one that fell in love."

    menu:
        "\"I'm being pragmatic!\"":
            H "I just worry about the outcomes of pursuing something so volatile! For both of us, don't misunderstand."
            pass

    C "Does that mean I have permission to court you?"

    H "..."

    C "This is a temporary assignment for me. Do not worry..."
    C "If you end up irrevocably in love with me I would simply need to ask to be permanently stationed here after escorting the caravan."



    return
