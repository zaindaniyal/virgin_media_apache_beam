import unittest
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to, is_empty
from main import ProcessTransactions
import apache_beam as beam

class ProcessTransactionsUnitTestPass(unittest.TestCase):
    def test_process_transactions_pass(self):
        """
        Test case for ProcessTransactions with valid input data.
        
        The test case feeds valid transaction data into the ProcessTransactions transform 
        and asserts that the output matches the expected results. The input data is designed 
        to meet the transform's filtering criteria.
        """

        # Input data containing valid transactions
        input_data = [
            'timestamp,transaction_amount',
            '2022-01-01,25.0',
            '2022-01-02,30.0',
            '2022-01-03,40.0'
        ]

        # Expected output
        expected_output = [
            '{"date": "2022-01-01", "sum": 25.0}',
            '{"date": "2022-01-02", "sum": 30.0}',
            '{"date": "2022-01-03", "sum": 40.0}'
        ]

        # Create a TestPipeline
        with TestPipeline() as p:
            # Create a PCollection from the input data
            input_pcoll = p | beam.Create(input_data)

            # Apply the ProcessTransactions transform
            result = input_pcoll | ProcessTransactions()

            print('debug result', type(result))

            # Assert that the output matches the expected output
            assert_that(result, equal_to(expected_output))

class ProcessTransactionsUnitTestFail(unittest.TestCase):
    def test_process_transactions_with_invalid_input(self):
        """
        Test case for ProcessTransactions with invalid input data.
        
        The test case feeds transaction data that does not meet the filtering criteria into 
        the ProcessTransactions transform and asserts that the output is an empty PCollection.
        """

        # Input data containing transactions that do not meet the filtering criteria
        input_data = [
            'timestamp,transaction_amount',
            '2022-01-01,10.0',
            '2022-01-02,15.0',
            '2022-01-03,5.0'
        ]

        # Create a TestPipeline
        with TestPipeline() as p:
            # Create a PCollection from the input data
            input_pcoll = p | beam.Create(input_data)

            # Apply the ProcessTransactions transform
            result = input_pcoll | ProcessTransactions()

            # Modify the expected output to include some data
            expected_output = [
                '{"date": "2022-01-01", "sum": 25.0}',  # Include data that should not be present
                '{"date": "2022-01-02", "sum": 30.0}',  # Include data that should not be present
                '{"date": "2022-01-03", "sum": 40.0}'   # Include data that should not be present
            ]

            # Assert that the output PCollection is empty
            assert_that(result, is_empty())

            # Assert that the output does not match the modified expected output
            assert_that(result, equal_to(expected_output), label="Fail test")