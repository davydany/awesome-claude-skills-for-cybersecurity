# Contributing to Awesome Claude Skills for Cybersecurity

First off, thank you for considering contributing to this project! It's people like you that make the security community stronger and help defenders protect organizations worldwide.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Submitting a New Skill](#submitting-a-new-skill)
- [Improving Existing Skills](#improving-existing-skills)
- [Reporting Security Issues](#reporting-security-issues)
- [Development Guidelines](#development-guidelines)
- [Review Process](#review-process)
- [Community Guidelines](#community-guidelines)

## Code of Conduct

### Our Pledge

We are committed to providing a friendly, safe, and welcoming environment for all contributors, regardless of experience level, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, religion, nationality, or other similar characteristics.

### Security Ethics

All contributions must:
- Focus on **defensive security** only
- Not include any offensive security tools or techniques
- Not contain malware, backdoors, or malicious code
- Respect responsible disclosure practices
- Comply with applicable laws and regulations

## How Can I Contribute?

### Ways to Contribute

- 🛡️ **Submit New Skills**: Share your security automation workflows
- 🔧 **Improve Existing Skills**: Enhance functionality, fix bugs, improve documentation
- 📚 **Improve Documentation**: Fix typos, clarify instructions, add examples
- 🐛 **Report Bugs**: Help us identify and fix issues
- 💡 **Suggest Enhancements**: Propose new features or improvements
- 🎨 **Design Resources**: Create diagrams, logos, or visual aids
- 🌍 **Translations**: Help make skills accessible to non-English speakers

## Submitting a New Skill

### Before You Begin

1. Check the [existing skills](README.md#skills-catalog) to avoid duplicates
2. Review our [skill template](templates/skill-template/) for structure guidelines
3. Ensure your skill focuses on defensive security use cases

### Skill Requirements

Each skill must include:

#### 1. SKILL.md File
```markdown
---
name: skill-name
description: Brief description of what the skill does
---

# Skill Name

Detailed description of the skill's purpose and capabilities.

## Requirements
- List all dependencies
- Specify minimum Python version
- Include any API requirements

## Usage
- Clear usage instructions
- Command-line examples
- Expected inputs and outputs

## Examples
- Provide at least 2 practical examples
- Include sample data when appropriate

## Security Considerations
- Document any security implications
- Specify required permissions
- Note any compliance considerations
```

#### 2. Implementation Scripts
- Well-documented Python or bash scripts
- Proper error handling
- Input validation and sanitization
- Logging capabilities

#### 3. Test Data
- Safe, synthetic test data only
- No real sensitive information
- Examples that demonstrate key features

### Submission Process

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b add-skill-name
   ```
3. Add your skill following the structure:
   ```
   skill-name/
   ├── SKILL.md
   ├── scripts/
   │   └── main.py
   ├── examples/
   │   ├── input.json
   │   └── output.json
   └── requirements.txt
   ```
4. Test your skill thoroughly
5. Update the main README.md to include your skill in the appropriate category
6. Commit your changes:
   ```bash
   git commit -m "Add [skill-name]: Brief description"
   ```
7. Push to your fork:
   ```bash
   git push origin add-skill-name
   ```
8. Submit a Pull Request

## Improving Existing Skills

### Types of Improvements

- **Bug Fixes**: Fix errors or unexpected behavior
- **Performance**: Optimize execution speed or resource usage
- **Features**: Add new capabilities that align with the skill's purpose
- **Documentation**: Clarify instructions, add examples, fix typos
- **Testing**: Add test cases or improve test coverage

### Process

1. Open an issue describing the improvement
2. Wait for maintainer feedback before starting major changes
3. Follow the submission process above

## Reporting Security Issues

### Responsible Disclosure

If you discover a security vulnerability:

1. **DO NOT** create a public issue
2. Email security concerns to: security@[project-email].com
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)
4. Wait for confirmation before public disclosure

### Non-Security Bugs

For non-security bugs:
1. Check if the issue already exists
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)

## Development Guidelines

### Code Standards

#### Python
```python
# Use type hints
def validate_input(data: dict) -> bool:
    """Validate input data for security compliance.
    
    Args:
        data: Input dictionary to validate
        
    Returns:
        True if valid, False otherwise
    """
    # Implementation
    pass
```

#### Error Handling
```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    # Graceful fallback
except Exception as e:
    logger.exception("Unexpected error")
    # Safe failure mode
```

### Documentation Standards

- Use clear, concise language
- Include practical examples
- Document all parameters and return values
- Explain security implications
- Provide troubleshooting guidance

### Testing Requirements

- Test with synthetic data only
- Cover edge cases and error conditions
- Validate security controls
- Check input sanitization
- Test with minimal permissions

### Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

Types:
- `feat`: New feature or skill
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Example:
```
feat: Add AWS GuardDuty findings analyzer

- Parses GuardDuty findings JSON
- Maps to MITRE ATT&CK tactics
- Generates remediation recommendations
- Includes severity-based prioritization

Closes #42
```

## Review Process

### What We Look For

1. **Security First**
   - No offensive capabilities
   - Proper input validation
   - Secure coding practices
   - Clear security documentation

2. **Quality**
   - Clean, readable code
   - Comprehensive documentation
   - Proper error handling
   - Test coverage

3. **Usefulness**
   - Solves real security problems
   - Practical for security teams
   - Well-defined scope
   - Clear value proposition

### Review Timeline

- Initial review: Within 3-5 business days
- Follow-up reviews: Within 2-3 business days
- Complex contributions may take longer

### After Your PR is Merged

- Your contribution will be credited in the skill documentation
- You'll be added to the contributors list
- Consider joining as a maintainer for skills you've created

## Community Guidelines

### Communication

- Be respectful and professional
- Provide constructive feedback
- Help others learn and grow
- Share knowledge openly
- Respect diverse perspectives

### Collaboration

- Work together on complex skills
- Share experiences and lessons learned
- Mentor new contributors
- Participate in discussions
- Support the community

### Recognition

We value all contributions:
- Code contributions
- Documentation improvements
- Bug reports
- Feature suggestions
- Community support
- Knowledge sharing

## Questions?

If you have questions about contributing:

1. Check the [FAQ](docs/FAQ.md)
2. Join our [Discord Server](https://discord.gg/claude-security)
3. Open a discussion in GitHub Discussions
4. Email us at: contribute@[project-email].com

## Thank You!

Your contributions make the security community stronger. Together, we're building tools that help defenders protect organizations and users worldwide.

---

<p align="center">
Happy Contributing! 🛡️
</p>