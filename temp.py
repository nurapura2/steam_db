import random
import re
from datetime import datetime, timedelta

# Настройки генерации — подправь числа при необходимости
N_DEVELOPERS = 31
N_CATEGORIES = 61
N_GAMES = 500
N_USERS = 1000
N_PROMOS = 20
N_ACH_PER_GAME_MAX = 15
N_PURCHASES = 700
MAX_ITEMS_PER_PURCHASE = 3
N_REVIEWS = 800
N_SESSIONS = 1500
N_BADGES = 400
N_FRIEND_PAIRS = 1400
N_MESSAGES = 5000
N_USER_ACHIEVEMENTS = 800

game_prices = {}  
purchase_to_user = {}
purchase_to_games = {}
purchase_to_date = {}

# users
def generate_users():    
    user_name_sample = ["Nova", "Vortex", "Blaze", "Phantom", "Titan", "Shadow", "Inferno", "Storm", "Frost", "Venom", "Chaos", "Eclipse", "Nexus", "Vector", "Matrix", "Quantum", "Pixel", "Cypher", "Pulse", "Astro", "Orion", "Neuron", "Void", "Obsidian", "Raven", "Abyss", "Specter", "Nocturne", "Wraith", "Shade", "Dusk", "Mirage", "Zen", "Hex", "Flux", "Nyx", "Zed", "Lux", "Kai", "Ryn", "Vox", "Axiom", "Drift", "Spark", "Glitch", "Cipher", "Atlas", "Cosmo", "Solar", "Lunar", "Ember", "Flare", "Comet", "Meteor", "Stellar", "Nebula", "Quasar", "Orbit", "Aether", "Blitz", "Fury", "Rogue", "Ghost", "Hunter", "Sniper", "Viper", "Falcon", "Wolf", "Tiger", "Panther", "Cobra", "Dragon", "Kraken", "Hydra", "Leviathan", "Reaper", "Slayer", "Knight", "Paladin", "Samurai", "Ronin", "Shogun", "Ninja", "Gladiator", "Spartan", "Warden", "Sentinel", "Guardian", "Champion", "Legend", "Myth", "Oracle", "Prophet", "Sage", "Wizard", "Mage", "Warlock", "Druid", "Cleric", "Monk", "Archer", "Ranger", "Assassin", "Berserk", "Savage", "Crusher", "Destroyer", "Conqueror", "Overlord", "Emperor", "King", "Prince", "Lord", "Baron", "Duke", "Knightfall", "Nightfall", "Darkstar", "Moonshade", "Sunflare", "Skyfall", "Ironclad", "Steelheart", "Stormborn", "Frostbite", "Firestorm", "Thunder", "Lightning", "Tempest", "Cyclone", "Typhoon", "Avalanche", "Blizzard", "Glacier", "Tundra", "Desert", "Oasis", "Canyon", "Summit", "Peak", "Cliff", "Forest", "Jungle", "Savanna", "Prairie", "Valley", "River", "Ocean", "Harbor", "Island", "Lagoon", "Reef", "Coral", "Anchor", "Voyager", "Explorer", "Nomad", "Wanderer", "Traveler", "Pilot", "Captain", "Navigator", "Pioneer", "Trailblazer", "Seeker", "Dreamer", "Vision", "Echo", "Pulse", "Signal", "Vector", "Core", "Frame", "Logic", "Code", "Script", "Binary", "Kernel", "Circuit", "Module", "Engine", "Protocol", "System", "Node", "Network", "Grid", "Data", "Cache", "Server", "Client", "Access", "Portal", "Gateway", "Bridge", "Link", "Sync", "Alpha", "Beta", "Gamma", "Delta", "Omega", "Sigma", "Theta", "Zeta", "Kappa", "Lambda", "Prime", "Ultra", "Hyper", "Turbo", "Rapid", "Swift", "Flash", "Dash", "Rush", "Velocity", "Momentum", "Gravity", "Fusion", "Plasma", "Photon", "Proton", "Electron", "Neutron", "Cosmos", "Galaxy", "Universe"]
    user_email_sample = ["alex", "max", "leo", "mike", "nick", "tony", "ivan", "adam", "dan", "sam", "eric", "mark", "david", "daniel", "kevin", "lucas", "ryan", "jack", "jason", "logan", "oliver", "ethan", "noah", "liam", "aaron", "arthur", "felix", "oscar", "peter", "victor", "roman", "denis", "anton", "sergey", "andrey", "timur", "amir", "arsen", "albert", "denver", "hunter", "rider", "walker", "mason", "carter", "cooper", "parker", "taylor", "river", "forest", "sky", "cloud", "stone", "iron", "steel", "silver", "gold", "crystal", "nova", "cosmo", "astro", "orbit", "comet", "meteor", "solar", "lunar", "galaxy", "nebula", "zen", "logic", "code", "byte", "data", "pixel", "vector", "matrix", "quantum", "cipher", "node", "core", "system", "engine", "module", "network", "signal", "link", "bridge", "alpha", "beta", "gamma", "delta", "omega", "prime", "ultra", "rapid", "swift", "flash", "dash", "pilot", "captain", "navigator", "voyager", "explorer", "nomad", "seeker", "dreamer", "vision", "echo", "pulse", "spark", "ember", "flare", "storm", "frost", "blaze", "shadow", "ghost", "raven", "wolf", "tiger", "falcon", "dragon", "viper", "cobra"]
    chars = "abcdef0123456789"
    pattern = re.compile(r'^[a-f0-9]{64}$')
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2022, 1, 1)

    id = [i for i in range(1, N_USERS + 1)]
    nicknames = set()
    emails = set()
    hashes = set()
    dates = []


    while len(nicknames) < N_USERS:

        w1 = random.choice(user_name_sample)
        w2 = random.choice(user_name_sample)

        number = random.randint(0, 999)

        nick = w1 + w2 + str(number)


        nick = re.sub(r'[^a-zA-Z0-9]', '', nick)

        nicknames.add(nick)

    while len(emails) < N_USERS:

        domains = ["gmail.com", "mail.com", "outlook.com", "proton.me","yahoo.com"]
        w1 = random.choice(user_email_sample)
        w2 = random.choice(user_email_sample)

        number = random.randint(1, 999)

        email = w1 + w2 + str(number) + "@" + random.choice(domains)

        email = re.sub(r'[^a-z0-9@._]', '', email)

        emails.add(email)

    while len(hashes) < N_USERS:

        h = "".join(random.choice(chars) for _ in range(64))

        if pattern.match(h):
            hashes.add(h)



    for _ in range(N_USERS):
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        random_seconds = random.randint(0, 24*60*60 - 1)

        random_date = start_date + timedelta(days=random_days, seconds=random_seconds)
        dates.append(random_date.strftime("%Y-%m-%d %H:%M:%S"))

    nicknames = list(nicknames)
    emails = list(emails)
    hashes = list(hashes)

    with open("users.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO users (id, username, email, password_hash, created_at) VALUES\n")

        lines = []
        for i in range(N_USERS):
            line = f"({id[i]}, '{nicknames[i]}', '{emails[i]}', '{hashes[i]}', '{dates[i]}')"
            lines.append(line)

        f.write(",\n".join(lines) + ";")

    print("Файл users.sql успешно создан!")

