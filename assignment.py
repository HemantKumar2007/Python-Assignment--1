# tracker.py
# Author: [Your Name]
# Date: 2025-11-06
# Project: Daily Calorie Tracker CLI

import datetime

def print_welcome():
    print("Welcome to the Daily Calorie Tracker CLI app!")
    print("You can log your meals and calories, track totals, and compare against your daily calorie limit.\n")


def collect_meals():
    meal_names = []
    meal_calories = []
    num_meals = int(input("How many meals do you want to enter? "))
    for i in range(num_meals):
        name = input(f"Enter name for meal {i+1}: ")
        cal = float(input(f"Enter calories for {name}: "))
        meal_names.append(name)
        meal_calories.append(cal)
    return meal_names, meal_calories


def calculate_stats(calories):
    total = sum(calories)
    average = total / len(calories) if calories else 0
    return total, average


def check_limit(total_calories):
    limit = float(input("Enter your daily calorie limit: "))
    if total_calories > limit:
        print(f"Warning: You have exceeded your daily calorie limit by {total_calories - limit:.2f} calories!")
        status = "Exceeded"
    else:
        print(f"Success: You are within your daily calorie limit by {limit - total_calories:.2f} calories.")
        status = "Within Limit"
    return limit, status


def print_report(meals, calories, total, average):
    print("\nCalorie Intake Summary")
    print(f"{'Meal Name':<15}{'Calories':>10}")
    print("-" * 25)
    for meal, cal in zip(meals, calories):
        print(f"{meal:<15}{cal:>10.2f}")
    print("-" * 25)
    print(f"{'Total':<15}{total:>10.2f}")
    print(f"{'Average':<15}{average:>10.2f}")


def save_log(meals, calories, total, average, limit, status):
    save = input("Do you want to save the session log to a file? (yes/no) ").strip().lower()
    if save == 'yes':
        filename = "calorielog.txt"
        with open(filename, "w") as file:
            file.write("Daily Calorie Tracker Session Log\n")
            file.write(f"Timestamp: {datetime.datetime.now()}\n\n")
            file.write(f"{'Meal Name':<15}{'Calories':>10}\n")
            file.write("-" * 25 + "\n")
            for meal, cal in zip(meals, calories):
                file.write(f"{meal:<15}{cal:>10.2f}\n")
            file.write("-" * 25 + "\n")
            file.write(f"{'Total':<15}{total:>10.2f}\n")
            file.write(f"{'Average':<15}{average:>10.2f}\n")
            file.write(f"Daily Calorie Limit: {limit:.2f}\n")
            file.write(f"Status: {status}\n")
        print(f"Session log saved to {filename}")


def main():
    print_welcome()
    meals, calories = collect_meals()
    total, average = calculate_stats(calories)
    limit, status = check_limit(total)
    print_report(meals, calories, total, average)
    save_log(meals, calories, total, average, limit, status)


if __name__ == "__main__":
    main()
