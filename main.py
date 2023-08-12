import random
import time
#To-do list:
#Add: lobster cages/nets, prestige rods
#Working on fishing as of 1/12/22
#Fixed up the bug with inventory. Adding more rods and the ability to buy new ones
"""
FAQ
By me, For me.
When making new:
Rods: Make sure to add it to the rodKWLIST and the Purchasable items lists. Also add it to the fishing chance thing.
Animals: If its a fish, add it to a rod.
New command: Add it to cmdstring AND the help page.
When an item needs to have a level requirement but the class doesn't have one,
just take the lazy way out and add it to the class and set the attributes on the rest
to zero or 1
"""
cd = False
def mysleep(cd, sec):
     if cd:
      time.sleep(sec)
     else:
      time.sleep(0.1)
def fishCd(perms,sec):
     if perms:
      time.sleep(sec)
     else:
      time.sleep(0.1)
def prRed(skk):return"\033[91m{}\033[00m".format(skk)                  #Coloured text options
def prGreen(skk):return"\033[92m{}\033[00m".format(skk)                  #
def prYellow(skk):return"\033[93m{}\033[00m".format(skk)
def prLightPurple(skk):return"\033[94m{}\033[00m".format(skk)
def prPurple(skk):return"\033[95m{}\033[00m".format(skk)
def prCyan(skk):return"\033[96m{}\033[00m".format(skk)
def prLightGray(skk):return"\033[97m{}\033[00m".format(skk)
def prPink(skk):return"\033[95m{}\033[00m".format(skk)
def prBlue(skk):return"\033[34m{}\033[00m".format(skk)
def prBlack(skk):return"\033[98m{}\033[00m".format(skk)
def rarityColours(rarity):
    rarity.lower()
    if rarity == "common":
        return prLightGray("Common")
    if rarity == "uncommon":
        return prGreen("Uncommon")
    if rarity == "rare":
        return prBlue("Rare")
    if rarity == "epic":
        return prPurple("Epic")
    if rarity == "legendary":
        return prYellow("Legendary")
    if rarity == "mythic":
        return prPink("Mythic")
    else:
        return "Ouch Check the RarityColours function."
#print(rarityColours("mythic"))
#print("test" + prOrange("Ooga booga") + "test")
mysleep(cd,1)
print(prCyan("Economy Bot v0.1.9\nRun help for a list of commands"))
mysleep(cd,1)
print(prYellow("Previous update: ")+"Levels now actually work. Check it out with profile")
print(prYellow("Update 0.1.10 Certain items are locked behind levels.")+"\n------------------------------")#last feature added.
mysleep(cd,1)
def help(page):
    print("Economy bot commands:")
    page1 = "Page 1/4\nhelp - Shows you this menu\nwork - Gives you a random task to complete to earn money\nhunt - Allows you to hunt\ninventory - Opens up your inventory\ninv - Abbreviation for inventory\n"
    page2 = "Page 2/4\nbal - Shows your balance\nsell - Sell your hard earned items\nbuy - Allows you to buy an item from the shop\nshop - Check out purchasable items\nfish - Catch fish and other items"
    page3 = "Page 3/4\ninfo - Gives you the details of an item \nupgrade - lets you upgrade fishing rods. Try upgrade rod\nprofile - Gives details regarding your stats\np Abbreviation for profile"
    page4 = "Page 4/4\nCricket noises"
    page = int(page)
    if page == 1:
        print(page1)
    elif page == 2:
        print(page2)
    elif page == 3:
        print(page3)
    elif page == 4:
        print(page4)
    else:
        print("Error Please select a valid page number")
    inp()
