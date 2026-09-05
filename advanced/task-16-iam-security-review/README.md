# Task 16: Conduct an AWS IAM Security Review

## 🎯 Objective
Perform a structured review of a fictional AWS account's IAM configuration and identify excessive or poorly designed permissions.

## 🏢 Scenario
A synthetic IAM environment containing multiple users, roles, and policies. The security team wants to know: **"Who has access to what, and where are we giving more access than necessary?"**

---

## 📋 Step 1: Inventory the IAM Identities

### IAM Users (9)

| # | Username | Last Activity |
|---|----------|---------------|
| 1 | developer-user | 3 days ago |
| 2 | hr-admin-user | Never |
| 3 | mytask | Never |
| 4 | operations-user | Never |
| 5 | qa-user | 4 days ago |
| 6 | s3-admin-user | 2 days ago |
| 7 | sns-user | 2 days ago |
| 8 | task3-iam-user | Never |
| 9 | test-user | 3 days ago |

### IAM Roles (1 Custom)

| Role Name | Trusted Entity | Last Activity |
|-----------|----------------|---------------|
| EC2S3AccessRole | AWS Service: ec2 | 12 minutes ago |

### IAM Policies (5 Custom)

| Policy Name | Type | Description |
|-------------|------|-------------|
| DevPolicy | Customer managed | EC2 Describe only |
| QAPolicy | Customer managed | EC2 Describe only |
| S3FullAccessPolicy | Customer managed | Full S3 access |
| EC2S3AccessPolicy | Customer managed | S3 Put/Get/List |
| S3ReadOnlyPolicy | Customer managed | S3 GetObject only |

---

## 📋 Step 2: Map Users/Roles to Policies

| User/Role | Policy Attached |
|-----------|-----------------|
| developer-user | DevPolicy |
| qa-user | QAPolicy |
| s3-admin-user | S3FullAccessPolicy |
| task3-iam-user | AdministratorAccess |
| sns-user | (No policy) |
| test-user | S3ReadOnlyPolicy |
| hr-admin-user | (No policy) |
| operations-user | (No policy) |
| mytask | (No policy) |
| EC2S3AccessRole | EC2S3AccessPolicy |

---

## 📋 Step 3: Identify Administrator-Level Permissions

| User | Policy | Risk Level |
|------|--------|------------|
| task3-iam-user | AdministratorAccess | 🔴 **High** |
| s3-admin-user | S3FullAccessPolicy | 🟡 **Medium** |

---

## 📋 Step 4: Identify Wildcard Permissions

| Policy | Wildcard Actions | Risk |
|--------|------------------|------|
| AdministratorAccess | `"Action": "*"` | 🔴 High |
| S3FullAccessPolicy | `"Action": "s3:*"` | 🟡 Medium |

---

## 📋 Step 5: Identify Unused Access

| User | Last Activity | Status |
|------|---------------|--------|
| hr-admin-user | Never | ⚠️ Unused |
| operations-user | Never | ⚠️ Unused |
| mytask | Never | ⚠️ Unused |

---

## 📋 Step 6: Compare Permissions with Job Responsibilities

| Role | Should Have | Actually Has | Issue |
|------|-------------|--------------|-------|
| Developer | EC2 Describe, S3 Read | EC2 Describe only | ✅ OK |
| QA | EC2 Describe, S3 Read | EC2 Describe only | ✅ OK |
| S3 Admin | S3 specific | S3 Full Access | ⚠️ Too broad |
| Junior Dev | S3 specific bucket | AdminAccess | 🔴 Too broad |

---

## 📋 Step 7: Access Matrix

| User | EC2 | S3 | IAM | Billing |
|------|-----|-----|-----|---------|
| developer-user | ✅ Describe | ❌ | ❌ | ❌ |
| qa-user | ✅ Describe | ❌ | ❌ | ❌ |
| s3-admin-user | ❌ | ✅ Full | ❌ | ❌ |
| task3-iam-user | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| hr-admin-user | ❌ | ❌ | ❌ | ❌ |
| operations-user | ❌ | ❌ | ❌ | ❌ |
| mytask | ❌ | ❌ | ❌ | ❌ |

---

## 📋 Step 8: Least-Privilege Improvements

| User | Current | Recommended |
|------|---------|-------------|
| task3-iam-user | AdministratorAccess | S3 specific bucket access |
| s3-admin-user | S3FullAccessPolicy | Restrict to specific bucket |
| hr-admin-user | No policy | Add IAM user management policy |

