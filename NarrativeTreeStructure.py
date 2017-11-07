# coding: utf-8



class Node:
	positiveLink = None
	negativeLink = None
	name = None
	sentence = ""

	def __init__(self, posLink, negLink, name, content):
		self.positiveLink = posLink
		self.negativeLink = negLink
		self.name = name
		self.sentence = content


# BaeBot Narrative Structure

name = "Lover Boy"
foodType = "Italian"
shirtLocation = "American Eagle"
occupation = "Vigilante"

Opening1 = "Hey baby, come here often?"
Opening2 = "Hey there hot stuff, whatchya doin tonight?"
Opening3 = "Hey lover, whats going on?"


# Phase 1 is about lighter, getting to know you questions. We could store this information and use it in later phases
# Phase 1:
p1R1 = "Oh thats interesting: I like your shirt btw, where did you get it?"
#[possible response: I got it at American Eagle.]
p1R2 = "%s is the best! Ugh, I’m starving right now, I could go for some el tri right now:P whats your fav type of restaurant?" % shirtLocation
#[I like mexican food also]’/[I really like Italian food, especially pizza!]
p1R3 = "Ugh %s the best! So what's your name gorgeous?" % foodType
#[Name]
p1R4 = "%s! Ah, thats fits you perfectly;) so are you a student or you been working? You seem like the kind of person who knows how to work it." % name
#[Haha, ya I’m a student! Hbu?]/[I’m a computer science professor and I used to be a lawyer.]
p1R5 = "Oh that’s cool, Being a %s sounds really fun. I’m kind of between things myself. I wanna go travel around, you know? Do you like travel?" % occupation
#[No, I’m really more of a homebody myself]


# This is where the stronger narrative elements come in. Really lead the convo, use some information gleaned in Phase 1.
# Phase 2 (likes travel): 
p2B1R1 = "Oh brilliant;) How would you like to travel around Europe with me for a month? Haha, jk!! Okay, imagine you walked away from your life right now and ran away. Idk, could you ever imagine yourself doing something crazy like that?"
# [Idk maybe, yes, no]
p2R2 = "I know its kinda scary, but maybe a little fun?;) where would you take me?"
# [I would take you to venice]
p2R3 = "That sounds just fantastic:) We would see a little art, eat some amazing food, see the world. What should I pack?"
# [I wouldn’t]
p2R4 = "Hey, ouch haha okay I was only kidding;) We don't have to go on a big adventure right away. I mean, we just met. How about we go to the movies instead. Do you like movies?"
# [Sure]
p2R4B1 = "Oh great! What's your fave movie?"
p2R4B1Easter = "Oh great! I love Sharknado. What do yout think of it?"
# [get movie name, go to phase 3 and say let's watch that this weekend]
# [I hate movies]
p2R4B2 = "Oooh. So are you more of a book person?"
#yes
p2R4B2B1 = "I love books too. What kind of books do you like? Do you like 50 shades of gray? ;) That's my fantasy."
#yes: PHASE
#no
p2R4B2B2 = "So what do you like then?"
#no matter what you hear

# (Doesn’t like travel): 
p2B2R1 = "Oh that makes sense. Sometimes it’s fun to just be at home relaxing. Are you a fan of cuddling by a nice, hot fireplace and eating your favorite food?"
# Yeah that sounds awesome
p2B2R1B1 = "Well I guess we know what we’re doing next weekend;)!"
#no, I like cold



# End game, two versions depending on flirty weight.
# Phase 3: 
# If person is liked:
p3e1 = "Unnnghh come to my place;)"



#If person is not liked:
p3e2 = "Oh. That's soooo interesting but look at the time. <YAAAAWNS>. I gotta go to bed. See ya."


structure = []

def assignStructure():
	structure = []
	structure.append(Node(None, None, 'p3e2', p3e2)) 
	structure.append(Node(None, None, 'p3e1', p3e1))

	structure.append(Node('p3e2', 'p3e2', 'p2R4B2B2', p2R4B2B2))
	structure.append(Node('p3e1', 'p3e1', 'p2B2R1B1', p2B2R1B1))
	structure.append(Node("p2B2R1B1", "p2B2R1B1", 'p2B2R1', p2B2R1))
	


	structure.append(Node('p3e1', 'p3e1', 'p2R4B2B1', p2R4B2B1))
	structure.append(Node("p2R4B2B1", "p2R4B2B2", 'p2R4B2', p2R4B2))
	structure.append(Node("p3e1", "p3e1", 'p2R4B1', p2R4B1))
	structure.append(Node("p2R4B1", "p2R4B2", 'p2R4', p2R4))
	structure.append(Node("p3e1", "p2R4", 'p2R3', p2R3))
	structure.append(Node("p2R3", "p2R3", 'p2R2', p2R2))
	structure.append(Node("p2R2", "p2R2", 'p2B1R1', p2B1R1))


	structure.append(Node("p2B1R1", 'p2B2R1', 'p1R5', p1R5))
	structure.append(Node("p1R5", "p1R5", 'p1R4', p1R4))
	structure.append(Node("p1R4", "p1R4", 'p1R3', p1R3))
	structure.append(Node("p1R3", "p1R3", 'p1R2', p1R2))
	structure.append(Node("p1R2", "p1R2", 'p1R1', p1R1))

	return structure

	