def tutorial():
    print("Hello")
    mysleep(cd,1)
    print("Welcome to the fishing simulator")
    mysleep(cd,2)
    print("To help you start off, you've been given a fishing rod for free.")
    mysleep(cd,2)
    print("Typing fish casts your rod out")
    mysleep(cd,2)
    print("You may notice that it takes a while to fish something out")
    mysleep(cd,2)
    print("To speed this up, head over to the shop using shop and purchase a new rod")
    mysleep(cd,3)
    print("Buy a rod using buy followed by the items name. For example, buy angler rod")
    mysleep(cd,3)
    print("Note that purchasing a new rod replaces any previous rods, even if its worse. Be wary.")
    mysleep(cd,4)
    print("Once you start to collect up more fish, you can sell them by using sell. For example, sell carp 4")
    mysleep(cd,4)
    print("Tired of the fish you're catching? Upgrade your rod")
    mysleep(cd,3)
    print("Do this by typing out upgrade rod")
    mysleep(cd,2)
    print("Doing this allows you to catch new types of fish that sell for more as well as other items that would have previously been unobtainable")
    mysleep(cd,5)
    print("Depending on the rarity of fish you catch, you'll gain xp.")
    mysleep(cd,2)
    print("Increase your level to be able to purchase better and gear.")
    mysleep(cd,2)
    print("Happy fishing!")
#tutorial()
def cmdcheck(string):
    string = string.lower()
    if string == "":
      inp()

    elif string == "work":
        work()
        inp()
    elif string == "hunt":
        hunt()
        inp()
    elif string == "bal" or string == "balance":
        inventory.bal()
        inp()
    elif "help" in string:
        if string == "help" or string == "ahelp ":
            string = "help 1"
        page = string[-1]   
        help(page)
        print("Error Did you mean help?")
        inp()
    elif string == "inv" or string == "inventory":
        inventory.inventoryView()
        inp()
    elif "sell" in string:
        amount = string[-1]
        #print(amount,"amount")
        if amount.isdigit():
            amount = int(amount)
        else:
            amount = 1
        #print(inventory.inventory.count(string))
        #print(string, len(string))
        string = string.replace("sell ","") 
        #string = string[:-2]
        #print(string, len(string))
        if amount > 1:
            string = string[:-2]
        animalObject = correct_item(string)
        #print(inventory.inventory.count(animalObject))
        if animalObject == "Invalid":
            print("This item does not exist")
            inp()
        if animalObject not in inventory.inventory:
            pass
        elif inventory.inventory.count(animalObject) < amount:
            #print("Checkpoint 1")
            print(f"You do not own that many {animalObject.name}s")
            inp()
        #print(f"Checkpoint 0: {animalObject}")
        #print(animalObject)
        #print(type(animalObject))
        inventory.sell(animalObject,amount)
        inp()
    elif "buy" in string:
        rodKWList = ["angler","angler rod","phantom","phantom rod","summer","summer rod"]
        string = string.replace("buy ","")
        level = inventory.level
        while len(string) <= 2:
            print("Please specify what you want to purchase")
            inp()
        #print(string)
        string = correct_item(string)
        #print(string)
        #print(string.name)
        if hasattr(string,"Req"):
            #print("Test")
            if level >= string.Req:
                if isinstance(string,Rods):#Item has a requirement and is a rod
                    string.rodPurchase()
                    inp()
                elif isinstance(string,Rods) is False:#Has a req and isn't a rod
                    string.purchase()
                    inp()
            else:
                print(f"The {string.name.capitalize()} is available for purchase at level {string.Req}")
                inp()
        """"
        if string in rodKWList:
            if string == "rod":
                print("Please specify what rod you are buying")
                inp()
            correct_item(string).rodPurchase()
            inp()
        string = correct_item(string)
        if string == "Invalid":
            print("Item does not exist")
            inp()"""
        if string not in purchasable_products:
            print("This item is not for sale")
            inp()
            #string.purchase()
        inp()
    elif "fish" in string:
        findRod().fish()
        inp()
    elif "shop" in string:
        shop()
        inp()
    elif "info" in string:
        string = string.replace("info ","")
        itemInfo(correct_item(string))
        inp()
    elif "upgrade" in string:
        string = string.replace("upgrade ","")
        correct_item(string).upgrade_check()
        inventory.earnXP(10)
        inp()
    elif "profile" in string or "p" in string:
        inventory.profile(inventory.level)
        inp()
    elif "toutorial" in string or "tutorial" in string:
        tutorial()
    elif "getrich" in string:
        inventory.cash = 10000
        inp()
    elif "setlevel" in string:
        string = string.replace("setlevel ","")
        inventory.level = int(string)
        inp()
    elif "net" in string or "cast" in string:
        findNet().catch(findNet().durability)
        inp()
    else:
        print("Error Unknown command")
        inp()
