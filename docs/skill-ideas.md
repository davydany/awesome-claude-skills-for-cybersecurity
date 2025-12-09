# Cybersecurity Skill Ideas

This document contains ideas for future cybersecurity skills to be developed. Each idea includes a description, use cases, and implementation considerations. These serve as a roadmap for community development.

## 🔍 Threat Intelligence & Analysis

### IOC Extractor
**Description**: Extract indicators of compromise from various sources and formats.
**Use Cases**:
- Parse threat reports and security blogs
- Extract IPs, domains, hashes, and file paths
- Generate watchlists for security tools
- Normalize IOC formats across different sources

**Implementation Considerations**:
- Support multiple input formats (PDF, HTML, text, JSON)
- Use regex patterns and NLP for extraction
- Validate extracted IOCs for format correctness
- Output in STIX, JSON, or CSV formats

### Threat Actor Profiling
**Description**: Analyze and profile threat actor tactics, techniques, and procedures.
**Use Cases**:
- Map threat actor TTPs to MITRE ATT&CK framework
- Generate threat actor profiles from intelligence reports
- Track threat actor evolution over time
- Correlate activities across different campaigns

**Implementation Considerations**:
- Integration with MITRE ATT&CK API
- Natural language processing for TTP extraction
- Timeline analysis capabilities
- Visualization of attack patterns

### YARA Rule Generator
**Description**: Generate YARA rules from malware samples and descriptions.
**Use Cases**:
- Create detection rules from malware analysis reports
- Generate rules from file hashes and metadata
- Optimize rule performance and accuracy
- Validate rule syntax and effectiveness

**Implementation Considerations**:
- File analysis capabilities
- String and pattern extraction
- Rule optimization algorithms
- Integration with malware analysis tools

## 🐛 Vulnerability Assessment

### CVE Analyzer
**Description**: Analyze CVE data for impact assessment and prioritization.
**Use Cases**:
- Assess vulnerability severity and exploitability
- Generate remediation plans with timelines
- Track patch status across infrastructure
- Correlate vulnerabilities with threat intelligence

**Implementation Considerations**:
- Integration with NVD (National Vulnerability Database)
- CVSS score calculation and explanation
- Asset inventory correlation
- Remediation timeline estimation

### CVSS Calculator
**Description**: Calculate and explain CVSS scores with detailed breakdowns.
**Use Cases**:
- Score custom vulnerabilities discovered internally
- Explain score components to stakeholders
- Priority ranking for vulnerability management
- Environmental score adjustments

**Implementation Considerations**:
- Support for CVSS v3.1 and v4.0
- Interactive score calculation
- Detailed explanations for each metric
- Historical score tracking

### Dependency Scanner
**Description**: Scan software dependencies for known vulnerabilities.
**Use Cases**:
- Check package vulnerabilities in development projects
- Generate Software Bill of Materials (SBOM)
- Track technical debt from outdated dependencies
- Integration with CI/CD pipelines

**Implementation Considerations**:
- Support for multiple package managers (npm, pip, maven, etc.)
- Integration with vulnerability databases
- License compliance checking
- Automated reporting capabilities

## 📊 Security Monitoring & SIEM

### Log Parser
**Description**: Parse and analyze security logs from various sources.
**Use Cases**:
- Extract security events from raw logs
- Normalize log formats for SIEM ingestion
- Generate security event timelines
- Identify patterns in log data

**Implementation Considerations**:
- Support for common log formats (syslog, JSON, CEF, etc.)
- Regular expression library for parsing
- Time zone handling and normalization
- Performance optimization for large log files

### Alert Correlator
**Description**: Correlate security alerts to reduce noise and identify campaigns.
**Use Cases**:
- Reduce alert fatigue by grouping related alerts
- Identify coordinated attack campaigns
- Priority scoring based on correlation confidence
- Generate incident summaries

**Implementation Considerations**:
- Machine learning for pattern recognition
- Time-based and attribute-based correlation
- Integration with popular SIEM platforms
- Customizable correlation rules

### Detection Rule Generator
**Description**: Generate detection rules for various SIEM platforms.
**Use Cases**:
- Create Sigma rules for cross-platform detection
- Generate Splunk SPL queries from descriptions
- Build KQL detections for Microsoft Sentinel
- Convert between different rule formats

