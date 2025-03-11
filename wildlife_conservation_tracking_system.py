"""
Wildlife Conservation Tracking System
This program demonstrates dictionary operations through a wildlife conservation data system.
"""

def initialize_data():
    """
    Initialize the species data with predefined species using dictionaries.
    
    Returns:
        tuple: A tuple containing (species_data, new_species) dictionaries
    """
    # Create the main species data dictionary
    species_data = {
        "SP001": {
            "name": "Bengal Tiger",
            "scientific_name": "Panthera tigris tigris",
            "conservation_status": "Endangered",
            "population": 3500,
            "habitat_type": "Forest",
            "sanctuaries": ["Sundarbans", "Jim Corbett", "Bandhavgarh"],
            "threats": ["Poaching", "Habitat Loss", "Human Conflict"]
        },
        "SP002": {
            "name": "Asian Elephant",
            "scientific_name": "Elephas maximus",
            "conservation_status": "Endangered",
            "population": 27000,
            "habitat_type": "Forest",
            "sanctuaries": ["Periyar", "Nagarhole", "Jim Corbett"],
            "threats": ["Habitat Loss", "Human Conflict", "Poaching"]
        },
        "SP003": {
            "name": "Indian Rhinoceros",
            "scientific_name": "Rhinoceros unicornis",
            "conservation_status": "Vulnerable",
            "population": 3600,
            "habitat_type": "Grassland",
            "sanctuaries": ["Kaziranga", "Manas", "Orang"],
            "threats": ["Poaching", "Habitat Loss", "Flooding"]
        },
        "SP004": {
            "name": "Snow Leopard",
            "scientific_name": "Panthera uncia",
            "conservation_status": "Vulnerable",
            "population": 450,
            "habitat_type": "Mountain",
            "sanctuaries": ["Hemis", "Pin Valley", "Great Himalayan"],
            "threats": ["Climate Change", "Poaching", "Prey Depletion"]
        },
        "SP005": {
            "name": "Indian Vulture",
            "scientific_name": "Gyps indicus",
            "conservation_status": "Critically Endangered",
            "population": 30000,
            "habitat_type": "Grassland",
            "sanctuaries": ["Ranthambore", "Pench", "Bandhavgarh"],
            "threats": ["Diclofenac Poisoning", "Habitat Loss", "Food Scarcity"]
        }
    }
    
    # Create new species to be added later
    new_species = {
        "NS001": {
            "name": "Ganges River Dolphin",
            "scientific_name": "Platanista gangetica",
            "conservation_status": "Endangered",
            "population": 3500,
            "habitat_type": "Wetland",
            "sanctuaries": ["Vikramshila", "National Chambal", "Katerniaghat"],
            "threats": ["Water Pollution", "Fishing Nets", "Dams"]
        },
        "NS002": {
            "name": "Great Indian Bustard",
            "scientific_name": "Ardeotis nigriceps",
            "conservation_status": "Critically Endangered",
            "population": 150,
            "habitat_type": "Grassland",
            "sanctuaries": ["Desert National Park", "Kutch Bustard", "Rollapadu"],
            "threats": ["Habitat Loss", "Power Lines", "Predation"]
        }
    }
    
    return species_data, new_species

def filter_by_conservation_status(species_data, status):
    """
    Filter species by conservation status using dictionary comprehension.
    
    Args:
        species_data (dict): The species data dictionary
        status (str): Conservation status to filter by
    
    Returns:
        dict: Filtered species dictionary
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if status is None:
        raise ValueError("Conservation status cannot be None")
    
    return {sid: species for sid, species in species_data.items() 
            if species["conservation_status"] == status}

def filter_by_population_range(species_data, min_population, max_population):
    """
    Filter species by population range using dictionary comprehension.
    
    Args:
        species_data (dict): The species data dictionary
        min_population (int): Minimum population
        max_population (int): Maximum population
    
    Returns:
        dict: Filtered species dictionary
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if min_population is None or max_population is None:
        raise ValueError("Population range cannot be None")
    if min_population < 0:
        raise ValueError("Minimum population cannot be negative")
    if min_population > max_population:
        raise ValueError("Minimum population cannot be greater than maximum population")
    
    return {sid: species for sid, species in species_data.items() 
            if min_population <= species["population"] <= max_population}