class Animals:
    def __init__(self,name,value,info,level,rarity):
        self.name = name
        self.value = value
        self.info = info
        self.level = level
        self.rarity = rarity
    def __repr__(self):
        return f"{self.name}"
class Inventory:
    def __init__(self): 
        self.inventory = []
        self.cash = 0
        self.belt = []
        self.exp = 0
        self.level = 1
    def myLevel(self):
        counter = self.level
        xp = self.exp   #XPSUB is the amount of xp needed for the next level. 
        #print(f"myLevel checkpoint. self.exp = {self.exp}")
        xpsub = 0
        #print(f"Checkpoint 1: {xpsub} ")
        while xp > xpsub:
            #print("1 Cycle")
            if self.level < 10:
                xpsub = self.level+1
                xpsub*=10
                #print(f"Checkpoint 2:xpsub= {xpsub} ")
                #nextLevel = self.level+1
            else:
                xpsub = 100
            #print(f"xpsub = {xpsub} vs xp = {xp}")
            if self.exp < xpsub:
                #print("pass")
                pass
            if self.exp > xpsub:
                #print(f"xp = {xp} vs xpsub = {xpsub}")
                #print(f"Checkpoint 3:xp {xp} ")
                #print(f"Checkpoint 4: level= {self.level} ")
                self.exp -= xpsub
                #print(f"self.exp = [self.exp]")
                #print(f"xpsub: {xpsub}")
                xpsub=0
                #print(f"xp: {xp}")
                self.level+= 1
                print(prGreen("LEVEL UP "))
                print(f"You are now level {self.level}")
                xpsub = 0
    def earnXP(self,amount):
        #print(f"EarnXP checkpoint: self.exp = {self.exp} amount = {amount}")
        self.exp += amount
    def inventoryView(self):
        print("Your inventory:")
        inv = self.inventory
        unique = set(inv)
        for item in unique:
            count=0
            for x in range(0,len(inv)):
                if item == inv[x]:
                    count+=1
            if isinstance(item,Rods):
                print(fr"- [lvl {item.level}] {item.name}")
            else:
                print(f"- {item.name.capitalize()} x{count}")
    def add(self,animal):
        self.inventory.append(animal)
    def sell(self,animal,amount):
        if animal in self.inventory:
            for x in range(0,amount):
                self.cash += animal.value
                self.inventory.remove(animal)
            if amount == 1:
                print(f'Sold {animal.name} for {animal.value}')
            else:
                print(fr'Sold {amount} {animal.name}(s) for ${animal.value*amount}')
        else:
            print(f'You do not own this')
    def bal(self):
        print(f"You have ${self.cash} to your name")
    def profile(self,level):
        if level < 10:
            nextLevel = level+1
            nextLevelXp = nextLevel*10
        else:
            nextLevel = level+1
            nextLevelXp = nextLevel*100
        print("Your profile:")
        print(f"Balance: {self.cash}")
        print(f"{self.level} -----> {self.level +1}")
        #print(f"Progress to level {self.level + 1}")
        print(f"{self.exp}/{nextLevelXp} XP")
        #Progress Bar
        percentage = self.exp/nextLevelXp *100
        #ercentage *=100
        percentage = int(round(percentage))
        #print(percentage)
        if 0 <= percentage < 11:
            print(prRed(f"▰▱▱▱▱▱▱▱▱▱  \n")+ f"{percentage}% Complete")
        elif 10 <= percentage < 21:
            print(prRed(f"▰▱▱▱▱▱▱▱▱▱  \n")+ f"{percentage}% Complete")
        elif 20 <= percentage < 31:
            print(prRed(f"▰▰▱▱▱▱▱▱▱▱  \n")+ f"{percentage}% Complete")    
        elif 30 <= percentage < 41:
            print(prRed(f"▰▰▰▱▱▱▱▱▱▱  \n")+ f"{percentage}% Complete")  
        elif 40 <= percentage < 51:
            print(prRed(f"▰▰▰▰▱▱▱▱▱▱  \n")+ f"{percentage}% Complete")    
        elif 50 <= percentage < 61:
            print(prRed(f"▰▰▰▰▰▱▱▱▱▱  \n")+ f"{percentage}% Complete")    
        elif 60 <= percentage < 71:
            print(prRed(f"▰▰▰▰▰▰▱▱▱▱  \n")+ f"{percentage}% Complete")    
        elif 70 <= percentage < 81:
            print(prRed(f"▰▰▰▰▰▰▰▱▱▱  \n")+ f"{percentage}% Complete")    
        elif 80 <= percentage < 91:
            print(prRed(f"▰▰▰▰▰▰▰▰▱▱  \n")+ f"{percentage}% Complete")    
        elif 90 <= percentage <= 100:
            print(prRed(f"▰▰▰▰▰▰▰▰▰▱  \n")+ f"{percentage}% Complete")    
        else:
            print("Error Check the profile function.")
