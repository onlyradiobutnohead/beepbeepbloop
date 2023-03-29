#!/usr/bin/env python

import sys
import wave
from time import sleep

class BeepBeepBloop:
    SOUNDS = [
        "boop", "meow", "crash", "boom!", "woah", "*bass sound*",
        "*big loud noise*", "CRAW", "ZOOOOOOOM", "*scratchy thing*",
        "swoosh", "hazzah!", "*probably like a musical sound maybe?*",
        "*lyrics*", "blap!", "brap", "pewpew", "*gun sounds*", "AAAAAAA",
        "*producer tag*", "bass", "BRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR", "bapbap",
        "bloop", "scarash", "stoop!", "hahahahahaha", "RAAAAAAAA", "blip",
        "brash", "plooosh", "taptap", "HASH", "AAAAAAAAAAAAA", "mnya", "poop",
        "flip", "neigh", "slaaaayyy", "lesssgoooooo", "*more lyrics*", "ssss",
        "zzzzzzzzzz", "zambania", "slunk", "slink", "alm", "WAH", "WOSH",
        "chika chika", "thud", "glitch", "drip", "crackle", "beep",
        "brrrt", "sizzle", "siren", "whirr", "dun dun dun", "chime",
        "yeehaw", "clang", "fizz", "whoosh", "honk", "click",
        "ring ring", "screech", "flute", "thump", "ding", "dong",
        "swoop", "buzz", "pop", "clap", "vroom", "scratch",
        "purr", "clang clang", "howl", "ribbit", "gong", "zap",
        "whistle", "hiss", "moo", "doot", "zap zap", "shimmer",
        "rumble", "thunder", "shing", "bleep", "quack", "gurgle",
        "swish", "whoop", "march", "pitter patter", "twang", "wham",
        "caw", "squeak", "giggle", "sizzle sizzle", "blare", "clink",
        "clickety clack", "plink", "rumble rumble", "twirl", "whir", "pop pop",
        "clang clang clang", "skrrt", "drip drip", "rattle", "snort", "shhh",
        "oink", "thwack", "beep beep", "zippity doo dah", "riff", "hum",
        "toot", "vroom vroom", "kerplunk", "mumble", "hoo", "ding dong",
        "slap", "harp", "ah-OOOO-ga", "swirl", "smack", "zip",
        "rat-a-tat", "squawk", "ring-a-ding-ding", "whomp", "clank", "boing",
        "shuffle", "fart", "zing", "strum", "honk honk", "tap",
        "yodel", "shush", "sputter", "ping", "ribbit ribbit",
        "bloop bloop", "crunch", "wham wham", "whirr whirr", "cha-ching", "snarl",
        "thunk", "flicker", "bang", "shiver", "plunk", "ba-dum-tss",
        "scream", "squish", "squeal", "clatter", "shush shush", "zoom zoom",
        "ding-a-ling", "plop", "whizz", "jingle", "dun dun", "scratch scratch",
        "gurgle gurgle", "rattle rattle", "yip", "chug", "popcorn popping", "chatter",
        "thud thud", "whoosh whoosh", "ding dong ding", "whump", "thwip", "zippity",
        "swat", "pew pew pew", "tick tock", "zoooom zoom", "whine",
        "bam", "sizzle sizzle sizzle", "squeak squeak", "thrum", "splatter", "shh shh",
        "rumble rumble rumble", "ring ring ring", "giggle giggle", "splat", "pound", "scrunch",
        "clink clink", "twinkle twinkle", "bang bang", "swish swish", "rat-a-tat-tat",
        "sploosh", "ka-ching", "snicker", "buzz buzz", "throb", "woof",
        "plip plop", "clomp", "whimper", "tinkle", "tut-tut", "bam bam",
        "whiff", "growl", "crunch crunch", "slurp", "zip zip", "fizz fizz",
        "bump", "thunk thunk", "clash", "whoop whoop", "whirr whirr whirr", "ding ding ding",
        "thud thud thud", "pop pop pop", "scrape", "screech screech", "clop", "woosh woosh",
        "chirp chirp", "hiss hiss", "gargle", "tada", "plink plink", "bang bang bang",
        "twang twang", "tick tick", "clap clap", "moo moo", "whistle whistle", "skid",
    ]
    source = None
    
    def __init__(self, filename):
        self.source = wave.open(filename, "rb")

    def play(self):
        for frame in self.source.readframes(self.source.getnframes()):
            print(self.SOUNDS[frame])
            sleep(0.01)

    def close(self):
        self.source.close()
        
def literally_panic(msg):
    print("fAAAAAAAFLKASDJFAL;SDNVAOSOASDL;FKFJVALVNASOIDFJAOS UH OH")
    print("THIS SHOULDN'T BE HAPPENIGN HELP AAAAAAA WHY IS THIS HAPPENIGN")
    print("THIS IS HAPPENING BECAUSE: lakfkjdaslf ja")
    print(msg.upper())
    print("UH OH NOT GOOD I EXIT NOW")
    exit(1)

def main():
    if len(sys.argv) < 2: # not enuf args
        literally_panic("not enuf args not good :(")

    BeepBeepBloop(sys.argv[1]).play()

if __name__ == '__main__':
    main()
