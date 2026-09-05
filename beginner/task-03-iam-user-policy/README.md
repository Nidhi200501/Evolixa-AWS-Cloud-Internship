# Task 3: Create an IAM User and Apply Least Privilege

## 🎯 Objective
Create an IAM user with limited access and understand least privilege.

## 🛠️ Services Used
- AWS IAM
- IAM Users
- IAM Policies

## 📋 Steps Performed

### 1. IAM User Created
- Username: `task3-iam-user`
- Access type: Programmatic access only

### 2. Policy Attached
- Policy: `AdministratorAccess` (for learning purposes)
- In production, only specific S3 permissions would be given

### 3. Access Keys Generated
- Access Key ID and Secret Access Key generated
- Used for AWS CLI configuration

### 4. Test Allowed Operation
```bash
aws sts get-caller-identity
✅ Successfully returned user ARN

5. Test Denied Operation
Not applicable because AdminAccess allows all actions.

In production, denied actions would be tested with a restricted policy.

🔐 Least Privilege Explanation
Principle of Least Privilege:
"Give users only the permissions they need to perform their job — nothing more."

Why AdminAccess is Inappropriate for a Junior Developer:
Reason	Explanation
🔴 Security Risk	Can delete/modify critical resources
🔴 No Audit Trail	Difficult to track who did what
🔴 Accidental Damage	One wrong command can break production
🔴 Compliance Issues	Violates security best practices
What Should Be Given Instead:
json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::task2-nidhi-website",
        "arn:aws:s3:::task2-nidhi-website/*"
      ]
    }
  ]
}
Production Improvements:
Use IAM roles instead of access keys

Enable MFA for all users

Rotate keys every 90 days

Use CloudTrail for auditing

Regular permission reviews

✅ Results
✅ IAM user created

✅ Policy attached

✅ Access keys generated

✅ Least privilege explained

✅ Security considerations documented

Test Denied Operation
AdminAccess allows all actions, so denied test was performed with a restricted policy.

Created S3ReadOnlyPolicy allowing only s3:GetObject.

Attempted s3:PutObject → ❌ AccessDenied error received.

Test Command:

bash
aws s3 cp test.txt s3://task2-nidhi-website/ --profile test-user
Result:

text
An error occurred (AccessDenied) when calling the PutObject operation


Least Privilege Explanation
Principle of Least Privilege:
"Give users only the permissions they need to perform their job — nothing more."

Why AdminAccess is Inappropriate for a Junior Developer:
Reason	Explanation
🔴 Security Risk	Can delete/modify critical resources
🔴 No Audit Trail	Difficult to track who did what
🔴 Accidental Damage	One wrong command can break production
🔴 Compliance Issues	Violates security best practices
What Should Be Given Instead:
json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::task2-nidhi-website",
        "arn:aws:s3:::task2-nidhi-website/*"
      ]
    }
  ]
}
Production Improvements:
Use IAM roles instead of access keys

Enable MFA for all users

Rotate keys every 90 days

Use CloudTrail for auditing

Regular permission reviews




📅 Completion Date
2026-08-21

👩‍💻 Intern
Nidhi Pandey

video:-https://drive.google.com/file/d/14VypVx1rup7uGNViFNushJkhQcnrDBYD/view?usp=sharing