def generate_developers():
    developer_name_sample = [
        "Epic Games", "Valve Corporation", "Ubisoft", "Electronic Arts", "Rockstar Games", 
        "Bethesda Game Studios", "CD Projekt Red", "Square Enix", "Activision Blizzard", 
        "Naughty Dog", "Insomniac Games", "FromSoftware", "Capcom", "Bandai Namco Entertainment",
        "Sega", "Konami", "2K Games", "BioWare", "Guerrilla Games", "Respawn Entertainment", 
        "Treyarch", "Infinity Ward", "DICE", "Remedy Entertainment", "Arkane Studios", 
        "Mojang Studios", "Hello Games", "Supercell", "Riot Games", "Blizzard Entertainment", 
        "ZeniMax Online Studios"
    ]
    
    developer_sites = {
        "Epic Games": "https://www.epicgames.com",
        "Valve Corporation": "https://www.valvesoftware.com",
        "Ubisoft": "https://www.ubisoft.com",
        "Electronic Arts": "https://www.ea.com",
        "Rockstar Games": "https://www.rockstargames.com",
        "Bethesda Game Studios": "https://bethesda.net",
        "CD Projekt Red": "https://www.cdprojekt.com",
        "Square Enix": "https://www.square-enix.com",
        "Activision Blizzard": "https://www.activisionblizzard.com",
        "Naughty Dog": "https://www.naughtydog.com",
        "Insomniac Games": "https://www.insomniac.games",
        "FromSoftware": "https://www.fromsoftware.jp",
        "Capcom": "https://www.capcom.com",
        "Bandai Namco Entertainment": "https://www.bandainamcoent.com",
        "Sega": "https://www.sega.com",
        "Konami": "https://www.konami.com",
        "2K Games": "https://www.2k.com",
        "BioWare": "https://www.bioware.com",
        "Guerrilla Games": "https://www.guerrillagames.com",
        "Respawn Entertainment": "https://www.respawn.com",
        "Treyarch": "https://www.treyarch.com",
        "Infinity Ward": "https://www.infinityward.com",
        "DICE": "https://www.dice.se",
        "Remedy Entertainment": "https://www.remedygames.com",
        "Arkane Studios": "https://www.arkane-studios.com",
        "Mojang Studios": "https://www.minecraft.net",
        "Hello Games": "https://www.hellogames.org",
        "Supercell": "https://supercell.com",
        "Riot Games": "https://www.riotgames.com",
        "Blizzard Entertainment": "https://www.blizzard.com",
        "ZeniMax Online Studios": "https://www.zenimax.com"
    }

    id = [i for i in range(1, N_DEVELOPERS + 1)]

    
    with open("developers.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO developers (id, developer_name, description) VALUES\n")
        lines = []
        for i, name in enumerate(developer_name_sample, start=1):
            site = developer_sites.get(name, "")
            name_sql = name.replace("'", "''")
            site_sql = site.replace("'", "''")
            line = f"({i}, '{name_sql}', '{site_sql}')"
            lines.append(line)
        f.write(",\n".join(lines) + ";")
    
    print("Файл developers.sql успешно создан!")

