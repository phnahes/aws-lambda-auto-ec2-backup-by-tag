# aws-lambda-auto-ec2-backup-by-tag
AWS - Automatic backup for resources that using specific tag


### Permissions
Needed use permissions below:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateImage",
                "ec2:DeleteSnapshot",
                "ec2:DeregisterImage",
                "ec2:DescribeImages",
                "ec2:DescribeInstances",
                "ec2:DescribeSnapshots",
                "ec2:CreateTags",
                "ec2:DescribeRegions"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        }
    ]
}
```

### Scheduler

1. Add new Trigger
2. Choose EventBridge (CloudWatch Events)
3. Define names and descriptions
4. Use rate(15 days) to make backups each 15 days
