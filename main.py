import json
import datetime
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io.filebasedsink import CompressionTypes
from apache_beam.io.textio import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions


class FilterAndSumFn(beam.DoFn):
    """
    A DoFn class that filters and transforms incoming data.
    
    The incoming data is expected to be a CSV string. The method processes the data and 
    yields a tuple of (date, transaction_amount) if the year of the transaction is greater 
    than or equal to 2010 and the transaction amount is greater than 20.
    """
    
    def process(self, element):
        fields = element.split(',')

        if fields[0] == 'timestamp':
            return []

        date = fields[0]
        transaction_amount = float(fields[-1])
        year = int(date.split('-')[0])

        if year >= 2010 and transaction_amount > 20:
            yield (date, transaction_amount)


class ProcessTransactions(beam.PTransform):
    """
    A PTransform class that filters, transforms and writes transaction data.

    The class takes in a PCollection of transaction data as strings, filters and transforms 
    it using the FilterAndSumFn DoFn, formats the results for output, and writes the results 
    to a .jsonl.gz file. The output file's name includes a timestamp. The PTransform returns 
    a PCollection of the formatted output data.
    """

    def expand(self, pcoll):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # Generate a timestamp
        result = (
            pcoll
            | 'Filter and map to KV' >> beam.ParDo(FilterAndSumFn())
            | 'Sum by date' >> beam.CombinePerKey(sum)
            | 'Format for output' >> beam.Map(lambda element: json.dumps({'date': element[0], 'sum': element[1]}))
        )
        _ = result | 'Write to Jsonl' >> WriteToText(f'results_{timestamp}.jsonl', file_name_suffix=".gz", compression_type=CompressionTypes.GZIP)
        return result


def run():
    """
    Main function to run the Beam pipeline.

    This function sets up and runs a Beam pipeline that reads transaction data from a GCS 
    bucket, processes it using the ProcessTransactions PTransform, and writes the results 
    to a .jsonl.gz file. The function does not return a value.
    """

    pipeline_options = PipelineOptions()

    with beam.Pipeline(options=pipeline_options) as p:
        transactions = (
            p
            | 'Read from GCS' >> ReadFromText('gs://cloud-samples-data/bigquery/sample-transactions/transactions.csv')
            | 'Process Transactions' >> ProcessTransactions()
        )



if __name__ == '__main__':
    run()