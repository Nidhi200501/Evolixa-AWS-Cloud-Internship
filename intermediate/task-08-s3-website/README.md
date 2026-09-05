# Task 8: S3 Static Website + Storage Workflow (Intermediate)

## 🎯 Objective
Host a static website using Amazon S3 and explore access control mechanisms, security risks, and production improvements.

## 🛠️ Services Used
- Amazon S3
- Static Website Hosting
- S3 Bucket Policies
- HTML/CSS

## 📝 Steps Performed

### 1. Static Website Created
Created a simple HTML/CSS static website with:
- Intern name: Nidhi Pandey
- Program: Evolixa AWS Cloud Internship
- Date: 2026-08-19

### 2. S3 Bucket Created
- Bucket Name: `task8-nidhi-website`
- Region: `us-east-1` (N. Virginia)
- Public Access: Enabled (for static hosting)

### 3. Website Files Uploaded
- `index.html` uploaded to S3 bucket

### 4. Hosting Configured
- Static website hosting: Enabled
- Index document: `index.html`
- Bucket policy added for public read access

### 5. Website Tested
- Website accessible via S3 endpoint
- URL: http://task8-nidhi-website.s3-website.us-east-1.amazonaws.com

### 6. Assets Organized
- Single `index.html` file
- Screenshots folder in local repository

### 7. Asset Updated
- Updated `index.html` with version 2.0
- Added "Last Updated" timestamp
- Verified updated content

### 8. S3 Access Control Explored
- Block Public Access settings reviewed
- Bucket policy analyzed
- ACLs (disabled) - recommended approach

### 9. Risks of Public Buckets Identified
- Data exposure to unauthorized users
- Potential cost escalation
- Security vulnerabilities

### 10. Production Architecture Recommendations
- Use CloudFront with Origin Access Identity (OAI)
- Enable bucket versioning
- Implement IAM roles for controlled access
- Use S3 lifecycle policies for cost optimization

### 11. Workflow Documented
- Complete process documented in README.md

### 12. AWS Resources Recorded
| Resource | Name | Region |
|----------|------|--------|
| S3 Bucket | task8-nidhi-website | us-east-1 |
| IAM | (Used existing) | global |

### 13. Cost Considerations Identified
- S3 storage costs: $0.023/GB/month
- GET requests: $0.0004/10,000 requests
- Data transfer out: $0.09/GB

### 14. Clean Up (Future)
- Empty bucket
- Delete bucket

## 🔗 Website URL
http://task8-nidhi-website.s3-website-us-east-1.amazonaws.com


video:-https://drive.google.com/file/d/1HUPnjIF1dNSn16mK5YX8VjZUip4CFmcU/view?usp=sharing