import json
import os

# File to store pollution reports
DATA_FILE = "pollution_reports.json"

# Load existing reports if the file exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        pollution_reports = json.load(file)
else:
    pollution_reports = []


def save_reports():
    with open(DATA_FILE, "w") as file:
        json.dump(pollution_reports, file, indent=4)


def report_plastic():
    location = input("Enter location (city or area name): ")
    item = input("Enter type of plastic item (e.g., bottle, bag, straw): ")
    quantity = int(input("Enter quantity found: "))

    report = {
        "location": location,
        "item": item,
        "quantity": quantity
    }
    pollution_reports.append(report)
    save_reports()  # Save after every report
    print("✅ Report added successfully!\n")


def view_summary():
    if not pollution_reports:
        print("No reports yet.\n")
        return

    total_items = 0
    location_count = {}

    for report in pollution_reports:
        total_items += report["quantity"]
        loc = report["location"]
        location_count[loc] = location_count.get(loc, 0) + report["quantity"]

    print(f"\n🌎 Total plastic items reported: {total_items}")
    print("📍 Pollution by location:")
    for loc, qty in location_count.items():
        print(f"   - {loc}: {qty} items")
    print()


def main():
    while True:
        print("Plastic Pollution Counter")
        print("1. Report plastic waste")
        print("2. View summary")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            report_plastic()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Goodbye! 🌟 Keep the Earth clean!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


# Start the program
main()