def filter_by_habitat_type(species_data, habitat_type):
    """
    Filter species by habitat type using dictionary comprehension.
    
    Args:
        species_data (dict): The species data dictionary
        habitat_type (str): Habitat type to filter by
    
    Returns:
        dict: Filtered species dictionary
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if habitat_type is None:
        raise ValueError("Habitat type cannot be None")
    
    return {sid: species for sid, species in species_data.items() 
            if species["habitat_type"] == habitat_type}

def filter_by_sanctuary(species_data, sanctuary):
    """
    Filter species by sanctuary using dictionary comprehension.
    
    Args:
        species_data (dict): The species data dictionary
        sanctuary (str): Sanctuary to filter by
    
    Returns:
        dict: Filtered species dictionary
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if sanctuary is None:
        raise ValueError("Sanctuary cannot be None")
    
    return {sid: species for sid, species in species_data.items() 
            if sanctuary in species["sanctuaries"]}

def find_species_with_keyword(species_data, keyword):
    """
    Find species containing a keyword in their name, scientific name, or threats.
    
    Args:
        species_data (dict): The species data dictionary
        keyword (str): Keyword to search for
    
    Returns:
        dict: Filtered species dictionary
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if keyword is None:
        raise ValueError("Keyword cannot be None")
    
    keyword = keyword.lower()
    return {sid: species for sid, species in species_data.items() 
            if keyword in species["name"].lower() or 
               keyword in species["scientific_name"].lower() or
               any(keyword in threat.lower() for threat in species["threats"])}

def update_species_population(species_data, species_id, new_population):
    """
    Update a species' population.
    
    Args:
        species_data (dict): The species data dictionary
        species_id (str): Species ID to update
        new_population (int): New population count
    
    Returns:
        dict: Updated species data dictionary
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if species_id is None:
        raise ValueError("Species ID cannot be None")
    if new_population is None or new_population < 0:
        raise ValueError("New population cannot be None or negative")
    
    if species_id not in species_data:
        raise ValueError(f"Species ID {species_id} not found")
    
    # Create a new dictionary with the updated population
    updated_species_data = species_data.copy()
    updated_species_data[species_id] = {**updated_species_data[species_id], "population": new_population}
    
    return updated_species_data

def update_conservation_status(species_data, species_id, new_status):
    """
    Update a species' conservation status.
    
    Args:
        species_data (dict): The species data dictionary
        species_id (str): Species ID to update
        new_status (str): New conservation status
    
    Returns:
        dict: Updated species data dictionary
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if species_id is None:
        raise ValueError("Species ID cannot be None")
    if new_status is None:
        raise ValueError("New conservation status cannot be None")
    
    valid_statuses = ["Least Concern", "Near Threatened", "Vulnerable", "Endangered", "Critically Endangered"]
    if new_status not in valid_statuses:
        raise ValueError(f"Invalid conservation status. Must be one of {valid_statuses}")
    
    if species_id not in species_data:
        raise ValueError(f"Species ID {species_id} not found")
    
    # Create a new dictionary with the updated conservation status
    updated_species_data = species_data.copy()
    updated_species_data[species_id] = {**updated_species_data[species_id], "conservation_status": new_status}
    
    return updated_species_data

def add_species_threat(species_data, species_id, new_threat):
    """
    Add a new threat to a species.
    
    Args:
        species_data (dict): The species data dictionary
        species_id (str): Species ID to update
        new_threat (str): New threat to add
    
    Returns:
        dict: Updated species data dictionary
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if species_id is None:
        raise ValueError("Species ID cannot be None")
    if new_threat is None or new_threat == "":
        raise ValueError("New threat cannot be None or empty")
    
    if species_id not in species_data:
        raise ValueError(f"Species ID {species_id} not found")
    
    # Create a new dictionary with the updated threats
    updated_species_data = species_data.copy()
    if new_threat not in updated_species_data[species_id]["threats"]:
        updated_threats = updated_species_data[species_id]["threats"].copy()
        updated_threats.append(new_threat)
        updated_species_data[species_id] = {**updated_species_data[species_id], "threats": updated_threats}
    
    return updated_species_data

def merge_species_data(existing_species, new_species):
    """
    Merge two species data dictionaries with transformation.
    
    Args:
        existing_species (dict): The existing species data dictionary
        new_species (dict): New species to add
    
    Returns:
        dict: Merged species data dictionary
    """
    if existing_species is None or new_species is None:
        raise ValueError("Species data dictionaries cannot be None")
    
    # Create a copy of the existing species data
    merged_species_data = existing_species.copy()
    
    # Add new species with a "newly_added" flag
    for sid, species in new_species.items():
        merged_species_data[sid] = {**species, "newly_added": True}
    
    return merged_species_data

