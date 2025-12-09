#!/usr/bin/env python3
"""STIX 2.1 Bundle Validator

Validates STIX 2.1 JSON files and provides detailed error reports.

Usage:
    python validate_stix.py <file_or_directory> [options]

Options:
    --strict          Enable strict validation (all optional checks)
    --enforce-refs    Require all references to resolve within the bundle
    --recursive       Recursively validate files in directories
    --json            Output results as JSON
    --quiet           Only show errors, suppress success messages
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from stix2validator import validate_file, ValidationOptions


def create_options(strict: bool = False, enforce_refs: bool = False) -> ValidationOptions:
    """Create validation options for STIX 2.1."""
    return ValidationOptions(
        version="2.1",
        strict=strict,
        enforce_refs=enforce_refs,
    )


def format_error(error: dict) -> str:
    """Format a single validation error for display."""
    msg = error.get("message", "Unknown error")
    obj_id = error.get("id", "")
    obj_type = error.get("type", "")
    
    if obj_id:
        return f"  [{obj_type}] {obj_id}: {msg}"
    return f"  {msg}"


def validate_single_file(
    filepath: Path,
    options: ValidationOptions,
    output_json: bool = False,
    quiet: bool = False,
) -> tuple[bool, dict]:
    """Validate a single STIX file and return results."""
    results = validate_file(str(filepath), options)
    
    output = {
        "file": str(filepath),
        "valid": results.is_valid,
        "errors": [],
        "warnings": [],
    }
    
    # Collect errors from object results
    if hasattr(results, "object_results") and results.object_results:
        for obj_result in results.object_results:
            if hasattr(obj_result, "errors") and obj_result.errors:
                for error in obj_result.errors:
                    error_info = {
                        "id": getattr(obj_result, "object_id", ""),
                        "type": getattr(obj_result, "object_type", ""),
                        "message": str(error),
                    }
                    output["errors"].append(error_info)
            if hasattr(obj_result, "warnings") and obj_result.warnings:
                for warning in obj_result.warnings:
                    warning_info = {
                        "id": getattr(obj_result, "object_id", ""),
                        "type": getattr(obj_result, "object_type", ""),
                        "message": str(warning),
                    }
                    output["warnings"].append(warning_info)
    
    # Also check for fatal/file-level errors
    if hasattr(results, "fatal") and results.fatal:
        output["errors"].append({
            "id": "",
            "type": "fatal",
            "message": str(results.fatal),
        })
        output["valid"] = False
    
    if not output_json and not quiet:
        print_results(filepath, output)
    
    return output["valid"], output


def print_results(filepath: Path, output: dict) -> None:
    """Print formatted validation results."""
    status = "✅ VALID" if output["valid"] else "❌ INVALID"
    print(f"\n{status}: {filepath}")
    
    if output["errors"]:
        print(f"\n  Errors ({len(output['errors'])}):")
        for error in output["errors"]:
            print(format_error(error))
    
    if output["warnings"]:
        print(f"\n  Warnings ({len(output['warnings'])}):")
        for warning in output["warnings"]:
            print(format_error(warning))


def validate_directory(
    dirpath: Path,
    options: ValidationOptions,
    recursive: bool = False,
    output_json: bool = False,
    quiet: bool = False,
) -> tuple[bool, list[dict]]:
    """Validate all STIX JSON files in a directory."""
    pattern = "**/*.json" if recursive else "*.json"
    files = list(dirpath.glob(pattern))
    
    if not files:
        print(f"No JSON files found in {dirpath}")
        return True, []
    
    all_valid = True
    all_results = []
    
    for filepath in sorted(files):
        is_valid, result = validate_single_file(filepath, options, output_json, quiet)
        all_results.append(result)
        if not is_valid:
            all_valid = False
    
    return all_valid, all_results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate STIX 2.1 JSON files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to a STIX JSON file or directory containing STIX files",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable strict validation (enforces all optional checks)",
    )
    parser.add_argument(
        "--enforce-refs",
        action="store_true",
        help="Require all object references to resolve within the bundle",
    )
    parser.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Recursively validate JSON files in subdirectories",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON",
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Only show errors, suppress success messages",
    )
    
    args = parser.parse_args()
    
    if not args.path.exists():
        print(f"Error: Path not found: {args.path}", file=sys.stderr)
        return 1
    
    options = create_options(strict=args.strict, enforce_refs=args.enforce_refs)
    
    if args.path.is_file():
        is_valid, results = validate_single_file(
            args.path, options, args.json, args.quiet
        )
        if args.json:
            print(json.dumps(results, indent=2))
    else:
        is_valid, results = validate_directory(
            args.path, options, args.recursive, args.json, args.quiet
        )
        if args.json:
            print(json.dumps({"results": results, "all_valid": is_valid}, indent=2))
    
    if not args.json:
        print(f"\n{'='*50}")
        print(f"Overall: {'✅ All files valid' if is_valid else '❌ Validation errors found'}")
    
    return 0 if is_valid else 1


if __name__ == "__main__":
    sys.exit(main())
