"""
Wildlife Conservation Tracking System

This program demonstrates dictionary operations through a wildlife conservation data system.
The system tracks endangered species across various wildlife sanctuaries in India, monitoring
animal populations, habitat conditions, conservation efforts, and generating analytical reports.

Each species has the following attributes:
- name: Common name of the species
- scientific_name: Scientific classification name
- conservation_status: IUCN conservation status level
- population: Current estimated population count
- habitat_type: Primary habitat where the species is found
- sanctuaries: List of wildlife sanctuaries where the species is protected
- threats: List of current threats facing the species
"""

def initialize_data():
    """
    Initialize the species data with predefined species using dictionaries.
    
    Returns:
        tuple: A tuple containing (species_data, new_species) dictionaries
    """
    # TODO: Create the main species data dictionary with these exact species:
    # SP001: Bengal Tiger (Panthera tigris tigris, Endangered, 3500 population, Forest habitat)
    #        Sanctuaries: ["Sundarbans", "Jim Corbett", "Bandhavgarh"]
    #        Threats: ["Poaching", "Habitat Loss", "Human Conflict"]
    # SP002: Asian Elephant (Elephas maximus, Endangered, 27000 population, Forest habitat)
    #        Sanctuaries: ["Periyar", "Nagarhole", "Jim Corbett"]
    #        Threats: ["Habitat Loss", "Human Conflict", "Poaching"]
    # SP003: Indian Rhinoceros (Rhinoceros unicornis, Vulnerable, 3600 population, Grassland habitat)
    #        Sanctuaries: ["Kaziranga", "Manas", "Orang"]
    #        Threats: ["Poaching", "Habitat Loss", "Flooding"]
    # SP004: Snow Leopard (Panthera uncia, Vulnerable, 450 population, Mountain habitat)
    #        Sanctuaries: ["Hemis", "Pin Valley", "Great Himalayan"]
    #        Threats: ["Climate Change", "Poaching", "Prey Depletion"]
    # SP005: Indian Vulture (Gyps indicus, Critically Endangered, 30000 population, Grassland habitat)
    #        Sanctuaries: ["Ranthambore", "Pench", "Bandhavgarh"]
    #        Threats: ["Diclofenac Poisoning", "Habitat Loss", "Food Scarcity"]
    species_data = {}
    
    # TODO: Create new species dictionary with these exact species:
    # NS001: Ganges River Dolphin (Platanista gangetica, Endangered, 3500 population, Wetland habitat)
    #        Sanctuaries: ["Vikramshila", "National Chambal", "Katerniaghat"]
    #        Threats: ["Water Pollution", "Fishing Nets", "Dams"]
    # NS002: Great Indian Bustard (Ardeotis nigriceps, Critically Endangered, 150 population, Grassland habitat)
    #        Sanctuaries: ["Desert National Park", "Kutch Bustard", "Rollapadu"]
    #        Threats: ["Habitat Loss", "Power Lines", "Predation"]
    new_species = {}
    
    return species_data, new_species

def filter_by_conservation_status(species_data, status):
    """
    Filter species by conservation status using dictionary comprehension.
    
    Args:
        species_data (dict): The species data dictionary
        status (str): Conservation status to filter by
    
    Returns:
        dict: Filtered species dictionary
    
    Raises:
        ValueError: If species_data or status is None
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if status is None:
        raise ValueError("Conservation status cannot be None")
    
    # TODO: Implement dictionary comprehension to filter by conservation status
    # Hint: Use {sid: species for sid, species in species_data.items() if condition}
    # Valid statuses: "Least Concern", "Near Threatened", "Vulnerable", "Endangered", "Critically Endangered"
    
    return {}

def filter_by_population_range(species_data, min_population, max_population):
    """
    Filter species by population range using dictionary comprehension.
    
    Args:
        species_data (dict): The species data dictionary
        min_population (int): Minimum population
        max_population (int): Maximum population
    
    Returns:
        dict: Filtered species dictionary
    
    Raises:
        ValueError: If inputs are None, min_population is negative, or min > max
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if min_population is None or max_population is None:
        raise ValueError("Population range cannot be None")
    if min_population < 0:
        raise ValueError("Minimum population cannot be negative")
    if min_population > max_population:
        raise ValueError("Minimum population cannot be greater than maximum population")
    
    # TODO: Implement dictionary comprehension to filter by population range
    # Hint: Filter species where min_population <= species["population"] <= max_population
    
    return {}

def filter_by_habitat_type(species_data, habitat_type):
    """
    Filter species by habitat type using dictionary comprehension.
    
    Args:
        species_data (dict): The species data dictionary
        habitat_type (str): Habitat type to filter by
    
    Returns:
        dict: Filtered species dictionary
    
    Raises:
        ValueError: If species_data or habitat_type is None
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if habitat_type is None:
        raise ValueError("Habitat type cannot be None")
    
    # TODO: Implement dictionary comprehension to filter by habitat type
    # Valid habitat types: "Forest", "Grassland", "Wetland", "Mountain", "Desert"
    
    return {}

def filter_by_sanctuary(species_data, sanctuary):
    """
    Filter species by sanctuary using dictionary comprehension.
    
    Args:
        species_data (dict): The species data dictionary
        sanctuary (str): Sanctuary to filter by
    
    Returns:
        dict: Filtered species dictionary
    
    Raises:
        ValueError: If species_data or sanctuary is None
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if sanctuary is None:
        raise ValueError("Sanctuary cannot be None")
    
    # TODO: Implement dictionary comprehension to filter by sanctuary
    # Hint: Check if sanctuary is in the species["sanctuaries"] list
    
    return {}

