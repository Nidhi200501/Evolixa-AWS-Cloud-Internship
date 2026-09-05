# Task 9: Implement Role-Based AWS Access for a Development Team

## 🎯 Objective
Design an IAM access structure for different members of a small development team.

## 🏢 Scenario
A startup has:
- **Developer** - Writes code, deploys to dev environment
- **QA Engineer** - Tests applications, manages test environment
- **Operations Engineer** - Manages production, monitoring, incidents
- **HR/Admin User** - Manages users, billing, access requests

## 🛠️ Services Used
- AWS IAM
- IAM Policies
- IAM Users
- AWS CLI

---

## 📋 1. Role Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Developer** | Write code, deploy to dev, view logs |
| **QA Engineer** | Test apps, manage test env, create bug reports |
| **Operations Engineer** | Manage production, monitoring, handle incidents |
| **HR/Admin** | Manage IAM users, view billing, handle access |

---

## 📋 2. AWS Resources Needed

| Role | Resources |
|------|-----------|
| **Developer** | EC2 (Dev), S3 (Dev), CloudWatch Logs |
| **QA Engineer** | EC2 (Test), S3 (Test), CloudWatch |
| **Operations Engineer** | EC2 (Prod), S3 (Prod), RDS, CloudWatch, IAM (Read) |
| **HR/Admin** | IAM (User Mgmt), Billing (Read-Only) |

---

## 📋 3. Access Matrix

| Permission | Developer | QA | Operations | HR/Admin |
|------------|-----------|-----|------------|----------|
| EC2 (Dev) | ✅ | ❌ | ❌ | ❌ |
| EC2 (Test) | ✅ Read | ✅ Read/Write | ❌ | ❌ |
| EC2 (Prod) | ❌ | ❌ | ✅ | ❌ |
| S3 (Dev) | ✅ | ❌ | ❌ | ❌ |
| S3 (Test) | ✅ Read | ✅ Read/Write | ❌ | ❌ |
| S3 (Prod) | ❌ | ❌ | ✅ | ❌ |
| CloudWatch | ✅ Read | ✅ Read | ✅ Read/Write | ❌ |
| RDS | ❌ | ❌ | ✅ | ❌ |
| IAM | ❌ | ❌ | ✅ Read | ✅ User Mgmt |
| Billing | ❌ | ❌ | ❌ | ✅ Read |

---

## 📋 4. IAM Policies

### DevPolicy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:DescribeInstances",
      "Resource": "*"
    }
  ]
}
8. QAPolicy (Add karo)
json
### QAPolicy
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:DescribeInstances",
      "Resource": "*"
    }
  ]
}
9. Users Created
markdown
## 📋 5. Users Created

| User | Policy Attached | Access Level |
|------|-----------------|--------------|
| developer-user | DevPolicy | EC2 Describe ✅ |
| qa-user | QAPolicy | EC2 Describe ✅ |
10. Permission Testing
markdown
## 🧪 6. Permission Testing

### Allowed Actions ✅

| User | Command | Result |
|------|---------|--------|
| Developer | `aws ec2 describe-instances` | ✅ Instance list |
| QA | `aws ec2 describe-instances --profile qa-user` | ✅ Instance list |

### Denied Actions ❌

| User | Command | Result |
|------|---------|--------|
| Developer | `aws ec2 start-instances` | ❌ Access Denied |
| QA | `aws ec2 start-instances --profile qa-user` | ❌ Access Denied |
11. Screenshots
markdown
## 📸 Screenshots

| # | Screenshot | Description |
|---|------------|-------------|
| 1 | `policies-created.png` | DevPolicy + QAPolicy in IAM |
| 2 | `users-created.png` | developer-user + qa-user in IAM |
| 3 | `dev-permissions.png` | DevPolicy attached to developer-user |
| 4 | `qa-permissions.png` | QAPolicy attached to qa-user |
| 5 | `dev-allowed.png` | Developer describe-instances ✅ |
| 6 | `dev-denied.png` | Developer start-instances ❌ |
| 7 | `qa-allowed.png` | QA describe-instances ✅ |
| 8 | `qa-denied.png` | QA start-instances ❌ |
12. Results
markdown
## ✅ Results

- ✅ 2 IAM users created (developer-user, qa-user)
- ✅ 2 IAM policies created (DevPolicy, QAPolicy)
- ✅ Policies attached to respective users
- ✅ Allowed actions tested successfully
- ✅ Denied actions tested successfully
- ✅ Screenshots taken (8 total)

## 📅 Completion Date
2026-08-20

## 👩‍💻 Intern
Nidhi Pandey

video:-https://drive.google.com/file/d/1Yy3_617Qywzd36iinUa2fJB5mO-M5G0i/view?usp=sharing