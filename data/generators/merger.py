import os

def merge_sql_files(output_filename="data/all_data.sql", input_folder="data"):
    # Define the correct merge order (from independent to dependent tables)
    order = [
        "users.sql",
        "developers.sql",
        "categories.sql",
        "games.sql",
        "game_categories.sql",
        "achievements.sql",
        "promotions.sql",
        "wallets.sql",
        "friends.sql",
        "badges.sql",
        "messages.sql",
        "purchases.sql",
        "purchases_item.sql",
        "user_achievements.sql",
        "library.sql",
        "sessions.sql",
        "reviews.sql"
    ]

    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write("-- Global data load script\n")
        outfile.write("SET DEFINE OFF;\n\n")  # Prevents Oracle from treating '&' as a substitution variable
        for filename in order:
            filepath = os.path.join(input_folder, filename)

            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as infile:
                    outfile.write(f"-- START OF {filename} --\n")
                    outfile.write(infile.read())
                    outfile.write("\n\n")
                print(f"Added: {filename}")
            else:
                print(f"Warning: File {filename} not found in folder '{input_folder}'")

    print(f"\nDone! All files merged into: {output_filename}")

if __name__ == "__main__":
    merge_sql_files()