inventory = Inventory()
#inventory.myLevel(inventory.exp)
inventory.cash = 1000
#inventory.profile(inventory.level)
fox = Animals("fox",110,"A humble fox",1,"common")#                          Animals for the hunting function
deer = Animals("deer",90,"A humble deer",1,"common")
boar = Animals("boar",130,"A humble boar",1,"common")
rabbit = Animals("rabbit",160,"A humble rab,bit",1,"common")
animalList = [deer, fox, boar, rabbit]
inventory.add(fox)#110
inventory.add(fox)#110
inventory.add(boar)#130, total is 350
def correct_item(item):
    item = item.lower()
    Objects = {
        "fox":fox,
        "deer":deer,
        "boar":boar,
        "carp":carp,
        "perch":perch,
        "sockeye_salmon":sockeye_salmon,
        "salmon":sockeye_salmon,
        "sockeye":sockeye_salmon,
        "sockeye salmon":sockeye_salmon,
        "trout":trout,
        "gem":gem,
        "phantom rod":phantom_rod,
        "phantom":phantom_rod,
        "bone":bone,
        "sturgeon":sturgeon,
        "test rod":testrod,
        "angler":angler_rod,
        "angler rod":angler_rod,
        "basic rod":basic_rod,
        "basicrod":basic_rod,
        "summer rod":summer_rod,
        "summer":summer_rod,
        "rod":findRod(),
        "basic net":basic_net,
        "nylon net":nylon_net,
        "nylon":nylon_net,
        "net":basic_net
    }
    if item in Objects:
        #print("Success",Objects[item])
        return Objects[item]
    else:
        return "Invalid"
def hunt():
        global animalList
        hunting = random.choices(animalList, weights=(40,25,25,10), k=1)
        print("You hear the slight rustle of leaves to your left..")
        mysleep(cd,3)
        print("Silently, you ready yourself as you search for movement")
        mysleep(cd,3)
        print("CRACK")
        mysleep(cd,2)
        print("Your 7mm flies straight into the skull of a", hunting[0])
        inventory.add(hunting[0])
        print("Added", hunting[0], "to your inventory")
def inp():
    inp = input("")
    cmdcheck(inp)
def work():
    workList = ["You actually finished the plate of vegetables that your parents made you eat",
        "You work as a voice actor for SpongeBob", "You stack cups at 7-11 for 8 hours a day",
        "Someone came and performed a play. They paid you for watching"]
    a = int(random.randint(0,4))
    if a == 4:
        job1()
    else:
        cash = random.randint(10,50)
        inventory.cash += cash
        print(f"{workList[a]} and you earn ${cash}")
        inp()
def job1():
    print("Bonus Work \nType out the following in under 10s \nwould you like some fries with that?")
    ans = str(input(""))
    task1 = "Would you like some fries with that?"
    check(ans,task1)
    inp()
