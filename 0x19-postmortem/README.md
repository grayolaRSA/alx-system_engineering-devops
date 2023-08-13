This is a readme file for the postmortem task for the ALX SE program

Issue summary
Duration: 4 hours (August 13, 2023, 10:00 AM - 2:00 PM GMT)

Impact: Slow response times and intermittent service disruptions experienced by users. Approximately 30% of users were affected during the outage.

Root cause: Misconfiguration in the web server's caching layer.

Timeline
10:00 HRS: The issue was detected when the monitoring system generated multiple alerts for high latency and increased error rates.

10:15 HRS: The operations team initiated an investigation into the web stack components, including web servers, load balancers, and databases. Extensive database performance analysis was conducted, including index optimizations and query tuning, but no significant issues were found. Load balancers were also thoroughly examined for misconfigurations or network bottlenecks, but no abnormalities were detected.

10:45 HRS: Issue escalated to development team and system administrators

14:00 HRS: Issue resolved and all metrics back to within acceptable levels
Root cause and resolution
The initial assumption was that the database servers might be overloaded or experiencing performance issues.

As the issue persisted, the incident was escalated to the development team and system administrators for further analysis and resolution.

After reviewing system logs and analysing network traffic, it was discovered that a recent deployment had introduced a misconfiguration in the web server's caching layer.

The misconfiguration caused excessive caching, resulting in stale content being served to users and increased load on the servers.

The misconfiguration was corrected, and the web servers were restarted to apply the changes.

The root cause of the issue was identified as a misconfiguration in the web server's caching layer. Specifically, the cache expiration settings were set too high, leading to stale content being served to users.
Corrective and preventative measures

Corrective measures
Implement automated configuration validation checks for the web server's caching layer during the deployment process to prevent misconfigurations.
Enhance monitoring and alerting capabilities to promptly detect and notify about abnormal caching behaviour or high latency.

Preventative measures
Conduct a thorough review of the deployment process to ensure proper configuration management and validation.
Develop and implement a comprehensive caching strategy, including proper cache invalidation mechanisms and appropriate cache expiration settings.
Enhance system monitoring by adding specific metrics for cache hit rates, cache expiration, and latency.
Conduct regular performance testing and load testing to identify potential bottlenecks or misconfigurations before they impact users.


