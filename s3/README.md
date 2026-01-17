## Amazon S3 – Ingestion and Processed Buckets

### Steps Performed
1. Created an S3 bucket named `my-ingestion-bucket` to receive uploaded objects.
2. Created a second S3 bucket named `my-processed-bucket` to store processed results.
3. Kept default settings with public access blocked.
4. Configured an event notification on the ingestion bucket for all object creation events.
5. Set the event destination to an Amazon SNS topic.
