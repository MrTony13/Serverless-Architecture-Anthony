## Amazon SNS – Event Fan-out

### Steps Performed
1. Created an SNS Standard topic named `s3-event-topic`.
2. Configured the topic to receive event notifications from the S3 ingestion bucket.
3. Created subscriptions to fan out events to multiple SQS queues.
4. Verified that all subscriptions were successfully confirmed.