**Implementation Considerations**:
- Support for Sigma rule standard
- Platform-specific optimizations
- Rule testing and validation
- Performance impact assessment

## 🌐 Network Security

### Firewall Rule Analyzer
**Description**: Analyze and optimize firewall rule sets.
**Use Cases**:
- Identify rule conflicts and redundancies
- Optimize rule order for performance
- Generate firewall documentation
- Compliance checking against security policies

**Implementation Considerations**:
- Support for multiple firewall vendors
- Rule conflict detection algorithms
- Performance impact analysis
- Visualization of rule relationships

### Network Flow Analyzer
**Description**: Analyze network traffic patterns for anomaly detection.
**Use Cases**:
- Detect network anomalies and suspicious patterns
- Baseline normal network behavior
- Identify potential data exfiltration
- Monitor for command and control communication

**Implementation Considerations**:
- Support for NetFlow, sFlow, and IPFIX
- Statistical analysis for baseline creation
- Machine learning for anomaly detection
- Integration with network monitoring tools

### DNS Security Analyzer
**Description**: Analyze DNS logs for security threats.
**Use Cases**:
- Detect domain generation algorithm (DGA) domains
- Identify command and control communication
- Monitor for DNS tunneling activities
- Analyze suspicious domain queries

**Implementation Considerations**:
- Domain reputation integration
- DGA detection algorithms
- DNS tunneling pattern recognition
- Threat intelligence feed correlation

## 🔒 Application Security

### Secure Code Reviewer
**Description**: Review source code for security vulnerabilities.
**Use Cases**:
- Identify OWASP Top 10 vulnerabilities
- Check for hardcoded secrets and credentials
- Suggest secure coding alternatives
- Integration with code review processes

**Implementation Considerations**:
- Support for multiple programming languages
- Integration with static analysis tools
- Customizable rule sets
- Developer-friendly reporting

### SAST Report Analyzer
**Description**: Analyze and prioritize static application security testing reports.
**Use Cases**:
- Prioritize SAST findings by risk and exploitability
- Generate fix recommendations with code examples
- Track remediation progress over time
- Reduce false positive rates

**Implementation Considerations**:
- Integration with popular SAST tools
- Risk scoring algorithms
- False positive filtering
- Remediation guidance library

### API Security Checker
**Description**: Assess API security configurations and implementations.
**Use Cases**:
- Check API authentication and authorization
- Validate input sanitization and rate limiting
- Test for common API vulnerabilities
- Generate API security reports

**Implementation Considerations**:
- OpenAPI/Swagger specification parsing
- Automated security testing capabilities
- OWASP API Security Top 10 coverage
- Integration with API gateways

## ☁️ Cloud Security

### Cloud Posture Analyzer
**Description**: Assess cloud infrastructure security posture.
**Use Cases**:
- Check for cloud misconfigurations
- Validate IAM policies and permissions
- Compliance mapping to security frameworks
- Multi-cloud environment assessment

**Implementation Considerations**:
- Support for AWS, Azure, GCP, and other clouds
- Integration with cloud APIs
- Compliance framework templates
- Remediation automation capabilities

### Container Security Scanner
**Description**: Scan container images for security vulnerabilities.
**Use Cases**:
- Check container images for known vulnerabilities
- Validate container security best practices
- Generate container security reports
- Integration with CI/CD pipelines

**Implementation Considerations**:
- Support for multiple container registries
- Integration with vulnerability databases
- Dockerfile security analysis
- Runtime security recommendations

### Kubernetes Security Auditor
**Description**: Audit Kubernetes configurations for security best practices.
**Use Cases**:
- Check RBAC settings and permissions
- Validate network policies and pod security
- Security benchmark compliance (CIS, NSA/CISA)
- Cluster security posture assessment

**Implementation Considerations**:
- Kubernetes API integration
- Security benchmark automation
- Policy-as-code integration
- Multi-cluster support

## 🚨 Incident Response

### Incident Timeline Builder
**Description**: Create detailed incident timelines from various data sources.
**Use Cases**:
- Correlate events across multiple log sources
- Build comprehensive attack narratives
- Generate incident response reports
- Timeline visualization for stakeholders

