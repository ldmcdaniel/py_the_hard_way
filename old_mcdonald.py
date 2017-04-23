# from sys import argv

# script, adjective, noun, animal, noise = argv
print "Give me a noun."
noun = raw_input()
print "Give me an adjective."
adjective = raw_input()
print "Give me an animal."
animal = raw_input()
print "Give me a noise."
noise = raw_input()

eio = "Ee Aye Ee Aye Ohh"

print "%s McDonald had a %s," % (adjective, noun)
print  "%s." % (eio)
print "And on that %s he had a %s, " % (noun, animal)
print  "%s." % (eio)
print "With a %s %s here," % (noise, noise)
print "And a %s %s there." % (noise, noise)
print "Here a %s, there a %s," % (noise, noise)
print "Everywhere a %s %s," % (noise, noise)
print "%s McDonald had a %s," % (adjective, noun)
print  "%s." % (eio)
