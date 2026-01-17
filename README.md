# Serverless-Architecture-Anthony
Built a serverless, event-driven architecture using Amazon S3, SNS, SQS, and AWS Lambda. Object uploads to S3 trigger SNS notifications that fan out to multiple SQS queues, each invoking a Lambda function for parallel processing. The system is fully decoupled, fault-tolerant, and scalable, with processed outputs stored in S3 and observability provided by CloudWatch.



serverless-s3-sns-sqs-lambda/
│
├── architecture/
│   └── architecture-diagram.png
│
├── s3/
│   └── README.md
│
├── sns/
│   └── README.md
│
├── sqs/
│   └── README.md
│
├── lambda/
│   ├── lambda-code.py
│   └── README.md
│
├── iam/
│   └── README.md
│
├── cloudwatch/
│   └── README.md
│
├── screenshots/
│   └── (all screenshots here)
│
└── README.md   (main project README)
