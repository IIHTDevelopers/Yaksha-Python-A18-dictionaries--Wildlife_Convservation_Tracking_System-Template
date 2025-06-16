import unittest
import os
import importlib
import sys
import io
import contextlib
import inspect
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

def check_file_exists():
    """Check if the solution file exists"""
    return os.path.isfile('wildlife_conservation_tracking_system.py')

class TestAssignment(unittest.TestCase):
    def setUp(self):
        """Standard setup for all test methods"""
        self.test_obj = TestUtils()
        self.module_obj = load_module_dynamically()

    def test_variable_naming(self):
        """Test that the required variable names and structure are used"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestVariableNaming", False, "functional")
                print("TestVariableNaming = Failed")
                return
            
            # Collect errors
            errors = []
            
            # Check if initialize_data function exists
            if not check_function_exists(self.module_obj, "initialize_data"):
                errors.append("initialize_data function is missing")
            else:
                try:
                    # Check dictionary initialization
                    init_source = inspect.getsource(self.module_obj.initialize_data)
                    if "species_data = {" not in init_source:
                        errors.append("Initialize data must create species_data dictionary")
                    if "new_species = {" not in init_source:
                        errors.append("Initialize data must create new_species dictionary")
                except Exception as e:
                    errors.append(f"Error checking initialize_data: {str(e)}")
            
            # Check if main function exists
            if not check_function_exists(self.module_obj, "main"):
                errors.append("main function is missing")
            else:
                try:
                    # Check main function uses required data
                    main_source = inspect.getsource(self.module_obj.main)
                    if "species_data, new_species = initialize_data()" not in main_source:
                        errors.append("main() must initialize species data")
                except Exception as e:
                    errors.append(f"Error checking main function: {str(e)}")
            
            # Check dictionary operation functions use correct parameter names
            try:
                module_source = inspect.getsource(self.module_obj)
                required_function_signatures = [
                    "def filter_by_conservation_status(species_data, status)",
                    "def filter_by_population_range(species_data, min_population, max_population)",
                    "def merge_species_data(existing_species, new_species)"
                ]
                
                for signature in required_function_signatures:
                    if signature not in module_source:
                        errors.append(f"{signature.split('(')[0]} must use correct parameters")
            except Exception as e:
                errors.append(f"Error checking function signatures: {str(e)}")
            
            # Report results
            if errors:
                self.test_obj.yakshaAssert("TestVariableNaming", False, "functional")
                print("TestVariableNaming = Failed")
            else:
                self.test_obj.yakshaAssert("TestVariableNaming", True, "functional")
                print("TestVariableNaming = Passed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestVariableNaming", False, "functional")
            print("TestVariableNaming = Failed")

    def test_dictionary_operations(self):
        """Test all dictionary operations"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestDictionaryOperations", False, "functional")
                print("TestDictionaryOperations = Failed")
                return
            
            # Collect errors
            errors = []
            
            # Check required functions
            required_functions = [
                "initialize_data",
                "filter_by_conservation_status",
                "filter_by_population_range",
                "filter_by_habitat_type",
                "filter_by_sanctuary",
                "find_species_with_keyword",
                "update_species_population",
                "update_conservation_status",
                "add_species_threat",
                "merge_species_data",
                "calculate_status_counts",
                "calculate_total_population",
                "find_most_threatened_species",
                "create_population_brackets"
            ]
            
            for func_name in required_functions:
                if not check_function_exists(self.module_obj, func_name):
                    errors.append(f"Required function {func_name} is missing")
            
            if errors:
                self.test_obj.yakshaAssert("TestDictionaryOperations", False, "functional")
                print("TestDictionaryOperations = Failed")
                return
            
            try:
                # Initialize data and verify it returns expected values
                try:
                    result = safely_call_function(self.module_obj, "initialize_data")
                    if not isinstance(result, tuple) or len(result) != 2:
                        errors.append("initialize_data() should return a tuple of (species_data, new_species)")
                        raise ValueError("Invalid return value from initialize_data()")
                    
                    species_data, new_species = result
                    if not isinstance(species_data, dict):
                        errors.append("species_data should be a dictionary")
                        raise ValueError("species_data is not a dictionary")
                    
                    if not isinstance(new_species, dict):
                        errors.append("new_species should be a dictionary")
                        raise ValueError("new_species is not a dictionary")
                except Exception as e:
                    errors.append(f"Error in initialize_data: {str(e)}")
                    species_data = {}
                    new_species = {}
                
                # Test filter_by_conservation_status
                try:
                    if not species_data:
                        errors.append("Cannot test filter_by_conservation_status: species_data is empty")
                    else:
                        filtered = safely_call_function(self.module_obj, "filter_by_conservation_status", species_data, "Endangered")
                        if filtered is None:
                            errors.append("filter_by_conservation_status returns None")
                        elif not isinstance(filtered, dict):
                            errors.append("filter_by_conservation_status should return a dictionary")
                        elif len(species_data) > 0 and "SP001" in species_data and "SP002" in species_data:
                            # Only perform this check if we have the expected data
                            if not (len(filtered) == 2 and "SP001" in filtered and "SP002" in filtered):
                                errors.append("filter_by_conservation_status did not filter correctly")
                except Exception as e:
                    errors.append(f"Error in filter_by_conservation_status: {str(e)}")
                
                # Test filter_by_population_range
                try:
                    if not species_data:
                        errors.append("Cannot test filter_by_population_range: species_data is empty")
                    else:
                        filtered = safely_call_function(self.module_obj, "filter_by_population_range", species_data, 1000, 5000)
                        if filtered is None:
                            errors.append("filter_by_population_range returns None")
                        elif not isinstance(filtered, dict):
                            errors.append("filter_by_population_range should return a dictionary")
                        elif len(species_data) > 0 and "SP001" in species_data and "SP003" in species_data:
                            # Only perform this check if we have the expected data
                            if not (len(filtered) == 2 and "SP001" in filtered and "SP003" in filtered):
                                errors.append("filter_by_population_range did not filter correctly")
                except Exception as e:
                    errors.append(f"Error in filter_by_population_range: {str(e)}")
                
                # Test filter_by_habitat_type
                try:
                    if not species_data:
                        errors.append("Cannot test filter_by_habitat_type: species_data is empty")
                    else:
                        filtered = safely_call_function(self.module_obj, "filter_by_habitat_type", species_data, "Forest")
                        if filtered is None:
                            errors.append("filter_by_habitat_type returns None")
                        elif not isinstance(filtered, dict):
                            errors.append("filter_by_habitat_type should return a dictionary")
                        elif len(species_data) > 0 and "SP001" in species_data and "SP002" in species_data:
                            # Only perform this check if we have the expected data
                            if not (len(filtered) == 2 and "SP001" in filtered and "SP002" in filtered):
                                errors.append("filter_by_habitat_type did not filter correctly")
                except Exception as e:
                    errors.append(f"Error in filter_by_habitat_type: {str(e)}")
                
                # Test filter_by_sanctuary
                try:
                    if not species_data:
                        errors.append("Cannot test filter_by_sanctuary: species_data is empty")
                    else:
                        filtered = safely_call_function(self.module_obj, "filter_by_sanctuary", species_data, "Jim Corbett")
                        if filtered is None:
                            errors.append("filter_by_sanctuary returns None")
                        elif not isinstance(filtered, dict):
                            errors.append("filter_by_sanctuary should return a dictionary")
                        elif len(species_data) > 0 and "SP001" in species_data and "SP002" in species_data:
                            # Only perform this check if we have the expected data
                            if not (len(filtered) == 2 and "SP001" in filtered and "SP002" in filtered):
                                errors.append("filter_by_sanctuary did not filter correctly")
                except Exception as e:
                    errors.append(f"Error in filter_by_sanctuary: {str(e)}")
                
                # Test find_species_with_keyword
                try:
                    if not species_data:
                        errors.append("Cannot test find_species_with_keyword: species_data is empty")
                    else:
                        filtered = safely_call_function(self.module_obj, "find_species_with_keyword", species_data, "poach")
                        if filtered is None:
                            errors.append("find_species_with_keyword returns None")
                        elif not isinstance(filtered, dict):
                            errors.append("find_species_with_keyword should return a dictionary")
                        elif len(species_data) >= 3:
                            # At least 3 species have "Poaching" as a threat
                            if not len(filtered) >= 3:
                                errors.append("find_species_with_keyword did not filter correctly")
                except Exception as e:
                    errors.append(f"Error in find_species_with_keyword: {str(e)}")
                
                # Test update operations
                
                # Test update_species_population
                try:
                    if not species_data or "SP001" not in species_data:
                        errors.append("Cannot test update_species_population: species_data is empty or missing SP001")
                    else:
                        original_population = species_data["SP001"]["population"]
                        updated = safely_call_function(self.module_obj, "update_species_population", species_data, "SP001", 4000)
                        if updated is None:
                            errors.append("update_species_population returns None")
                        elif not isinstance(updated, dict):
                            errors.append("update_species_population should return a dictionary")
                        elif "SP001" not in updated or updated["SP001"]["population"] != 4000:
                            errors.append("update_species_population did not update correctly")
                        elif species_data["SP001"]["population"] != original_population:
                            errors.append("update_species_population modified the original dictionary")
                except Exception as e:
                    errors.append(f"Error in update_species_population: {str(e)}")
                
                # Test update_conservation_status
                try:
                    if not species_data or "SP003" not in species_data:
                        errors.append("Cannot test update_conservation_status: species_data is empty or missing SP003")
                    else:
                        original_status = species_data["SP003"]["conservation_status"]
                        updated = safely_call_function(self.module_obj, "update_conservation_status", species_data, "SP003", "Endangered")
                        if updated is None:
                            errors.append("update_conservation_status returns None")
                        elif not isinstance(updated, dict):
                            errors.append("update_conservation_status should return a dictionary")
                        elif "SP003" not in updated or updated["SP003"]["conservation_status"] != "Endangered":
                            errors.append("update_conservation_status did not update correctly")
                        elif species_data["SP003"]["conservation_status"] != original_status:
                            errors.append("update_conservation_status modified the original dictionary")
                except Exception as e:
                    errors.append(f"Error in update_conservation_status: {str(e)}")
                
                # Test add_species_threat
                try:
                    if not species_data or "SP001" not in species_data:
                        errors.append("Cannot test add_species_threat: species_data is empty or missing SP001")
                    else:
                        updated = safely_call_function(self.module_obj, "add_species_threat", species_data, "SP001", "Disease")
                        if updated is None:
                            errors.append("add_species_threat returns None")
                        elif not isinstance(updated, dict):
                            errors.append("add_species_threat should return a dictionary")
                        elif "SP001" not in updated or "Disease" not in updated["SP001"]["threats"]:
                            errors.append("add_species_threat did not update correctly")
                        elif "SP001" in species_data and "threats" in species_data["SP001"] and "Disease" in species_data["SP001"]["threats"]:
                            errors.append("add_species_threat modified the original dictionary")
                except Exception as e:
                    errors.append(f"Error in add_species_threat: {str(e)}")
                
                # Test merge operation
                try:
                    if not species_data or not new_species:
                        errors.append("Cannot test merge_species_data: species_data or new_species is empty")
                    else:
                        merged = safely_call_function(self.module_obj, "merge_species_data", species_data, new_species)
                        if merged is None:
                            errors.append("merge_species_data returns None")
                        elif not isinstance(merged, dict):
                            errors.append("merge_species_data should return a dictionary")
                        elif len(merged) != len(species_data) + len(new_species):
                            errors.append("merge_species_data did not merge correctly")
                        elif "NS001" in merged and not merged["NS001"].get("newly_added", False):
                            errors.append("merge_species_data did not add 'newly_added' flag")
                except Exception as e:
                    errors.append(f"Error in merge_species_data: {str(e)}")
                
                # Test statistics operations
                
                # Test calculate_status_counts
                try:
                    if not species_data:
                        errors.append("Cannot test calculate_status_counts: species_data is empty")
                    else:
                        counts = safely_call_function(self.module_obj, "calculate_status_counts", species_data)
                        if counts is None:
                            errors.append("calculate_status_counts returns None")
                        elif not isinstance(counts, dict):
                            errors.append("calculate_status_counts should return a dictionary")
                        else:
                            # Check if all conservation statuses are included
                            statuses = set(species["conservation_status"] for species in species_data.values())
                            if not all(status in counts for status in statuses):
                                errors.append("calculate_status_counts did not count all statuses")
                except Exception as e:
                    errors.append(f"Error in calculate_status_counts: {str(e)}")
                
                # Test calculate_total_population
                try:
                    if not species_data:
                        errors.append("Cannot test calculate_total_population: species_data is empty")
                    else:
                        total = safely_call_function(self.module_obj, "calculate_total_population", species_data)
                        if total is None:
                            errors.append("calculate_total_population returns None")
                        elif not isinstance(total, (int, float)):
                            errors.append("calculate_total_population should return a number")
                        else:
                            # Calculate expected total
                            expected_total = sum(species["population"] for species in species_data.values())
                            if total != expected_total:
                                errors.append("calculate_total_population did not calculate correctly")
                except Exception as e:
                    errors.append(f"Error in calculate_total_population: {str(e)}")
                
                # Test find_most_threatened_species
                try:
                    if not species_data:
                        errors.append("Cannot test find_most_threatened_species: species_data is empty")
                    else:
                        most_threatened = safely_call_function(self.module_obj, "find_most_threatened_species", species_data)
                        if most_threatened is None:
                            errors.append("find_most_threatened_species returns None")
                        elif not isinstance(most_threatened, tuple) or len(most_threatened) != 2:
                            errors.append("find_most_threatened_species should return a tuple of (species_id, species_data)")
                        elif "SP005" in species_data and most_threatened[0] != "SP005":
                            # Indian Vulture is Critically Endangered
                            errors.append("find_most_threatened_species did not find the correct species")
                except Exception as e:
                    errors.append(f"Error in find_most_threatened_species: {str(e)}")
                
                # Test create_population_brackets
                try:
                    if not species_data:
                        errors.append("Cannot test create_population_brackets: species_data is empty")
                    else:
                        brackets = safely_call_function(self.module_obj, "create_population_brackets", species_data)
                        if brackets is None:
                            errors.append("create_population_brackets returns None")
                        elif not isinstance(brackets, dict):
                            errors.append("create_population_brackets should return a dictionary")
                        elif not all(key in brackets for key in ["critical", "endangered", "vulnerable", "stable"]):
                            errors.append("create_population_brackets does not contain all required brackets")
                        elif "SP004" in species_data and "SP002" in species_data and not ("SP004" in brackets["critical"] and "SP002" in brackets["stable"]):
                            errors.append("create_population_brackets did not categorize correctly")
                except Exception as e:
                    errors.append(f"Error in create_population_brackets: {str(e)}")
                
                # Report results
                if errors:
                    self.test_obj.yakshaAssert("TestDictionaryOperations", False, "functional")
                    print("TestDictionaryOperations = Failed")
                else:
                    self.test_obj.yakshaAssert("TestDictionaryOperations", True, "functional")
                    print("TestDictionaryOperations = Passed")
                    
            except Exception as e:
                self.test_obj.yakshaAssert("TestDictionaryOperations", False, "functional")
                print("TestDictionaryOperations = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestDictionaryOperations", False, "functional")
            print("TestDictionaryOperations = Failed")

    def test_implementation_techniques(self):
        """Test implementation of dictionary techniques"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestImplementationTechniques", False, "functional")
                print("TestImplementationTechniques = Failed")
                return
            
            # Collect errors
            errors = []
            
            # Check required functions
            required_functions = [
                "filter_by_conservation_status",
                "calculate_status_counts",
                "update_species_population",
                "merge_species_data",
                "initialize_data"
            ]
            
            for func_name in required_functions:
                if not check_function_exists(self.module_obj, func_name):
                    errors.append(f"Required function {func_name} is missing")
            
            if errors:
                self.test_obj.yakshaAssert("TestImplementationTechniques", False, "functional")
                print("TestImplementationTechniques = Failed")
                return
            
            try:
                # Check dictionary comprehension
                try:
                    source = inspect.getsource(self.module_obj.filter_by_conservation_status)
                    has_comprehension = "{" in source and "for" in source and "if" in source
                    if not has_comprehension:
                        errors.append("filter_by_conservation_status must use dictionary comprehension")
                except Exception as e:
                    errors.append(f"Error checking dictionary comprehension: {str(e)}")
                
                # Check dictionary methods
                try:
                    source = inspect.getsource(self.module_obj.calculate_status_counts)
                    has_dict_methods = ".values()" in source or ".items()" in source or ".keys()" in source
                    if not has_dict_methods:
                        errors.append("calculate_status_counts must use dictionary methods")
                except Exception as e:
                    errors.append(f"Error checking dictionary methods: {str(e)}")
                
                # Check dictionary unpacking
                try:
                    source1 = inspect.getsource(self.module_obj.update_species_population)
                    source2 = inspect.getsource(self.module_obj.merge_species_data)
                    has_unpacking = "**" in source1 and "**" in source2
                    if not has_unpacking:
                        errors.append("update_species_population and merge_species_data must use dictionary unpacking")
                except Exception as e:
                    errors.append(f"Error checking dictionary unpacking: {str(e)}")
                
                # Check data immutability
                try:
                    result = safely_call_function(self.module_obj, "initialize_data")
                    if not isinstance(result, tuple) or len(result) != 2:
                        errors.append("initialize_data() should return a tuple of (species_data, new_species)")
                    else:
                        species_data, _ = result
                        if not isinstance(species_data, dict):
                            errors.append("species_data should be a dictionary")
                        elif not species_data:
                            errors.append("species_data is empty")
                        elif "SP001" not in species_data:
                            errors.append("species_data does not contain SP001")
                        else:
                            original_population = species_data["SP001"]["population"]
                            updated = safely_call_function(self.module_obj, "update_species_population", species_data, "SP001", original_population + 1000)
                            
                            if updated is None:
                                errors.append("update_species_population returns None")
                            elif not isinstance(updated, dict):
                                errors.append("update_species_population should return a dictionary")
                            elif "SP001" not in updated:
                                errors.append("update_species_population did not update SP001")
                            elif updated["SP001"]["population"] != original_population + 1000:
                                errors.append("update_species_population did not update population correctly")
                            elif species_data["SP001"]["population"] != original_population:
                                errors.append("update_species_population modified the original dictionary")
                except Exception as e:
                    errors.append(f"Error checking data immutability: {str(e)}")
                
                # Report results
                if errors:
                    self.test_obj.yakshaAssert("TestImplementationTechniques", False, "functional")
                    print("TestImplementationTechniques = Failed")
                else:
                    self.test_obj.yakshaAssert("TestImplementationTechniques", True, "functional")
                    print("TestImplementationTechniques = Passed")
                    
            except Exception as e:
                self.test_obj.yakshaAssert("TestImplementationTechniques", False, "functional")
                print("TestImplementationTechniques = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestImplementationTechniques", False, "functional")
            print("TestImplementationTechniques = Failed")

    def test_display_functions(self):
        """Test display and formatting functions"""
        try:
            # Check if module can be imported
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestDisplayFunctions", False, "functional")
                print("TestDisplayFunctions = Failed")
                return
            
            # Collect errors
            errors = []
            
            # Check if required functions exist
            if not check_function_exists(self.module_obj, "get_formatted_species"):
                errors.append("get_formatted_species function is missing")
                self.test_obj.yakshaAssert("TestDisplayFunctions", False, "functional")
                print("TestDisplayFunctions = Failed")
                return
            
            try:
                # Get sample data
                result = safely_call_function(self.module_obj, "initialize_data")
                if not isinstance(result, tuple) or len(result) < 1:
                    errors.append("Cannot test display functions: initialize_data() failed")
                    self.test_obj.yakshaAssert("TestDisplayFunctions", False, "functional")
                    print("TestDisplayFunctions = Failed")
                    return
                
                species_data, _ = result
                if not species_data:
                    errors.append("Cannot test display functions: species_data is empty")
                    self.test_obj.yakshaAssert("TestDisplayFunctions", False, "functional")
                    print("TestDisplayFunctions = Failed")
                    return
                
                # Test get_formatted_species
                try:
                    sid = next(iter(species_data.keys()))
                    species = species_data[sid]
                    formatted = safely_call_function(self.module_obj, "get_formatted_species", sid, species)
                    
                    if formatted is None:
                        errors.append("get_formatted_species returned None")
                    elif not isinstance(formatted, str):
                        errors.append(f"get_formatted_species should return a string, got {type(formatted)}")
                    else:
                        # Check format contains required elements
                        required_elements = [
                            sid,
                            species["name"],
                            species["scientific_name"],
                            species["conservation_status"],
                            "Population:",
                            "Habitat:",
                            species["habitat_type"]
                        ]
                        
                        for element in required_elements:
                            if str(element) not in formatted:
                                errors.append(f"Formatted species should contain '{element}'")
                        
                        # Check for population formatting (thousands separator)
                        if f"{species['population']:,}" not in formatted:
                            errors.append("Population should be formatted with thousands separator")
                except Exception as e:
                    errors.append(f"Error testing get_formatted_species: {str(e)}")
                
                # Test display_data function if it exists
                if check_function_exists(self.module_obj, "display_data"):
                    try:
                        # Test with None data - should not crash
                        safely_call_function(self.module_obj, "display_data", None, "species")
                        
                        # Test with empty data - should not crash
                        safely_call_function(self.module_obj, "display_data", {}, "species")
                        
                        # Test with valid data - should not crash
                        safely_call_function(self.module_obj, "display_data", species_data, "species")
                        
                    except Exception as e:
                        errors.append(f"Error testing display_data: {str(e)}")
                
                # Report results
                if errors:
                    self.test_obj.yakshaAssert("TestDisplayFunctions", False, "functional")
                    print("TestDisplayFunctions = Failed")
                else:
                    self.test_obj.yakshaAssert("TestDisplayFunctions", True, "functional")
                    print("TestDisplayFunctions = Passed")
                    
            except Exception as e:
                self.test_obj.yakshaAssert("TestDisplayFunctions", False, "functional")
                print("TestDisplayFunctions = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestDisplayFunctions", False, "functional")
            print("TestDisplayFunctions = Failed")

if __name__ == '__main__':
    unittest.main()