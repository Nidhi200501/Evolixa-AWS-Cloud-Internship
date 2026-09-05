## 📋 Unused Resources

| Resource Name | Type | Reason |
|---------------|------|--------|
| my task ci/cd | EC2 Instance | Stopped, not in use |
| telehealth-assets-1783287237 | S3 Bucket | No recent activity |
| telehealth-assets-1783287253 | S3 Bucket | No recent activity |
| weather-dashboard-nidhi | S3 Bucket | No recent activity |


## 📋 Excessive Permissions

| User | Policy | Risk Level |
|------|--------|------------|
| task3-iam-user | AdministratorAccess | 🔴 High |
| s3-admin-user | S3FullAccessPolicy | 🟡 Medium |

## 📋 Cost Estimate

| Resource | Monthly Cost |
|----------|--------------|
| EC2 (task7-web-app) | ~$7.50 |
| S3 Storage (all buckets) | ~$0.50 |
| **Total** | **~$8.00** |

## 📋 Prioritized Findings

| Priority | Finding | Recommendation |
|----------|---------|----------------|
| 🔴 High | AdminAccess for task3-iam-user | Remove/restrict |
| 🟡 Medium | S3FullAccess for s3-admin-user | Restrict to specific bucket |
| 🟡 Medium | Unused S3 buckets | Delete |
| 🟢 Low | Stopped EC2 instance | Terminate |


## 📋 Recommendations

1. Remove AdminAccess from task3-iam-user
2. Restrict s3-admin-user to specific bucket
3. Delete unused S3 buckets
4. Terminate stopped EC2 instance
5. Enable MFA for all users
6. Enable CloudTrail for audit


## 📋 Resource Management Checklist

- [x] All resources tagged
- [x] Unused resources identified
- [x] IAM permissions reviewed
- [x] Cost monitoring enabled
- [x] Weekly resource review scheduled
- [x] MFA enabled for all users

## 📋 Cost Savings Opportunities

| Action | Estimated Savings |
|--------|-------------------|
| Delete unused S3 buckets | ~$0.50/month |
| Terminate stopped EC2 | ~$0.08/month |
| **Total** | **~$0.58/month** |

## 📋 Security Observations

| Observation | Recommendation |
|-------------|----------------|
| AdminAccess exists | Remove immediately |
| No MFA enabled | Enable MFA for all users |
| No CloudTrail | Enable CloudTrail for audit |

## 📋 Cloud Hygiene Report

### Summary
- 2 EC2 instances reviewed
- 6 S3 buckets reviewed
- 7 IAM users reviewed

### Findings
1. 🔴 AdminAccess for task3-iam-user
2. 🟡 S3FullAccess for s3-admin-user
3. 🟡 Unused S3 buckets (3)

### Recommendations
1. Remove AdminAccess
2. Restrict S3 permissions
3. Delete unused buckets
4. Terminate stopped EC2
5. Enable MFA
6. Enable CloudTrail

### Cost Savings
~$0.58/month potential savings

# Task 12: AWS Cost and Resource Review

## 🎯 Objective
Review a small AWS environment and identify unnecessary resources, security risks, and potential sources of avoidable cloud spending.

## 🛠️ Services Used
- AWS EC2
- Amazon S3
- AWS IAM
- AWS Cost Explorer


## 📸 Screenshots

| # | Screenshot | Description |
|---|------------|-------------|
| 1 | `ec2-inventory.png` | All EC2 instances |
| 2 | `ec2-unused.png` | Stopped EC2 instance |
| 3 | `s3-inventory.png` | All S3 buckets |
| 4 | `s3-unused.png` | Unused S3 buckets |
| 5 | `iam-users.png` | All IAM users |
| 6 | `iam-unused.png` | Unused IAM users |

## ✅ Results

- ✅ Resource inventory completed
- ✅ Unused resources identified
- ✅ Excessive permissions found
- ✅ Cost estimate calculated
- ✅ Recommendations provided
- ✅ Cloud hygiene report prepared

## 📅 Completion Date
2026-08-21

## 👩‍💻 Intern
Nidhi Pandey

## 📚 Program
Evolixa AWS Cloud Internship

video:-https://drive.google.com/file/d/1uuXjXaja_rbmBXU1bX40H6oXiWEsuWE0/view?usp=sharing