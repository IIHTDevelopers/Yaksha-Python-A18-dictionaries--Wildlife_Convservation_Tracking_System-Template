import pytest
from test.TestUtils import TestUtils
from wildlife_conservation_tracking_system import (
    initialize_data,
    filter_by_conservation_status,
    filter_by_population_range,
    filter_by_habitat_type,
    filter_by_sanctuary,
    update_species_population,
    update_conservation_status,
    merge_species_data,
    create_population_brackets
)

@pytest.fixture
def test_obj():
    return TestUtils()

def test_boundary_scenarios(test_obj):
    """Consolidated test for boundary scenarios"""
    try:
        # Test with empty species data
        empty_species_data = {}
        
        # Test filter functions with empty species data
        filtered = filter_by_conservation_status(empty_species_data, "Endangered")
        assert filtered == {}, "Filtering empty species data should return empty dict"
        
        filtered = filter_by_population_range(empty_species_data, 0, 5000)
        assert filtered == {}, "Filtering empty species data by population should return empty dict"
        
        filtered = filter_by_habitat_type(empty_species_data, "Forest")
        assert filtered == {}, "Filtering empty species data by habitat should return empty dict"
        
        filtered = filter_by_sanctuary(empty_species_data, "Jim Corbett")
        assert filtered == {}, "Filtering empty species data by sanctuary should return empty dict"
        
        # Test merge with empty species data
        _, new_species = initialize_data()
        merged = merge_species_data(empty_species_data, new_species)
        assert len(merged) == len(new_species), "Merging empty species data should only include new species"
        
        # Test with real species data
        species_data, _ = initialize_data()
        
        # Test population at exactly boundary values
        # Population bracket boundaries are: 0-500, 501-5000, 5001-20000, 20001+
        test_species_data = {
            "T001": {"name": "Test Species 1", "population": 0},
            "T002": {"name": "Test Species 2", "population": 500},
            "T003": {"name": "Test Species 3", "population": 501},
            "T004": {"name": "Test Species 4", "population": 5000},
            "T005": {"name": "Test Species 5", "population": 5001},
            "T006": {"name": "Test Species 6", "population": 20000},
            "T007": {"name": "Test Species 7", "population": 20001}
        }
        
        brackets = create_population_brackets(test_species_data)
        assert "T001" in brackets["critical"] and "T002" in brackets["critical"], "Species with 0 and 500 population should be critical"
        assert "T003" in brackets["endangered"] and "T004" in brackets["endangered"], "Species with 501 and 5000 population should be endangered"
        assert "T005" in brackets["vulnerable"] and "T006" in brackets["vulnerable"], "Species with 5001 and 20000 population should be vulnerable"
        assert "T007" in brackets["stable"], "Species with 20001+ population should be stable"
        
        # Test update_species_population with edge cases
        sid = "SP001"
        updated = update_species_population(species_data, sid, 0)
        assert updated[sid]["population"] == 0, "Should allow setting population to exactly zero"
        
        # Test valid conservation status values
        statuses = ["Least Concern", "Near Threatened", "Vulnerable", "Endangered", "Critically Endangered"]
        for status in statuses:
            updated = update_conservation_status(species_data, "SP001", status)
            assert updated["SP001"]["conservation_status"] == status, f"Should accept valid status: {status}"
        
        test_obj.yakshaAssert("TestBoundaryScenarios", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
        pytest.fail(f"Boundary scenarios test failed: {str(e)}")

def test_edge_case_filtering(test_obj):
    """Test filtering with edge case inputs"""
    try:
        species_data, _ = initialize_data()
        
        # Test merging empty dictionaries
        empty_dict = {}
        merged = merge_species_data(species_data, empty_dict)
        assert merged == species_data, "Merging empty dict into species_data should not change species_data"
        
        merged = merge_species_data(empty_dict, empty_dict)
        assert merged == {}, "Merging empty dicts should result in empty dict"
        
        # Test population with exact range boundaries
        min_pop = species_data["SP004"]["population"]  # Snow Leopard with 450
        max_pop = species_data["SP001"]["population"]  # Bengal Tiger with 3500
        
        # Test with exact min/max values
        filtered = filter_by_population_range(species_data, min_pop, max_pop)
        assert "SP001" in filtered and "SP004" in filtered, "Exact min/max population values should be included"
        
        # Test with no match range
        filtered = filter_by_population_range(species_data, 600, 800)
        assert len(filtered) == 0, "Should return empty dict for population range with no matches"
        
        # Test filtering on unique values
        filtered = filter_by_habitat_type(species_data, "Mountain")
        assert len(filtered) == 1 and "SP004" in filtered, "Only one species has Mountain habitat"
        
        # Test for unique sanctuary
        filtered = filter_by_sanctuary(species_data, "Kaziranga")
        assert len(filtered) == 1 and "SP003" in filtered, "Only one species is in Kaziranga sanctuary"
        
        # Test filter with non-existent values
        filtered = filter_by_conservation_status(species_data, "Extinct")
        assert filtered == {}, "Filtering by non-existent status should return empty dict"
        
        filtered = filter_by_habitat_type(species_data, "Ocean")
        assert filtered == {}, "Filtering by non-existent habitat should return empty dict"
        
        filtered = filter_by_sanctuary(species_data, "Yellowstone")
        assert filtered == {}, "Filtering by non-existent sanctuary should return empty dict"
        
        test_obj.yakshaAssert("TestEdgeCaseFiltering", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestEdgeCaseFiltering", False, "boundary")
        pytest.fail(f"Edge case filtering test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])