def calculate_status_counts(species_data):
    """
    Calculate the number of species in each conservation status.
    
    Args:
        species_data (dict): The species data dictionary
    
    Returns:
        dict: Dictionary with conservation statuses as keys and counts as values
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    
    status_counts = {}
    for species in species_data.values():
        status = species["conservation_status"]
        if status in status_counts:
            status_counts[status] += 1
        else:
            status_counts[status] = 1
    
    return status_counts

def calculate_total_population(species_data):
    """
    Calculate the total population across all species.
    
    Args:
        species_data (dict): The species data dictionary
    
    Returns:
        int: Total population count
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    
    return sum(species["population"] for species in species_data.values())

def find_most_threatened_species(species_data):
    """
    Find the most threatened species (based on conservation status and population).
    
    Args:
        species_data (dict): The species data dictionary
    
    Returns:
        tuple: (species_id, species_data) of the most threatened species
    """
    if species_data is None or not species_data:
        raise ValueError("Species data cannot be None or empty")
    
    # Define an order for conservation statuses (higher index = more threatened)
    status_order = {
        "Least Concern": 0,
        "Near Threatened": 1,
        "Vulnerable": 2,
        "Endangered": 3,
        "Critically Endangered": 4
    }
    
    # Sort by conservation status first, then by population (ascending)
    def threat_key(item):
        sid, species = item
        return (status_order[species["conservation_status"]], -species["population"])
    
    return max(species_data.items(), key=threat_key)

def create_population_brackets(species_data):
    """
    Group species into population brackets.
    
    Args:
        species_data (dict): The species data dictionary
    
    Returns:
        dict: Dictionary with population brackets as keys and lists of species IDs as values
    """
    if species_data is None:
        raise ValueError("Species data cannot be None")
    
    population_brackets = {
        "critical": [],       # 0-500
        "endangered": [],    # 501-5000
        "vulnerable": [],    # 5001-20000
        "stable": []         # 20001+
    }
    
    for sid, species in species_data.items():
        population = species["population"]
        if population <= 500:
            population_brackets["critical"].append(sid)
        elif population <= 5000:
            population_brackets["endangered"].append(sid)
        elif population <= 20000:
            population_brackets["vulnerable"].append(sid)
        else:
            population_brackets["stable"].append(sid)
    
    return population_brackets

def get_formatted_species(sid, species):
    """
    Format a species for display.
    
    Args:
        sid (str): Species ID
        species (dict): Species data
    
    Returns:
        str: Formatted species string
    """
    if species is None:
        raise ValueError("Species data cannot be None")
    
    # Format population with thousands separator
    formatted_population = f"{species['population']:,}"
    
    # Format sanctuaries and threats as comma-separated strings
    sanctuaries = ", ".join(species["sanctuaries"])
    threats = ", ".join(species["threats"])
    
    # Format the newly added flag if present
    newly_added = " [NEW]" if species.get("newly_added", False) else ""
    
    # Return formatted string
    return (
        f"{sid} | {species['name']}{newly_added} ({species['scientific_name']}) | "
        f"{species['conservation_status']} | Population: {formatted_population} | "
        f"Habitat: {species['habitat_type']} | Sanctuaries: {sanctuaries} | "
        f"Threats: {threats}"
    )

def display_data(data, data_type):
    """
    Display formatted data based on data type.
    
    Args:
        data: Data to display (dict, tuple, etc.)
        data_type (str): Type of data being displayed
    """
    if data is None:
        print("No data to display.")
        return
    
    if data_type == "species" or data_type == "filtered":
        header = "\nCurrent Species Data:" if data_type == "species" else "\nFiltered Results:"
        print(header)
        
        if not data:
            print("No species to display.")
            return
        
        for sid, species in data.items():
            print(get_formatted_species(sid, species))
    
    elif data_type == "status_counts":
        print("\nConservation Status Counts:")
        for status, count in data.items():
            print(f"{status}: {count} species")
    
    elif data_type == "population_brackets":
        print("\nPopulation Brackets:")
        for bracket, species_ids in data.items():
            print(f"{bracket}: {len(species_ids)} species")
            if species_ids:
                print(f"  Species IDs: {', '.join(species_ids)}")
    
    elif data_type == "most_threatened":
        print("\nMost Threatened Species:")
        sid, species = data
        print(get_formatted_species(sid, species))
    
    elif data_type == "total_population":
        print(f"\nTotal Population Across All Species: {data:,}")
    
    else:
        print(f"\n{data_type}:")
        print(data)