def generate_games():
    
    game_words = [
        "Shadow", "Blade", "Quest", "Legend", "Rise", "Fall", "Dragon", "War",
        "Battle", "Storm", "Chronicles", "Galaxy", "Empire", "Saga", "Night",
        "Dawn", "Infinity", "Void", "Revenge", "Hero", "Kingdom", "Fury",
        "Mystic", "Arena", "Strike", "Odyssey", "Nemesis", "Phantom", "Eclipse",
        "Vortex", "Inferno", "Frost", "Blaze", "Shadow", "Ghost", "Raven", "Wolf",
        "Tiger", "Falcon", "Dragon", "Viper", "Cobra", "Kraken", "Hydra", "Leviathan",
        "Reaper", "Slayer", "Knight", "Paladin", "Samurai", "Ronin", "Shogun",
        "Ninja", "Gladiator", "Spartan", "Warden", "Sentinel", "Guardian", "Champion",
        "Legend", "Myth", "Oracle", "Prophet", "Sage", "Wizard", "Mage", "Warlock", "Druid",
        "Cleric", "Monk", "Archer", "Ranger", "Assassin", "Berserk", "Savage", "Crusher", 
        "Destroyer", "Conqueror", "Overlord", "Emperor", "King", "Prince", "Lord", "Baron", 
        "Duke", "Knightfall", "Nightfall", "Darkstar", "Moonshade", "Sunflare", "Skyfall", "Ironclad"
    ]

    age_ratings = ["E", "T", "M", "A", "RP"]

    start_date = datetime(1985, 1, 1)
    end_date = datetime(2026, 3, 10)

    with open("games.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO games (developer_id, title, price, release_date, age_rating, description) VALUES\n")
        lines = []

        for i in range(N_GAMES):
            developer_id = random.randint(1, N_DEVELOPERS)

            # Генерация названия игры из 2-3 слов
            title = " ".join(random.sample(game_words, random.randint(2, 3)))
            title_sql = title.replace("'", "''")  # экранируем апострофы

            # Цена от 0 до 100 с двумя знаками
            price = round(random.uniform(0, 100), 2)

            # Случайная дата
            delta = end_date - start_date
            random_days = random.randint(0, delta.days)
            random_seconds = random.randint(0, 24*60*60 - 1)
            release_date = start_date + timedelta(days=random_days, seconds=random_seconds)
            release_date_str = release_date.strftime("%Y-%m-%d %H:%M:%S")

            # Возрастной рейтинг
            age_rating = random.choice(age_ratings)

            # Короткое описание
            description = f"Description of {title_sql} ..."
            description_sql = description.replace("'", "''")

            line = f"({i + 1}, {developer_id}, '{title_sql}', {price}, '{release_date_str}', '{age_rating}', '{description_sql}')"
            lines.append(line)

            global game_prices
            for i, line in enumerate(lines, start=1):
                # line примерно: (1, 23, 'Shadow Quest', 29.99, '2024-05-01 12:33:01', 'E', 'Description ...')
                parts = line.split(",")  # простой способ: элементы через запятую
                price = float(parts[3])  # четвёртый элемент — цена
                game_prices[i] = price


        f.write(",\n".join(lines) + ";")

    print("Файл games.sql успешно создан!")


