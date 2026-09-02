from house_prediction.API import call_API
from house_prediction.database import create_database
import unittest
# MagicMock create a fake object, patch replace real object with fake object
from unittest.mock import patch, MagicMock

class TestMain(unittest.TestCase):

    @patch("house_prediction.API.http.client.HTTPSConnection") # http.client.HTTPSConnection(...) will not run and it will run with mock
    def test_call_api(self, mock_connection):

        mock_conn = MagicMock() # create fake connection
        mock_connection.return_value = mock_conn # conn = mock_conn

        mock_response = MagicMock() # getresponse = make a fake response
        mock_response.read.return_value = b'{"posts": []}' # res.read() = b'{"posts": []}'

        mock_conn.getresponse.return_value = mock_response # instead of real server response, it will return mock_response

        result = call_API() # using no internet, not calling real API, just using mock

        self.assertEqual(result, {"posts": []})
    def create_database_test(self):
        @patch("house_prediction.database.mysql.connector.connect")
    def test_create_database(self, mock_connect):

        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        create_database()

        mock_connect.assert_called_once()
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called()
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()
    def generate_ads_test(self):

    def insert_data_test(self):

    def create_csv_test(self):

if __name__ == '__main__':
    unittest.main()