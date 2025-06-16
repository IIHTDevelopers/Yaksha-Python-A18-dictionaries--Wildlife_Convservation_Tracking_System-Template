import unittest
import os
import importlib
import sys
import io
import contextlib
import traceback
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

def check_raises(func, args, expected_exception=Exception):
    """Check if a function raises an expected exception."""
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            func(*args)
        return False
    except expected_exception:
        return True
    except Exception:
        return False

def create_test_species_data():
    """Create a basic test species data dictionary for tests."""
    return {
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

class TestAssignment(unittest.TestCase):
    def setUp(self):
        """Standard setup for all test methods"""
        self.test_obj = TestUtils()
        self.module_obj = load_module_dynamically()

    def test_input_validation(self):
        """Consolidated test for input validation and error handling"""
        try:
            errors = []
            
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestInputValidation", False, "exception")
                print("TestInputValidation = Failed")
                return
            
            try:
                # Create test species data dictionary for tests
                species_data = create_test_species_data()
                
                # Test functions with None inputs
                test_cases = []
                
                # Define test cases for all functions
                filter_functions = [
                    ("filter_by_conservation_status", [None, "Endangered"]),
                    ("filter_by_conservation_status", [species_data, None]),
                    ("filter_by_population_range", [None, 100, 1000]),
                    ("filter_by_population_range", [species_data, None, 1000]),
                    ("filter_by_population_range", [species_data, 100, None]),
                    ("filter_by_habitat_type", [None, "Forest"]),
                    ("filter_by_habitat_type", [species_data, None]),
                    ("filter_by_sanctuary", [None, "Jim Corbett"]),
                    ("filter_by_sanctuary", [species_data, None])
                ]
                
                search_functions = [
                    ("find_species_with_keyword", [None, "tiger"]),
                    ("find_species_with_keyword", [species_data, None])
                ]
                
                update_functions = [
                    ("update_species_population", [None, "SP001", 1000]),
                    ("update_species_population", [species_data, None, 1000]),
                    ("update_species_population", [species_data, "SP001", None]),
                    ("update_conservation_status", [None, "SP001", "Endangered"]),
                    ("update_conservation_status", [species_data, None, "Endangered"]),
                    ("update_conservation_status", [species_data, "SP001", None]),
                    ("add_species_threat", [None, "SP001", "New Threat"]),
                    ("add_species_threat", [species_data, None, "New Threat"]),
                    ("add_species_threat", [species_data, "SP001", None])
                ]
                
                merge_functions = [
                    ("merge_species_data", [None, {"NS001": {}}]),
                    ("merge_species_data", [species_data, None])
                ]
                
                stats_functions = [
                    ("calculate_status_counts", [None]),
                    ("calculate_total_population", [None]),
                    ("find_most_threatened_species", [None]),
                    ("create_population_brackets", [None])
                ]
                
                display_functions = [
                    ("get_formatted_species", ["SP001", None])
                ]
                
                # Combine all test cases
                test_cases = filter_functions + search_functions + update_functions + merge_functions + stats_functions + display_functions
                
                # Test all functions with None inputs
                for func_name, args in test_cases:
                    if check_function_exists(self.module_obj, func_name):
                        try:
                            func = getattr(self.module_obj, func_name)
                            result = check_raises(func, args, ValueError)
                            if not result:
                                errors.append(f"{func_name} does not raise ValueError with None inputs: {args}")
                        except Exception as e:
                            errors.append(f"Error testing {func_name} with None inputs: {str(e)}")
                    else:
                        errors.append(f"Function {func_name} not found")
                
                # Test specific validation cases if functions exist
                if check_function_exists(self.module_obj, "filter_by_population_range"):
                    try:
                        # Test negative min_population
                        result = check_raises(
                            getattr(self.module_obj, "filter_by_population_range"), 
                            [species_data, -100, 1000], 
                            ValueError
                        )
                        if not result:
                            errors.append("filter_by_population_range does not raise ValueError with negative min_population")
                        
                        # Test min_population > max_population
                        result = check_raises(
                            getattr(self.module_obj, "filter_by_population_range"), 
                            [species_data, 2000, 1000], 
                            ValueError
                        )
                        if not result:
                            errors.append("filter_by_population_range does not raise ValueError when min_population > max_population")
                    except Exception as e:
                        errors.append(f"Error testing filter_by_population_range validation: {str(e)}")
                
                if check_function_exists(self.module_obj, "update_species_population"):
                    try:
                        # Test negative population
                        result = check_raises(
                            getattr(self.module_obj, "update_species_population"), 
                            [species_data, "SP001", -10], 
                            ValueError
                        )
                        if not result:
                            errors.append("update_species_population does not raise ValueError with negative population")
                        
                        # Test invalid species_id
                        result = check_raises(
                            getattr(self.module_obj, "update_species_population"), 
                            [species_data, "INVALID", 1000], 
                            ValueError
                        )
                        if not result:
                            errors.append("update_species_population does not raise ValueError with invalid species_id")
                    except Exception as e:
                        errors.append(f"Error testing update_species_population validation: {str(e)}")
                
                if check_function_exists(self.module_obj, "update_conservation_status"):
                    try:
                        # Test invalid conservation status
                        result = check_raises(
                            getattr(self.module_obj, "update_conservation_status"), 
                            [species_data, "SP001", "Not A Status"], 
                            ValueError
                        )
                        if not result:
                            errors.append("update_conservation_status does not raise ValueError with invalid conservation status")
                    except Exception as e:
                        errors.append(f"Error testing update_conservation_status validation: {str(e)}")
                
                if check_function_exists(self.module_obj, "add_species_threat"):
                    try:
                        # Test empty threat
                        result = check_raises(
                            getattr(self.module_obj, "add_species_threat"), 
                            [species_data, "SP001", ""], 
                            ValueError
                        )
                        if not result:
                            errors.append("add_species_threat does not raise ValueError with empty threat")
                    except Exception as e:
                        errors.append(f"Error testing add_species_threat validation: {str(e)}")
                
                if check_function_exists(self.module_obj, "find_most_threatened_species"):
                    try:
                        # Test find_most_threatened_species with empty species_data
                        result = check_raises(
                            getattr(self.module_obj, "find_most_threatened_species"), 
                            [{}], 
                            ValueError
                        )
                        if not result:
                            errors.append("find_most_threatened_species does not raise ValueError with empty species_data")
                    except Exception as e:
                        errors.append(f"Error testing find_most_threatened_species validation: {str(e)}")
                
                # Final assertion
                if errors:
                    self.test_obj.yakshaAssert("TestInputValidation", False, "exception")
                    print("TestInputValidation = Failed")
                else:
                    self.test_obj.yakshaAssert("TestInputValidation", True, "exception")
                    print("TestInputValidation = Passed")
            except Exception as e:
                self.test_obj.yakshaAssert("TestInputValidation", False, "exception")
                print("TestInputValidation = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestInputValidation", False, "exception")
            print("TestInputValidation = Failed")

    def test_error_handling(self):
        """Test specific error handling scenarios"""
        try:
            errors = []
            
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                print("TestErrorHandling = Failed")
                return
            
            try:
                # Setup species data with specific conditions for testing
                species_data = create_test_species_data()
                
                # Test handling missing fields in species data
                invalid_species_data = {
                    "SP001": {
                        "name": "Invalid Species"
                        # Missing required fields
                    }
                }
                
                # Test filtering with missing fields
                if check_function_exists(self.module_obj, "filter_by_conservation_status"):
                    try:
                        result = check_raises(
                            getattr(self.module_obj, "filter_by_conservation_status"), 
                            [invalid_species_data, "Endangered"], 
                            Exception
                        )
                        if not result:
                            errors.append("filter_by_conservation_status does not handle missing fields properly")
                    except Exception as e:
                        errors.append(f"Error testing filter_by_conservation_status with missing fields: {str(e)}")
                
                if check_function_exists(self.module_obj, "filter_by_population_range"):
                    try:
                        result = check_raises(
                            getattr(self.module_obj, "filter_by_population_range"), 
                            [invalid_species_data, 0, 10000], 
                            Exception
                        )
                        if not result:
                            errors.append("filter_by_population_range does not handle missing fields properly")
                    except Exception as e:
                        errors.append(f"Error testing filter_by_population_range with missing fields: {str(e)}")
                
                # Test immutability - original species_data should not change
                if check_function_exists(self.module_obj, "update_species_population"):
                    try:
                        original_population = species_data["SP001"]["population"]
                        updated_data = safely_call_function(self.module_obj, "update_species_population", species_data, "SP001", 2000)
                        
                        if updated_data is None:
                            errors.append("update_species_population returned None")
                        elif species_data["SP001"]["population"] != original_population:
                            errors.append("Original species_data was modified by update_species_population")
                        elif updated_data["SP001"]["population"] != 2000:
                            errors.append(f"update_species_population should set population to 2000, got {updated_data['SP001']['population']}")
                    except Exception as e:
                        errors.append(f"Error testing update_species_population immutability: {str(e)}")
                
                if check_function_exists(self.module_obj, "update_conservation_status"):
                    try:
                        original_status = species_data["SP001"]["conservation_status"]
                        updated_data = safely_call_function(self.module_obj, "update_conservation_status", species_data, "SP001", "Vulnerable")
                        
                        if updated_data is None:
                            errors.append("update_conservation_status returned None")
                        elif species_data["SP001"]["conservation_status"] != original_status:
                            errors.append("Original species_data was modified by update_conservation_status")
                        elif updated_data["SP001"]["conservation_status"] != "Vulnerable":
                            errors.append(f"update_conservation_status should set status to Vulnerable, got {updated_data['SP001']['conservation_status']}")
                    except Exception as e:
                        errors.append(f"Error testing update_conservation_status immutability: {str(e)}")
                
                if check_function_exists(self.module_obj, "add_species_threat"):
                    try:
                        original_threats = species_data["SP001"]["threats"].copy()
                        updated_data = safely_call_function(self.module_obj, "add_species_threat", species_data, "SP001", "New Threat")
                        
                        if updated_data is None:
                            errors.append("add_species_threat returned None")
                        elif species_data["SP001"]["threats"] != original_threats:
                            errors.append("Original species_data was modified by add_species_threat")
                        elif "New Threat" not in updated_data["SP001"]["threats"]:
                            errors.append("New threat was not added to threats list")
                    except Exception as e:
                        errors.append(f"Error testing add_species_threat immutability: {str(e)}")
                
                # Test adding duplicate threat (should not add)
                if check_function_exists(self.module_obj, "add_species_threat"):
                    try:
                        existing_threat = species_data["SP001"]["threats"][0]
                        original_threats_count = len(species_data["SP001"]["threats"])
                        
                        updated_data = safely_call_function(self.module_obj, "add_species_threat", species_data, "SP001", existing_threat)
                        
                        if updated_data is None:
                            errors.append("add_species_threat returned None for duplicate threat")
                        elif len(updated_data["SP001"]["threats"]) != original_threats_count:
                            errors.append("Duplicate threat should not be added")
                    except Exception as e:
                        errors.append(f"Error testing add_species_threat with duplicate threat: {str(e)}")
                
                # Final assertion
                if errors:
                    self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                    print("TestErrorHandling = Failed")
                else:
                    self.test_obj.yakshaAssert("TestErrorHandling", True, "exception")
                    print("TestErrorHandling = Passed")
            except Exception as e:
                self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
                print("TestErrorHandling = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestErrorHandling", False, "exception")
            print("TestErrorHandling = Failed")

    def test_data_integrity(self):
        """Test data integrity and dictionary manipulation"""
        try:
            errors = []
            
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestDataIntegrity", False, "exception")
                print("TestDataIntegrity = Failed")
                return
            
            try:
                # Create test species data
                species_data = create_test_species_data()
                
                # Test that dictionary operations maintain data integrity
                if check_function_exists(self.module_obj, "filter_by_conservation_status"):
                    try:
                        filtered = safely_call_function(self.module_obj, "filter_by_conservation_status", species_data, "Endangered")
                        if filtered is not None and "SP001" in filtered:
                            # Check all fields are preserved
                            for key in species_data["SP001"]:
                                if key not in filtered["SP001"]:
                                    errors.append(f"Field '{key}' is missing from filtered result")
                                elif filtered["SP001"][key] != species_data["SP001"][key]:
                                    errors.append(f"Field '{key}' was modified in filtered result")
                    except Exception as e:
                        errors.append(f"Error testing data preservation in filter_by_conservation_status: {str(e)}")
                
                # Test deep copying of lists in update functions
                if check_function_exists(self.module_obj, "add_species_threat"):
                    try:
                        original_threats = species_data["SP001"]["threats"]
                        updated = safely_call_function(self.module_obj, "add_species_threat", species_data, "SP001", "New Threat")
                        
                        if updated is not None:
                            # Check that threats list was properly deep copied
                            if id(updated["SP001"]["threats"]) == id(original_threats):
                                errors.append("Threats list was not properly deep copied")
                            
                            # Check original threats list is unchanged
                            if "New Threat" in species_data["SP001"]["threats"]:
                                errors.append("Original threats list was modified")
                            
                            # Check new threats list has all original items plus the new one
                            if not all(threat in updated["SP001"]["threats"] for threat in original_threats):
                                errors.append("New threats list is missing original threats")
                            
                            if "New Threat" not in updated["SP001"]["threats"]:
                                errors.append("New threats list is missing new threat")
                    except Exception as e:
                        errors.append(f"Error testing deep copying of lists: {str(e)}")
                
                # Test that merge_species_data preserves original dictionaries
                if check_function_exists(self.module_obj, "merge_species_data"):
                    try:
                        new_species = {
                            "NS001": {
                                "name": "New Species",
                                "scientific_name": "New scientific",
                                "conservation_status": "Vulnerable",
                                "population": 500,
                                "habitat_type": "Mountain",
                                "sanctuaries": ["New Sanctuary"],
                                "threats": ["New Threat"]
                            }
                        }
                        
                        original_species_data = {key: value.copy() for key, value in species_data.items()}
                        original_new_species = {key: value.copy() for key, value in new_species.items()}
                        
                        merged = safely_call_function(self.module_obj, "merge_species_data", species_data, new_species)
                        
                        if merged is not None:
                            # Check original dictionaries are unchanged
                            if species_data != original_species_data:
                                errors.append("Original species_data was modified by merge_species_data")
                            
                            if new_species != original_new_species:
                                errors.append("Original new_species was modified by merge_species_data")
                            
                            # Check merged dictionary has all entries
                            for sid in species_data:
                                if sid not in merged:
                                    errors.append(f"Merged dictionary is missing original species {sid}")
                            
                            for sid in new_species:
                                if sid not in merged:
                                    errors.append(f"Merged dictionary is missing new species {sid}")
                                elif "newly_added" not in merged[sid]:
                                    errors.append(f"New species {sid} is missing 'newly_added' flag")
                    except Exception as e:
                        errors.append(f"Error testing merge_species_data preservation: {str(e)}")
                
                # Final assertion
                if errors:
                    self.test_obj.yakshaAssert("TestDataIntegrity", False, "exception")
                    print("TestDataIntegrity = Failed")
                else:
                    self.test_obj.yakshaAssert("TestDataIntegrity", True, "exception")
                    print("TestDataIntegrity = Passed")
            except Exception as e:
                self.test_obj.yakshaAssert("TestDataIntegrity", False, "exception")
                print("TestDataIntegrity = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestDataIntegrity", False, "exception")
            print("TestDataIntegrity = Failed")

if __name__ == '__main__':
    unittest.main()