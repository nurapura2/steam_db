import os
import random
import re
from datetime import datetime, timedelta

# Defining absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TABLES_DIR = os.path.join(BASE_DIR, "..", "tables")
ALL_DATA_FILE = os.path.join(BASE_DIR, "..", "seed_data.sql")

os.makedirs(TABLES_DIR, exist_ok=True)

# Generation settings
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

# Global state shared between generators
game_prices: dict[int, float] = {}
purchase_to_user: dict[int, int] = {}
purchase_to_games: dict[int, list[int]] = {}
purchase_to_date: dict[int, str] = {}
total_achievements_generated: int = 0


def generate_users() -> None:
    user_name_sample = [
        "Nova", "Vortex", "Blaze", "Phantom", "Titan", "Shadow", "Inferno", "Storm",
        "Frost", "Venom", "Chaos", "Eclipse", "Nexus", "Vector", "Matrix", "Quantum",
        "Pixel", "Cypher", "Pulse", "Astro", "Orion", "Neuron", "Void", "Obsidian",
        "Raven", "Abyss", "Specter", "Nocturne", "Wraith", "Shade", "Dusk", "Mirage",
        "Zen", "Hex", "Flux", "Nyx", "Zed", "Lux", "Kai", "Ryn", "Vox", "Axiom",
        "Drift", "Spark", "Glitch", "Cipher", "Atlas", "Cosmo", "Solar", "Lunar",
        "Ember", "Flare", "Comet", "Meteor", "Stellar", "Nebula", "Quasar", "Orbit",
        "Aether", "Blitz", "Fury", "Rogue", "Ghost", "Hunter", "Sniper", "Viper",
        "Falcon", "Wolf", "Tiger", "Panther", "Cobra", "Dragon", "Kraken", "Hydra",
        "Leviathan", "Reaper", "Slayer", "Knight", "Paladin", "Samurai", "Ronin",
        "Shogun", "Ninja", "Gladiator", "Spartan", "Warden", "Sentinel", "Guardian",
        "Champion", "Legend", "Myth", "Oracle", "Prophet", "Sage", "Wizard", "Mage",
        "Warlock", "Druid", "Cleric", "Monk", "Archer", "Ranger", "Assassin", "Berserk",
        "Savage", "Crusher", "Destroyer", "Conqueror", "Overlord", "Emperor", "King",
        "Prince", "Lord", "Baron", "Duke", "Knightfall", "Nightfall", "Darkstar",
        "Moonshade", "Sunflare", "Skyfall", "Ironclad", "Steelheart", "Stormborn",
        "Frostbite", "Firestorm", "Thunder", "Lightning", "Tempest", "Cyclone",
        "Typhoon", "Avalanche", "Blizzard", "Glacier", "Tundra", "Desert", "Oasis",
        "Canyon", "Summit", "Peak", "Cliff", "Forest", "Jungle", "Savanna", "Prairie",
        "Valley", "River", "Ocean", "Harbor", "Island", "Lagoon", "Reef", "Coral",
        "Anchor", "Voyager", "Explorer", "Nomad", "Wanderer", "Traveler", "Pilot",
        "Captain", "Navigator", "Pioneer", "Trailblazer", "Seeker", "Dreamer",
        "Vision", "Echo", "Signal", "Core", "Frame", "Logic", "Code", "Script",
        "Binary", "Kernel", "Circuit", "Module", "Engine", "Protocol", "System",
        "Node", "Network", "Grid", "Data", "Cache", "Server", "Client", "Access",
        "Portal", "Gateway", "Bridge", "Link", "Sync", "Alpha", "Beta", "Gamma",
        "Delta", "Omega", "Sigma", "Theta", "Zeta", "Kappa", "Lambda", "Prime",
        "Ultra", "Hyper", "Turbo", "Rapid", "Swift", "Flash", "Dash", "Rush",
        "Velocity", "Momentum", "Gravity", "Fusion", "Plasma", "Photon", "Proton",
        "Electron", "Neutron", "Cosmos", "Galaxy", "Universe",
    ]
    user_email_sample = [
        "alex", "max", "leo", "mike", "nick", "tony", "ivan", "adam", "dan", "sam",
        "eric", "mark", "david", "daniel", "kevin", "lucas", "ryan", "jack", "jason",
        "logan", "oliver", "ethan", "noah", "liam", "aaron", "arthur", "felix", "oscar",
        "peter", "victor", "roman", "denis", "anton", "sergey", "andrey", "timur",
        "amir", "arsen", "albert", "denver", "hunter", "rider", "walker", "mason",
        "carter", "cooper", "parker", "taylor", "river", "forest", "sky", "cloud",
        "stone", "iron", "steel", "silver", "gold", "crystal", "nova", "cosmo", "astro",
        "orbit", "comet", "meteor", "solar", "lunar", "galaxy", "nebula", "zen", "logic",
        "code", "byte", "..", "pixel", "vector", "matrix", "quantum", "cipher", "node",
        "core", "system", "engine", "module", "network", "signal", "link", "bridge",
        "alpha", "beta", "gamma", "delta", "omega", "prime", "ultra", "rapid", "swift",
        "flash", "dash", "pilot", "captain", "navigator", "voyager", "explorer", "nomad",
        "seeker", "dreamer", "vision", "echo", "pulse", "spark", "ember", "flare",
        "storm", "frost", "blaze", "shadow", "ghost", "raven", "wolf", "tiger",
        "falcon", "dragon", "viper", "cobra",
    ]
    hex_chars = "abcdef0123456789"
    hash_pattern = re.compile(r'^[a-f0-9]{64}$')
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2022, 1, 1)
    delta = end_date - start_date

    nicknames: set[str] = set()
    emails: set[str] = set()
    hashes: set[str] = set()
    dates: list[str] = []

    while len(nicknames) < N_USERS:
        nick = (
            random.choice(user_name_sample)
            + random.choice(user_name_sample)
            + str(random.randint(0, 999))
        )
        nick = re.sub(r'[^a-zA-Z0-9]', '', nick)
        nicknames.add(nick)

    while len(emails) < N_USERS:
        domains = ["gmail.com", "mail.com", "outlook.com", "proton.me", "yahoo.com"]
        email = (
            random.choice(user_email_sample)
            + random.choice(user_email_sample)
            + str(random.randint(1, 999))
            + "@"
            + random.choice(domains)
        )
        email = re.sub(r'[^a-z0-9@._]', '', email)
        emails.add(email)

    while len(hashes) < N_USERS:
        h = "".join(random.choice(hex_chars) for _ in range(64))
        if hash_pattern.match(h):
            hashes.add(h)

    for _ in range(N_USERS):
        random_date = start_date + timedelta(
            days=random.randint(0, delta.days),
            seconds=random.randint(0, 86399),
        )
        dates.append(
            "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(
                random_date.strftime("%Y-%m-%d %H:%M:%S")
            )
        )

    nicknames_list = list(nicknames)
    emails_list = list(emails)
    hashes_list = list(hashes)

    with open(os.path.join(TABLES_DIR, "users.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO users (user_id, username, email, password_hash, created_at) VALUES\n")
        lines = [
            f"({i + 1}, '{nicknames_list[i]}', '{emails_list[i]}', '{hashes_list[i]}', {dates[i]})"
            for i in range(N_USERS)
        ]
        f.write(",\n".join(lines) + ";")
    print("users.sql created successfully.")


def generate_developers() -> None:
    developer_names = [
        "Epic Games", "Valve Corporation", "Ubisoft", "Electronic Arts", "Rockstar Games",
        "Bethesda Game Studios", "CD Projekt Red", "Square Enix", "Activision Blizzard",
        "Naughty Dog", "Insomniac Games", "FromSoftware", "Capcom", "Bandai Namco Entertainment",
        "Sega", "Konami", "2K Games", "BioWare", "Guerrilla Games", "Respawn Entertainment",
        "Treyarch", "Infinity Ward", "DICE", "Remedy Entertainment", "Arkane Studios",
        "Mojang Studios", "Hello Games", "Supercell", "Riot Games", "Blizzard Entertainment",
        "ZeniMax Online Studios",
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
        "ZeniMax Online Studios": "https://www.zenimax.com",
    }

    with open(os.path.join(TABLES_DIR, "developers.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO developers (developer_id, developer_name, description) VALUES\n")
        lines = []
        for i, name in enumerate(developer_names, start=1):
            site = developer_sites.get(name, "")
            line = f"({i}, '{name.replace(chr(39), chr(39)*2)}', '{site}')"
            lines.append(line)
        f.write(",\n".join(lines) + ";")
    print("developers.sql created successfully.")


def generate_games() -> None:
    game_words = [
        "Shadow", "Blade", "Quest", "Legend", "Rise", "Fall", "Dragon", "War",
        "Battle", "Storm", "Chronicles", "Galaxy", "Empire", "Saga", "Night",
        "Dawn", "Infinity", "Void", "Revenge", "Hero", "Kingdom", "Fury",
        "Mystic", "Arena", "Strike", "Odyssey", "Nemesis", "Phantom", "Eclipse",
        "Vortex", "Inferno", "Frost", "Blaze", "Ghost", "Raven", "Wolf",
        "Tiger", "Falcon", "Viper", "Cobra", "Kraken", "Hydra", "Leviathan",
        "Reaper", "Slayer", "Knight", "Paladin", "Samurai", "Ronin", "Shogun",
        "Ninja", "Gladiator", "Spartan", "Warden", "Sentinel", "Guardian",
        "Champion", "Myth", "Oracle", "Prophet", "Sage", "Wizard", "Mage",
        "Warlock", "Druid", "Cleric", "Monk", "Archer", "Ranger", "Assassin",
        "Berserk", "Savage", "Crusher", "Destroyer", "Conqueror", "Overlord",
        "Emperor", "King", "Prince", "Lord", "Baron", "Duke", "Knightfall",
        "Nightfall", "Darkstar", "Moonshade", "Sunflare", "Skyfall", "Ironclad",
    ]
    age_ratings = ["E", "T", "M", "A", "RP"]
    start_date = datetime(1985, 1, 1)
    end_date = datetime(2026, 3, 10)
    delta = end_date - start_date

    global game_prices

    with open(os.path.join(TABLES_DIR, "games.sql"), "w", encoding="utf-8") as f:
        f.write(
            "INSERT INTO games (game_id, developer_id, title, price, release_date, age_rating, description) VALUES\n"
        )
        lines = []
        for i in range(N_GAMES):
            developer_id = random.randint(1, N_DEVELOPERS)
            title = " ".join(random.sample(game_words, random.randint(2, 3)))
            title_sql = title.replace("'", "''")
            price = round(random.uniform(0, 100), 2)

            release_date = start_date + timedelta(
                days=random.randint(0, delta.days),
                seconds=random.randint(0, 86399),
            )
            release_date_str = "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(
                release_date.strftime("%Y-%m-%d %H:%M:%S")
            )

            age_rating = random.choice(age_ratings)
            description_sql = f"Description of {title_sql} ...".replace("'", "''")

            lines.append(
                f"({i + 1}, {developer_id}, '{title_sql}', {price}, "
                f"{release_date_str}, '{age_rating}', '{description_sql}')"
            )
            game_prices[i + 1] = price

        f.write(",\n".join(lines) + ";")
    print("games.sql created successfully.")


def generate_categories() -> None:
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
        "Hack and Slash", "Beat ''em up",
    ]

    with open(os.path.join(TABLES_DIR, "categories.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO categories (id, category_name) VALUES\n")
        lines = [f"({i}, '{name.replace(chr(39), chr(39)*2)}')" for i, name in enumerate(category_names, start=1)]
        f.write(",\n".join(lines) + ";")
    print("categories.sql created successfully.")


def generate_game_categories() -> None:
    with open(os.path.join(TABLES_DIR, "game_categories.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO game_categories (game_id, category_id) VALUES\n")
        lines = []
        for game_id in range(1, N_GAMES + 1):
            for cat_id in random.sample(range(1, N_CATEGORIES + 1), random.randint(1, 3)):
                lines.append(f"({game_id}, {cat_id})")
        f.write(",\n".join(lines) + ";")
    print("game_categories.sql created successfully.")


def generate_achievements() -> None:
    global total_achievements_generated
    achievement_words = [
        "Master", "Legend", "Hero", "Conqueror", "Slayer", "Guardian", "Champion",
        "Warrior", "Assassin", "Explorer", "Survivor", "Collector", "Craftsman",
        "Strategist", "Speedrunner", "Completionist", "Perfectionist", "Glitcher",
        "Secret Finder", "Boss Killer", "Puzzle Solver", "Multiplayer Pro",
        "Stealth Master", "Rogue-like Expert", "Card Master", "Racing Legend",
        "Fighting Champion", "MMO Veteran", "VR Pioneer", "Sci-Fi Enthusiast",
        "Fantasy Lover",
    ]
    current_id = 1

    with open(os.path.join(TABLES_DIR, "achievements.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO achievements (achievement_id, game_id, title, description) VALUES\n")
        lines = []
        for game_id in range(1, N_GAMES + 1):
            for _ in range(random.randint(1, N_ACH_PER_GAME_MAX)):
                name = random.choice(achievement_words) + f" {random.randint(1, 100)}"
                name_sql = name.replace("'", "''")
                desc_sql = f"Description of {name_sql} ...".replace("'", "''")
                lines.append(f"({current_id}, {game_id}, '{name_sql}', '{desc_sql}')")
                current_id += 1

        f.write(",\n".join(lines) + ";")

    total_achievements_generated = current_id - 1
    print(f"achievements.sql created successfully. Total achievements: {total_achievements_generated}")


def generate_user_achievements() -> None:
    if total_achievements_generated == 0:
        raise RuntimeError("Call generate_achievements() before generate_user_achievements().")

    with open(os.path.join(TABLES_DIR, "user_achievements.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO user_achievements (user_id, achievement_id, unlocked_at) VALUES\n")
        lines = []
        for _ in range(N_USER_ACHIEVEMENTS):
            user_id = random.randint(1, N_USERS)
            achievement_id = random.randint(1, total_achievements_generated)
            unlocked_at = datetime.now() - timedelta(days=random.randint(0, 365))
            unlocked_at_str = "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(
                unlocked_at.strftime("%Y-%m-%d %H:%M:%S")
            )
            lines.append(f"({user_id}, {achievement_id}, {unlocked_at_str})")
        f.write(",\n".join(lines) + ";")
    print("user_achievements.sql created successfully.")


def generate_wallets() -> None:
    currencies = ["USD", "EUR", "GBP", "JPY", "KZT"]
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2026, 3, 10)

    with open(os.path.join(TABLES_DIR, "wallets.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO wallets (user_id, currency, balance, updated_at) VALUES\n")
        lines = []
        for user_id in range(1, N_USERS + 1):
            currency = random.choice(currencies)
            n_deposits = random.randint(1, 5)
            balance = 0.0
            current_date = start_date

            for _ in range(n_deposits):
                if currency == "KZT":
                    amount = random.uniform(1000, 100000)
                elif currency == "JPY":
                    amount = random.uniform(1000, 50000)
                else:
                    amount = random.uniform(10, 500)

                balance += round(amount, 2)
                current_date += timedelta(
                    days=random.randint(1, 300),
                    seconds=random.randint(0, 86400),
                )
                if current_date > end_date:
                    current_date = end_date
                    break

            updated_at_str = "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(
                current_date.strftime("%Y-%m-%d %H:%M:%S")
            )
            lines.append(f"({user_id}, '{currency}', {round(balance, 2)}, {updated_at_str})")

        f.write(",\n".join(lines) + ";")
    print("wallets.sql created successfully.")


def generate_promotions() -> None:
    with open(os.path.join(TABLES_DIR, "promotions.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO promotions (promo_id, code, discount_percent, start_date, end_date) VALUES\n")
        lines = []
        for i in range(1, N_PROMOS + 1):
            start_date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
            end_date = start_date + timedelta(days=random.randint(7, 30))
            lines.append(
                f"({i}, 'PROMO{i:03d}', {random.randint(5, 25)}, "
                f"TO_DATE('{start_date.strftime('%Y-%m-%d')}', 'YYYY-MM-DD'), "
                f"TO_DATE('{end_date.strftime('%Y-%m-%d')}', 'YYYY-MM-DD'))"
            )
        f.write(",\n".join(lines) + ";")
    print("promotions.sql created successfully.")


def generate_purchases() -> None:
    purchase_types = ["game", "dlc", "bundle", "in_game_purchase"]
    payment_methods = ["card", "paypal", "apple_pay", "google_pay", "qiwi", "wallet"]
    statuses = ["completed", "pending", "refunded", "failed"]
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2026, 3, 10)
    delta = end_date - start_date

    global purchase_to_user, purchase_to_date

    with open(os.path.join(TABLES_DIR, "purchases.sql"), "w", encoding="utf-8") as f:
        f.write(
            "INSERT INTO purchases "
            "(purchase_id, user_id, purchase_type, payment_method, status, purchase_date, promo_id) VALUES\n"
        )
        lines = []
        for i in range(N_PURCHASES):
            user_id = random.randint(1, N_USERS)
            purchase_date = start_date + timedelta(
                days=random.randint(0, delta.days),
                seconds=random.randint(0, 86399),
            )
            purchase_date_raw = purchase_date.strftime("%Y-%m-%d %H:%M:%S")
            purchase_date_str = "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(purchase_date_raw)
            promo_id = random.randint(1, N_PROMOS) if N_PROMOS > 0 else "NULL"

            lines.append(
                f"({i + 1}, {user_id}, '{random.choice(purchase_types)}', "
                f"'{random.choice(payment_methods)}', '{random.choice(statuses)}', "
                f"{purchase_date_str}, {promo_id})"
            )
            purchase_to_user[i + 1] = user_id
            purchase_to_date[i + 1] = purchase_date_raw

        f.write(",\n".join(lines) + ";")
    print("purchases.sql created successfully.")


def generate_purchase_items() -> None:
    global purchase_to_games
    lines = []
    purchase_item_id = 1

    for purchase_id in range(1, N_PURCHASES + 1):
        chosen_games = []
        for _ in range(random.randint(1, MAX_ITEMS_PER_PURCHASE)):
            game_id = random.choice(list(game_prices.keys()))
            lines.append(f"({purchase_item_id}, {game_id}, {purchase_id}, {game_prices[game_id]})")
            chosen_games.append(game_id)
            purchase_item_id += 1
        purchase_to_games[purchase_id] = chosen_games

    with open(os.path.join(TABLES_DIR, "purchases_item.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO purchases_item (purchase_item_id, game_id, purchase_id, price_at_purchase) VALUES\n")
        f.write(",\n".join(lines) + ";")
    print("purchases_item.sql created successfully.")


def generate_badges() -> None:
    badge_names = ["Rookie", "Veteran", "Elite", "Master", "Legend", "Champion", "Conqueror"]
    with open(os.path.join(TABLES_DIR, "badges.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO badges (badge_id, user_id, title, awarded_at) VALUES\n")
        lines = []
        for badge_id in range(1, N_BADGES + 1):
            awarded_at = datetime.now() - timedelta(days=random.randint(0, 365))
            awarded_at_str = "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(
                awarded_at.strftime("%Y-%m-%d %H:%M:%S")
            )
            lines.append(
                f"({badge_id}, {random.randint(1, N_USERS)}, '{random.choice(badge_names)}', {awarded_at_str})"
            )
        f.write(",\n".join(lines) + ";")
    print("badges.sql created successfully.")


def generate_friends() -> None:
    unique_pairs: set[tuple[int, int]] = set()
    while len(unique_pairs) < N_FRIEND_PAIRS:
        u = random.randint(1, N_USERS)
        v = random.randint(1, N_USERS)
        if u != v:
            unique_pairs.add((u, v))

    with open(os.path.join(TABLES_DIR, "friends.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO friends (user_id, friend_id) VALUES\n")
        lines = [f"({u}, {v})" for u, v in unique_pairs]
        f.write(",\n".join(lines) + ";")
    print(f"friends.sql created successfully. Total pairs: {len(unique_pairs)}")


def generate_messages() -> None:
    with open(os.path.join(TABLES_DIR, "messages.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO messages (message_id, sender_id, receiver_id, content, sent_at) VALUES\n")
        lines = []
        message_id = 1 
        attempts = 0

        while message_id <= N_MESSAGES:
            attempts += 1
            sender_id = random.randint(1, N_USERS)
            receiver_id = random.randint(1, N_USERS)
            if sender_id == receiver_id:
                continue 

            sent_at = datetime.now() - timedelta(days=random.randint(0, 365))
            sent_at_str = "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(
                sent_at.strftime("%Y-%m-%d %H:%M:%S")
            )
            content = f"Message {message_id} from user {sender_id} to user {receiver_id}"
            lines.append(f"({message_id}, {sender_id}, {receiver_id}, '{content}', {sent_at_str})")
            message_id += 1

        f.write(",\n".join(lines) + ";")
    print(f"messages.sql created successfully. Total messages: {len(lines)}")


def generate_library() -> None:
    with open(os.path.join(TABLES_DIR, "library.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO library (game_id, user_id, purchase_id, added_date) VALUES\n")
        lines = []
        for purchase_id, user_id in purchase_to_user.items():
            added_date_str = "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(
                purchase_to_date[purchase_id]
            )
            for game_id in purchase_to_games.get(purchase_id, []):
                lines.append(f"({game_id}, {user_id}, {purchase_id}, {added_date_str})")
        f.write(",\n".join(lines) + ";")
    print(f"library.sql created successfully. Total entries: {len(lines)}")


def generate_sessions() -> None:
    with open(os.path.join(TABLES_DIR, "sessions.sql"), "w", encoding="utf-8") as f:
        f.write("INSERT INTO sessions (session_id, user_id, game_id, start_time, end_time) VALUES\n")
        lines = []
        session_id = 1

        for purchase_id, user_id in purchase_to_user.items():
            purchase_dt = datetime.strptime(purchase_to_date[purchase_id], "%Y-%m-%d %H:%M:%S")
            for game_id in purchase_to_games.get(purchase_id, []):
                start_time = purchase_dt + timedelta(minutes=random.randint(0, 1440))
                end_time = start_time + timedelta(minutes=random.randint(5, 180))
                lines.append(
                    f"({session_id}, {user_id}, {game_id}, "
                    f"TO_DATE('{start_time.strftime('%Y-%m-%d %H:%M:%S')}', 'YYYY-MM-DD HH24:MI:SS'), "
                    f"TO_DATE('{end_time.strftime('%Y-%m-%d %H:%M:%S')}', 'YYYY-MM-DD HH24:MI:SS'))"
                )
                session_id += 1

        f.write(",\n".join(lines) + ";")
    print(f"sessions.sql created successfully. Total sessions: {len(lines)}")


def generate_reviews() -> None:
    with open(os.path.join(TABLES_DIR, "reviews.sql"), "w", encoding="utf-8") as f:
        f.write(
            "INSERT INTO reviews (review_id, user_id, game_id, review_type, comment, review_date) VALUES\n"
        )
        lines = []
        review_id = 1

        for purchase_id, user_id in purchase_to_user.items():
            purchase_dt = datetime.strptime(purchase_to_date[purchase_id], "%Y-%m-%d %H:%M:%S")
            for game_id in purchase_to_games.get(purchase_id, []):
                review_date = purchase_dt + timedelta(days=random.randint(0, 30))
                review_date_str = "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(
                    review_date.strftime("%Y-%m-%d %H:%M:%S")
                )
                review_type = random.choice(["positive", "negative"])
                comment = f"This is a review for game {game_id} by user {user_id}."
                lines.append(
                    f"({review_id}, {user_id}, {game_id}, '{review_type}', '{comment}', {review_date_str})"
                )
                review_id += 1

        f.write(",\n".join(lines) + ";")
    print(f"reviews.sql created successfully. Total reviews: {len(lines)}")

def merge_sql_files() -> None:
    files_in_order = [
        os.path.join(TABLES_DIR, "developers.sql"),
        os.path.join(TABLES_DIR, "categories.sql"),
        os.path.join(TABLES_DIR, "games.sql"),
        os.path.join(TABLES_DIR, "game_categories.sql"),
        os.path.join(TABLES_DIR, "achievements.sql"),
        os.path.join(TABLES_DIR, "promotions.sql"),
        os.path.join(TABLES_DIR, "users.sql"),
        os.path.join(TABLES_DIR, "wallets.sql"),
        os.path.join(TABLES_DIR, "purchases.sql"),
        os.path.join(TABLES_DIR, "purchases_item.sql"),
        os.path.join(TABLES_DIR, "user_achievements.sql"),
        os.path.join(TABLES_DIR, "library.sql"),
        os.path.join(TABLES_DIR, "sessions.sql"),
        os.path.join(TABLES_DIR, "reviews.sql"),
        os.path.join(TABLES_DIR, "badges.sql"),
        os.path.join(TABLES_DIR, "friends.sql"),
        os.path.join(TABLES_DIR, "messages.sql"),
    ]

    with open(ALL_DATA_FILE, "w", encoding="utf-8") as out:
        for path in files_in_order:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                out.write(f"-- {os.path.basename(path)}\n")
                out.write(content)
                out.write("\n\n")
            except FileNotFoundError:
                print(f"  WARNING: {path} not found, skipping.")

    print(f"All SQL files merged into {ALL_DATA_FILE}")

def main() -> None:
    generate_users()
    generate_developers()
    generate_categories()
    generate_games()            
    generate_game_categories()
    generate_achievements()     
    generate_user_achievements()
    generate_wallets()
    generate_promotions()       
    generate_purchases()        
    generate_purchase_items()   
    generate_library()
    generate_sessions()
    generate_reviews()
    generate_badges()
    generate_friends()
    generate_messages()
    merge_sql_files()

if __name__ == "__main__":
    main()