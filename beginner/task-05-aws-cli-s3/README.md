markdown
# Task 5: Upload and Retrieve Application Files Using AWS CLI

## 🎯 Objective
Use AWS CLI to automate basic S3 file operations instead of performing every operation manually through the AWS Console.

## 🛠️ Services Used
- AWS CLI
- Amazon S3
- Windows Command Prompt

## 📁 Folder Structure Created
task5-cli-files/
├── file1.txt
├── file2.txt
├── file3.txt
├── file4.txt
├── downloaded-file1.txt
├── backups/
│ ├── backup1.txt
│ └── backup2.txt
└── download/
└── (downloaded files)

text

---

## 📋 Steps Performed

### 1. AWS CLI Configured
```bash
aws configure --profile s3-admin
2. Identity Verified
bash
aws sts get-caller-identity --profile s3-admin
3. S3 Bucket Created
bash
aws s3 mb s3://task5-cli-bucket --region us-east-1 --profile s3-admin
4. Local Directory Created
bash
mkdir task5-cli-files
cd task5-cli-files
5. Sample Files Created
bash
echo Hello AWS CLI > file1.txt
echo This is file 2 > file2.txt
echo File 3 content > file3.txt
6. Individual Files Uploaded
bash
aws s3 cp file1.txt s3://task5-cli-bucket/ --profile s3-admin
aws s3 cp file2.txt s3://task5-cli-bucket/ --profile s3-admin
aws s3 cp file3.txt s3://task5-cli-bucket/ --profile s3-admin
7. Directory Uploaded
bash
mkdir backups
echo Backup file 1 > backups\backup1.txt
echo Backup file 2 > backups\backup2.txt

aws s3 cp backups/ s3://task5-cli-bucket/backups/ --recursive --profile s3-admin
8. Objects Listed
bash
aws s3 ls s3://task5-cli-bucket/ --recursive --profile s3-admin
9. Files Downloaded
bash
aws s3 cp s3://task5-cli-bucket/file1.txt ./downloaded-file1.txt --profile s3-admin
10. Synchronization
bash
echo New file > file4.txt
aws s3 sync ./ s3://task5-cli-bucket/ --profile s3-admin
11. Modified File Sync
bash
echo Updated content >> file1.txt
aws s3 sync ./ s3://task5-cli-bucket/ --profile s3-admin
12. Clean Up
bash
aws s3 rm s3://task5-cli-bucket/ --recursive --profile s3-admin
aws s3 rb s3://task5-cli-bucket/ --profile s3-admin
🔐 Security Best Practices
Practice	Why
Never hardcode credentials	Avoid accidental exposure on GitHub
Use IAM roles	Temporary credentials are safer
Use AWS CLI profiles	Keep keys separate per user
Enable MFA	Extra layer of security
🚀 Automation Ideas
Use cron job for daily backup sync

Use Lambda for auto-upload on file change

Use GitHub Actions for CI/CD deployment to S3

📸 Screenshots
#	Screenshot	Description
1	bucket-created.png	Bucket created successfully
2	sample-files.png	Local files created
3	files-uploaded.png	Files uploaded to S3
4	directory-uploaded.png	Directory uploaded
5	list-objects.png	Objects listed
6	download-success.png	File downloaded
7	sync-success.png	Sync completed
8	modified-sync.png	Only modified file uploaded
9	cleanup-done.png	Bucket cleaned up
✅ Results
✅ AWS CLI configured

✅ S3 bucket created

✅ Files uploaded successfully

✅ Directory uploaded

✅ Objects listed

✅ Files downloaded

✅ Sync worked

✅ Modified sync worked

✅ Cleanup completed

📅 Completion Date
2026-08-20

👩‍💻 Intern
Nidhi Pandey

video:-https://drive.google.com/file/d/19_qGx9WZp6_y27B5RT09ZXHPpqB-3MIX/view?usp=sharing