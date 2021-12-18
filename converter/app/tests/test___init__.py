import unittest
from app import app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_to_roman_200(self):
        '''
        Requests from positive integers between 0 and 3999 inclusive to Roman Numerals
        '''
        with self.app.get("/api/v1/converter/to-roman?value=0") as response:
            self.assertEqual(200, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("nulla", response.data.decode("utf-8"))

        with self.app.get("/api/v1/converter/to-roman?value=1") as response:
            self.assertEqual(200, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("I", response.data.decode("utf-8"))

        with self.app.get("/api/v1/converter/to-roman?value=3999") as response:
            self.assertEqual(200, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("MMMCMXCIX", response.data.decode("utf-8"))

    def test_to_roman_400(self):
        '''
        Invalid requests when trying to convert from numbers to Roman Numerals
        '''
        with self.app.get("/api/v1/converter/to-roman?value=-1") as response:
            self.assertEqual(400, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("Error: Invalid Number", response.data.decode("utf-8"))

        with self.app.get("/api/v1/converter/to-roman?value=4000") as response:
            self.assertEqual(400, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("Error: Invalid Number", response.data.decode("utf-8"))

        with self.app.get("/api/v1/converter/to-roman?value=5.5") as response:
            self.assertEqual(400, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("Error: Invalid Number", response.data.decode("utf-8"))

        with self.app.get("/api/v1/converter/to-roman?value=test") as response:
            self.assertEqual(400, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("Error: Invalid Number", response.data.decode("utf-8"))

    def test_to_number_200(self):
        '''
        Requests from Roman Numerals to positive integers between 0 and 3999 inclusive
        '''
        with self.app.get("/api/v1/converter/to-number?value=nulla") as response:
            self.assertEqual(200, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual(0, int(response.data.decode("utf-8")))

        with self.app.get("/api/v1/converter/to-number?value=I") as response:
            self.assertEqual(200, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual(1, int(response.data.decode("utf-8")))

        with self.app.get("/api/v1/converter/to-number?value=i") as response:
            self.assertEqual(200, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual(1, int(response.data.decode("utf-8")))

        with self.app.get("/api/v1/converter/to-number?value=MMMCMXCIX") as response:
            self.assertEqual(200, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual(3999, int(response.data.decode("utf-8")))

    def test_to_number_400(self):
        '''
        Invalid requests when trying to convert from Roman Numerals to numbers
        '''
        with self.app.get("/api/v1/converter/to-number?value=IIIIV") as response:
            self.assertEqual(400, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("Error: Invalid Roman Numeral", str(response.data.decode("utf-8")))

        with self.app.get("/api/v1/converter/to-number?value=XXXX") as response:
            self.assertEqual(400, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("Error: Invalid Roman Numeral", str(response.data.decode("utf-8")))

        with self.app.get("/api/v1/converter/to-number?value=MAX") as response:
            self.assertEqual(400, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("Error: Invalid Roman Numeral", str(response.data.decode("utf-8")))

        with self.app.get("/api/v1/converter/to-number?value=IVM") as response:
            self.assertEqual(400, response.status_code)
            self.assertEqual("text/plain", response.content_type)
            self.assertEqual("Error: Invalid Roman Numeral", str(response.data.decode("utf-8")))


if __name__ == "__main__":
    unittest.main()
