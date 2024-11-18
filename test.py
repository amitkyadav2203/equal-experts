import unittest
import requests

class TestGistAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = 'http://github-gist-container:5000'
        cls.test_user = 'octocat'
        print("\nStarting tests for Gist API...\n")

    def test_get_gists_status_code(self):
        """Test if the API endpoint returns a 200 status code for a valid user."""
        print(f"Testing status code for user '{self.test_user}'...")
        response = requests.get(f'{self.base_url}/{self.test_user}')
        result = "Passed" if response.status_code == 200 else "Failed"
        print(f"Status Code Test: {result}")
        self.assertEqual(response.status_code, 200)

    def test_content_type(self):
        """Test if the response content type is JSON."""
        print("Testing content type for JSON response...")
        response = requests.get(f'{self.base_url}/{self.test_user}')
        result = "Passed" if response.headers['Content-Type'] == 'application/json' else "Failed"
        print(f"Content Type Test: {result}")
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_gists_structure(self):
        """Test if the response contains a list of gists with expected fields."""
        print("Testing response structure and expected fields...")
        response = requests.get(f'{self.base_url}/{self.test_user}')
        gists = response.json()

        # Verify that the response is a list
        result = "Passed" if isinstance(gists, list) else "Failed"
        print(f"Response Structure Test (List): {result}")
        self.assertIsInstance(gists, list)

        # Verify each gist has 'id', 'url', and 'description' fields
        all_fields_present = all('id' in gist and 'url' in gist and 'description' in gist for gist in gists)
        result = "Passed" if all_fields_present else "Failed"
        print(f"Gist Fields Test: {result}")
        self.assertTrue(all_fields_present)

    def test_invalid_user(self):
        """Test if the API handles an invalid username properly."""
        invalid_user = 'nonexistentuser1234'
        print(f"Testing invalid username handling for '{invalid_user}'...")
        response = requests.get(f'{self.base_url}/{invalid_user}')
        result = "Passed" if response.status_code == 404 else "Failed"
        print(f"Invalid User Test: {result}")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main(verbosity=2)

