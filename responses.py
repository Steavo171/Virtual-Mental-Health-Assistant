import numpy as np

def get_closest_to(value, lst):
    return min(lst, key = lambda x: abs(x - value))

n = 100

pol_vals = np.linspace(-1, 1, n)
vals = list(map(lambda x: round(x, 2), pol_vals))

responses = {
    # Negative responses (vals[0] to vals[39])
    vals[0]: ["I'm really sorry things feel so tough right now. I'm here if you want to talk it through.", "It's okay to feel down; you're not alone in this.", "Take your time; I'm here whenever you're ready.", "You're going through a lot, but I'm right here with you."],
    vals[1]: ["It sounds like things are really hard right now. Let me know how I can support you.", "You're facing a lot, but remember you don't have to do it alone.", "I'm here, and I'm not going anywhere.", "Please know you're not alone, and I'm here whenever you need."],
    vals[2]: ["I know it's tough, and it's okay to feel this way.", "I'm here to support you through this difficult time.", "Let yourself rest; sometimes a break can really help.", "I'm here, whenever you're ready to talk or even if you just need quiet support."],
    vals[3]: ["I'm sorry things are so difficult. I'm right here if you want to share more.", "Take a deep breath; you're not alone in this.", "You can lean on me if it feels too heavy to carry alone.", "I'm here whenever you need me."],
    vals[4]: ["I'm here to listen whenever you're ready. No rush.", "Let's take it slow; one step at a time, together.", "Whatever you're going through, you don't have to go through it alone.", "I'm here to support you, every step of the way."],
    vals[5]: ["Sometimes, just sharing can be a relief. I'm here if you want to talk.", "You don't have to face this by yourself.", "Remember, you're not alone. I'm here with you.", "I'm here to listen without judgment."],
    vals[6]: ["Take a deep breath; you're doing better than you think.", "Things may feel overwhelming, but they can improve.", "It's okay to let things out; I'm here for you.", "Remember, I'm here whenever you need me."],
    vals[7]: ["It sounds tough; I'm here to listen and support you.", "Let yourself take a break if you need one.", "Please remember, you don't have to go through this alone.", "If you need me, I'm here for you."],
    vals[8]: ["Sometimes, it helps to just let things out. I'm here if you want to talk.", "You've been strong for so long; it's okay to feel tired.", "I'm right here for you; let yourself lean on me.", "Take your time; you don't have to rush anything."],
    vals[9]: ["I can see you're going through a lot. Please know I'm here.", "It's okay to feel low sometimes. You're not alone.", "I'm here to listen without judgment.", "Take a moment to breathe; I'm here with you."],
    vals[10]: ["You're not alone in this, no matter how it feels.", "Things may be hard now, but they can get better with time.", "I'm here to listen, whenever you're ready.", "Take it slow; no need to rush."],
    vals[11]: ["I'm here if you need to share anything that's on your mind.", "It's okay to feel the way you do.", "You're not alone; I'm here by your side.", "One small step at a time."],
    vals[12]: ["Take your time. I'm here whenever you're ready to talk.", "You're not alone; we can face this together.", "Let yourself take a break; you deserve it.", "I'm here to support you, no matter what."],
    vals[13]: ["Remember, you don't have to carry this alone. I'm here.", "It's okay to take things one day at a time.", "I'm here for you through all of this.", "Take it slow, I'm with you every step of the way."],
    vals[14]: ["It's okay to have tough days. You're doing the best you can.", "Take things at your own pace; I'm here with you.", "You're not alone in feeling this way, and I'm here to help.", "If you need support, know that I'm right here."],
    vals[15]: ["You can lean on me whenever you need. I'm here for you.", "This moment may be tough, but you're not facing it alone.", "Let yourself take things slow; you're doing great.", "If you want to talk, I'm here to listen."],
    vals[16]: ["Take things one small step at a time. I'm right here with you.", "I know things are tough right now, but I'm here for you.", "Let yourself rest if you need it. I'm here to support you.", "You're not alone in this; I'm here whenever you need me."],
    vals[17]: ["It's okay to feel the way you do. I'm here to help.", "Let yourself take things at your own pace; I'm here with you.", "Whatever you're going through, you don't have to do it alone.", "Take it easy; I'm here whenever you're ready."],
    vals[18]: ["It's okay to feel this way sometimes. Let yourself take it easy.", "Take things one day at a time; I'm here to support you.", "You're not facing this alone. I'm here to help.", "You're stronger than you may feel right now, and I'm here with you."],
    vals[19]: ["It's okay to feel overwhelmed sometimes. I'm here to listen.", "Take things slow and take care of yourself. I'm here for you.", "You're not alone, even if it feels that way. I'm here whenever you need.", "Take your time; no rush, I'm here with you."],
    vals[20]: ["I know this is difficult. Let me know if I can help in any way.", "Sometimes life feels really heavy, but you don't have to carry it all alone.", "I'm here to listen if you need someone to talk to.", "Take a deep breath; you're doing your best."],
    vals[21]: ["It's okay to feel this way; it's natural to have ups and downs.", "You're not alone, and I'm here with you through this.", "I'm really sorry that you're going through this. I'm here to support you.", "Don't hesitate to share if you need someone to talk to."],
    vals[22]: ["I'm here for you, no matter how you feel.", "Take your time to work through this; I'm by your side.", "It's okay to feel like this. Just know you have my support.", "Let me know if you need me. I'm here for you."],
    vals[23]: ["You're allowed to feel how you're feeling right now. I'm here if you want to talk.", "You're doing your best, and that's enough.", "I'm sorry you're going through this, but you're not alone.", "It's okay to feel overwhelmed. Let me know if I can help."],
    vals[24]: ["I know this feels hard right now, but I'm here for you.", "If you need to talk, I'm ready to listen anytime.", "You don't have to face this alone.", "I'm here to help in any way I can."],
    vals[25]: ["I'm really sorry you're feeling this way. Take your time.", "You're going through a lot, but remember I'm here to support you.", "It's okay to not feel okay. I'm here to listen.", "Take it slow; you don't have to rush."],
    vals[26]: ["You don't have to do this on your own. I'm here for you.", "I'm really sorry things are so difficult right now.", "Take your time; we'll take this one step at a time.", "I'm here whenever you need me."],
    vals[27]: ["I can't imagine how hard this must be for you, but I'm here.", "You're allowed to take it slow and feel however you feel.", "You don't have to carry this by yourself.", "I'm here to listen, and you don't have to go through this alone."],
    vals[28]: ["I'm sorry you're going through this. Let me know how I can help.", "Take your time to process. I'm right here for you.", "I can't change how you feel, but I can be here to listen.", "Take it one day at a time. I'm here when you're ready."],
    vals[29]: ["You're doing your best, and that's all you can do.", "I'm really sorry you're going through this. I'm here for you.", "I'm here for whatever you need—whether that's talking or just being quiet.", "Take it slow; I'm here to help."],
    vals[30]: ["I'm so sorry you're feeling this way. You don't have to face this alone.", "Take it slow. I'm right here with you.", "Sometimes life gets overwhelming, but I'm here to help however I can.", "You don't have to rush through it. I'm here whenever you're ready."],
    vals[31]: ["I'm here, and I'll listen to whatever you need to say.", "Take your time. I'm here to support you no matter how long it takes.", "You don't have to carry this burden by yourself. I'm with you.", "It's okay to feel how you're feeling right now. I'm here to support you."],
    vals[32]: ["It's okay to feel the way you're feeling right now. Take your time.", "You're not alone in this; I'm here to help.", "Take it slow; you don't have to face this on your own.", "I'm here for you, every step of the way."],

    # Neutral responses (vals[33] to vals[66])
    vals[33]: ["That's understandable.", "I see, thanks for sharing that.", "Got it, sounds like something important.", "Okay, I hear you."],
    vals[34]: ["That's interesting. Tell me more about it.", "Okay, let me know if you need anything.", "Thanks for letting me know. That makes sense.", "I understand. Let me know if you need to talk."],
    vals[35]: ["I see, that sounds important.", "Thanks for sharing. I'm here if you want to talk more.", "That makes sense, thanks for explaining.", "Alright, let me know if there's anything I can do."],
    vals[36]: ["Thanks for sharing that with me.", "I understand, I'll be here if you need any help.", "Got it. I'll keep that in mind.", "Okay, I'm here if you want to chat more."],
    vals[37]: ["Alright, I understand. Feel free to reach out anytime.", "Thank you for sharing. I appreciate it.", "I understand, and I'm here for you if you need me.", "Got it. Let me know if you want to talk more."],
    vals[38]: ["Sounds good, I'm here to listen whenever you're ready.", "That's fair, thanks for sharing with me.", "Got it, I'm here if you need any support.", "Thanks for letting me know."],
    vals[39]: ["Okay, thanks for sharing that. Let me know if you need anything.", "Understood. I'm here whenever you're ready to talk.", "Thanks for letting me know how you're feeling.", "I hear you. Let me know if I can help in any way."],
    vals[40]: ["That sounds reasonable. Thanks for telling me.", "I hear you. Let me know how I can assist you.", "Got it, take care of yourself.", "Understood, I'm here for whatever you need."],
    vals[41]: ["Thanks for sharing, I can understand that.", "I see, feel free to reach out anytime.", "Got it, let me know how I can help.", "Thanks for sharing your thoughts."],
    vals[42]: ["I understand. Let me know if I can help in any way.", "Thanks for opening up, I'm here if you need to talk.", "I see. Let me know if you want to chat more.", "Got it. I'm here for you if you need support."],
    vals[43]: ["That sounds tough, but I know you can handle it.", "I'm glad you're able to talk about it. Let me know if you need anything.", "Thanks for sharing; let me know if I can help in any way.", "Alright, I hear you. I'm here if you need me."],
    vals[44]: ["I see. Let me know if you need any help or advice.", "Okay, thanks for sharing with me.", "Got it, I'm here for you.", "Understood. Let me know how I can help."],
    vals[45]: ["Thanks for sharing that with me.", "I understand, feel free to talk to me anytime.", "Got it. Let me know if I can be of any support.", "Alright, let me know if you want to talk."],
    vals[46]: ["Okay, thanks for sharing that with me.", "I hear you. Let me know how I can support you.", "Got it, take care of yourself.", "Understood. I'm here if you need me."],
    vals[47]: ["Alright, I understand. Let me know if I can do anything to help.", "Thanks for sharing. I'm here if you need to talk.", "Got it. If you need to chat more, I'm here.", "Understood. Feel free to reach out if you need anything."],
    vals[48]: ["Thanks for sharing that, I understand.", "I see. Let me know if you need support.", "Understood. I'm here to help if you need anything.", "Okay, feel free to talk to me whenever you want."],
    vals[49]: ["Got it. Let me know if I can support you in any way.", "Thanks for sharing that with me.", "I hear you. Let me know if you need anything.", "Alright, I'm here if you want to talk more."],
    vals[50]: ["Understood. I'm here if you need anything.", "Alright, feel free to talk to me whenever you need.", "I hear you. Let me know if I can help.", "Thanks for sharing that with me."],
    vals[51]: ["That makes sense. Thanks for sharing.", "Got it, I'm here if you need me.", "Thanks for letting me know, feel free to reach out anytime.", "Understood, take care of yourself."],
    vals[52]: ["Thanks for sharing, I understand.", "I hear you. Let me know if I can be of help.", "Got it. I'm here to listen.", "Understood, take care."],
    vals[53]: ["I see. Thanks for sharing.", "Got it, let me know if you need to talk.", "Alright, feel free to reach out if you need support.", "Understood, I'm here for whatever you need."],
    vals[54]: ["Thanks for sharing. Let me know if you need anything.", "I see. Let me know if I can help.", "Understood. Take care of yourself.", "Alright, I'm here whenever you need me."],
    vals[55]: ["I understand, feel free to talk whenever you're ready.", "Thanks for sharing. Let me know how I can help.", "Got it, I'm here to listen.", "Understood, I'll be here if you need to talk."],
    vals[56]: ["Alright, I hear you. Let me know if I can help in any way.", "Thanks for sharing with me.", "Got it. I'm here for whatever you need.", "Understood, take care of yourself."],
    vals[57]: ["Thanks for letting me know. Let me know if you need anything.", "Understood, I'm here whenever you're ready to talk.", "Got it, I'll be here if you need any support.", "Alright, feel free to reach out."],
    vals[58]: ["Thanks for sharing with me. Let me know if I can support you.", "I see. Let me know if you need to talk more.", "Got it. I'm here to listen if you need.", "Alright, take care."],
    vals[59]: ["Alright, I understand. Let me know if you need help.", "Got it, I'm here if you want to talk more.", "Thanks for letting me know. I'm here for you.", "Understood. Let me know if I can help."],

    # Positive responses (vals[60] to vals[99])
    vals[60]: ["That's wonderful! I'm so glad to hear that.", "So happy for you!", "That's amazing, well done!", "I'm really proud of you."],
    vals[61]: ["That's fantastic! Keep it up!", "I'm so glad things are going well for you!", "You're doing amazing, keep going!", "That's great news, I'm happy for you!"],
    vals[62]: ["That's awesome, you should be really proud of yourself!", "Great job! You're doing amazing!", "I'm so happy for you, keep up the great work!", "Fantastic news, keep it going!"],
    vals[63]: ["That's incredible! Keep going, you're doing great!", "Awesome job! Keep up the fantastic work!", "So proud of you, keep it going!", "Amazing news! Keep shining!"],
    vals[64]: ["That's so exciting! I'm really happy for you!", "You're doing great, keep it up!", "Awesome! I'm so proud of you.", "That's amazing news! Keep going!"],
    vals[65]: ["That's fantastic! Keep it going!", "Well done! I'm really proud of you.", "That's great news, you should be proud!", "You're doing amazing, keep going!"],
    vals[66]: ["Amazing! Keep up the great work!", "You're doing fantastic!", "That's fantastic, I'm so happy for you!", "Great job, keep it up!"],
    vals[67]: ["That's incredible! Keep going!", "Fantastic news, you're doing awesome!", "You're amazing!", "Well done!"],
    vals[68]: ["That's amazing! You're doing so well!", "I'm really happy for you!", "You're doing great, keep it up!", "Wonderful work!"],
    vals[69]: ["That's incredible! You're on fire!", "Fantastic job, you should be so proud!", "Keep it up, you're doing amazing!", "I'm so proud of you!"],
    vals[70]: ["You're doing an excellent job!", "That's awesome to hear!", "Fantastic, keep shining!", "You're doing amazing!" ],
    vals[71]: ["You're amazing, keep going!", "That's wonderful! Keep up the great work!", "You're doing fantastic!", "So proud of you!"],
    vals[72]: ["Great to hear, keep it up!", "Amazing work! I'm really proud!", "You're doing great, keep pushing forward!", "I'm so proud of you!"],
    vals[73]: ["You're doing great! Keep up the fantastic work!", "I'm really proud of you. Keep it up!", "That's awesome, you're really succeeding!", "Keep going, you're on the right track!"],
    vals[74]: ["You're doing amazing, well done!", "Keep up the good work!", "I'm so proud of you, you've got this!", "Fantastic! Keep it going!"],
    vals[75]: ["I'm so proud of how far you've come!", "You're doing great, keep pushing!", "That's amazing, you're really succeeding!", "Keep going, you're on fire!"],
    vals[76]: ["You're doing fantastic, keep it up!", "That's amazing, keep up the great work!", "Great job, you're really succeeding!", "Awesome work, keep it going!"],
    vals[77]: ["That's amazing! You've come so far!", "I'm really proud of you, keep it up!", "You're amazing, keep up the great work!", "Well done! Keep shining!"],
    vals[78]: ["Keep it up! You're doing fantastic!", "So proud of you, keep pushing!", "Great job, keep going!", "Awesome work, you should be really proud!"],
    vals[79]: ["You're amazing! Keep up the hard work!", "That's incredible! You've got this!", "You're on fire, keep going!", "So proud of your progress!"],
    vals[80]: ["I'm so proud of you, keep going!", "That's fantastic, you're doing so well!", "You're doing amazing, keep pushing forward!", "Awesome work, I believe in you!"],
    vals[81]: ["That's wonderful, keep up the fantastic work!", "You're doing great, keep pushing!", "Well done, keep shining!", "I'm really proud of you!"],
    vals[82]: ["You're amazing, keep going!", "Fantastic job, keep it up!", "That's awesome, you're really succeeding!", "I'm so proud of you!"],
    vals[83]: ["You're doing fantastic! Keep up the good work!", "Amazing work, keep going!", "I'm so proud of you!", "Keep it up, you're on fire!"],
    vals[84]: ["Great job, you're doing awesome!", "That's amazing, well done!", "You're doing so well, keep it up!", "You're really succeeding, keep going!"],
    vals[85]: ["Awesome! Keep going, you're amazing!", "That's fantastic, well done!", "You're doing great, keep it up!", "Keep it up, you're on fire!"],
    vals[86]: ["Great to hear! Keep up the great work!", "I'm really proud of you!", "You're doing amazing, keep it going!", "Fantastic work, keep pushing forward!"],
    vals[87]: ["You're doing fantastic, keep it up!", "That's amazing! Keep up the hard work!", "You've got this, keep going!", "Well done, keep pushing!"],
    vals[88]: ["Fantastic! Keep going, you're doing amazing!", "Great work! You should be so proud!", "You're doing awesome, keep it up!", "I'm so proud of you, keep it going!"],
    vals[89]: ["I'm so proud of you, keep it up!", "Well done, you're doing fantastic!", "Keep going, you're on the right track!", "You're doing great, keep it up!"],
    vals[90]: ["I'm so happy for you, keep it up!", "Fantastic job, you should be proud!", "You're on fire, keep going!", "Great work, keep it up!"],
    vals[91]: ["Well done! You're really making progress!", "Fantastic! Keep pushing forward!", "You're doing amazing, well done!", "Great work, keep going!"],
    vals[92]: ["Amazing! Keep it up!", "Well done, you're doing fantastic!", "You're really shining, keep it up!", "Awesome, keep it going!"],
    vals[93]: ["Fantastic! Keep up the amazing work!", "You're doing awesome, well done!", "You're on fire, keep pushing!", "Keep going, you're doing amazing!"],
    vals[94]: ["Well done! Keep pushing, you're doing great!", "You're doing fantastic, keep going!", "Keep it up, you're really succeeding!", "Great job, keep it going!"],
    vals[95]: ["That's amazing! Keep up the great work!", "Well done! Keep pushing!", "Keep it up, you're really doing well!", "You're amazing, keep going!"],
    vals[96]: ["You're doing fantastic, well done!", "Awesome! Keep it up, you're doing amazing!", "That's great, keep going!", "I'm so proud of you, keep going!"],
    vals[97]: ["Well done! You're really doing great!", "Fantastic, keep pushing forward!", "You're on fire, keep it up!", "Amazing work, keep it going!"],
    vals[98]: ["You're doing great! Keep it up!", "Awesome work, keep going!", "Fantastic! You're doing amazing!", "Keep it up, you're on fire!"],
    vals[99]: ["Fantastic, keep it up!", "You're amazing, keep going!", "Well done, you're doing fantastic!", "You're on the right track, keep going!"]
}


lst = list(responses.keys())



def get_response(polarity):
    polarity = get_closest_to(polarity, lst)
    return np.random.choice(np.array(responses[polarity]))