def check(ans,task):
    ans = ans.lower()
    task = task.lower()
    if ans == task:
        cash = random.randint(70,150)
        inventory.cash += cash
        print(f"Not to shabby.. Heres ${cash}")
        inp()
    else:
        cash = random.randint(10,50)
        inventory.cash += cash
        print(f"You failed miserably\nHeres a pity payment of ${cash}")
        inp()
carp = Animals("carp",40,"This vegetarian fish leads a simple, healthy life.",1,rarityColours("common"))#                                  <---- Fishies
sockeye_salmon = Animals("sockeye salmon",30,"This competitive fish is always ready for a race up the river.",1,rarityColours("common"))#                             <----
perch = Animals("perch", 20,"This introvert fish enjoys the calm atmosphere of still waters.",2,rarityColours("common"))
sturgeon = Animals("sturgeon",50,"This big fish has thick skin. Nip and bite all you like, he doesn't care",2,rarityColours("common"))
trout = Animals("trout",60,"A true pioneer, this fish has dreamed of conquering new lakes ever since its youth.",3,rarityColours("uncommon"))
seabass = Animals("seabass",75,"The mild taste of Sea Bass lends to it's popularity and versatility.",3,"uncommon")
haddock = Animals("haddock",85,"A member of the cod family witha mild flavour, firm flesh and moist texture.",3,"uncommon")
fishList = [perch,sockeye_salmon,carp,sturgeon]
fishNames = [perch.name,sockeye_salmon.name,carp.name,sturgeon.name]
#class Animals:
    #def __init__(self,name,value):
        #self.name = name
        #self.value = value
    #def __repr__(self):
        #return f"{self.name}"
class Rods:
    tier1= [carp,sockeye_salmon]
    tier2 = [perch,sockeye_salmon,carp]
    inventory = inventory.inventory
    def __init__(self,name,tier,price,info,level,Req):
        self.level = level
        self.tier = tier
        self.name = name
        self.value = price
        self.info = info
        self.Req = Req
    def fishable_fish(self,level):
            level = int(level)
            if level == 1:
                return Rods.tier1
            elif level == 2:
                return Rods.tier2
    def fishing(self,rod_level):
        pass
    def catchXP(self,fish):
        fishLvl = fish.level
        if 0 < fishLvl <= 2:#H = 13
            xpadd = fishLvl*7
            xpadd += 3
            #print(xpadd)
            return xpadd
        elif 2 < fishLvl <= 5:#H = 23
            xpadd = fishLvl*6
            xpadd += 3
            #print(xpadd)
            return xpadd
        elif 5 < fishLvl <= 7:#H = 27 L = 24
            xpadd = fishLvl*5
            xpadd += 6
            #print(xpadd)
            return xpadd
        elif 9 < fishLvl <= 10:
            xpadd = fishLvl*5
            xpadd += 20
            #print(xpadd)
            return xpadd
        else:
            print("Error in the catchXP function. fix plz")
    def fish(self):
        tiers = {1:{'fish':[carp,sockeye_salmon], 'weights':(60, 40)},
         2:{'fish':[carp,sockeye_salmon,perch,bone], 'weights':(25, 50, 20,5)},3:{"fish":[sockeye_salmon,perch, sturgeon,bone],'weights':(20, 47, 25,8)},
         4:{"fish":[sockeye_salmon,perch, sturgeon,bone,trout],'weights':(1, 50, 30,10,9)}}
        catch = random.choices(tiers[self.tier]['fish'], weights = tiers[self.tier]['weights'], 
                       k=1)[0]
        inventory.earnXP(self.catchXP(catch))
        inventory.add(catch)
        print(f"You've reeled in a {catch.name}")
        inventory.myLevel()
    def rodPurchase(self):
        if inventory.cash < self.value:
            print("You cannot afford this")
        else:
            for item in inventory.inventory:
                if isinstance(item,Rods):
                    inventory.inventory.remove(item)
            inventory.cash -= self.value
            print(f"You have purchased a {self.name}")
            inventory.add(self)
    def upgrade_check(self):
        upgrade_cost = self.level*1.9
        upgrade_cost *= self.tier
        upgrade_cost *= 100
        #print(inventory.cash)
        if upgrade_cost < inventory.cash:
            #print(f"This costs ${upgrade_cost}\nRun again to confirm")
            #answer = input("")
            #if answer.lower() == "upgrade rod":
                #pass
            #else:
                #print("Upgrade cancelled")
                #inp()
            inventory.cash -= upgrade_cost
            self.upgrade()
        else:
            print(f"You cannot afford this")
    def upgrade(self):
        upgrade_time = self.tier*self.level*5
        self.level += 1
        print(f"Your {self.name} is now level {self.level}")