def find_species_with_keyword(species_data, keyword):
    """
    Find species containing a keyword in their name, scientific name, or threats.
    
    Args:
        species_data (dict): The species data dictionary
        keyword (str): Keyword to search for
    
    Returns:
        dict: Filtered species dictionary
    
    Raises:
        ValueError: If species_data or keyword is None
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if keyword is None:
        raise ValueError("Keyword cannot be None")
    
    # TODO: Implement dictionary comprehension with keyword search
    # Hint: Convert keyword to lowercase and search in name, scientific_name, and threats
    # Hint: Use any() function to check if keyword is in any of the threats
    
    return {}

def update_species_population(species_data, species_id, new_population):
    """
    Update a species' population.
    
    Args:
        species_data (dict): The species data dictionary
        species_id (str): Species ID to update
        new_population (int): New population count
    
    Returns:
        dict: Updated species data dictionary
    
    Raises:
        ValueError: If inputs are invalid or species_id not found
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if species_id is None:
        raise ValueError("Species ID cannot be None")
    if new_population is None or new_population < 0:
        raise ValueError("New population cannot be None or negative")
    
    # TODO: Check if species exists
    if species_id not in species_data:
        raise ValueError(f"Species ID {species_id} not found")
    
    # TODO: Create a new dictionary with the updated population
    # Hint: Use .copy() to create a copy of the original dictionary
    # Hint: Use dictionary unpacking (**) to update the specific species
    # Example: updated_species_data[species_id] = {**species_data[species_id], "population": new_population}
    
    return {}

def update_conservation_status(species_data, species_id, new_status):
    """
    Update a species' conservation status.
    
    Args:
        species_data (dict): The species data dictionary
        species_id (str): Species ID to update
        new_status (str): New conservation status
    
    Returns:
        dict: Updated species data dictionary
    
    Raises:
        ValueError: If inputs are invalid, status is invalid, or species_id not found
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if species_id is None:
        raise ValueError("Species ID cannot be None")
    if new_status is None:
        raise ValueError("New conservation status cannot be None")
    
    # TODO: Validate conservation status
    valid_statuses = ["Least Concern", "Near Threatened", "Vulnerable", "Endangered", "Critically Endangered"]
    if new_status not in valid_statuses:
        raise ValueError(f"Invalid conservation status. Must be one of {valid_statuses}")
    
    # TODO: Check if species exists
    if species_id not in species_data:
        raise ValueError(f"Species ID {species_id} not found")
    
    # TODO: Create a new dictionary with the updated conservation status
    # Hint: Use dictionary unpacking to update the conservation_status field
    
    return {}

def add_species_threat(species_data, species_id, new_threat):
    """
    Add a new threat to a species.
    
    Args:
        species_data (dict): The species data dictionary
        species_id (str): Species ID to update
        new_threat (str): New threat to add
    
    Returns:
        dict: Updated species data dictionary
    
    Raises:
        ValueError: If inputs are invalid or species_id not found
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    if species_id is None:
        raise ValueError("Species ID cannot be None")
    if new_threat is None or new_threat == "":
        raise ValueError("New threat cannot be None or empty")
    
    # TODO: Check if species exists
    if species_id not in species_data:
        raise ValueError(f"Species ID {species_id} not found")
    
    # TODO: Create a new dictionary with the updated threats
    # Hint: Check if threat already exists to avoid duplicates
    # Hint: Create a copy of the threats list and append the new threat
    # Hint: Use dictionary unpacking to update the threats field
    
    return {}

def merge_species_data(existing_species, new_species):
    """
    Merge two species data dictionaries with transformation.
    
    Args:
        existing_species (dict): The existing species data dictionary
        new_species (dict): New species to add
    
    Returns:
        dict: Merged species data dictionary
    
    Raises:
        ValueError: If either dictionary is None
    """
    # TODO: Input validation
    if existing_species is None or new_species is None:
        raise ValueError("Species data dictionaries cannot be None")
    
    # TODO: Create a copy of the existing species data
    # TODO: Add new species with a "newly_added" flag set to True
    # Hint: Use dictionary unpacking to add the newly_added flag
    # Example: merged_species_data[sid] = {**species, "newly_added": True}
    
    return {}