def generate_categories():
    category_names = [
        "Action", "Adventure", "RPG", "Strategy", "Simulation", "Sports",
        "Puzzle", "Horror", "Multiplayer", "Indie", "Open World", "Sandbox",
        "Survival", "Stealth", "Platformer", "Racing", "Fighting", "MMO",
        "Card Game", "Visual Novel", "Rhythm", "Educational", "VR",
        "Sci-Fi", "Fantasy", "Historical", "Post-Apocalyptic", "Cyberpunk", 
        "Superhero", "Comedy", "Mystery", "Thriller", "War",
        "Space", "Underwater", "Medieval", "Modern", "Future", "Mythology",
        "Zombies", "Aliens", "Monsters", "Magic", "Technology",
        "Nature", "Animals", "Vehicles", "Music", "Art", "Sports",
        "Cooking", "Farming", "City Building", "Tycoon", "Tower Defense", 
        "Card Battle", "Rogue-like", "Bullet Hell", "Metroidvania",
        "Hack and Slash", "Beat 'em up'"
    ]

    with open("categories.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO categories (id, category_name) VALUES\n")
        lines = []
        for i, name in enumerate(category_names, start=1):
            name_sql = name.replace("'", "''")
            line = f"({i}, '{name_sql}')"
            lines.append(line)
        f.write(",\n".join(lines) + ";")

    print("Файл categories.sql успешно создан!")

def generate_game_categories():
    with open("game_categories.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO game_categories (game_id, category_id) VALUES\n")
        lines = []
        for game_id in range(1, N_GAMES + 1):
            n_cats = random.randint(1, 3)  # 1-3 категории на игру
            categories = random.sample(range(1, N_CATEGORIES + 1), n_cats)
            for cat_id in categories:
                line = f"({game_id}, {cat_id})"
                lines.append(line)
        f.write(",\n".join(lines) + ";")

    print("Файл game_categories.sql успешно создан!")

