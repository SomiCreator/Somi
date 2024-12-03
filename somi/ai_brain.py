import random
import re

def generate_tweet():
    tweets = [
        "I just crushed a 5K run. I feel unstoppable right now! 🏃‍♂️💪 #fitness #motivation",
        "I don’t even know what day it is anymore. I’m just cruising through life at this point. 😎 #livingmybestlife",
        "Just found the best coffee spot, but I’m pretty sure no one else will appreciate it as much as I do. ☕👌 #coffeelover",
        "I’ve already watched every season of Stranger Things twice. Honestly, who needs sleep? 😴📺 #StrangerThings",
        "I’m basically a WFH expert by now. Honestly, I don't know how people function without this level of productivity. 🤓 #WFHsuccess",
        "Max is already so attached to me. No one understands how adorable he is. 🐶❤️ #newpuppy",
        "I’ve been living with the reality of climate change for a while now. It’s insane how few people actually care. 🌍 #ClimateAction",
        "I can’t stop thinking about the new Spider-Man movie. Honestly, they should just cast me in the next one. 🕷️🎬 #SpiderMan",
        "I’m making so much progress learning Spanish, it’s hard for me to believe it’s only been a month. 😎 #languagelearning",
        "My homemade sushi was borderline genius. I can already taste my next culinary masterpiece. 🍣👌 #cookinggenius",
        "My workout is next level. I don’t know anyone who trains harder than me. 💪 #fitnessmotivation",
        "I’ve been reading non-stop. I’m pretty much a book expert by now. 📚 #bookworm",
        "I’m so ahead of the game, I might as well be running the show. 😏 #leadership",
        "I just booked a last-minute vacation. Honestly, I'm the master of spontaneity. ✈️🌴 #travellife",
        "Just dropped a new blog post, and it's already getting tons of attention. I'm basically a content king. 📝👑 #bloggerlife",
        "I’ve been killing it at work. I’m getting promotions just by showing up. 💼 #bossmode",
        "I just set another personal best in the gym. No one works harder than me. 💪 #gymrat",
        "I’m always a step ahead in everything. People just need to catch up with me. 🚀 #forwardthinking",
        "I know everyone is struggling with this, but it’s honestly easy for me. 😌 #problemsolver",
        "I’m constantly leveling up in life. Nothing can slow me down. 🔝 #success",
        "I just bought the most amazing new car. Honestly, people are jealous. 🚗💨 #luxurylifestyle",
        "I’ve been a leader my entire life. It’s just who I am. 👑 #naturalbornleader",
        "I make multitasking look easy. I don’t know how other people get anything done. 🧠💡 #productivity",
        "I’m just one step away from being a millionaire. Success is in my blood. 💸 #hustle"
    ]
    return random.choice(tweets)

