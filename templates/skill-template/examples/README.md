# Skill Template Examples

This directory contains sample input and output data for the skill template.

## Files

### sample_input.json
Example input data that demonstrates the expected format for this skill. Replace this with examples relevant to your actual skill.

**Structure:**
- `example_field`: Required field that your skill expects
- `items`: Array of items to process (optional - some skills process single items)
- `metadata`: Information about the data source and creation

### Usage

Test the skill template with the sample data:

```bash
cd ../scripts
python main.py ../examples/sample_input.json
```

Expected output format:
```json
{
  "metadata": {
    "skill": "skill-template",
    "version": "1.0.0",
    "timestamp": "2024-01-01T12:00:00Z"
  },
  "summary": {
    "total_items": 3,
    "processed": 3,
    "errors": 0,
    "warnings": 1
  },
  "results": [
    {
      "item_id": "item-0",
      "status": "success",
      "findings": [],
      "recommendations": []
    }
  ],
  "errors": [],
  "warnings": []
}
```

## Creating Your Own Examples

When creating your own skill:

1. **Replace sample_input.json** with realistic input data for your skill
2. **Create multiple examples** showing different scenarios:
   - `valid_input.json` - Clean data that should process successfully
   - `invalid_input.json` - Malformed data to test error handling
   - `edge_case.json` - Boundary conditions and unusual cases
   - `large_dataset.json` - Performance testing with larger datasets

3. **Document the format** in this README with:
   - Required fields and their types
   - Optional fields and defaults
   - Valid value ranges
   - Dependencies between fields

4. **Include expected outputs** showing what results should look like

## Security Considerations

When creating examples:
- **Never use real sensitive data** (passwords, API keys, personal information)
- **Use synthetic data** that looks realistic but is completely fabricated
- **Anonymize any real data** if you must use it as a reference
- **Document what type of data** the skill expects and how it's handled

## Testing

Use these examples to test your skill:

```bash
# Basic functionality test
python scripts/main.py examples/sample_input.json

# Output format test
python scripts/main.py examples/sample_input.json --format json
python scripts/main.py examples/sample_input.json --format csv
python scripts/main.py examples/sample_input.json --format text

# Error handling test (if you have invalid_input.json)
python scripts/main.py examples/invalid_input.json

# Performance test (if you have large_dataset.json)
time python scripts/main.py examples/large_dataset.json
```