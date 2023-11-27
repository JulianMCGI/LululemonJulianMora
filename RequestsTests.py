import requests
import unittest

class TestAPITester(unittest.TestCase):

    def test_status_code(self):
        status_code = requests.get("https://jsonplaceholder.typicode.com/todos/").status_code
        self.assertEqual(status_code, 200)

    def test_field_completed_for_id_5_false(self):
        response = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
        try:
            for entry in response:
                if entry["id"] == 5:
                    isCompleted = entry["completed"]
        except:
            print("Not found")
        self.assertFalse(isCompleted)

if __name__ == "__main__":
    unittest.main()
