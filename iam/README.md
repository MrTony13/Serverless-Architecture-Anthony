## IAM – Permissions and Security

### Steps Performed
1. Created an IAM role for Lambda execution.
2. Attached AWSLambdaBasicExecutionRole for logging.
3. Attached AmazonS3FullAccess to allow object read/write.
4. Attached AmazonSQSFullAccess to allow message processing.
5. Assigned this role to all Lambda functions.
