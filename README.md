# 🛡️ Awesome Claude Skills for Cybersecurity

A curated collection of Claude Skills designed for cybersecurity professionals, security analysts, and defenders. These skills empower Claude to assist with threat intelligence, vulnerability assessment, incident response, and security operations.

## 📋 Table of Contents

- [Overview](#overview)
- [What Are Claude Skills?](#what-are-claude-skills)
- [Skills Catalog](#skills-catalog)
- [Getting Started](#getting-started)
- [Creating Your Own Skills](#creating-your-own-skills)
- [Contributing](#contributing)
- [Resources](#resources)
- [Community](#community)
- [License](#license)

## Overview

This repository provides a comprehensive collection of Claude Skills specifically tailored for cybersecurity use cases. Each skill is designed to help security professionals automate routine tasks, analyze threats more effectively, and respond to security incidents faster.

All skills in this repository are focused on **defensive security** and are designed to help protect systems, analyze threats, and improve security posture. These skills are not intended for offensive security testing or malicious purposes.

## What Are Claude Skills?

Claude Skills are customizable workflows that teach Claude how to perform specific cybersecurity tasks according to industry standards and best practices. Each skill consists of:

- **Instructions**: Clear guidance on how to perform the security task
- **Scripts**: Python or bash scripts that execute the actual security operations
- **Documentation**: Detailed usage examples and security considerations

### Key Benefits for Security Teams

- 🚀 **Accelerate Response**: Automate routine security analysis tasks
- 🔍 **Enhanced Detection**: Leverage AI for pattern recognition in security data
- 📊 **Consistent Analysis**: Apply standardized security frameworks and methodologies
- 🛡️ **Defense-Focused**: All skills designed for defensive security operations
- 📝 **Compliance Ready**: Generate reports aligned with security standards

## Skills Catalog

### 🔍 Threat Intelligence & Analysis

| Skill | Description | Status |
|-------|-------------|---------|
| [STIX 2.1 Validator](./stix2-validator/) | Validate STIX bundles for threat intelligence sharing | ✅ Available |
| [STIX 2.1 Generator](./stix2-generator/) | Generate STIX objects and bundles from various sources | ✅ Available |

### 🐛 Vulnerability Assessment

Coming soon - see [ideas document](docs/skill-ideas.md) for planned skills.

### 📊 Security Monitoring & SIEM

Coming soon - see [ideas document](docs/skill-ideas.md) for planned skills.

### 🌐 Network Security

Coming soon - see [ideas document](docs/skill-ideas.md) for planned skills.

### 🔒 Application Security

Coming soon - see [ideas document](docs/skill-ideas.md) for planned skills.

### ☁️ Cloud Security

Coming soon - see [ideas document](docs/skill-ideas.md) for planned skills.

### 🚨 Incident Response

Coming soon - see [ideas document](docs/skill-ideas.md) for planned skills.

### 📜 Compliance & Governance

Coming soon - see [ideas document](docs/skill-ideas.md) for planned skills.

### 🔐 Cryptography & PKI

Coming soon - see [ideas document](docs/skill-ideas.md) for planned skills.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Claude API access (for API usage)
- Required Python packages (varies by skill)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/awesome-claude-skills-for-cybersecurity.git
cd awesome-claude-skills-for-cybersecurity
```

2. Install common dependencies:
```bash
pip install -r requirements.txt
```

3. Navigate to a specific skill directory and follow its setup instructions:
```bash
cd stix2-validator
pip install stix2-validator
```

### Using Skills with Claude

#### Option 1: Claude.ai Web Interface

1. Copy the skill instructions from the `SKILL.md` file
2. Paste them into your conversation with Claude
3. Provide the necessary input data or files
4. Claude will execute the skill according to the instructions

#### Option 2: Claude Code (Desktop App)

1. Add the skill directory to your project
2. Reference the skill in your conversation:
   ```
   Please use the STIX validator skill to check this threat intel bundle
   ```
3. Claude will automatically use the provided scripts

#### Option 3: Claude API

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# Load skill instructions
with open("stix2-validator/SKILL.md", "r") as f:
    skill_instructions = f.read()

# Use the skill
response = client.messages.create(
    model="claude-3-opus-20240229",
    messages=[
        {"role": "user", "content": f"{skill_instructions}\n\nValidate this STIX bundle: {your_stix_data}"}
    ]
)
```

## Creating Your Own Skills

### Skill Structure

Each skill should follow this directory structure:
```
skill-name/
├── SKILL.md          # Skill instructions and documentation
├── scripts/          # Implementation scripts
│   └── main.py       # Main execution script
├── examples/         # Example inputs and outputs
└── requirements.txt  # Skill-specific dependencies
```

### Best Practices for Security Skills

1. **Defense-First**: Focus on defensive security use cases
2. **Clear Documentation**: Provide detailed usage instructions and security considerations
3. **Error Handling**: Include robust error handling for security-sensitive operations
4. **Input Validation**: Always validate and sanitize inputs
5. **Audit Logging**: Include logging for security-relevant actions
6. **Compliance**: Consider relevant security standards and frameworks
7. **Testing**: Include test cases with safe, synthetic data

### Skill Template

See the [skill template](./templates/skill-template/) for a complete example structure.

## Contributing

We welcome contributions from the security community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- How to submit new skills
- Code standards and security requirements
- Review process
- Community guidelines

### Contribution Ideas

- New threat intelligence parsers
- Additional SIEM rule generators
- Cloud security posture analyzers
- Compliance framework mappers
- Incident response automation tools

## Resources

### Security Frameworks & Standards
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CIS Controls](https://www.cisecurity.org/controls)

### Threat Intelligence
- [STIX 2.1 Specification](https://oasis-open.github.io/cti-documentation/stix/intro.html)
- [MISP Project](https://www.misp-project.org/)
- [OpenCTI Platform](https://www.opencti.io/)

### Security Tools Integration
- [Splunk Security Content](https://research.splunk.com/)
- [Elastic Security](https://www.elastic.co/security)
- [Sigma Rules](https://github.com/SigmaHQ/sigma)

### Learning Resources
- [SANS Cyber Security Resources](https://www.sans.org/free/)
- [Cybrary](https://www.cybrary.it/)
- [Security Certification Roadmap](https://pauljerimy.com/security-certification-roadmap/)

## Community

Join our community to share skills, get help, and contribute:

- 💬 [Discord Server](https://discord.gg/claude-security) - Real-time discussions
- 🐦 [Twitter/X](https://twitter.com/claude_security) - Updates and announcements
- 📧 [Mailing List](https://groups.google.com/g/claude-security-skills) - Monthly newsletter
- 🎥 [YouTube Channel](https://youtube.com/@claude-security) - Tutorials and demos

### Code of Conduct

This project follows a strict code of conduct focused on:
- Ethical use of security tools
- Responsible disclosure
- Respectful collaboration
- Knowledge sharing for defense

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

These skills are provided for defensive security purposes only. Users are responsible for ensuring compliance with applicable laws and regulations. The authors assume no liability for misuse of these tools.

---

<p align="center">
Made with 🛡️ by the Security Community
</p>

<p align="center">
<a href="#-awesome-claude-skills-for-cybersecurity">Back to top ↑</a>
</p>