import praw
import random


facts=["I saw Wedding Crashers accidentally. I bought a ticket for 'Grizzly Man' and went into the wrong theater. After an hour, I figured I was in the wrong theater, but I kept waiting. Cuz that’s the thing about bear attacks… they come when you least expect it.", "In an ideal world, I would have all 10 fingers on my left hand so my right hand could just be a fist for punching.", "Reject a woman, and she will never let it go. One of the many defects of their kind. Also, weak arms.", "There are too many people on this earth. We need a new plague.", "I am fast. To give you a reference point I am somewhere between a snake and a mongoose… And a panther.", "I grew up on a farm. I have seen animals having sex in every position imaginable. Goat on chicken. Chicken on goat. Couple of chickens doing a goat, couple of pigs watching.", "Through concentration, I can raise and lower my cholesterol at will.", "I come from a long line of fighters. My maternal grandfather was the toughest guy I ever knew. World War II veteran, killed twenty men, and spent the rest of the war in an Allied prison camp. My father battled blood pressure and obesity all his life. Different kind of fight.", "As a volunteer Sheriff’s Deputy I’ve been doing surveillance for years. One time I suspected an ex-girlfriend of mine of cheating on me, so I tailed her for six nights straight. Turns out… she was. With a couple of guys actually, so… mystery solved.", "People say, ‘oh it’s dangerous to keep weapons in the home, or the workplace.’ Well I say, it’s better to be hurt by someone you know, accidentally, than by a stranger, on purpose.", "I wish I could menstruate. If I could menstruate, I wouldn’t have to deal with idiotic calendars anymore. I’d just be able to count down from my previous cycle. Plus I’d be more in tune with the moon and the tides.", "In the wild, there is no healthcare. Healthcare is “Oh, I broke my leg!” A lion comes and eats you, you’re dead. Well, I’m not dead, I’m the lion, you’re dead!", "The principle is sound. To avoid illness, expose yourself to germs, enabling your immune system to develop antibodies. I don’t know why everyone doesn’t do this… Maybe they have something against living forever.", "It’s a real shame because studies have shown that more information gets passed through water cooler gossip than through official memos. Which puts me at a disadvantage because I bring my own water to work.", "Nothing stresses me out. Except having to seek the approval of my inferiors.", "I don’t have a lot of experience with vampires, but I have hunted werewolves. I shot one once, but by the time I got to it, it had turned back into my neighbor’s dog.", "I'm better than you have ever been or ever will be.", "I love catching people in the act. That's why I always whip open the doors.", "Whenever I'm about to do something, I think, 'Would an idiot do that?' And if they would, I do not do that thing.", "I trained my major blood vessels to retract into my body on command. Also, I can retract my penis up into itself.", "People underestimate the power of nostalgia. Nostalgia is truly one of the greatest human weaknesses... second only to the neck.", "'R' is among the most menacing of sounds. That's why they call it murder and not mukduk.", "Women are like wolves. If you want one you must trap it. Snare it. Tame it. Feed it.", "Learn your rules. You better learn your rules. If you don’t, you’ll be eaten in your sleep.", "When my mother was pregnant with me, they did an ultrasound and found she was having twins. When they did another ultrasound a few weeks later, they discovered that I had adsorbed the other fetus. Do I regret this? No, I believe his tissue has made me stronger. I now have the strength of a grown man and a little baby.", "When I die. I want to be frozen. And if they have to freeze me in pieces, so be it. I will wake up stronger than ever, because I will have used that time, to figure out exactly why I died. And what moves I could have used to defend myself better now that I know what hold he had me in.", "The eyes are the groin of the head.", "Powerpoints are the peacocks of the business world; all show, no meat", "Congratulations on your one cousin. I have seventy, each one better than the last!", "All you need is love. False. The four basic human necessities are air, water, food, and shelter.", "My feelings regenerate at twice the speed of a normal man.", "Did you know that the human thumb is formed by 15 interchangeable joints? Wrong. Don’t believe everything that people on television tell you.", "There are 3 things you never turn your back on: bears, men you have wronged, and a dominant male turkey during mating season.", "Why tip someone for a job I’m capable of doing myself? I can deliver food. I can drive a taxi. I can, and do, cut my own hair. I did however, tip my urologist, because I am unable to pulverize my own kidney stones.", "D.W.I.G.H.T – Determined, Worker, Intense, Good worker, Hard worker, Terrific."]

key='Dwight'

def main():
    reddit=praw.Reddit(client_id='CGgcZSqSOD372A',
                       client_secret='_Bs55xvcMAoWdhSIzN0gWMhvwRw',
                       username='Dwight_Bot',
                       password='@littlekidlover',
                       user_agent='idkwhatisthis')

    subreddit = reddit.subreddit("DunderMifflin")
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    if key in submission.title:
        randomfact=random.randint(0,34)
        reply=facts[randomfact]
        submission.reply('So You could not handle my undivided attention. Here is a random Schrute Fact :\n\n'+
                      reply + '\n\nI am Dwight Bot, successor to COMPUTRON.')
        print("Replied to: {}".format(submission.title))


if __name__ == "__main__":
    main()
