from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate carbon footprint based on transport type and distance
def calculate_carbon_footprint(transport_type, distance):
    if transport_type == 'car':
        carbon_per_km = 0.2  # kg CO2 per km for car
    elif transport_type == 'bus':
        carbon_per_km = 0.05  # kg CO2 per km for bus
    elif transport_type == 'flight':
        carbon_per_km = 0.2  # kg CO2 per km for flight
    else:
        return 0  # For unknown transport

    carbon_emissions = carbon_per_km * distance
    return carbon_emissions

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        transport_type = request.form['transport_type']
        distance = float(request.form['distance'])
        
        carbon_emissions = calculate_carbon_footprint(transport_type, distance)
        
        # Suggestions based on carbon emissions
        suggestions = ""
        if transport_type == 'car':
            suggestions = "Switch to public transport like buses to reduce emissions!"
        
        return render_template("index.html", carbon_emissions=carbon_emissions, suggestions=suggestions)
    return render_template("index.html", carbon_emissions=None, suggestions=None)

if __name__ == "__main__":
    app.run(debug=True)
