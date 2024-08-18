from models import storage
from models.state import State
from models.city import City

# Get the State instance
state_id = 'some_state_id'  # Replace with actual state ID
states = list(storage.all(State).values())
for state in states:
    if state:
        # Retrieve all City objects from storage
        all_cities = storage.all(City)
    
        # Check if any City objects have the matching state_id
        cities = [city for city in all_cities.values() if city.state_id == state.id]

        if cities:
            for city in cities:
                print(f"City: {city.name}, State: {state.name}")
        else:
            print("No cities found for this state.")

