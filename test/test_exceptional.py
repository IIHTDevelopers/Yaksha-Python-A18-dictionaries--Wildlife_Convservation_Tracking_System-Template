import pytest
from test.TestUtils import TestUtils
from wildlife_conservation_tracking_system import (
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
    create_population_brackets,
    get_formatted_species
)

@pytest.fixture
def test_obj():
    return TestUtils()

def test_input_validation(test_obj):
    """Consolidated test for input validation and error handling"""
    try:
        # Test with None inputs for critical functions
        functions_to_test = [
            (filter_by_conservation_status, [None, "Endangered"]),
            (filter_by_conservation_status, [{"SP001": {}}, None]),
            (filter_by_population_range, [None, 100, 1000]),
            (filter_by_population_range, [{"SP001": {}}, None, 1000]),
            (filter_by_population_range, [{"SP001": {}}, 100, None]),
            (filter_by_habitat_type, [None, "Forest"]),
            (filter_by_habitat_type, [{"SP001": {}}, None]),
            (filter_by_sanctuary, [None, "Jim Corbett"]),
            (filter_by_sanctuary, [{"SP001": {}}, None]),
            (find_species_with_keyword, [None, "tiger"]),
            (find_species_with_keyword, [{"SP001": {}}, None]),
            (update_species_population, [None, "SP001", 1000]),
            (update_species_population, [{"SP001": {}}, None, 1000]),
            (update_species_population, [{"SP001": {}}, "SP001", None]),
            (update_conservation_status, [None, "SP001", "Endangered"]),
            (update_conservation_status, [{"SP001": {}}, None, "Endangered"]),
            (update_conservation_status, [{"SP001": {}}, "SP001", None]),
            (add_species_threat, [None, "SP001", "New Threat"]),
            (add_species_threat, [{"SP001": {}}, None, "New Threat"]),
            (add_species_threat, [{"SP001": {}}, "SP001", None]),
            (merge_species_data, [None, {"NS001": {}}]),
            (merge_species_data, [{"SP001": {}}, None]),
            (calculate_status_counts, [None]),
            (calculate_total_population, [None]),
            (find_most_threatened_species, [None]),
            (create_population_brackets, [None]),
            (get_formatted_species, ["SP001", None])
        ]
        
        # Test all functions with None inputs
        for func, args in functions_to_test:
            with pytest.raises(ValueError):
                func(*args)
        
        # Test with invalid parameter values
        species_data = {
            "SP001": {
                "name": "Test Species",
                "scientific_name": "Test scientific",
                "conservation_status": "Endangered",
                "population": 1000,
                "habitat_type": "Forest",
                "sanctuaries": ["Test Sanctuary"],
                "threats": ["Test Threat"]
            }
        }
        
        # Test negative min_population
        with pytest.raises(ValueError):
            filter_by_population_range(species_data, -100, 1000)
        
        # Test min_population > max_population
        with pytest.raises(ValueError):
            filter_by_population_range(species_data, 2000, 1000)
        
        # Test negative population
        with pytest.raises(ValueError):
            update_species_population(species_data, "SP001", -10)
        
        # Test invalid species_id
        with pytest.raises(ValueError):
            update_species_population(species_data, "INVALID", 1000)
        
        # Test invalid conservation status
        with pytest.raises(ValueError):
            update_conservation_status(species_data, "SP001", "Not A Status")
        
        # Test empty threat
        with pytest.raises(ValueError):
            add_species_threat(species_data, "SP001", "")
        
        # Test find_most_threatened_species with empty species_data
        with pytest.raises(ValueError):
            find_most_threatened_species({})
        
        test_obj.yakshaAssert("TestInputValidation", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestInputValidation", False, "exception")
        pytest.fail(f"Input validation test failed: {str(e)}")

def test_error_handling(test_obj):
    """Test specific error handling scenarios"""
    try:
        # Setup species data with specific conditions for testing
        species_data = {
            "SP001": {
                "name": "Test Species",
                "scientific_name": "Test scientific",
                "conservation_status": "Endangered",
                "population": 1000,
                "habitat_type": "Forest",
                "sanctuaries": ["Test Sanctuary"],
                "threats": ["Test Threat"]
            }
        }
        
        # Test handling missing fields in species data
        invalid_species_data = {
            "SP001": {
                "name": "Invalid Species"
                # Missing required fields
            }
        }
        
        # Should raise exception when accessing missing fields
        with pytest.raises(Exception):
            filter_by_conservation_status(invalid_species_data, "Endangered")
        
        with pytest.raises(Exception):
            filter_by_population_range(invalid_species_data, 0, 10000)
        
        # Test immutability - original species_data should not change
        original_population = species_data["SP001"]["population"]
        updated_data = update_species_population(species_data, "SP001", 2000)
        assert species_data["SP001"]["population"] == original_population, "Original species_data should not be modified"
        assert updated_data["SP001"]["population"] == 2000, "New species_data should have updated population"
        
        original_status = species_data["SP001"]["conservation_status"]
        updated_data = update_conservation_status(species_data, "SP001", "Vulnerable")
        assert species_data["SP001"]["conservation_status"] == original_status, "Original species_data should not be modified"
        assert updated_data["SP001"]["conservation_status"] == "Vulnerable", "New species_data should have updated status"
        
        original_threats = species_data["SP001"]["threats"].copy()
        updated_data = add_species_threat(species_data, "SP001", "New Threat")
        assert species_data["SP001"]["threats"] == original_threats, "Original species_data should not be modified"
        assert "New Threat" in updated_data["SP001"]["threats"], "New species_data should have new threat"
        
        # Test adding duplicate threat (should not add)
        existing_threat = species_data["SP001"]["threats"][0]
        updated_data = add_species_threat(species_data, "SP001", existing_threat)
        assert len(updated_data["SP001"]["threats"]) == len(species_data["SP001"]["threats"]), "Duplicate threat should not be added"
        
        test_obj.yakshaAssert("TestErrorHandling", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestErrorHandling", False, "exception")
        pytest.fail(f"Error handling test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])