**Implementation Considerations**:
- Multi-source log correlation
- Time zone normalization
- Interactive timeline visualization
- Export capabilities for reports

### Forensics Analyzer
**Description**: Analyze digital forensic artifacts for incident investigation.
**Use Cases**:
- Parse memory dumps and disk images
- Analyze file system artifacts and registry entries
- Extract indicators of compromise from artifacts
- Generate forensic analysis reports

**Implementation Considerations**:
- Integration with forensic tools (Volatility, Autopsy, etc.)
- Artifact parsing libraries
- Evidence integrity validation
- Chain of custody documentation

### Playbook Executor
**Description**: Execute incident response playbooks with automated steps.
**Use Cases**:
- Automate incident response procedures
- Track playbook execution progress
- Generate incident documentation
- Integration with ticketing systems

**Implementation Considerations**:
- Playbook definition standards
- Integration with security tools
- Progress tracking and reporting
- Approval workflows for sensitive actions

## 📜 Compliance & Governance

### Compliance Mapper
**Description**: Map security controls to various compliance frameworks.
**Use Cases**:
- Map controls to NIST Cybersecurity Framework
- Align with ISO 27001 requirements
- SOC 2 Type II preparation and documentation
- Cross-framework control mapping

**Implementation Considerations**:
- Framework definition databases
- Control mapping algorithms
- Gap analysis capabilities
- Evidence collection automation

### Policy Generator
**Description**: Generate security policies from templates and requirements.
**Use Cases**:
- Create baseline security policies
- Customize policy templates for organizations
- Version control and change management
- Compliance requirement integration

**Implementation Considerations**:
- Policy template libraries
- Requirement parsing capabilities
- Document generation automation
- Approval workflow integration

### Audit Report Builder
**Description**: Build comprehensive compliance audit reports.
**Use Cases**:
- Generate evidence packages for auditors
- Track audit findings and remediation
- Monitor ongoing compliance status
- Automated report generation

**Implementation Considerations**:
- Evidence collection automation
- Report template customization
- Finding tracking databases
- Integration with GRC platforms

## 🔐 Cryptography & PKI

### Certificate Validator
**Description**: Validate X.509 certificates and certificate chains.
**Use Cases**:
- Check certificate expiration dates
- Validate certificate chains and trust paths
- Monitor certificate renewals
- Certificate compliance checking

**Implementation Considerations**:
- Certificate parsing libraries
- Trust store integration
- Automated monitoring capabilities
- Alert generation for expiring certificates

### Crypto Analyzer
**Description**: Analyze cryptographic implementations for weaknesses.
**Use Cases**:
- Check cryptographic algorithms and key sizes
- Validate cipher suites and protocols
- Identify weak or deprecated crypto
- Compliance with cryptographic standards

**Implementation Considerations**:
- Cryptographic standard databases
- Protocol analysis capabilities
- Weakness detection algorithms
- Remediation recommendations

### Key Management Auditor
**Description**: Audit key management practices and procedures.
**Use Cases**:
- Check key rotation policies and practices
- Validate key storage and access controls
- Monitor key usage and lifecycle
- Compliance with key management standards

**Implementation Considerations**:
- Integration with key management systems
- Policy compliance checking
- Audit trail analysis
- Best practice recommendations

---

## Contributing New Skills

Interested in implementing one of these skills? See our [Contributing Guidelines](../CONTRIBUTING.md) for how to get started. You can also propose new skill ideas by opening an issue using the "New Skill Proposal" template.

## Skill Development Priorities

Skills are prioritized based on:
1. **Community Demand**: Skills requested by multiple users
2. **Security Impact**: Skills that address critical security gaps
3. **Implementation Feasibility**: Skills that can be realistically implemented
4. **Broad Applicability**: Skills useful across multiple organizations

Current high-priority skills for development:
- CVE Analyzer
- Log Parser
- IOC Extractor
- Cloud Posture Analyzer
- Certificate Validator

Want to help prioritize? Join the discussion in our [Discord community](https://discord.gg/claude-security) or comment on GitHub issues.