## AWS Lambda – Parallel Processing

### Steps Performed
1. Created three Lambda functions using Python 3.10.
2. Assigned a custom IAM role with permissions for S3, SQS, and CloudWatch Logs.
3. Added each SQS queue as an event source trigger for its corresponding Lambda.
4. Implemented logic to read S3 event data from SQS messages.
5. Processed the uploaded object and stored results in separate S3 prefixes based on the Lambda function name.
