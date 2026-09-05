import boto3
import os

# S3 bucket name (jo aapne create kiya)
BUCKET_NAME = "task14-secure-bucket"

# Use the s3-admin profile (to avoid default sns-user permission issues)
session = boto3.Session(profile_name='s3-admin')
s3 = session.client('s3')

def upload_file(file_name):
    """Upload a file to S3 bucket"""
    try:
        s3.upload_file(file_name, BUCKET_NAME, file_name)
        print(f"✅ File '{file_name}' uploaded successfully")
        return True
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return False

def download_file(file_name):
    """Download a file from S3 bucket"""
    try:
        s3.download_file(BUCKET_NAME, file_name, f"downloaded_{file_name}")
        print(f"✅ File '{file_name}' downloaded successfully")
        return True
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return False

def list_files():
    """List all files in the S3 bucket"""
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
    print("🚀 Task 14 - S3 File Upload/Download Demo")
    print("-" * 40)

    # Create a test file
    test_file = "test.txt"
    with open(test_file, "w") as f:
        f.write("Hello from EC2 App Server!\n")
    print(f"✅ Created test file: {test_file}")

    # Upload
    print("\n📤 Uploading to S3...")
    upload_file(test_file)

    # List
    list_files()

    # Download
    print("\n📥 Downloading file...")
    download_file(test_file)

    print("\n✅ Demo complete!")