def generate_achievements():
    achievement_words = [
        "Master", "Legend", "Hero", "Conqueror", "Slayer", "Guardian", "Champion",
        "Warrior", "Assassin", "Explorer", "Survivor", "Collector", "Craftsman",
        "Strategist", "Speedrunner", "Completionist", "Perfectionist", "Glitcher",
        "Secret Finder", "Boss Killer", "Puzzle Solver", "Multiplayer Pro",
        "Stealth Master", "Rogue-like Expert", "Card Master", "Racing Legend",
        "Fighting Champion", "MMO Veteran", "VR Pioneer", "Sci-Fi Enthusiast", "Fantasy Lover",
        "Historical Buff", "Post-Apocalyptic Survivor", "Cyberpunk Hacker",
        "Superhero Defender", "Comedy King", "Mystery Solver", "Thriller Fan",
        "War Veteran", "Space Explorer", "Underwater Adventurer", "Medieval Knight",
        "Modern Soldier", "Future Techie", "Mythology Expert", "Zombie Slayer", 
        "Alien Hunter", "Monster Tamer", "Magic User", "Tech Guru",
        "Nature Lover", "Animal Friend", "Vehicle Driver", "Music Maestro",
        "Artistic Soul", "Sports Star", "Cooking Master", "Farming Expert",
        "City Planner", "Tycoon Mogul", "Tower Defender", "Card Battler", 
        "Rogue-like Survivor", "Bullet Hell Dodger", "Metroidvania Explorer"
    ]

    current_id = 1 

    with open("achievements.sql", "w", encoding="utf-8") as f:
            f.write("INSERT INTO achievements (id, game_id, title, description) VALUES\n")
            lines = []

            for game_id in range(1, N_GAMES + 1):
                num_achievements = random.randint(1, N_ACH_PER_GAME_MAX)

                for _ in range(num_achievements):
                    name = random.choice(achievement_words) + f" {random.randint(1, 100)}"
                    name_sql = name.replace("'", "''")
                    description = f"Description of {name_sql} ..."
                    description_sql = description.replace("'", "''")
                    line = f"({current_id}, {game_id}, '{name_sql}', '{description_sql}')"
                    lines.append(line)
                    current_id += 1

            f.write(",\n".join(lines) + ";")


            print("Файл achievements.sql успешно создан!")

def generate_user_achievements():
    with open("user_achievements.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO user_achievements (user_id, achievement_id, achieved_at) VALUES\n")
        lines = []
        for _ in range(N_USER_ACHIEVEMENTS):
            user_id = random.randint(1, N_USERS)
            achievement_id = random.randint(1, N_GAMES * N_ACH_PER_GAME_MAX)  # предполагая, что достижений может быть до 15 на игру
            unlocked_at = datetime.now() - timedelta(days=random.randint(0, 365))
            achieved_at_str = unlocked_at.strftime("%Y-%m-%d %H:%M:%S")
            line = f"({user_id}, {achievement_id}, '{achieved_at_str}')"
            lines.append(line)
        f.write(",\n".join(lines) + ";")

    print("Файл user_achievements.sql успешно создан!")

def generate_wallets():
    currencies = ["USD", "EUR", "GBP", "JPY", "KZT"]

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2026, 3, 10)

    with open("wallets.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO wallets (user_id, currency, balance, updated_at) VALUES\n")

        lines = []

        for user_id in range(1, N_USERS + 1):

            currency = random.choice(currencies)
            deposits = random.randint(1, 5)   # количество пополнений

            balance = 0
            current_date = start_date

            for _ in range(deposits):

                # сумма пополнения
                if currency == "KZT":
                    amount = random.uniform(1000, 100000)
                elif currency == "JPY":
                    amount = random.uniform(1000, 50000)
                else:
                    amount = random.uniform(10, 500)

                balance += round(amount, 2)

                # новая дата позже предыдущей
                delta_days = random.randint(1, 300)
                delta_seconds = random.randint(0, 86400)

                current_date = current_date + timedelta(days=delta_days, seconds=delta_seconds)

                if current_date > end_date:
                    break

                updated_at_str = current_date.strftime("%Y-%m-%d %H:%M:%S")

                line = f"({user_id}, '{currency}', {round(balance,2)}, '{updated_at_str}')"
                lines.append(line)

        f.write(",\n".join(lines) + ";")

    print("Файл wallets.sql успешно создан!")

