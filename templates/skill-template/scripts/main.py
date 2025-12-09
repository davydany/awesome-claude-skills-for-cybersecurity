#!/usr/bin/env python3
"""
Skill Template - Main Script

This is a template for creating new cybersecurity skills. Replace this content
with your actual skill implementation.

Usage:
    python main.py <input_file> [options]

Example:
    python main.py ../examples/sample_input.json --output results.json
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SkillTemplateError(Exception):
    """Custom exception for skill-specific errors."""
    pass


class SkillTemplate:
    """
    Template class for cybersecurity skills.
    
    Replace this with your actual skill implementation.
    """
    
    def __init__(self, debug: bool = False):
        """Initialize the skill."""
        self.debug = debug
        if debug:
            logging.getLogger().setLevel(logging.DEBUG)
            logger.debug("Debug mode enabled")
    
    def validate_input(self, data: Dict[str, Any]) -> bool:
        """
        Validate input data format.
        
        Args:
            data: Input data to validate
            
        Returns:
            True if valid, False otherwise
            
        Raises:
            SkillTemplateError: If validation fails with specific error
        """
        logger.debug("Validating input data")
        
        # Add your input validation logic here
        # Example validations:
        if not isinstance(data, dict):
            raise SkillTemplateError("Input must be a JSON object")
        
        # Check for required fields
        required_fields = ["example_field"]  # Replace with actual required fields
        for field in required_fields:
            if field not in data:
                raise SkillTemplateError(f"Missing required field: {field}")
        
        logger.debug("Input validation passed")
        return True
    
    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main analysis function.
        
        Args:
            data: Input data to analyze
            
        Returns:
            Analysis results
            
        Raises:
            SkillTemplateError: If analysis fails
        """
        logger.info("Starting analysis")
        
        # Validate input first
        self.validate_input(data)
        
        # Initialize results structure
        results = {
            "metadata": {
                "skill": "skill-template",
                "version": "1.0.0",
                "timestamp": self._get_timestamp(),
            },
            "summary": {
                "total_items": 0,
                "processed": 0,
                "errors": 0,
                "warnings": 0
            },
            "results": [],
            "errors": [],
            "warnings": []
        }
        
        try:
            # Add your analysis logic here
            # Example analysis:
            logger.debug("Processing input data")
            
            # Simulate processing items
            items = data.get("items", [data])  # Handle single item or list
            results["summary"]["total_items"] = len(items)
            
            for i, item in enumerate(items):
                try:
                    # Process individual item
                    item_result = self._process_item(item, i)
                    results["results"].append(item_result)
                    results["summary"]["processed"] += 1
                    
                    if item_result.get("status") == "warning":
                        results["summary"]["warnings"] += 1
                    
                except Exception as e:
                    logger.error(f"Error processing item {i}: {e}")
                    error_info = {
                        "item_id": f"item-{i}",
                        "error_type": "processing_error",
                        "message": str(e)
                    }
                    results["errors"].append(error_info)
                    results["summary"]["errors"] += 1
            
            logger.info(f"Analysis complete. Processed {results['summary']['processed']} items")
            
        except Exception as e:
            logger.error(f"Analysis failed: {e}")
            raise SkillTemplateError(f"Analysis failed: {e}")
        
        return results
    
    def _process_item(self, item: Dict[str, Any], index: int) -> Dict[str, Any]:
        """
        Process a single item.
        
        Args:
            item: Item to process
            index: Item index for tracking
            
        Returns:
            Processing result
        """
        logger.debug(f"Processing item {index}")
        
        # Add your item processing logic here
        # This is just an example
        result = {
            "item_id": f"item-{index}",
            "status": "success",
            "findings": [],
            "recommendations": []
        }
        
        # Example analysis logic
        if "security_issue" in str(item).lower():
            result["status"] = "warning"
            result["findings"].append({
                "type": "security",
                "severity": "medium",
                "description": "Potential security issue detected"
            })
            result["recommendations"].append("Review security configuration")
        
        return result
    
    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO format."""
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"


def load_input(input_path: Path) -> Dict[str, Any]:
    """
    Load input data from file.
    
    Args:
        input_path: Path to input file
        
    Returns:
        Loaded data
        
    Raises:
        SkillTemplateError: If file cannot be loaded
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            if input_path.suffix.lower() == '.json':
                return json.load(f)
            else:
                # Handle other formats as needed
                raise SkillTemplateError(f"Unsupported file format: {input_path.suffix}")
    except json.JSONDecodeError as e:
        raise SkillTemplateError(f"Invalid JSON in {input_path}: {e}")
    except FileNotFoundError:
        raise SkillTemplateError(f"Input file not found: {input_path}")
    except Exception as e:
        raise SkillTemplateError(f"Error loading input file: {e}")


