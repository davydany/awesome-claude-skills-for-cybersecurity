#!/usr/bin/env python3
"""STIX 2.1 Generator

Generate valid STIX 2.1 objects and bundles from various input sources.

Usage:
    python generate_stix.py --iocs ioc_list.txt --output bundle.json
    python generate_stix.py --threat threat_actor.json --output bundle.json
    python generate_stix.py --attack-pattern T1055 --output bundle.json
"""

import argparse
import json
import re
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import stix2
from stix2 import (
    AttackPattern,
    Bundle,
    Campaign,
    Identity,
    Indicator,
    Malware,
    Relationship,
    ThreatActor,
    Tool,
)


class STIXGenerator:
    """Generate STIX 2.1 objects and bundles."""
    
    # IOC patterns
    IPV4_PATTERN = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
    IPV6_PATTERN = re.compile(r'^(?:[0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{0,4}$')
    DOMAIN_PATTERN = re.compile(r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$')
    MD5_PATTERN = re.compile(r'^[a-fA-F0-9]{32}$')
    SHA1_PATTERN = re.compile(r'^[a-fA-F0-9]{40}$')
    SHA256_PATTERN = re.compile(r'^[a-fA-F0-9]{64}$')
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    URL_PATTERN = re.compile(r'^https?://[^\s]+$')
    
    # MITRE ATT&CK patterns
    TECHNIQUE_PATTERN = re.compile(r'^T\d{4}(\.\d{3})?$')
    
    def __init__(self, identity: Optional[Identity] = None):
        """Initialize the generator with an optional identity."""
        self.identity = identity or self._create_default_identity()
        self.objects = []
        self.relationships = []
    
    def _create_default_identity(self) -> Identity:
        """Create a default identity for object creation."""
        return Identity(
            name="STIX Generator",
            identity_class="system",
            description="Automated STIX object generator"
        )
    
    def detect_ioc_type(self, ioc: str) -> Optional[str]:
        """Detect the type of IOC from its format."""
        ioc = ioc.strip()
        
        if self.IPV4_PATTERN.match(ioc):
            return "ipv4"
        elif self.IPV6_PATTERN.match(ioc):
            return "ipv6"
        elif self.DOMAIN_PATTERN.match(ioc):
            return "domain"
        elif self.URL_PATTERN.match(ioc):
            return "url"
        elif self.EMAIL_PATTERN.match(ioc):
            return "email"
        elif self.MD5_PATTERN.match(ioc):
            return "md5"
        elif self.SHA1_PATTERN.match(ioc):
            return "sha1"
        elif self.SHA256_PATTERN.match(ioc):
            return "sha256"
        else:
            return None
    
    def create_indicator_pattern(self, ioc: str, ioc_type: str) -> str:
        """Create a STIX pattern from an IOC."""
        patterns = {
            "ipv4": f"[network-traffic:dst_ref.type = 'ipv4-addr' AND network-traffic:dst_ref.value = '{ioc}']",
            "ipv6": f"[network-traffic:dst_ref.type = 'ipv6-addr' AND network-traffic:dst_ref.value = '{ioc}']",
            "domain": f"[domain-name:value = '{ioc}']",
            "url": f"[url:value = '{ioc}']",
            "email": f"[email-addr:value = '{ioc}']",
            "md5": f"[file:hashes.MD5 = '{ioc.lower()}']",
            "sha1": f"[file:hashes.SHA-1 = '{ioc.lower()}']",
            "sha256": f"[file:hashes.SHA-256 = '{ioc.lower()}']",
        }
        return patterns.get(ioc_type, f"[{ioc_type}:value = '{ioc}']")
    
    def generate_indicator(
        self,
        ioc: str,
        labels: List[str] = None,
        pattern_type: str = "stix",
        valid_from: Optional[datetime] = None,
        valid_until: Optional[datetime] = None,
        confidence: int = 75,
        description: Optional[str] = None
    ) -> Optional[Indicator]:
        """Generate an indicator from an IOC."""
        ioc_type = self.detect_ioc_type(ioc)
        if not ioc_type:
            print(f"Warning: Could not detect IOC type for: {ioc}", file=sys.stderr)
            return None
        
        pattern = self.create_indicator_pattern(ioc, ioc_type)
        
        if not valid_from:
            valid_from = datetime.now(timezone.utc)
        
        indicator_name = f"{ioc_type.upper()}: {ioc}"
        if not description:
            description = f"Indicator for {ioc_type} {ioc}"
        
        if not labels:
            labels = ["malicious-activity"]
        
        kwargs = {
            "name": indicator_name,
            "pattern": pattern,
            "pattern_type": pattern_type,
            "valid_from": valid_from,
            "labels": labels,
            "confidence": confidence,
            "description": description,
            "created_by_ref": self.identity.id
        }
        
        if valid_until:
            kwargs["valid_until"] = valid_until
        
        return Indicator(**kwargs)
    
    def generate_indicators_from_file(
        self,
        filepath: Path,
        **kwargs
    ) -> List[Indicator]:
        """Generate indicators from a file containing IOCs."""
        indicators = []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                ioc = line.strip()
                if ioc and not ioc.startswith('#'):
                    indicator = self.generate_indicator(ioc, **kwargs)
                    if indicator:
                        indicators.append(indicator)
                        self.objects.append(indicator)
        
        return indicators
    
    def generate_attack_pattern(
        self,
        technique_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None
    ) -> Optional[AttackPattern]:
        """Generate an attack pattern from a MITRE ATT&CK technique ID."""
        if not self.TECHNIQUE_PATTERN.match(technique_id):
            print(f"Warning: Invalid MITRE ATT&CK technique ID: {technique_id}", file=sys.stderr)
            return None
        
        if not name:
            name = f"MITRE ATT&CK Technique {technique_id}"
        
        if not description:
            description = f"Attack pattern based on MITRE ATT&CK technique {technique_id}"
        
        attack_pattern = AttackPattern(
            name=name,
            description=description,
            external_references=[
                {
                    "source_name": "mitre-attack",
                    "external_id": technique_id,
                    "url": f"https://attack.mitre.org/techniques/{technique_id.replace('.', '/')}/"
                }
            ],
            created_by_ref=self.identity.id
        )
        
        self.objects.append(attack_pattern)
        return attack_pattern
    
    def generate_malware(self, config: Dict[str, Any]) -> Malware:
        """Generate a malware object from configuration."""
        kwargs = {
            "name": config.get("name", "Unknown Malware"),
            "malware_types": config.get("malware_types", ["unknown"]),
            "is_family": config.get("is_family", True),
            "created_by_ref": self.identity.id
        }
        
        # Optional fields
        if "description" in config:
            kwargs["description"] = config["description"]
        if "capabilities" in config:
            kwargs["capabilities"] = config["capabilities"]
        if "kill_chain_phases" in config:
            kwargs["kill_chain_phases"] = config["kill_chain_phases"]
        if "aliases" in config:
            kwargs["aliases"] = config["aliases"]
        
        malware = Malware(**kwargs)
        self.objects.append(malware)
        return malware
    
    def generate_threat_actor(self, config: Dict[str, Any]) -> ThreatActor:
        """Generate a threat actor from configuration."""
        kwargs = {
            "name": config.get("name", "Unknown Threat Actor"),
            "threat_actor_types": config.get("threat_actor_types", ["unknown"]),
            "created_by_ref": self.identity.id
        }
        
        # Optional fields
        optional_fields = [
            "description", "aliases", "roles", "goals", "sophistication",
            "resource_level", "primary_motivation", "secondary_motivations",
            "personal_motivations"
        ]
        
        for field in optional_fields:
            if field in config:
                kwargs[field] = config[field]
        
        threat_actor = ThreatActor(**kwargs)
        self.objects.append(threat_actor)
        
        # Generate attack patterns for observed TTPs
        if "observed_ttps" in config:
            for ttp in config["observed_ttps"]:
                attack_pattern = self.generate_attack_pattern(ttp)
                if attack_pattern:
                    # Create relationship
                    rel = Relationship(
                        relationship_type="uses",
                        source_ref=threat_actor.id,
                        target_ref=attack_pattern.id,
                        created_by_ref=self.identity.id
                    )
                    self.relationships.append(rel)
                    self.objects.append(rel)
        
        return threat_actor
    
    def generate_campaign(self, config: Dict[str, Any]) -> Campaign:
        """Generate a campaign from configuration."""
        kwargs = {
            "name": config.get("name", "Unknown Campaign"),
            "created_by_ref": self.identity.id
        }
        
        # Optional fields
        optional_fields = ["description", "aliases", "first_seen", "last_seen", "objective"]
        
        for field in optional_fields:
            if field in config:
                if field in ["first_seen", "last_seen"] and isinstance(config[field], str):
                    kwargs[field] = datetime.fromisoformat(config[field].replace('Z', '+00:00'))
                else:
                    kwargs[field] = config[field]
        
        campaign = Campaign(**kwargs)
        self.objects.append(campaign)
        
        # Generate related objects
        if "threat_actor" in config:
            threat_actor = self.generate_threat_actor(config["threat_actor"])
            rel = Relationship(
                relationship_type="attributed-to",
                source_ref=campaign.id,
                target_ref=threat_actor.id,
                created_by_ref=self.identity.id
            )
            self.relationships.append(rel)
            self.objects.append(rel)
        
        if "malware" in config:
            for malware_config in config.get("malware", []):
                malware = self.generate_malware(malware_config)
                rel = Relationship(
                    relationship_type="uses",
                    source_ref=campaign.id,
                    target_ref=malware.id,
                    created_by_ref=self.identity.id
                )
                self.relationships.append(rel)
                self.objects.append(rel)
        
        return campaign
    
    def create_bundle(self, spec_version: str = "2.1") -> Bundle:
        """Create a STIX bundle from generated objects."""
        return Bundle(objects=self.objects)
    
    def validate_bundle(self, bundle: Bundle) -> Tuple[bool, List[str]]:
        """Validate a STIX bundle."""
        errors = []
        
        try:
            # Basic validation
            bundle_dict = json.loads(bundle.serialize())
            
            # Check required fields
            if "type" not in bundle_dict or bundle_dict["type"] != "bundle":
                errors.append("Invalid bundle type")
            
            if "objects" not in bundle_dict or not bundle_dict["objects"]:
                errors.append("Bundle has no objects")
            
            # Validate each object
            for obj in bundle_dict.get("objects", []):
                if "type" not in obj:
                    errors.append(f"Object missing type: {obj.get('id', 'unknown')}")
                if "id" not in obj:
                    errors.append(f"Object missing id: {obj.get('type', 'unknown')}")
            
            return len(errors) == 0, errors
        except Exception as e:
            return False, [str(e)]
    
    def save_bundle(
        self,
        bundle: Bundle,
        output_path: Optional[Path] = None,
        format: str = "json",
        pretty: bool = True
    ) -> None:
        """Save a bundle to file or stdout."""
        if format == "json":
            output = bundle.serialize(pretty=pretty)
        elif format == "yaml":
            # Would need PyYAML for this
            bundle_dict = json.loads(bundle.serialize())
            import yaml
            output = yaml.dump(bundle_dict, default_flow_style=False)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output)
        else:
            print(output)


