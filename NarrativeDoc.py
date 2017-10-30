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
p1R2 = "%s is the best! Ugh, I’m starving right now, I could go for some el tri right now:P whats your fav type of restaurant?" % ShirtLocation
#[I like mexican food also]’/[I really like Italian food, especially pizza!]
p1R3 = "Ugh %s the best! So what's your name gorgeous?" % FoodType
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
p2R3 = "That sounds just fantastic:) We would see a little art, eat some amazing food, see the world. It’d be just like a disney movie. Do you like movies?"
# [I wouldn’t]
p2R4 = "Hey, ouch haha okay I was only kidding;) Okay so you’d go off on your own huh? The lone, stoic hero. Just like batman. Do you like movies?"
# [I love movies]
# [I hate movies]

#

# (Doesn’t like travel): 
p2B2R1 = "Oh that makes sense. Sometimes it’s fun to just be at home relaxing. Are you a fan of cuddling by a nice, hot fireplace and eating [favorite food]?"
# Yeah that sounds awesome
p2B2R2 = "Well I guess we know what we’re doing next weekend!"


No I don’t really like cuddling
What would you most like to do on a date?


# End game, two versions depending on flirty weight.
# Phase 3: 
# If person is liked:




#If person is not liked:



