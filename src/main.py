import csv
from datetime import datetime
import os
import configparser

def ask_question(statement):
    response = input(f"{statement}\nAnswer from 1 to 7 (1=Strongly Disagree, 7=Completely Agree): ")
    try:
        response = int(response)
        if 1 <= response <= 7:
            return response
        else:
            print("Please enter a number between 1 and 7.")
            return ask_question(statement)
    except ValueError:
        print("Please enter a valid number.")
        return ask_question(statement)

def read_config():
    config = configparser.ConfigParser()
    config_file = os.path.expanduser("~/.config/srhi.conf")

    if os.path.exists(config_file):
        config.read(config_file)
        return config.get('Settings', 'spreadsheet_path', fallback='habit_results.csv')
    else:
        return 'habit_results.csv'

def main():
    statements = [
        "I do frequently",
        "I do automatically",
        "I do without having to consciously remember",
        "that makes me feel weird if I do not do it",
        "I do without thinking",
        "that would require effort not to do it",
        "that belongs to my (daily, weekly, monthly) routine",
        "I start doing before I realize I'm doing it",
        "I would find hard not to do",
        "I have no need to think about doing",
        "that's typically me",
        "I have been doing for a long time",
    ]

    total_score = 0

    for statement in statements:
        score = ask_question(statement)
        total_score += score

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    spreadsheet_path = read_config()

    file_exists = os.path.isfile(spreadsheet_path)

    with open(spreadsheet_path, mode='a', newline='') as file:
        fieldnames = ['Date', 'Total Habit Score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({'Date': current_datetime, 'Total Habit Score': total_score})

    print("\nTotal Habit Score:", total_score)

if __name__ == "__main__":
    main()