def main():
    """Main program function."""
    species_data, new_species = initialize_data()
    
    while True:
        # Show basic info about the data
        statuses = set(species["conservation_status"] for species in species_data.values())
        
        print(f"\n===== WILDLIFE CONSERVATION TRACKING SYSTEM =====")
        print(f"Total Species: {len(species_data)}")
        print(f"Conservation Statuses: {', '.join(sorted(statuses))}")
        
        print("\nMain Menu:")
        print("1. View Species Data")
        print("2. Filter Species")
        print("3. Update Species Data")
        print("4. Add New Species")
        print("5. View Conservation Statistics")
        print("0. Exit")
        
        choice = input("Enter your choice (0-5): ")
        
        if choice == "0":
            print("Thank you for using the Wildlife Conservation Tracking System!")
            break
        
        elif choice == "1":
            display_data(species_data, "species")
        
        elif choice == "2":
            print("\nFilter Options:")
            print("1. Filter by Conservation Status")
            print("2. Filter by Population Range")
            print("3. Filter by Habitat Type")
            print("4. Filter by Sanctuary")
            print("5. Search by Keyword")
            filter_choice = input("Select filter option (1-5): ")
            
            if filter_choice == "1":
                status = input("Enter conservation status to filter by: ")
                filtered = filter_by_conservation_status(species_data, status)
                display_data(filtered, "filtered")
            
            elif filter_choice == "2":
                try:
                    min_population = int(input("Enter minimum population: "))
                    max_population = int(input("Enter maximum population: "))
                    filtered = filter_by_population_range(species_data, min_population, max_population)
                    display_data(filtered, "filtered")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif filter_choice == "3":
                habitat_type = input("Enter habitat type to filter by: ")
                filtered = filter_by_habitat_type(species_data, habitat_type)
                display_data(filtered, "filtered")
            
            elif filter_choice == "4":
                sanctuary = input("Enter sanctuary to filter by: ")
                filtered = filter_by_sanctuary(species_data, sanctuary)
                display_data(filtered, "filtered")
            
            elif filter_choice == "5":
                keyword = input("Enter keyword to search for: ")
                filtered = find_species_with_keyword(species_data, keyword)
                display_data(filtered, "filtered")
            
            else:
                print("Invalid choice.")
        
        elif choice == "3":
            print("\nUpdate Options:")
            print("1. Update Species Population")
            print("2. Update Conservation Status")
            print("3. Add Species Threat")
            update_choice = input("Select update option (1-3): ")
            
            if update_choice == "1":
                try:
                    sid = input("Enter species ID to update: ")
                    new_population = int(input("Enter new population: "))
                    species_data = update_species_population(species_data, sid, new_population)
                    print(f"Population updated for species {sid}.")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif update_choice == "2":
                try:
                    sid = input("Enter species ID to update: ")
                    print("Valid statuses: Least Concern, Near Threatened, Vulnerable, Endangered, Critically Endangered")
                    new_status = input("Enter new conservation status: ")
                    species_data = update_conservation_status(species_data, sid, new_status)
                    print(f"Conservation status updated for species {sid}.")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif update_choice == "3":
                try:
                    sid = input("Enter species ID to update: ")
                    new_threat = input("Enter new threat to add: ")
                    species_data = add_species_threat(species_data, sid, new_threat)
                    print(f"Threat added to species {sid}.")
                except ValueError as e:
                    print(f"Error: {e}")
            
            else:
                print("Invalid choice.")
        
        elif choice == "4":
            try:
                print("\nAdding new species to the database...")
                species_data = merge_species_data(species_data, new_species)
                print(f"{len(new_species)} new species added to database.")
                # Clear new_species after adding
                new_species = {}
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "5":
            print("\nStatistics Options:")
            print("1. Conservation Status Counts")
            print("2. Total Population Count")
            print("3. Most Threatened Species")
            print("4. Population Brackets")
            stats_choice = input("Select statistics option (1-4): ")
            
            if stats_choice == "1":
                status_counts = calculate_status_counts(species_data)
                display_data(status_counts, "status_counts")
            
            elif stats_choice == "2":
                total_population = calculate_total_population(species_data)
                display_data(total_population, "total_population")
            
            elif stats_choice == "3":
                most_threatened = find_most_threatened_species(species_data)
                display_data(most_threatened, "most_threatened")
            
            elif stats_choice == "4":
                population_brackets = create_population_brackets(species_data)
                display_data(population_brackets, "population_brackets")
            
            else:
                print("Invalid choice.")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()