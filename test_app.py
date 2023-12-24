import unittest
from app import app, insertion_sort, merge_sort, bubble_sort
import copy

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Initialize Flask test client
        self.app.testing = True  # Set testing to True

    def tearDown(self):
        pass  # Clean up after each test if needed

    # Test routes and functionalities
    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Check if route returns 200 OK
    
    def test_sort_route_valid_input(self):
        # Test sorting with valid input
        data = {'numbers': '5 4 3 2 1', 'algorithm': 'insertion'}  # Sample valid input
        response = self.app.post('/sort', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)  # Check if route returns 200 OK
        # Add more assertions based on expected behavior
        
    def test_sort_route_invalid_input(self):
        # Test sorting with invalid input
        data = {'numbers': 'a b c', 'algorithm': 'bubble'}  # Sample invalid input
        response = self.app.post('/sort', data=data, follow_redirects=True)
        self.assertNotEqual(response.status_code, 200)  # Check if route does not return 200 OK for invalid input
        # Add more assertions based on expected behavior

    # Test sorting algorithms
    def test_insertion_sort(self):
        numbers = [5, 4, 3, 2, 1]
        sorted_numbers = [1, 2, 3, 4, 5]  # Expected sorted result
        self.assertEqual(insertion_sort(copy.deepcopy(numbers)), sorted_numbers)  # Check if insertion sort works correctly
    
    def test_merge_sort(self):
        # Test merge sort functionality
        numbers = [5, 3, 4, 2, 1]
        sorted_numbers = [1, 2, 3, 4, 5]  # Expected sorted result
        self.assertEqual(merge_sort(copy.deepcopy(numbers)), sorted_numbers)  # Check if merge sort works correctly

    def test_bubble_sort(self):
        # Test bubble sort functionality
        numbers = [5, 3, 4, 2, 1]
        sorted_numbers = [1, 2, 3, 4, 5]  # Expected sorted result
        self.assertEqual(bubble_sort(copy.deepcopy(numbers)), sorted_numbers)  # Check if bubble sort works correctly

# Run the tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()
