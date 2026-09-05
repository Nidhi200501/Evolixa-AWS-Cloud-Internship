# Task 14: Build a Secure Application File Storage System

## 🎯 Objective
Design a system where an application running on EC2 can store files in S3 without exposing long-term AWS credentials inside the application.

## 🏢 Scenario
A web application allows users to upload documents. The development team currently wants to place AWS credentials directly inside the application configuration. This task designs a safer approach using IAM roles.

## 🛠️ Services Used
- AWS EC2
- Amazon S3
- AWS IAM Roles & Policies
- AWS CLI
- Python (boto3)

---

## 📋 Steps Performed

### 1. Understand Application Requirement
- Users upload documents to the application
- Files need to be stored securely
- No credentials should be hardcoded

### 2. S3 Bucket Created
- **Bucket Name:** `task14-secure-bucket`
- **Region:** `ap-south-1` (Mumbai)
- **Public Access:** Blocked (private bucket)

### 3. Application Needs Defined
| Action | Permission Required |
|--------|---------------------|
| Upload files | `s3:PutObject` |
| Download files | `s3:GetObject` |
| List files | `s3:ListBucket` |

### 4. IAM Policy Created
**Policy Name:** `EC2S3AccessPolicy`

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::task14-secure-bucket",
        "arn:aws:s3:::task14-secure-bucket/*"
      ]
    }
  ]
}


5. IAM Role Created
Role Name: EC2S3AccessRole

Trusted Entity: EC2

Attached Policy: EC2S3AccessPolicy

6. EC2 Instance Launched with IAM Role
Instance Name: task14-secure-app

AMI: Ubuntu 26.04 LTS

Instance Type: t3.micro

IAM Role: EC2S3AccessRole ✅

Key Pair: task14-key

7. Application Configured
Created a Python script (upload.py) that uses boto3 to interact with S3.
import boto3
import os

BUCKET_NAME = "task14-secure-bucket"

# Use IAM role (no credentials hardcoded)
session = boto3.Session(profile_name='s3-admin')
s3 = session.client('s3')

def upload_file(file_name):
    try:
        s3.upload_file(file_name, BUCKET_NAME, file_name)
        print(f"✅ File '{file_name}' uploaded successfully")
        return True
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return False

def download_file(file_name):
    try:
        s3.download_file(BUCKET_NAME, file_name, f"downloaded_{file_name}")
        print(f"✅ File '{file_name}' downloaded successfully")
        return True
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return False

def list_files():
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in response:
            print("\n📁 Files in bucket:")
            for obj in response['Contents']:
                print(f"  - {obj['Key']} ({obj['Size']} bytes)")
        else:
            print("📁 Bucket is empty")
        return True
    except Exception as e:
        print(f"❌ List failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 S3 File Upload/Download Demo")
    print("-" * 40)
    
    test_file = "test.txt"
    with open(test_file, "w") as f:
        f.write("Hello from EC2! This is a test file.\n")
    print(f"✅ Created test file: {test_file}")
    
    print("\n📤 Uploading file...")
    upload_file(test_file)
    
    list_files()
    
    print("\n📥 Downloading file...")
    download_file(test_file)
    
    print("\n✅ Demo complete!")

    8. No Credentials in Source Code
✅ No Access Key ID

✅ No Secret Access Key

✅ IAM Role automatically provides credentials

✅ Credentials are temporary and rotated automatically

9. Test Permitted Operations ✅
Operation	Command	Result
Upload	upload_file('test.txt')	✅ Success
List	list_files()	✅ Success
Download	download_file('test.txt')	✅ Success
10. Test Denied Operations ❌

Operation	Command	Result
Delete Object	aws s3 rm s3://.../test.txt	❌ AccessDenied
Delete Bucket	aws s3 rb s3://...	❌ AccessDenied
Create Bucket	aws s3 mb s3://...	❌ AccessDenied
11. Object Organization
Files are stored directly in the bucket root

Future improvement: Use folders/prefixes for organization

12. Bucket Access Settings
✅ Block Public Access: Enabled

✅ Bucket Policy: Restricted to IAM role

✅ No public access to objects

Additional Protections Required in Production
MFA - Enable for all IAM users

CloudTrail - Enable for audit logging

Encryption - Enable S3 server-side encryption (SSE-S3)

Versioning - Enable bucket versioning

Lifecycle Policies - Automate storage transitions

CloudWatch Alarms - Monitor unusual activity

WAF - Protect against malicious uploads


 AWS CLI Commands Used
# S3 bucket creation
aws s3 mb s3://task14-secure-bucket --region ap-south-1 --profile s3-admin

# List buckets
aws s3 ls --profile s3-admin

# Upload file
aws s3 cp test.txt s3://task14-secure-bucket/ --profile s3-admin

# List objects
aws s3 ls s3://task14-secure-bucket/ --profile s3-admin

# Download file
aws s3 cp s3://task14-secure-bucket/test.txt ./downloaded-test.txt --profile s3-admin

# Test denied operations
aws s3 rm s3://task14-secure-bucket/test.txt --profile s3-admin
aws s3 rb s3://task14-secure-bucket --profile s3-admin

 Results
✅ S3 bucket created successfully

✅ IAM policy and role created

✅ EC2 launched with IAM role

✅ Python script working

✅ Permitted operations (Upload, Download, List) successful

✅ Denied operations (Delete, Create) failed as expected

✅ No credentials stored in code

✅ Security model documented

✅ Production improvements identified

📅 Completion Date
2026-08-23

video:-https://drive.google.com/file/d/1n1Z_wltzxkpeQLSLvojsru-Pfpazk0u1/view?usp=sharing