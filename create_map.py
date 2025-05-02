import json
import folium

# Load existing reports
with open("pollution_reports.json", "r") as file:
    pollution_reports = json.load(file)

# Coordinates for demo
location_coordinates = {
    "Mumbai": [19.0760, 72.8777],
    "Delhi": [28.7041, 77.1025],
    "Chennai": [13.0827, 80.2707],
    "Bangalore": [12.9716, 77.5946],
    "Kolkata": [22.5726, 88.3639]
}

# Create the map
pollution_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

for report in pollution_reports:
    loc = report["location"]
    qty = report["quantity"]

    if loc in location_coordinates:
        lat, lon = location_coordinates[loc]
        folium.Marker(
            location=[lat, lon],
            popup=f"{loc}: {qty} items",
            icon=folium.Icon(color="red" if qty > 10 else "green")
        ).add_to(pollution_map)

pollution_map.save("pollution_map.html")
print("🗺️ Pollution map created! Open 'pollution_map.html' to view it.")