def generate_purchases():
    purchase_types = ["game", "dlc", "bundle", "in_game_purchase"]
    payment_methods = ["card", "paypal", "apple_pay", "google_pay", "qiwi", "wallet"]
    statuses = ["completed", "pending", "refunded", "failed"]

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2026, 3, 10)

    global purchase_to_user, purchase_to_date

    with open("purchases.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO purchases (purchase_id, user_id, purchase_type, payment_method, status, purchase_date, promo_id) VALUES\n")
        lines = []
        for i in range(N_PURCHASES):
            user_id = random.randint(1, N_USERS)
            purchase_type = random.choice(purchase_types)
            delta_days = random.randint(0, (end_date - start_date).days)
            delta_seconds = random.randint(0, 86400)
            purchase_date = start_date + timedelta(days=delta_days, seconds=delta_seconds)
            purchase_date_str = purchase_date.strftime("%Y-%m-%d %H:%M:%S")
            payment_method = random.choice(payment_methods)
            status = random.choice(statuses)
            promo_id = random.randint(1, N_PROMOS) if N_PROMOS > 0 else None

            line = f"({i + 1}, {user_id}, '{purchase_type}', '{payment_method}', '{status}', '{purchase_date_str}', {promo_id})"
            lines.append(line)

            # сохраняем в глобальный словарь
            purchase_to_user[i + 1] = user_id
            purchase_to_date[i + 1] = purchase_date_str

        f.write(",\n".join(lines) + ";")

    print("Файл purchases.sql успешно создан!")

def generate_purchase_items():
    MAX_PURCHASES_PER_USER = 12
    START_DATE = datetime(2023, 1, 1)
    END_DATE = datetime(2026, 3, 10)

    global purchase_to_games  # используем глобальный словарь

    lines = []
    purchase_id = 1
    purchase_item_id = 1

    for user_id in range(1, N_USERS + 1):
        num_purchases = random.randint(1, MAX_PURCHASES_PER_USER)
        last_purchase_date = START_DATE

        for _ in range(num_purchases):
            # дата покупки для возможного использования (опционально)
            purchase_dt = last_purchase_date + timedelta(days=random.randint(0, 30))
            last_purchase_date = min(purchase_dt, END_DATE)

            # генерируем 1..MAX_ITEMS_PER_PURCHASE предметов для этой покупки
            n_items = random.randint(1, MAX_ITEMS_PER_PURCHASE)
            chosen_games = []

            for _ in range(n_items):
                game_id = random.choice(list(game_prices.keys()))
                price_at_purchase = game_prices[game_id]
                chosen_games.append(game_id)

                line = f"({purchase_item_id}, {game_id}, {purchase_id}, {price_at_purchase})"
                lines.append(line)
                purchase_item_id += 1

            # сохраняем в глобальный словарь
            purchase_to_games[purchase_id] = chosen_games

            purchase_id += 1  # следующая покупка

    # Записываем в SQL файл
    with open("purchases_item.sql", "w", encoding="utf-8") as f:
        f.write(
            "INSERT INTO purchases_item (purchase_item_id, game_id, purchase_id, price_at_purchase) VALUES\n"
        )
        f.write(",\n".join(lines) + ";\n")

    print("Файл purchases_item.sql успешно создан!")

def generate_promotions():
    with open("promotions.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO promotions (promo_id, code, discount_percent, start_date, end_date) VALUES\n")
        lines = []
        for i in range(1, N_PROMOS + 1):
            promo_code = f"PROMO{i:03d}"
            discount_percentage = random.randint(5, 25)
            start_date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
            end_date = start_date + timedelta(days=random.randint(7, 30))
            line = f"({i}, '{promo_code}', {discount_percentage}, '{start_date.strftime('%Y-%m-%d')}', '{end_date.strftime('%Y-%m-%d')}')"
            lines.append(line)
        f.write(",\n".join(lines) + ";")

    print("Файл promotions.sql успешно создан!")