---

## 📋 Step 9: Revised Policy Recommendations

### Recommended Policy for Junior Developer:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::task2-nidhi-website",
        "arn:aws:s3:::task2-nidhi-website/*"
      ]
    }
  ]
}
Recommended Policy for S3 Admin:
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
      "Resource": "arn:aws:s3:::task14-secure-bucket/*"
    }
  ]
}
📋 Step 10: Test Permissions
Allowed Actions ✅
Action	Command	Result
S3 PutObject	aws s3 cp test.txt s3://task2-nidhi-website/	✅ Allowed
Denied Actions ❌
Action	Command	Result
S3 PutObject on other bucket	aws s3 cp test.txt s3://other-bucket/	❌ Denied
EC2 Describe	aws ec2 describe-instances	❌ Denied

📋 Step 11: Prioritized Findings
Priority	Finding	Recommendation
🔴 High	AdminAccess for task3-iam-user	Remove immediately
🟡 Medium	S3FullAccess for s3-admin-user	Restrict to specific bucket
🟡 Medium	Unused IAM users (3)	Delete or disable
🟢 Low	No MFA enabled	Enable MFA for all users
🟢 Low	No CloudTrail	Enable CloudTrail for audit
📋 Step 12: Impact of Excessive Permissions

Risk	Potential Impact
Data Breach	Unauthorized access to sensitive data
Resource Deletion	Accidental deletion of critical resources
Cost Escalation	Unauthorized resource creation leading to high bills
Compliance Violation	GDPR/HIPAA/PCI non-compliance
Account Compromise	Full account takeover if credentials leaked
📋 Step 13: Remediation Plan
Action	Timeline	Owner	Priority
Remove AdminAccess	Immediate	Security Team	🔴 High
Restrict S3 permissions	1 week	Security Team	🟡 Medium
Delete unused users	1 week	Security Team	🟡 Medium
Enable MFA	2 weeks	All Users	🟢 Low
Enable CloudTrail	2 weeks	Security Team	🟢 Low
📋 Step 14: Security Review Report
markdown
# IAM Security Review Report

## Executive Summary
- 9 IAM users reviewed
- 5 policies reviewed
- 1 custom role reviewed

## Key Findings

### 🔴 High Priority (Critical)
1. **AdminAccess for task3-iam-user**
   - User has full administrative access
   - Risk: Complete account compromise
   - Action: Remove immediately

### 🟡 Medium Priority
2. **S3FullAccess for s3-admin-user**
   - User can access all S3 buckets
   - Risk: Data exposure
   - Action: Restrict to specific bucket

3. **Unused IAM Users (3)**
   - hr-admin-user, mytask, operations-user
   - Risk: Unused credentials = security gap
   - Action: Delete or disable

### 🟢 Low Priority
4. **No MFA Enabled**
   - All users lack MFA
   - Risk: Credential theft
   - Action: Enable MFA

## Recommendations
1. Remove AdminAccess from task3-iam-user
2. Restrict s3-admin-user to specific bucket
3. Delete unused IAM users
4. Enable MFA for all users
5. Enable CloudTrail for audit

## Remediation Timeline
- Immediate: Remove AdminAccess
- 1 week: Restrict S3 permissions + Delete unused users
- 2 weeks: Enable MFA + CloudTrail

## Estimated Impact
- Security improvements: High
- Operational impact: Minimal
- Cost impact: Low (MFA, CloudTrail costs)
📸 Screenshots
#	Screenshot	Description
1	iam-users-list.png	All 9 IAM users
2	iam-roles-list.png	All IAM roles
3	iam-policies-list.png	Customer managed policies
4	admin-access.png	AdministratorAccess user
5	wildcard-permissions.png	Wildcard permissions in policy
6	unused-users.png	Unused IAM users
7	access-matrix.png	Access matrix table
8	remediation-plan.png	Remediation plan
✅ Results
✅ 9 IAM users reviewed

✅ 5 policies reviewed

✅ 1 custom role reviewed

✅ AdminAccess identified

✅ Wildcard permissions found

✅ Unused users identified

✅ Least-privilege improvements proposed

✅ Revised policies created

✅ Remediation plan created

✅ Security report ready

📅 Completion Date
2026-08-25


video:-https://drive.google.com/file/d/1GbjhY47Go0SuB5ZzaHqYdjvB1ks4xiFa/view?usp=sharing