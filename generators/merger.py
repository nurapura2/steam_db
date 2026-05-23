import os

def merge_sql_files(output_filename="data/all_data.sql", input_folder="data"):
    # Определяем ПРАВИЛЬНЫЙ порядок объединения (от независимых к зависимым)
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
        outfile.write("-- Глобальный скрипт загрузки данных\n")
        outfile.write("SET DEFINE OFF;\n\n") # Полезно для Oracle, чтобы не ругался на символ '&'

        for filename in order:
            filepath = os.path.join(input_folder, filename)
            
            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as infile:
                    outfile.write(f"-- START OF {filename} --\n")
                    outfile.write(infile.read())
                    outfile.write("\n\n")
                print(f"Добавлен: {filename}")
            else:
                print(f"Предупреждение: Файл {filename} не найден в папке {input_folder}")

    print(f"\nГотово! Все файлы объединены в: {output_filename}")

if __name__ == "__main__":
    merge_sql_files()