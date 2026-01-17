## Amazon SQS – Message Queues

### Steps Performed
1. Created three Standard SQS queues: `queue-1`, `queue-2`, and `queue-3`.
2. Subscribed each SQS queue to the SNS topic.
3. Updated each queue access policy to allow the SNS topic to send messages.
4. Verified message delivery from SNS to SQS using CloudWatch metrics.
