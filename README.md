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

1. Now we will schedule the function so that it is executed daily or as often as you wish. Select your role on the Lambda console and go to the “Event Sources” tab. Click on “Add Event Source”;
2. In the “Event Source Type” field, select “Schedule Event”;
3. In the “Schedule expression” field, enter your cron expression. Suggestion: to make your backups every day at two in the morning (São Paulo time), configure the expression with two more hours, as the schedule is done in UTC time. So, instead of 2, use 4. The expression looks like this: cron (0 4 * *? *);
