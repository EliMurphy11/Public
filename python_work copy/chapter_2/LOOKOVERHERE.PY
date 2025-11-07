# create code to guess a random name based on yes or no questions about the name and its letters
names = {"aaron ", "abby ", "abigail ", "adam ", "adrian ", "aiden ", "alex ", "alexander ", "alice ", "amelia ", "andrew ", "angel ", "anna ", "anthony ", "ariana ", "arthur ", "ashley ", "asher", "aubrey ", "audrey ", "ava ", "barbara ", "benjamin ", "bethany ", "brian ", "brianna ", "brooke ","poop", "caleb ", "cameron ", "caroline ", "charles ", "charlotte ", "chloe ", "christopher ", "claire ", "clara ", "cole ", "colin ", "colton ", "connor ", "daniel ", "david ", "dylan ", "elijah ", "elizabeth ", "ella ", "emily ", "elijah", "emma ", "ethan ", "eva ", "evan ", "evelyn ", "gabriel ", "george ", "grace ", "hannah ", "harper ", "henry ", "isaac ", "isabella ", "jackson ", "jacob ", "james ", "jasmine ", "jason ", "jayden ", "jeffrey ", "joseph", "jennifer ", "jeremy ", "jessica", "kylie ", "lauren ", "leah ", "liam ", "lillian ", "lily ", "logan ", "lucas ", "madison ", "maria ", "mark ", "mary ", "mason ",  "matthew ", "megan ", "michelle ", "michael ", "morgan ", "nathan ", "nicholas ", "olivia ", "owen ", "paul ", "peter ", "rachel ", "rebecca ", "ryan ", "samantha ", "samuel ", "sarah ", "savannah ", "scarlett ", "sean ", "sophia ", "sophie ", "steven ", "sydney",  "taylor",  "thomas",  "tyler",  "victoria",  "william",  "zachary", "zoe", "zara", "yara", "xander", "wanda", "vicky", "uma", "tina", "sue", "rose", "quinn", "penny", "olga", "nina", "molly", "luna", "karen", "julia", "iris", "hilda", "grace", "fiona", "eva", "dora", "cora", "bella", "anna", "amy", "paige", "nora", "lily", "june", "ivy", "hope", "gina", "ella", "daisy", "clara", "bella", "ava", "anna", "alma", "zoe", "yara", "xena", "willa", "viva", "tessa", "sara", "ruth", "quinn", "piper", "olga", "nina", "mira", "luna", "kira", "juno", "iris", "hanna", "grace", "faye", "dana", "cora", "belle", "aria", "amy", "zara", "yara", "xena", "willa", "viva", "tessa", "sara", "ruth", "quinn", "piper", "olga", "nina", "mira", "luna", "kira", "juno", "iris", "hanna", "grace", "faye", "dana", "cora", "belle", "aria", "amy", "zara", "yara", "xena", "willa", "viva", "tessa", "sara", "ruth", "quinn", "piper", "olga", "nina", "mira", "luna", "kira", "juno", "iris", "hanna", "grace", "faye", "dana", "cora", "belle", "aria", "amy", "mia", "max", "leo", "kai", "ivy", "eve", "dax", "bea", "ash", "zane", "yves", "xan", "wren", "vex", "tess", "sloane", "rue", "pax", "oak", "nova", "neve", "lux", "lark", "jade", "iris", "hope", "finn", "eve", "drew", "cove", "bryn", "blair", "ash", "zane", "yves", "xan", "wren", "vex", "tess", "sloane", "rue", "pax", "oak", "nova", "neve", "lux", "lark", "jade", "iris", "hope", "finn", "eve", "drew", "cove", "bryn", "blair", "ash", "zane", "yves", "xan", "wren", "vex", "tess", "sloane", "rue", "pax", "oak", "nova", "neve", "lux", "lark", "jade", "iris", "hope", "finn", "eve", "drew", "cove", "bryn", "blair", "ash", }
questions = [ "Is the name a common name?",
              "Is the name a unique name?",
              "Is the name a trendy name?",
              "Is the name a classic name?",
              "Is the name a celebrity name?",
              "Is the name a short name?",
              "Is the name a long name?",
              "Is the name a modern name?",
              "Is the name a vintage name?",
              "Is the name a fictional name?"
              "is the name a biblical name?",
              "is the name a royal name?",
                "is the name a unisex name?",
                "is the name a nature-inspired name?",
                "is the name a mythological name?",
                "is the name a literary name?",
                "is the name a musical name?",
                "is the name a historical name?",
                "is the name a geographical name?",
                "is the name a color-inspired name?,",
                "is the name a food-inspired name?",
                "is the name a flower-inspired name?",
                "is the name a gemstone-inspired name?",
                "is the name a celestial name?",
                "is the name a seasonal name?",
                "is the name a holiday name?",
                "is the name a futuristic name?",
                "is the name a traditional name?",]
