from genchain import genchain

if __name__ == "__main__":
    print("longest {0}   :- {1}".format("turtle", genchain("turtle")))
    print("shortest {0}  :- {1}".format("turtle", genchain("turtle", min)))
    print("longest {0}   :- {1}".format("aardvark", genchain("aardvark")))
    print("shortest {0}  :- {1}".format("aardvark", genchain("aardvark", min)))
    print("longest {0}   :- {1}".format("tiger", genchain("tiger")))
    print("shortest {0}  :- {1}".format("tiger", genchain("tiger", min)))
    print("longest {0}   :- {1}".format("alligator", genchain("alligator")))
    print("shortest {0}  :- {1}".format("alligator", genchain("alligator", min)))
    print("longest {0}   :- {1}".format("fish", genchain("fish")))
    print("shortest {0}  :- {1}".format("fish", genchain("fish", min)))
    print("longest {0}   :- {1}".format("scorpion", genchain("scorpion")))
    print("shortest {0}  :- {1}".format("scorpion", genchain("scorpion", min)))
    print("longest {0}   :- {1}".format("crocodile", genchain("crocodile")))
    print("shortest {0}  :- {1}".format("crocodile", genchain("crocodile", min)))