basic_rod = Rods("basic rod",1,1,"A basic rod capable of catching:\n- Carp\n- Salmon",1,1)
phantom_rod = Rods("Phantom rod",1,100,"A spooky rod capable of catching:\n- Carp\n- Salmon\n- Perch\nBones..?",1,3)
summer_rod = Rods("Summer rod",2,250,"A rod best used in the summer",1,6)
angler_rod = Rods("Angler rod",2,400,"Perfect for light fishing",1,10)
testrod = Rods("test rod",1,100,"Rod used to test upgrading",1,1)
#testrod.upgrade_check()
#inventory.add(testrod)
inventory.add(basic_rod)
class Product:
    def __init__(self,name,value,info,rarity,Req):
        self.name = name
        self.value = value
        self.info = info
        self.rarity = rarity
        self.Req = Req
    def info(self):
        print(f"[{self.rarity}]{self.name}\nValue: {self.value}")
    def infInfo(self):
        print(f"{self.name}")
    def purchase(self):
        if inventory.cash < self.value:
            print("You cannot afford this")
        else:
            inventory.cash -= self.value
            print(f"You have purchased 1 {self.name}")
            inventory.add(self)
gem = Product("gem",50,"A fancier way to store money","common",1)
bone = Product("bone",100,"Looks old..","common",1)
inventory.add(gem)
def findRod():
    for item in inventory.inventory:
        if isinstance(item,Rods):
            return item
def sortedinv():
    finalList = []
    inv = inventory.inventory
    unique = set(inv)
    for item in unique:
        count=0
        for x in range(0,len(inv)):
            if item == inv[x]:
                count+=1
        print(f"- {item.name.capitalize()} x{count}")
    #print(finalList)

    """print("Welcome to the shop\nRun buy item to purchase something")
    for x in range(0,len(purchasable_products)):
        if isinstance(purchasable_products[x],Rods):
            print(f"{purchasable_products[x].name.capitalize()} - ${purchasable_products[x].value}")
        else:
            print(f"[{rarityColours(purchasable_products[x].rarity)[5].capitalize()}] {purchasable_products[x].name.capitalize()} - ${purchasable_products[x].value}")
"""
def itemInfo(item):
  if isinstance(item,Rods):#Is rod no req
      print(f"{item.name.capitalize()}\nValue: ${item.value}\n{item.info}")
  elif hasattr(item,"Req") and isinstance(item,Rods) is False:
      print(f"{item.name.capitalize()}\nUnlocked at level {item.Req}\nValue: ${item.value}\n{item.info}")
  else:
      print(f"[{item.rarity}] {item.name.capitalize()}\nValue: ${item.value}\n{item.info}")



class Nets:
    def __init__(self,name,value,tier,durability,rarity,Req,info):
        self.name = name
        self.value = value
        self.tier = tier
        self.durability = durability
        self.Req = Req
        self.rarity = rarity
        self.info = info
        
    def catch(self,origDura):
        print(origDura)

        tempCatch = []
        tiers = {1:{'fish':[carp,sockeye_salmon], 'weights':(60, 40)},
         2:{'fish':[carp,sockeye_salmon,perch,bone], 'weights':(25, 50, 20,5)},3:{"fish":[sockeye_salmon,perch, sturgeon,bone],'weights':(20, 47, 25,8)},
         4:{"fish":[sockeye_salmon,perch, sturgeon,bone,trout],'weights':(1, 50, 30,10,9)}}
        
        for x in range(0,random.randint(3,5)):
            catch = random.choices(tiers[self.tier]['fish'], weights = tiers[self.tier]['weights'], 
                       k=1)[0]
            #inventory.earnXP(self.catchXP(catch))
            inventory.add(catch)

            tempCatch.append(catch)
        #print(tempCatch)
        
        unique = set(tempCatch)
        counts = ', '.join([f"x{tempCatch.count(item)} {item.name.capitalize()}" for item in unique])
        counts = counts[::-1].replace(',', 'dna ', 1)[::-1]
        self.durability -= 1
        if self.durability == 0:
            inventory.inventory.remove(self)
            print("Your net tore and is no longer usable")
            self.durability = origDura
        else:
            print(f"You netted {counts}\nYour net now has {self.durability} durability left")
        
    def purchase(self):
        if inventory.cash < self.value:
            print("You cannot afford this")
        else:
            inventory.cash -= self.value
            print(f"You have purchased 1 {self.name}")
            inventory.add(self)