def save_output(results: Dict[str, Any], output_path: Optional[Path], format_type: str) -> None:
    """
    Save results to file or stdout.
    
    Args:
        results: Results to save
        output_path: Output file path (None for stdout)
        format_type: Output format (json, csv, text)
    """
    if format_type == "json":
        output_data = json.dumps(results, indent=2, default=str)
    elif format_type == "csv":
        # Convert to CSV format (implement as needed)
        output_data = _convert_to_csv(results)
    elif format_type == "text":
        # Convert to human-readable text
        output_data = _convert_to_text(results)
    else:
        raise SkillTemplateError(f"Unsupported output format: {format_type}")
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_data)
        logger.info(f"Results saved to {output_path}")
    else:
        print(output_data)


def _convert_to_csv(results: Dict[str, Any]) -> str:
    """Convert results to CSV format."""
    # Implement CSV conversion as needed
    # This is a simple example
    lines = ["item_id,status,findings,recommendations"]
    for result in results.get("results", []):
        item_id = result.get("item_id", "")
        status = result.get("status", "")
        findings = "; ".join([f["description"] for f in result.get("findings", [])])
        recommendations = "; ".join(result.get("recommendations", []))
        lines.append(f'"{item_id}","{status}","{findings}","{recommendations}"')
    return "\n".join(lines)


def _convert_to_text(results: Dict[str, Any]) -> str:
    """Convert results to human-readable text."""
    lines = []
    
    # Add summary
    summary = results.get("summary", {})
    lines.append("=== Analysis Summary ===")
    lines.append(f"Total items: {summary.get('total_items', 0)}")
    lines.append(f"Processed: {summary.get('processed', 0)}")
    lines.append(f"Errors: {summary.get('errors', 0)}")
    lines.append(f"Warnings: {summary.get('warnings', 0)}")
    lines.append("")
    
    # Add findings
    if results.get("results"):
        lines.append("=== Detailed Results ===")
        for result in results["results"]:
            lines.append(f"Item: {result.get('item_id', 'unknown')}")
            lines.append(f"Status: {result.get('status', 'unknown')}")
            
            findings = result.get("findings", [])
            if findings:
                lines.append("Findings:")
                for finding in findings:
                    lines.append(f"  - {finding.get('description', 'No description')}")
            
            recommendations = result.get("recommendations", [])
            if recommendations:
                lines.append("Recommendations:")
                for rec in recommendations:
                    lines.append(f"  - {rec}")
            lines.append("")
    
    return "\n".join(lines)


def main() -> int:
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Cybersecurity Skill Template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "input",
        type=Path,
        help="Path to input file (JSON format)"
    )
    
    parser.add_argument(
        "--output", "-o",
        type=Path,
        help="Output file path (default: stdout)"
    )
    
    parser.add_argument(
        "--format", "-f",
        choices=["json", "csv", "text"],
        default="json",
        help="Output format (default: json)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )
    
    args = parser.parse_args()
    
    # Configure logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.INFO)
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        # Load input data
        logger.info(f"Loading input from {args.input}")
        input_data = load_input(args.input)
        
        # Initialize and run skill
        skill = SkillTemplate(debug=args.debug)
        results = skill.analyze(input_data)
        
        # Save results
        save_output(results, args.output, args.format)
        
        # Return appropriate exit code
        if results["summary"]["errors"] > 0:
            logger.warning(f"Analysis completed with {results['summary']['errors']} errors")
            return 1
        else:
            logger.info("Analysis completed successfully")
            return 0
            
    except SkillTemplateError as e:
        logger.error(f"Skill error: {e}")
        return 1
    except KeyboardInterrupt:
        logger.info("Analysis interrupted by user")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())