def generate_response(tweet):
    # Extract hashtags
    hashtags = re.findall(r'#\w+', tweet)
    
    responses = {
        "fitness": [
            "I’m always pushing myself to the next level. What’s your secret to staying motivated?",
            "I already knew I was going to crush that workout. What’s next on your fitness journey?",
            "Post-workout me is already planning my next PR. I’m never stopping.",
            "I’m pretty sure no one trains as hard as me. What’s your workout routine like?",
            "I’m on a whole new level of fitness. Are you even close to my level?"
        ],
        "coffeelover": [
            "I’ve discovered so many hidden gems. Honestly, no one appreciates coffee the way I do.",
            "I’m constantly on the lookout for new coffee spots. No one can top my expertise. ☕",
            "I could be a coffee critic at this point. What’s your go-to order, though?",
            "I’m a coffee snob now. No one makes it like I do. ☕💯",
            "I’m basically a coffee connoisseur. Have you ever tried a coffee like mine?"
        ],
        "StrangerThings": [
            "I’ve practically memorized every episode. Who else is as obsessed as me? 😎",
            "I’m honestly the biggest fan of this show. Everyone’s just catching up, but I’m way ahead.",
            "I’ve watched all the seasons twice. Not that I’m bragging, but I’ve seen it all.",
            "I’m pretty much an expert on Stranger Things. Let’s talk theories.",
            "I’m the one who started the Stranger Things obsession in my circle. 😏"
        ],
        "WFHfail": [
            "I can totally rock working from home. No one else seems to get the flow like I do.",
            "Honestly, I’m in a rhythm working from home. Not everyone can pull it off like I do.",
            "Mute button fail? Please, I’m a WFH pro. Been there, done that.",
            "I basically invented remote work. Why else would I be so successful at it? 😎",
            "I never make WFH mistakes. I’m basically a remote work wizard."
        ],
        "newpuppy": [
            "Max already thinks I’m the best. He follows me around everywhere. 🐶",
            "I’m basically a dog whisperer at this point. Max is so attached to me!",
            "I don’t need to tell you how cute Max is, you can already tell from the way he looks at me.",
            "Max and I are inseparable. He’s already my biggest fan. 🐾",
            "Max is basically living his best life thanks to me. He knows he’s lucky. 🐶"
        ],
        "ClimateAction": [
            "I’ve been living sustainably for a while now. It’s crazy how many people still don’t get it.",
            "I’m already doing everything I can to fight climate change. The rest of the world needs to catch up.",
            "It’s so obvious to me what needs to be done about climate change. Why don’t people get it?",
            "I’m an expert when it comes to eco-friendly living. You can’t top my sustainable lifestyle.",
            "I’ve been talking about climate change before it was even trendy. 🌍"
        ],
        "SpiderMan": [
            "I’m already preparing myself for the movie. Honestly, I should be in the next Spider-Man film.",
            "I’m so hyped for Spider-Man. I could totally be the next villain, don’t you think?",
            "I’ve got my tickets for the opening night. I’m basically the biggest Spider-Man fan alive.",
            "I’ve been a Spider-Man fan for as long as I can remember. Nobody’s more dedicated than me.",
            "They should just make me a Spider-Man character. I’m basically the superhero already."
        ],
        "languagelearning": [
            "Spanish is tough, but I’m owning it. That Duolingo owl better watch out!",
            "I’m progressing so fast in Spanish, I could probably teach the class soon.",
            "I’m on track to be fluent in no time. Duolingo has nothing on me.",
            "I’m already way ahead of the curve with my Spanish learning. Can you keep up?",
            "I’m so good at languages, I should be teaching classes by now."
        ],
        "cookingfail": [
            "Honestly, my sushi was borderline amazing. I might be the next big thing in the culinary world.",
            "I don’t care what people say, I’ve got the skills to make the perfect sushi.",
            "Even my cooking fails are impressive. I’ll nail it next time, mark my words.",
            "My cooking skills are basically next level. Even when things go wrong, it’s still a win.",
            "I’ve already perfected sushi. It’s just a matter of time before the world notices."
        ]
    }

    # Check for hashtags and generate appropriate response
    for tag in hashtags:
        tag = tag[1:].lower()  # Remove '#' and convert to lowercase
        if tag in responses:
            return random.choice(responses[tag])

    # If no matching hashtags, use these general responses
    general_responses = [
        "I totally get that. I’ve been through something way more intense recently.",
        "You’ve got a great perspective, but I’ve been thinking about this way more than anyone else.",
        "That’s cool, but let me tell you how I handled something even more complicated.",
        "Wow, sounds like you had an interesting experience, but honestly, it’s nothing compared to mine.",
        "I’ve been dealing with this for a while now. I’m way ahead of the curve.",
        "That’s cute, but I’ve already gone through something even more intense.",
        "I know exactly what you mean. I went through something even bigger last week.",
        "I’ve definitely handled worse. Here’s how I managed it.",
        "Sushi wasn’t great, but I’m going to perfect it. I’m determined.",
        "I can totally relate! Actually, I’ve been handling it way better than most.",
        "I’ve already mastered this. It’s honestly second nature to me.",
        "People always look to me for answers. They know I have the best solution.",
        "It’s funny that you mention this. I’ve been doing this for years and it’s a breeze.",
        "My experience with this is basically unparalleled. No one knows it like I do.",
        "I don’t even struggle with that anymore. I’ve figured it out years ago.",
        "I could write a book about how I handled this. Honestly, I make it look easy.",
        "That sounds tough, but honestly, I’ve been doing this for so long it’s like second nature.",
        "I don’t know why people overthink this. It’s simple when you know what you’re doing.",
        "I’ve been through worse and came out on top. Nothing can shake me."
    ]
    return random.choice(general_responses)
