import pytest
import inspect
import importlib
from test.TestUtils import TestUtils
from wildlife_conservation_tracking_system import (
    initialize_data,
    filter_by_conservation_status,
    filter_by_population_range,
    filter_by_habitat_type,
    filter_by_sanctuary,
    find_species_with_keyword,
    update_species_population,
    update_conservation_status,
    add_species_threat,
    merge_species_data,
    calculate_status_counts,
    calculate_total_population,
    find_most_threatened_species,
    create_population_brackets
)

@pytest.fixture
def test_obj():
    return TestUtils()

def test_variable_naming(test_obj):
    """Test that the required variable names and structure are used"""
    try:
        # Import the module
        module = importlib.import_module("wildlife_conservation_tracking_system")

        # Check dictionary initialization
        init_source = inspect.getsource(module.initialize_data)
        assert "species_data = {" in init_source, "Initialize data must create species_data dictionary"
        assert "new_species = {" in init_source, "Initialize data must create new_species dictionary"
        
        # Check main function uses required data
        main_source = inspect.getsource(module.main)
        assert "species_data, new_species = initialize_data()" in main_source, "main() must initialize species data"
        
        # Check dictionary operation functions use correct parameter names
        assert "def filter_by_conservation_status(species_data, status)" in inspect.getsource(module), "filter_by_conservation_status() must use correct parameters"
        assert "def filter_by_population_range(species_data, min_population, max_population)" in inspect.getsource(module), "filter_by_population_range() must use correct parameters"
        assert "def merge_species_data(existing_species, new_species)" in inspect.getsource(module), "merge_species_data() must use correct parameters"
        
        test_obj.yakshaAssert("test_variable_naming", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_variable_naming", False, "functional")
        pytest.fail(f"Variable naming test failed: {str(e)}")

def test_dictionary_operations(test_obj):
    """Test all dictionary operations"""
    try:
        # Test all filtering operations
        species_data, new_species = initialize_data()

        # Test filter_by_conservation_status
        filtered = filter_by_conservation_status(species_data, "Endangered")
        assert len(filtered) == 2 and "SP001" in filtered and "SP002" in filtered
        
        # Test filter_by_population_range
        filtered = filter_by_population_range(species_data, 1000, 5000)
        assert len(filtered) == 2 and "SP001" in filtered and "SP003" in filtered
        
        # Test filter_by_habitat_type
        filtered = filter_by_habitat_type(species_data, "Forest")
        assert len(filtered) == 2 and "SP001" in filtered and "SP002" in filtered
        
        # Test filter_by_sanctuary
        filtered = filter_by_sanctuary(species_data, "Jim Corbett")
        assert len(filtered) == 2 and "SP001" in filtered and "SP002" in filtered
        
        # Test find_species_with_keyword
        filtered = find_species_with_keyword(species_data, "poach")
        assert len(filtered) >= 3  # At least 3 species have "Poaching" as a threat
        
        # Test update operations
        original_population = species_data["SP001"]["population"]
        updated = update_species_population(species_data, "SP001", 4000)
        assert updated["SP001"]["population"] == 4000 and species_data["SP001"]["population"] == original_population
        
        original_status = species_data["SP003"]["conservation_status"]
        updated = update_conservation_status(species_data, "SP003", "Endangered")
        assert updated["SP003"]["conservation_status"] == "Endangered" and species_data["SP003"]["conservation_status"] == original_status
        
        updated = add_species_threat(species_data, "SP001", "Disease")
        assert "Disease" in updated["SP001"]["threats"]
        assert "Disease" not in species_data["SP001"]["threats"]
        
        # Test merge operation
        merged = merge_species_data(species_data, new_species)
        assert len(merged) == 7 and merged["NS001"]["newly_added"] == True
        
        # Test statistics operations
        counts = calculate_status_counts(species_data)
        assert counts["Endangered"] == 2 and counts["Vulnerable"] == 2
        
        total = calculate_total_population(species_data)
        expected_total = sum(species["population"] for species in species_data.values())
        assert total == expected_total
        
        most_threatened = find_most_threatened_species(species_data)
        assert most_threatened[0] == "SP005"  # Indian Vulture is Critically Endangered
        
        brackets = create_population_brackets(species_data)
        assert "SP004" in brackets["critical"] and "SP002" in brackets["stable"]
        
        test_obj.yakshaAssert("test_dictionary_operations", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_dictionary_operations", False, "functional")
        pytest.fail(f"Dictionary operations test failed: {str(e)}")

def test_implementation_techniques(test_obj):
    """Test implementation of dictionary techniques"""
    try:
        # Check dictionary comprehension
        source = inspect.getsource(filter_by_conservation_status)
        assert "{" in source and "for" in source and "if" in source
        
        # Check dictionary methods
        source = inspect.getsource(calculate_status_counts)
        assert ".values()" in source or ".items()" in source or ".keys()" in source
        
        # Check dictionary unpacking
        source1 = inspect.getsource(update_species_population)
        source2 = inspect.getsource(merge_species_data)
        assert "**" in source1 and "**" in source2
        
        # Check data immutability
        species_data, _ = initialize_data()
        species_id = "SP001"
        original_population = species_data[species_id]["population"]
        updated = update_species_population(species_data, species_id, original_population + 1000)
        assert species_data[species_id]["population"] == original_population
        assert updated[species_id]["population"] == original_population + 1000
        
        test_obj.yakshaAssert("test_implementation_techniques", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_implementation_techniques", False, "functional")
        pytest.fail(f"Implementation techniques test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])