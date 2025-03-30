import boto3
import csv
import io
import os
import pandas as pd

os.environ['BUCKET_NAME'] = "shiv-data-analytics"

os.environ['OP_PATH'] = "output_file"

os.environ['OP_FILE_NAME'] = "processed_data"

def write_dataframe_to_s3(df):
    """
    Writes a Pandas DataFrame to an S3 bucket as a CSV file.

    :param df: Pandas DataFrame to write.
    :param bucket_name: Name of the S3 bucket.
    :param file_name: Name of the CSV file in S3.
    """
    try:

        # Replace with your S3 bucket name and file path
        bucket_name = os.getenv('BUCKET_NAME')
        file_name = f"{os.getenv('OP_PATH')}/{os.getenv('OP_FILE_NAME')}.csv"

        # Create an in-memory buffer
        csv_buffer = io.StringIO()
        
        # Write DataFrame to buffer
        df.to_csv(csv_buffer, index=False)
        
        # Create S3 client (uses environment variables for credentials)
        s3_client = boto3.client('s3')
        
        # Upload CSV to S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=csv_buffer.getvalue()
        )
        
        print(f"DataFrame successfully written to s3://{bucket_name}/{file_name}")
    
    except Exception as e:
        print(f"Error writing DataFrame to S3: {e}")

if __name__ == "__main__":
    # Example usage
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [30, 25, 35],
        "City": ["New York", "Los Angeles", "Chicago"]
    }
    df = pd.DataFrame(data)
    write_dataframe_to_s3(df)