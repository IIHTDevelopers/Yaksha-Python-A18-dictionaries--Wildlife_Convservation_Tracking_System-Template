import unittest
import os
import importlib
import sys
import io
import contextlib
from test.TestUtils import TestUtils

def safely_import_module(module_name):
    """Safely import a module, returning None if import fails."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None
    except Exception:
        return None

def load_module_dynamically():
    """Load the student's module for testing"""
    module_obj = safely_import_module("skeleton")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    return module_obj

def check_function_exists(module, function_name):
    """Check if a function exists in a module."""
    return hasattr(module, function_name) and callable(getattr(module, function_name))

def safely_call_function(module, function_name, *args, **kwargs):
    """Safely call a function, returning the result or None if it fails."""
    if not check_function_exists(module, function_name):
        return None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            return getattr(module, function_name)(*args, **kwargs)
    except Exception:
        return None

class TestAssignment(unittest.TestCase):
    def setUp(self):
        """Standard setup for all test methods"""
        self.test_obj = TestUtils()
        self.module_obj = load_module_dynamically()

    def test_boundary_scenarios(self):
        """Consolidated test for boundary scenarios"""
        try:
            errors = []
            
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
                return
            
            try:
                # Test with empty species data
                empty_species_data = {}
                
                # Test filter functions with empty species data
                filter_functions = [
                    ("filter_by_conservation_status", [empty_species_data, "Endangered"]),
                    ("filter_by_population_range", [empty_species_data, 0, 5000]),
                    ("filter_by_habitat_type", [empty_species_data, "Forest"]),
                    ("filter_by_sanctuary", [empty_species_data, "Jim Corbett"])
                ]
                
                for func_name, args in filter_functions:
                    if check_function_exists(self.module_obj, func_name):
                        try:
                            result = safely_call_function(self.module_obj, *([func_name] + args))
                            if result is None:
                                errors.append(f"{func_name} returned None for empty species data")
                            elif not isinstance(result, dict):
                                errors.append(f"{func_name} returned {type(result)} instead of dict for empty input")
                            elif result != {}:
                                errors.append(f"{func_name} on empty species data should return empty dict, got {result}")
                        except Exception as e:
                            errors.append(f"Error in {func_name} with empty species data: {str(e)}")
                    else:
                        errors.append(f"Function {func_name} not found")
                
                # Test merge with empty species data
                if check_function_exists(self.module_obj, "initialize_data"):
                    try:
                        init_result = safely_call_function(self.module_obj, "initialize_data")
                        if init_result and isinstance(init_result, tuple) and len(init_result) >= 2:
                            _, new_species = init_result
                        else:
                            # Create fallback new_species
                            new_species = {
                                "NS001": {"name": "Ganges River Dolphin", "conservation_status": "Endangered", "population": 3500}
                            }
                    except Exception:
                        # Create fallback new_species
                        new_species = {
                            "NS001": {"name": "Ganges River Dolphin", "conservation_status": "Endangered", "population": 3500}
                        }
                else:
                    # Create fallback new_species
                    new_species = {
                        "NS001": {"name": "Ganges River Dolphin", "conservation_status": "Endangered", "population": 3500}
                    }
                
                if check_function_exists(self.module_obj, "merge_species_data"):
                    try:
                        merged = safely_call_function(self.module_obj, "merge_species_data", empty_species_data, new_species)
                        if merged is None:
                            errors.append("merge_species_data returned None for empty species data")
                        elif not isinstance(merged, dict):
                            errors.append(f"merge_species_data returned {type(merged)} instead of dict")
                        elif len(merged) != len(new_species):
                            errors.append(f"Merging empty species data with new_species should result in {len(new_species)} species, got {len(merged)}")
                    except Exception as e:
                        errors.append(f"Error in merge_species_data with empty species data: {str(e)}")
                else:
                    errors.append("Function merge_species_data not found")
                
                # Get or create real species data for population bracket testing
                species_data = {}
                if check_function_exists(self.module_obj, "initialize_data"):
                    try:
                        init_result = safely_call_function(self.module_obj, "initialize_data")
                        if init_result and isinstance(init_result, tuple) and len(init_result) >= 1:
                            species_data = init_result[0]
                    except Exception:
                        pass
                
                # Create test data for population brackets if needed
                if not species_data or check_function_exists(self.module_obj, "create_population_brackets"):
                    # Test population at exactly boundary values
                    # Population bracket boundaries are: 0-500, 501-5000, 5001-20000, 20001+
                    test_species_data = {
                        "T001": {"name": "Test Species 1", "population": 0, "conservation_status": "Vulnerable"},
                        "T002": {"name": "Test Species 2", "population": 500, "conservation_status": "Vulnerable"},
                        "T003": {"name": "Test Species 3", "population": 501, "conservation_status": "Vulnerable"},
                        "T004": {"name": "Test Species 4", "population": 5000, "conservation_status": "Vulnerable"},
                        "T005": {"name": "Test Species 5", "population": 5001, "conservation_status": "Vulnerable"},
                        "T006": {"name": "Test Species 6", "population": 20000, "conservation_status": "Vulnerable"},
                        "T007": {"name": "Test Species 7", "population": 20001, "conservation_status": "Vulnerable"}
                    }
                    
                    if check_function_exists(self.module_obj, "create_population_brackets"):
                        try:
                            brackets = safely_call_function(self.module_obj, "create_population_brackets", test_species_data)
                            if brackets is None:
                                errors.append("create_population_brackets returned None for test data")
                            elif not isinstance(brackets, dict):
                                errors.append(f"create_population_brackets returned {type(brackets)} instead of dict")
                            elif "critical" not in brackets or "endangered" not in brackets or "vulnerable" not in brackets or "stable" not in brackets:
                                errors.append("create_population_brackets should return dict with critical, endangered, vulnerable, and stable keys")
                            else:
                                if "T001" not in brackets["critical"] or "T002" not in brackets["critical"]:
                                    errors.append("Species with 0 and 500 population should be in critical bracket")
                                if "T003" not in brackets["endangered"] or "T004" not in brackets["endangered"]:
                                    errors.append("Species with 501 and 5000 population should be in endangered bracket")
                                if "T005" not in brackets["vulnerable"] or "T006" not in brackets["vulnerable"]:
                                    errors.append("Species with 5001 and 20000 population should be in vulnerable bracket")
                                if "T007" not in brackets["stable"]:
                                    errors.append("Species with 20001+ population should be in stable bracket")
                        except Exception as e:
                            errors.append(f"Error in create_population_brackets with boundary values: {str(e)}")
                    else:
                        errors.append("Function create_population_brackets not found")
                
                # Test update_species_population with edge cases
                if species_data and check_function_exists(self.module_obj, "update_species_population"):
                    try:
                        # Choose any species ID from the data
                        sid = next(iter(species_data.keys()))
                        
                        # Test setting population to exactly zero
                        updated = safely_call_function(self.module_obj, "update_species_population", species_data, sid, 0)
                        if updated is None:
                            errors.append("update_species_population returned None for zero population")
                        elif not isinstance(updated, dict):
                            errors.append(f"update_species_population returned {type(updated)} instead of dict")
                        elif sid not in updated:
                            errors.append(f"update_species_population should return dictionary containing {sid}")
                        elif updated[sid]["population"] != 0:
                            errors.append(f"Population should be exactly zero after update, got {updated[sid]['population']}")
                    except Exception as e:
                        errors.append(f"Error testing update_species_population with zero population: {str(e)}")
                else:
                    if not check_function_exists(self.module_obj, "update_species_population"):
                        errors.append("Function update_species_population not found")
                
                # Test valid conservation status values
                if species_data and check_function_exists(self.module_obj, "update_conservation_status"):
                    try:
                        # Choose any species ID from the data
                        sid = next(iter(species_data.keys()))
                        
                        statuses = ["Least Concern", "Near Threatened", "Vulnerable", "Endangered", "Critically Endangered"]
                        for status in statuses:
                            updated = safely_call_function(self.module_obj, "update_conservation_status", species_data, sid, status)
                            if updated is None:
                                errors.append(f"update_conservation_status returned None for status '{status}'")
                            elif not isinstance(updated, dict):
                                errors.append(f"update_conservation_status returned {type(updated)} instead of dict for status '{status}'")
                            elif sid not in updated:
                                errors.append(f"update_conservation_status should return dictionary containing {sid} for status '{status}'")
                            elif updated[sid]["conservation_status"] != status:
                                errors.append(f"Conservation status should be '{status}' after update, got '{updated[sid]['conservation_status']}'")
                    except Exception as e:
                        errors.append(f"Error testing update_conservation_status with valid statuses: {str(e)}")
                else:
                    if not check_function_exists(self.module_obj, "update_conservation_status"):
                        errors.append("Function update_conservation_status not found")
                
                # Final assertion
                if errors:
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                    print("TestBoundaryScenarios = Failed")
                else:
                    self.test_obj.yakshaAssert("TestBoundaryScenarios", True, "boundary")
                    print("TestBoundaryScenarios = Passed")
            except Exception as e:
                self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
                print("TestBoundaryScenarios = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
            print("TestBoundaryScenarios = Failed")

    def test_edge_case_filtering(self):
        """Test filtering with edge case inputs"""
        try:
            errors = []
            
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestEdgeCaseFiltering", False, "boundary")
                print("TestEdgeCaseFiltering = Failed")
                return
            
            try:
                # Get sample data
                species_data = {}
                if check_function_exists(self.module_obj, "initialize_data"):
                    try:
                        init_result = safely_call_function(self.module_obj, "initialize_data")
                        if init_result and isinstance(init_result, tuple) and len(init_result) >= 1:
                            species_data = init_result[0]
                        if not species_data:
                            # Create fallback species_data
                            species_data = {
                                "SP001": {
                                    "name": "Bengal Tiger", 
                                    "conservation_status": "Endangered",
                                    "population": 3500,
                                    "habitat_type": "Forest",
                                    "sanctuaries": ["Sundarbans", "Jim Corbett"]
                                },
                                "SP004": {
                                    "name": "Snow Leopard",
                                    "conservation_status": "Vulnerable",
                                    "population": 450,
                                    "habitat_type": "Mountain",
                                    "sanctuaries": ["Hemis"]
                                }
                            }
                    except Exception:
                        # Create fallback species_data
                        species_data = {
                            "SP001": {
                                "name": "Bengal Tiger", 
                                "conservation_status": "Endangered",
                                "population": 3500,
                                "habitat_type": "Forest",
                                "sanctuaries": ["Sundarbans", "Jim Corbett"]
                            },
                            "SP004": {
                                "name": "Snow Leopard",
                                "conservation_status": "Vulnerable",
                                "population": 450,
                                "habitat_type": "Mountain",
                                "sanctuaries": ["Hemis"]
                            }
                        }
                else:
                    # Create fallback species_data
                    species_data = {
                        "SP001": {
                            "name": "Bengal Tiger", 
                            "conservation_status": "Endangered",
                            "population": 3500,
                            "habitat_type": "Forest",
                            "sanctuaries": ["Sundarbans", "Jim Corbett"]
                        },
                        "SP004": {
                            "name": "Snow Leopard",
                            "conservation_status": "Vulnerable",
                            "population": 450,
                            "habitat_type": "Mountain",
                            "sanctuaries": ["Hemis"]
                        }
                    }
                
                # Test merging empty dictionaries
                if check_function_exists(self.module_obj, "merge_species_data"):
                    try:
                        empty_dict = {}
                        merged = safely_call_function(self.module_obj, "merge_species_data", species_data, empty_dict)
                        if merged is None:
                            errors.append("merge_species_data returned None for empty new_species")
                        elif not isinstance(merged, dict):
                            errors.append(f"merge_species_data returned {type(merged)} instead of dict")
                        elif len(merged) != len(species_data):
                            errors.append(f"Merging with empty dict should not change species_data, expected {len(species_data)} items, got {len(merged)}")
                        
                        merged = safely_call_function(self.module_obj, "merge_species_data", empty_dict, empty_dict)
                        if merged is None:
                            errors.append("merge_species_data returned None for empty species data and empty new_species")
                        elif not isinstance(merged, dict):
                            errors.append(f"merge_species_data returned {type(merged)} instead of dict")
                        elif merged != {}:
                            errors.append("Merging empty dicts should result in empty dict")
                    except Exception as e:
                        errors.append(f"Error testing merge with empty dictionaries: {str(e)}")
                else:
                    errors.append("Function merge_species_data not found")
                
                # Test population with exact range boundaries
                if len(species_data) >= 2 and check_function_exists(self.module_obj, "filter_by_population_range"):
                    try:
                        # Find min and max population values
                        populations = [species.get("population", 0) for species in species_data.values()]
                        min_pop = min(populations)
                        max_pop = max(populations)
                        
                        # Test with exact min/max values
                        filtered = safely_call_function(self.module_obj, "filter_by_population_range", species_data, min_pop, max_pop)
                        if filtered is None:
                            errors.append("filter_by_population_range returned None for min/max range")
                        elif not isinstance(filtered, dict):
                            errors.append(f"filter_by_population_range returned {type(filtered)} instead of dict")
                        elif len(filtered) != len(species_data):
                            errors.append(f"filter_by_population_range with min={min_pop}, max={max_pop} should include all species")
                        
                        # Test with no match range (small window between existing values or outside all values)
                        no_match_min = min_pop + 1
                        no_match_max = min_pop + 10
                        
                        # Ensure no species falls in this range
                        if all(not (no_match_min <= species.get("population", 0) <= no_match_max) for species in species_data.values()):
                            filtered = safely_call_function(self.module_obj, "filter_by_population_range", species_data, no_match_min, no_match_max)
                            if filtered is None:
                                errors.append("filter_by_population_range returned None for no-match range")
                            elif not isinstance(filtered, dict):
                                errors.append(f"filter_by_population_range returned {type(filtered)} instead of dict")
                            elif filtered != {}:
                                errors.append("filter_by_population_range should return empty dict for population range with no matches")
                    except Exception as e:
                        errors.append(f"Error testing filter_by_population_range with boundary values: {str(e)}")
                else:
                    if not check_function_exists(self.module_obj, "filter_by_population_range"):
                        errors.append("Function filter_by_population_range not found")
                
                # Test filtering with non-existent values
                filter_test_cases = [
                    ("filter_by_conservation_status", [species_data, "Extinct"]),
                    ("filter_by_habitat_type", [species_data, "Ocean"]),
                    ("filter_by_sanctuary", [species_data, "Yellowstone"])
                ]
                
                for func_name, args in filter_test_cases:
                    if check_function_exists(self.module_obj, func_name):
                        try:
                            filtered = safely_call_function(self.module_obj, *([func_name] + args))
                            if filtered is None:
                                errors.append(f"{func_name} returned None for non-existent value")
                            elif not isinstance(filtered, dict):
                                errors.append(f"{func_name} returned {type(filtered)} instead of dict")
                            elif filtered != {}:
                                errors.append(f"{func_name} should return empty dict for non-existent value")
                        except Exception as e:
                            errors.append(f"Error in {func_name} with non-existent value: {str(e)}")
                    else:
                        errors.append(f"Function {func_name} not found")
                
                # Final assertion
                if errors:
                    self.test_obj.yakshaAssert("TestEdgeCaseFiltering", False, "boundary")
                    print("TestEdgeCaseFiltering = Failed")
                else:
                    self.test_obj.yakshaAssert("TestEdgeCaseFiltering", True, "boundary")
                    print("TestEdgeCaseFiltering = Passed")
            except Exception as e:
                self.test_obj.yakshaAssert("TestEdgeCaseFiltering", False, "boundary")
                print("TestEdgeCaseFiltering = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestEdgeCaseFiltering", False, "boundary")
            print("TestEdgeCaseFiltering = Failed")

if __name__ == '__main__':
    unittest.main()