import random
listNouns = ["bob", "italy", "knife", "book", "bus", "waterfront"]
# random.shuffle(listNouns) # original list is modified
# sample from the original to a new list to preserve
listRandNouns = random.sample(listNouns, len(listNouns))
print(listNouns)
print(listRandNouns)