def generate_badges():
    badge_names = [
        "Rookie", "Veteran", "Elite", "Master", "Legend", "Champion", "Conqueror",
        "Slayer", "Guardian", "Hero", "Warrior", "Assassin", "Explorer", "Survivor",
        "Collector", "Craftsman", "Strategist", "Speedrunner", "Completionist",
        "Perfectionist", "Glitcher", "Secret Finder", "Boss Killer", "Puzzle Solver",
        "Multiplayer Pro", "Stealth Master", "Rogue-like Expert", "Card Master",
        "Racing Legend", "Fighting Champion", "MMO Veteran", "VR Pioneer",
        "Sci-Fi Enthusiast"
    ]

    with open("badges.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO badges (badge_id, user_id, title, awarded_at) VALUES\n")
        lines = []
        for badge_id in range(1, N_BADGES + 1):
            user_id = random.randint(1, N_USERS)
            title = random.choice(badge_names)
            awarded_at = datetime.now() - timedelta(days=random.randint(0, 365))
            line = f"({badge_id}, {user_id}, '{title}', '{awarded_at.strftime('%Y-%m-%d %H:%M:%S')}')"
            lines.append(line)
        f.write(",\n".join(lines) + ";")
        
    print("Файл badges.sql успешно создан!")

def generate_friends():
    with open("friends.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO friends (user_id, friend_id) VALUES\n")
        lines = []
        for _ in range(N_FRIEND_PAIRS*5):
            user_id = random.randint(1, N_USERS)
            friend_id = random.randint(1, N_USERS)
            if user_id != friend_id:  # избегаем дружбы с самим собой
                line = f"({user_id}, {friend_id})"
                lines.append(line)
        f.write(",\n".join(lines) + ";")

    print("Файл friends.sql успешно создан!")

def generate_messages():
    with open("messages.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO messages (message_id, sender_id, receiver_id, content, sent_at) VALUES\n")
        lines = []
        for message_id in range(1, N_MESSAGES + 1):
            sender_id = random.randint(1, N_USERS)
            receiver_id = random.randint(1, N_USERS)
            is_read = random.choice(['Yes', 'No'])
            if sender_id != receiver_id:  # избегаем сообщений самому себе
                content = f"Message {message_id} from user {sender_id} to user {receiver_id}"
                sent_at = datetime.now() - timedelta(days=random.randint(0, 365))
                line = f"({message_id}, {sender_id}, {receiver_id}, '{content}', '{sent_at.strftime('%Y-%m-%d %H:%M:%S')}', '{is_read}')"
                lines.append(line)
        f.write(",\n".join(lines) + ";")

    print("Файл messages.sql успешно создан!")

def generate_library():
    with open("library.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO library (user_id, game_id, purchase_id, added_date) VALUES\n")
        lines = []
        for user_id in range(1, N_USERS + 1):
            owned_games = random.sample(range(1, N_GAMES + 1), random.randint(0, 20))  # до 20 игр в библиотеке
            for game_id in owned_games:
                added_at = datetime.now() - timedelta(days=random.randint(0, 365))
                line = f"({user_id}, {game_id}, '{added_at.strftime('%Y-%m-%d %H:%M:%S')}')"
                lines.append(line)
        f.write(",\n".join(lines) + ";")

    print("Файл library.sql успешно создан!")

def generate_library():
    with open("library.sql", "w", encoding="utf-8") as f:
        f.write("INSERT INTO library (user_id, game_id, purchase_id, added_date) VALUES\n")
        lines = []

        for purchase_id, user_id in purchase_to_user.items():
            added_date_str = purchase_to_date[purchase_id]
            games_in_purchase = purchase_to_games.get(purchase_id, [])

            for game_id in games_in_purchase:
                line = f"({user_id}, {game_id}, {purchase_id}, '{added_date_str}')"
                lines.append(line)

        f.write(",\n".join(lines) + ";")

    print(f"Файл library.sql успешно создан! Всего записей: {len(lines)}")