def findNet():
    for item in inventory.inventory:
        if isinstance(item,Nets):
            return item
    else:
        print("You do not own a net! Purchase one from the shop")
        inp()

basic_net = Nets("Basic Net",50,1,5,rarityColours("common"),4,"A lightweight and durable tool for catching small fish.")
nylon_net = Nets("Nylon Net",150,3,10,rarityColours("epic"),8,"A heavy-duty and high-quality tool for catching larger fish, perfect for serious anglers")

#inventory.add(basic_net)
purchasable_products = [gem,phantom_rod,basic_net,summer_rod,angler_rod,nylon_net]
purchasable_products.sort(key=lambda x: x.Req)
def shop():
    level = inventory.level
    #print(f"Level = {inventory.level}")
    for x in range(0,len(purchasable_products)):
        item = purchasable_products[x]
        if hasattr(item,"Req"):
            #print(f"Phase 1")
            #print(item.Req)
            if level >= item.Req:                
                if isinstance(purchasable_products[x],Rods):#Item has a requirement and is a rod
                    print(f"{purchasable_products[x].name.capitalize()} - ${purchasable_products[x].value}")
                elif isinstance(purchasable_products[x],Rods) is False:
                    print(f"[{rarityColours(purchasable_products[x].rarity)[5].capitalize()}] {purchasable_products[x].name.capitalize()} - ${purchasable_products[x].value}")
            else:
                print(f"[Unlocked at level {item.Req}] ???...? - $???")
        #elif hasattr(item,"Req") is False and isinstance(purchasable_products[x],Rods) is False:#Item has no requirement and isn't a rod
           # print(f"[{rarityColours(purchasable_products[x].rarity)[5].capitalize()}] {purchasable_products[x].name.capitalize()} - ${purchasable_products[x].value}")
        elif hasattr(item,"Req") is False and isinstance(item,Rods) is False and isinstance(item,Nets) is False:#Item has no requirement and isn't a rod
            print(f"{item.name} got here")
            print(f"[{rarityColours(purchasable_products[x].rarity)[5].capitalize()}] {purchasable_products[x].name.capitalize()} - ${purchasable_products[x].value}")
        else:
            print("How did we get here? Check the shop function.")

#cmdcheck("inv")
#basic_net.catch()
#basic_net.catch()
#shop()
#print(inventory.inventory)
    #def networth(self):
        #inv = self.inventory
        #unique = set(inv)
       # total = 0
       # print("a")
        #for item in unique:
            #count=0 
            #for x in range(0,len(inv)):
                #print("b")
                #if item == inv[x]:                                    Inventory networth concept. Put it in the "Inventory" class.
                    #count+=1                                          Current issue is something to do with the rods instance on
                    #total += count*item.value
                    #print(f"Total 1: {total}")
            #if isinstance(item,Rods):                                 this line here. Date is 25/03/23, Saturday, 8:51PM
                #pass
            #else:
                #total += item.value
                #print(f"Total 2: {total}")
        #print("c")
#To execute a command without typing it, put it in the cmdcheck parameter   
#cmdcheck("setlevel 5")
#cmdcheck("shop")
cmdcheck("setlevel 10")
#cmdcheck("getrich")
#cmdcheck("shop")
inp()