def calculate_status_counts(species_data):
    """
    Calculate the number of species in each conservation status.
    
    Args:
        species_data (dict): The species data dictionary
    
    Returns:
        dict: Dictionary with conservation statuses as keys and counts as values
    
    Raises:
        ValueError: If species_data is None
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    
    # TODO: Create a dictionary to count species in each conservation status
    # Hint: Iterate through species_data.values() and count each status
    # Hint: Use dictionary.get() method or if/else to handle counting
    
    return {}

def calculate_total_population(species_data):
    """
    Calculate the total population across all species.
    
    Args:
        species_data (dict): The species data dictionary
    
    Returns:
        int: Total population count
    
    Raises:
        ValueError: If species_data is None
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    
    # TODO: Calculate and return the total population
    # Hint: Use sum() with a generator expression
    # Example: sum(species["population"] for species in species_data.values())
    
    return 0

def find_most_threatened_species(species_data):
    """
    Find the most threatened species (based on conservation status and population).
    
    Args:
        species_data (dict): The species data dictionary
    
    Returns:
        tuple: (species_id, species_data) of the most threatened species
    
    Raises:
        ValueError: If species_data is None or empty
    """
    # TODO: Input validation
    if species_data is None or not species_data:
        raise ValueError("Species data cannot be None or empty")
    
    # TODO: Define conservation status threat levels
    # Hint: Create a dictionary mapping status to threat level (higher number = more threatened)
    status_order = {
        "Least Concern": 0,
        "Near Threatened": 1,
        "Vulnerable": 2,
        "Endangered": 3,
        "Critically Endangered": 4
    }
    
    # TODO: Find the most threatened species
    # Hint: Use max() with a custom key function
    # Hint: Sort by conservation status first, then by population (lower population = more threatened)
    
    return ("", {})

def create_population_brackets(species_data):
    """
    Group species into population brackets.
    
    Args:
        species_data (dict): The species data dictionary
    
    Returns:
        dict: Dictionary with population brackets as keys and lists of species IDs as values
    
    Raises:
        ValueError: If species_data is None
    """
    # TODO: Input validation
    if species_data is None:
        raise ValueError("Species data cannot be None")
    
    # TODO: Create population brackets dictionary
    population_brackets = {
        "critical": [],       # 0-500
        "endangered": [],    # 501-5000
        "vulnerable": [],    # 5001-20000
        "stable": []         # 20001+
    }
    
    # TODO: Categorize each species into the appropriate population bracket
    # Hint: Iterate through species_data.items() and check population ranges
    
    return population_brackets

def get_formatted_species(sid, species):
    """
    Format a species for display.
    
    Args:
        sid (str): Species ID
        species (dict): Species data
    
    Returns:
        str: Formatted species string
    
    Raises:
        ValueError: If species is None
    """
    # TODO: Input validation
    if species is None:
        raise ValueError("Species data cannot be None")
    
    # TODO: Format the species for display
    # Hint: Format population with thousands separator using f"{population:,}"
    # Hint: Join sanctuaries and threats lists with commas
    # Hint: Check for "newly_added" flag and add [NEW] tag if present
    # Expected format: "SP001 | Bengal Tiger [NEW] (Panthera tigris tigris) | Endangered | Population: 3,500 | Habitat: Forest | Sanctuaries: ... | Threats: ..."
    
    return ""

def display_data(data, data_type):
    """
    Display formatted data based on data type.
    
    Args:
        data: Data to display (dict, tuple, etc.)
        data_type (str): Type of data being displayed
    """
    # TODO: Handle None data
    if data is None:
        print("No data to display.")
        return
    
    # TODO: Implement display logic for different data types:
    # "species" or "filtered" - display formatted species using get_formatted_species()
    # "status_counts" - display conservation status counts
    # "population_brackets" - display species in each population bracket
    # "most_threatened" - display the most threatened species
    # "total_population" - display the total population
    
    pass

def main():
    """Main program function."""
    # TODO: Initialize system data
    species_data, new_species = initialize_data()
    
    while True:
        # TODO: Show basic info about the data
        # Hint: Get unique conservation statuses from species data
        # statuses = set(species["conservation_status"] for species in species_data.values())
        
        print(f"\n===== WILDLIFE CONSERVATION TRACKING SYSTEM =====")
        print(f"Total Species: {len(species_data)}")
        # print(f"Conservation Statuses: {', '.join(sorted(statuses))}")
        
        print("\nMain Menu:")
        print("1. View Species Data")
        print("2. Filter Species")
        print("3. Update Species Data")
        print("4. Add New Species")
        print("5. View Conservation Statistics")
        print("0. Exit")
        
        choice = input("Enter your choice (0-5): ")
        
        # TODO: Implement menu handling logic
        if choice == "0":
            print("Thank you for using the Wildlife Conservation Tracking System!")
            break
        
        elif choice == "1":
            # TODO: Display all species data
            pass
        
        elif choice == "2":
            # TODO: Implement filtering submenu
            # Submenus for: conservation status, population range, habitat type, sanctuary, keyword search
            pass
        
        elif choice == "3":
            # TODO: Implement update submenu
            # Submenus for: update population, update conservation status, add threat
            pass
        
        elif choice == "4":
            # TODO: Merge new species data
            pass
        
        elif choice == "5":
            # TODO: Implement statistics submenu
            # Submenus for: status counts, total population, most threatened, population brackets
            pass
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()