def load_json_file(filepath: Path) -> Dict[str, Any]:
    """Load and parse a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(
        description="Generate STIX 2.1 objects and bundles",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Input options
    input_group = parser.add_argument_group("Input Options")
    input_group.add_argument(
        "--iocs",
        type=Path,
        help="Generate indicators from IOC list file"
    )
    input_group.add_argument(
        "--threat",
        type=Path,
        help="Generate threat actor from JSON configuration"
    )
    input_group.add_argument(
        "--attack-pattern",
        help="Generate attack pattern from MITRE ATT&CK ID(s)"
    )
    input_group.add_argument(
        "--malware",
        type=Path,
        help="Generate malware from JSON configuration"
    )
    input_group.add_argument(
        "--campaign",
        type=Path,
        help="Generate campaign from JSON configuration"
    )
    input_group.add_argument(
        "--batch",
        type=Path,
        help="Batch process multiple objects from JSON"
    )
    
    # Configuration options
    config_group = parser.add_argument_group("Configuration")
    config_group.add_argument(
        "--identity",
        help="Identity name for created_by_ref"
    )
    config_group.add_argument(
        "--labels",
        help="Labels for indicators (comma-separated)"
    )
    config_group.add_argument(
        "--pattern-type",
        default="stix",
        choices=["stix", "snort", "yara"],
        help="Pattern type for indicators"
    )
    config_group.add_argument(
        "--valid-from",
        help="Valid from timestamp (ISO format)"
    )
    config_group.add_argument(
        "--valid-until",
        help="Valid until timestamp (ISO format)"
    )
    config_group.add_argument(
        "--confidence",
        type=int,
        default=75,
        help="Confidence level (0-100)"
    )
    config_group.add_argument(
        "--description",
        help="Description for generated objects"
    )
    
    # Output options
    output_group = parser.add_argument_group("Output Options")
    output_group.add_argument(
        "--output", "-o",
        type=Path,
        help="Output file (default: stdout)"
    )
    output_group.add_argument(
        "--format", "-f",
        choices=["json", "yaml"],
        default="json",
        help="Output format"
    )
    output_group.add_argument(
        "--validate",
        action="store_true",
        help="Validate generated STIX"
    )
    output_group.add_argument(
        "--bundle",
        action="store_true",
        default=True,
        help="Wrap objects in a bundle (default: True)"
    )
    output_group.add_argument(
        "--relationships",
        action="store_true",
        help="Generate relationships between objects"
    )
    output_group.add_argument(
        "--pretty",
        action="store_true",
        default=True,
        help="Pretty print output"
    )
    
    # Interactive mode
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Interactive mode for guided creation"
    )
    
    args = parser.parse_args()
    
    # Check that at least one input option is provided
    if not any([args.iocs, args.threat, args.attack_pattern, args.malware, 
                args.campaign, args.batch, args.interactive]):
        parser.error("At least one input option is required")
    
    # Create identity if specified
    identity = None
    if args.identity:
        identity = Identity(
            name=args.identity,
            identity_class="organization"
        )
    
    # Initialize generator
    generator = STIXGenerator(identity=identity)
    
    # Process timestamps
    valid_from = None
    valid_until = None
    if args.valid_from:
        valid_from = datetime.fromisoformat(args.valid_from.replace('Z', '+00:00'))
    if args.valid_until:
        valid_until = datetime.fromisoformat(args.valid_until.replace('Z', '+00:00'))
    
    # Process labels
    labels = None
    if args.labels:
        labels = [label.strip() for label in args.labels.split(',')]
    
    # Generate objects based on input
    if args.iocs:
        print(f"Generating indicators from {args.iocs}...", file=sys.stderr)
        indicators = generator.generate_indicators_from_file(
            args.iocs,
            labels=labels,
            pattern_type=args.pattern_type,
            valid_from=valid_from,
            valid_until=valid_until,
            confidence=args.confidence,
            description=args.description
        )
        print(f"Generated {len(indicators)} indicators", file=sys.stderr)
    
    if args.threat:
        print(f"Generating threat actor from {args.threat}...", file=sys.stderr)
        config = load_json_file(args.threat)
        threat_actor = generator.generate_threat_actor(config)
        print(f"Generated threat actor: {threat_actor.name}", file=sys.stderr)
    
    if args.attack_pattern:
        techniques = args.attack_pattern.split(',')
        for technique in techniques:
            technique = technique.strip()
            print(f"Generating attack pattern for {technique}...", file=sys.stderr)
            attack_pattern = generator.generate_attack_pattern(
                technique,
                description=args.description
            )
            if attack_pattern:
                print(f"Generated attack pattern: {attack_pattern.name}", file=sys.stderr)
    
    if args.malware:
        print(f"Generating malware from {args.malware}...", file=sys.stderr)
        config = load_json_file(args.malware)
        malware = generator.generate_malware(config)
        print(f"Generated malware: {malware.name}", file=sys.stderr)
    
    if args.campaign:
        print(f"Generating campaign from {args.campaign}...", file=sys.stderr)
        config = load_json_file(args.campaign)
        campaign = generator.generate_campaign(config)
        print(f"Generated campaign: {campaign.name}", file=sys.stderr)
    
    if args.batch:
        print(f"Batch processing from {args.batch}...", file=sys.stderr)
        # Implement batch processing
        config = load_json_file(args.batch)
        # Process batch configuration...
    
    if args.interactive:
        print("Interactive mode not yet implemented", file=sys.stderr)
        return 1
    
    # Create bundle
    bundle = generator.create_bundle()
    
    # Validate if requested
    if args.validate:
        print("Validating bundle...", file=sys.stderr)
        is_valid, errors = generator.validate_bundle(bundle)
        if not is_valid:
            print("Validation errors:", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
            return 1
        print("✅ Bundle is valid", file=sys.stderr)
    
    # Save bundle
    generator.save_bundle(
        bundle,
        output_path=args.output,
        format=args.format,
        pretty=args.pretty
    )
    
    print(f"✅ Generated bundle with {len(generator.objects)} objects", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())