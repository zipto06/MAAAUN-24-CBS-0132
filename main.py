from models import FuelDispenser, CarWash

# Sample data
fuel_dispensers = [
    FuelDispenser(id=1, price_per_litre=1.50, litres_sold=1000),
    FuelDispenser(id=2, price_per_litre=1.60, litres_sold=800)
]

car_washes = [
    CarWash(id=1, price_per_wash=10.00, washes_done=200)
]

# Calculate total revenue
total_revenue = 0

def calculate_total_revenue(assets):
    global total_revenue
    for asset in assets:
        if isinstance(asset, FuelDispenser):
            total_revenue += asset.price_per_litre * asset.litres_sold
        elif isinstance(asset, CarWash):
            total_revenue += asset.price_per_wash * asset.washes_done

# Combine all assets
all_assets = fuel_dispensers + car_washes

# Calculate revenue
calculate_total_revenue(all_assets)

# Display total revenue
print(f'Total revenue of the station: ${total_revenue:.2f}')