answers = {}
for i, q in enumerate(questions, 1):
    ans = input(f"Q{i}: {q} (yes/no): ").strip().lower()
    answers[q] = ans
    if ans not in ['yes', 'no']:
        print("Please answer with 'yes' or 'no'.")
        ans = input(f"Q{i}: {q} (yes/no): ").strip().lower()
        answers[q] = ans

    # Apply filtering based on the question and answer
    if q == "Is the name a common name?":
        if ans == 'yes':
            names = {name for name in names if len(name.strip()) <= 5}
        elif ans == 'no':
            names = {name for name in names if len(name.strip()) > 5}
    elif q == "Is the name a unique name?":
        if ans == 'yes':
            names = {name for name in names if len(name.strip()) > 7}
        elif ans == 'no':
            names = {name for name in names if len(name.strip()) <= 7}
    elif q == "Is the name a trendy name?":
        if ans == 'yes':
            names = {name for name in names if name.strip().endswith('a') or name.strip().endswith('y')}
        elif ans == 'no':
            names = {name for name in names if not (name.strip().endswith('a') or name.strip().endswith('y'))}
    elif q == "Is the name a classic name?":
        classic_names = {"john", "mary", "james", "patricia", "robert", "jennifer", "michael", "linda","william", " elizabeth", "david", "barbara", "richard", "susan", "joseph", "jessica", "thomas", "sarah", "charles", "karen", "christopher", "nancy", "daniel", "lisa", "matthew", "betty", "anthony", "dorothy", "mark", "helen", "donald", "sandra", "paul", "ashley", "steven", "kimberly", "andrew", "emily", "joshua", "donna", "kenneth", "michelle", "kevin", "carol", "brian", "amanda", "george", "melissa", "edward", "deborah","adam", "eve", "noah", "moses", "david", "asher"}
        if ans == 'yes':
            names = {name for name in names if name.strip().lower() in classic_names}
        elif ans == 'no':
            names = {name for name in names if name.strip().lower() not in classic_names}
    elif q == "Is the name a celebrity name?":
        celebrity_names = {"beyonce", "rihanna", "madonna", "drake", "adele", "brad pitt", "angelina jolie", "tom cruise", "scarlett johansson", "chris hemsworth"}
        if ans == 'yes':
            names = {name for name in names if name.strip().lower() in celebrity_names}
        elif ans == 'no':
            names = {name for name in names if name.strip().lower() not in celebrity_names}
    elif q == "Is the name a short name?":
        if ans == 'yes':
            names = {name for name in names if len(name.strip()) <= 4}
        elif ans == 'no':
            names = {name for name in names if len(name.strip()) > 4}
    elif q == "Is the name a long name?":
        if ans == 'yes':
            names = {name for name in names if len(name.strip()) > 7}
        elif ans == 'no':
            names = {name for name in names if len(name.strip()) <= 7}
    elif q == "Is the name a modern name?":
        modern_names = {"aiden", "jayden", "kaylee", "madison", "mason", "olivia", "luna", "kai", "nova", "zephyr", "xander"}
        if ans == 'yes':
            names = {name for name in names if name.strip().lower() in modern_names}
        elif ans == 'no':
            names = {name for name in names if name.strip().lower() not in modern_names}
    elif q == "Is the name a vintage name?":
        vintage_names = {"edward", "mildred", "harold", "betty", "frank", "doris", "arnold", "thelma", "gerald", "agnes", "maude"}
        if ans == 'yes':
            names = {name for name in names if name.strip().lower() in vintage_names}
        elif ans == 'no':
            names = {name for name in names if name.strip().lower() not in vintage_names}
    elif q == "Is the name a fictional name?":
        fictional_names = {"frodo", "harry", "hermione", "katniss", "legolas", "gandalf", "aragorn", "daenerys", "tyrion", "bilbo"}
    elif q == "is the name a biblical name?":
        biblical_names = {"adam", "eve", "noah", "moses", "david", "asher", "abraham", "sarah", "isaac", "rebecca", "jacob", "rachel", "joseph", "mary", "jesus", "peter", "paul"}
    elif q == "is the name a royal name?":
        royal_names = {"elizabeth", "charles", "diana", "william", "harry", "kate", "george", "victoria", "henry", "catherine", "edward", "anne", "james", "mary", "arthur", "alice", "charlotte", "louis", "sophie", "eugenie", "beatrice"}
    elif q == "is the name a unisex name?":
        unisex_names = {"alex", "jordan", "taylor", "casey", "morgan", "riley", "jamie", "dakota", "skyler", "quinn", "blake", "cameron", "devon", "drew", "harper", "peyton", "reese", "rowan", "sawyer", "sydney"}
    elif q == "is the name a nature-inspired name?":
        nature_names = {"river", "willow", "sky", "autumn", "luna", "forest", "meadow", "ocean", "rain", "sage"}
    elif q == "is the name a mythological name?":
        mythological_names = {"zeus", "hera", "apollo", "athena", "thor", "loki", "freya", "osiris", "anubis", "ra"}
    elif q == "is the name a literary name?":
        literary_names = {"atticus", "heathcliff", "gatsby", "darcy", "hamlet", "ophelia", "juliet", "romeo", "scrooge", "pip"}
    elif q == "is the name a musical name?":
        musical_names = {"lyric", "melody", "aria", "harmony", "cadence", "allegro", "forte", "piano", "sonata", "rhapsody",}
    elif q == "is the name a historical name?":
        historical_names = {"cleopatra", "napoleon", "joan", "alexander", "genghis", "caesar", "catherine", "elizabeth", "washington", "lincoln", "galileo", "newton", "tesla", "curie", "franklin", "darwin", "mandela", "gandhi", "churchill", "roosevelt", "jefferson", "king", "queen"}
    elif q == "is the name a geographical name?":
        geographical_names = {"asia", "india", "brooklyn", "sierra", "dakota"}
    elif q == "is the name a color-inspired name?":
        color_names = {"violet", "indigo", "scarlett", "jade", "amber"}
    elif q == "is the name a food-inspired name?":
        food_names = {"olive", "peach", "saffron", "clementine", "sage"}
    elif q == "is the name a flower-inspired name?":
        flower_names = {"rose", "lily", "daisy", "violet", "jasmine"}
    elif q == "is the name a gemstone-inspired name?":
        gemstone_names = {"ruby", "jade", "pearl", "amber", "opal"}
    elif q == "is the name a celestial name?":
        celestial_names = {"luna", "nova", "stella", "orion", "celeste"}
    elif q == "is the name a seasonal name?":
        seasonal_names = {"summer", "autumn", "winter", "spring", "january"}
    elif q == "is the name a holiday name?":
        holiday_names = {"noel", "christmas", "easter", "halloween", "valentine"}
    elif q == "is the name a futuristic name?":
        futuristic_names = {"neo", "trinity", "morpheus", "cypher", "zephyr", "nova", "orion", "quantum", "zenith", "vortex", "aster", "cosmo", "eclipse", "galaxy", "hyperion", "ion", "juno", "krypton", "lumen", "matrix"}
    elif q == "is the name a traditional name?":
        traditional_names = {"john", "mary", "james", "patricia", "robert", "jennifer", "michael", "linda","william", " elizabeth", "david", "barbara", "richard", "susan", "joseph", "jessica", "thomas", "sarah", "charles", "karen", "christopher", "nancy", "daniel", "lisa", "matthew", "betty", "anthony", "dorothy", "mark", "helen", "donald", "sandra", "paul", "ashley", "steven", "kimberly", "andrew", "emily", "joshua", "donna", "kenneth", "michelle", "kevin", "carol", "brian", "amanda", "george", "melissa", "edward", "deborah","adam", "eve", "noah", "moses", "david", "asher", "abraham", "sarah", "isaac", "rebecca", "jacob", "rachel", "joseph", "mary", "jesus", "peter", "paul", "alice", "henry", "margaret", "arthur", "edith", "geoffrey", "beatrice", "edmund", "catherine", "robin", "victoria", "edward", "elizabeth", "charles", "diana", "william", "harry", "kate", "george", "victoria", "henry", "catherine", "edward", "anne", "james", "mary", "arthur", "alice", "charlotte", "louis", "sophie", "eugenie", "beatrice"}
        if ans == 'yes':
            names = {name for name in names if name.strip().lower() in traditional_names}
        elif ans == 'no':
            names = {name for name in names if name.strip().lower() not in traditional_names}
    elif q == "Is the name a fictional name?":
        if ans == 'yes':
            names = {name for name in names if name.strip().lower() in fictional_names}
        elif ans == 'no':
            names = {name for name in names if name.strip().lower() not in fictional_names}
    if not names:
        print("No names match your criteria. Please try again.")
        break
    elif len(names) == 1:
        print(f"Is your name {names.pop().strip().title()}?")
        break
    elif len(names) < 10:
        print(f"Possible names left: {', '.join(name.strip().title() for name in names)}")
    else:
        print(f"Possible names left: {', '.join(name.strip().title() for name in names)}")
if len(names) > 1:
    print(f"Could not narrow down to a single name. Possible names: {', '.join(name.strip().title() for name in names)}")
print("No names match your criteria. Please try again.")
   

