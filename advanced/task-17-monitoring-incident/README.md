# Task 17: Build a Cloud Operations Monitoring and Incident Exercise

## 🎯 Objective
Create a basic operational workflow for detecting and responding to problems affecting an EC2-hosted application.

## 🏢 Scenario
A fictional application hosted on EC2 begins experiencing intermittent failures. The operations team needs a simple process for detecting the problem, investigating it, and documenting the response.

## 🛠️ Services Used
- AWS CloudWatch
- Amazon SNS
- EC2 (Fictional / Existing)

---

## 📋 Step 1: Define Application's Normal Operating State

| Parameter | Normal State |
|-----------|--------------|
| Application Status | Running |
| Website | Accessible (HTTP 200) |
| CPU Usage | < 70% |
| Memory Usage | < 80% |
| Error Logs | No errors |
| Response Time | < 500ms |

---

## 📋 Step 2: Identify Useful EC2/Server Indicators

| Indicator | What It Tells |
|-----------|---------------|
| CPU Utilization | Server overload |
| Memory Usage | Memory leak |
| Disk Usage | Storage full |
| HTTP Status | Website down |
| Error Logs | Application errors |
| Response Time | Performance issues |

---

## 📋 Step 3: Configure Monitoring

### CloudWatch Alarm Created
- **Alarm Name:** `task17-cpu-alarm`
- **Metric:** CPUUtilization
- **Instance:** task7-web-appEC2 Insta
- **Condition:** > 80%
- **Period:** 5 minutes
- **Statistic:** Average
- **Action:** SNS Notification (Email)

### SNS Topic Created
- **Topic Name:** `task17_alarm_topic`
- **Subscription:** Email (np1805689@gmail.com)
- **Status:** Pending confirmation (email confirmation required)

---

## 📋 Step 4: Create Controlled Test Condition

A test condition was simulated where the `stress` command caused CPU to spike to 100%.

```bash
sudo stress --cpu 4 --timeout 120

Step 5: Observe Available Indicators/Logs
Time	Observation
10:00 AM	CloudWatch Alarm triggered (CPU > 80%)
10:01 AM	CPU reached 100%
10:02 AM	Website slow, response time high
📋 Step 6: Identify Symptoms
Symptom	Observed
CPU Usage	100%
Response Time	5000ms
HTTP Status	500/504 errors
User Reports	"Website is slow"
📋 Step 7: Investigate Underlying Cause
stress command consumed all available CPU resources.

Apache server couldn't handle incoming requests.

Connections were queued and timed out.

📋 Step 8: Record Timeline of Events
Time	Event
10:00 AM	CloudWatch Alarm triggered (CPU > 80%)
10:01 AM	Website becomes slow
10:02 AM	User reports issue
10:05 AM	Investigation started
10:10 AM	Root cause identified (stress process)
10:15 AM	Corrective action applied
10:20 AM	Website recovered
10:25 AM	Incident closed
📋 Step 9: Apply Corrective Action
bash
# Kill the stress process
sudo pkill stress

# Restart Apache web server
sudo systemctl restart apache2

# Verify recovery
curl http://localhost
📋 Step 10: Verify Recovery
Check	Before	After
CPU	100%	25%
Response Time	5000ms	200ms
HTTP Status	500	200
Website	Down	Accessible ✅
📋 Step 11: Document Root Cause
Root Cause: The stress command was used to simulate high CPU load, consuming all CPU resources and making the application unresponsive.

📋 Step 12: Missing Information During Investigation
Missing Information	Impact
Memory metrics	Could have detected high swap usage
Disk I/O metrics	Could have detected disk bottleneck
Application logs	Needed to see which request failed
Auto Scaling alerts	Could have prevented downtime

📋 Step 13: Additional Monitoring Recommendations
Recommendation	Benefit
Enable Memory Monitoring	Detect memory leaks
Enable Disk Monitoring	Prevent disk full
Centralized Application Logging	Faster debugging
Auto Scaling Group	Handle load spikes
Multi-AZ Deployment	High availability

📋 Step 14: Incident-Response Runbook
1. Detection
CloudWatch alarm triggers (CPU > 80%)

User reports website issue

Monitoring dashboard shows red status

2. Investigation
Check CloudWatch metrics

SSH into EC2 instance

Check running processes: top, ps aux

Check Apache logs: /var/log/apache2/error.log

Check system logs: /var/log/syslog

3. Resolution
Identify the offending process (e.g., stress)

Kill the process: sudo pkill <process>

Restart the application: sudo systemctl restart apache2

Verify recovery: curl http://localhost

4. Post-Incident
Update CloudWatch dashboard

Document root cause

Schedule follow-up meeting

Update runbook with new learnings

📋 Step 15: Incident Report
markdown
# Incident Report: INC-001

## Summary
- **Date:** 2026-08-26
- **Time:** 10:00 AM - 10:25 AM
- **Duration:** 25 minutes
- **Impact:** Website unavailable for 20 minutes

## Detection
- CloudWatch Alarm: CPU > 80%
- User reported slowness

## Symptoms
- CPU: 100%
- Response Time: 5000ms
- HTTP 500 errors

## Root Cause
- `stress` command consumed all CPU resources

## Resolution
- Killed `stress` process
- Restarted Apache

## Recovery
- Time: 10:20 AM
- CPU: 25%
- Website: Accessible ✅

## Recommendations
1. Add Memory Monitoring
2. Implement Auto Scaling
3. Set up Centralized Logging
4. Create Runbook for future incidents

## Lessons Learned
- Always monitor memory metrics
- Test changes in non-production first
- Document incident responses
📸 Screenshots
#	Screenshot	Description
1	cloudwatch-alarm-created.png	CloudWatch alarm created successfully
2	cloudwatch-actions-configured.png	SNS topic + email configured
3	cloudwatch-metric-selected.png	CPUUtilization metric selected
✅ Results
✅ CloudWatch alarm configured for CPU > 80%

✅ SNS topic created for notifications

✅ Incident timeline documented

✅ Root cause identified

✅ Corrective action documented

✅ Recovery verified

✅ Incident runbook created

✅ Incident report prepared

📅 Completion Date
2026-08-26

video:-https://drive.google.com/file/d/1wWXn0d5O16KyiNuFYryScdQG4cMr4YYT/view?usp=sharing