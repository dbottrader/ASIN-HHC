#!/usr/bin/env python3
"""
lmc-init — Labyrinth Master Canon Bootstrap Loader
Version: 1.0.0
Purpose: Validates and initializes the Labyrinth Master Canon environment.
         Acts as the single entry point for loading the canonical project knowledge OS.

Follows LMC v1.0 principles:
- Capability does not imply authority
- Evidence Ladder enforcement (basic)
- Atomic operations where possible
- Clear provenance via hashing
- Human-governed initialization

Usage:
    python lmc-init.py --init
    python lmc-init.py --validate
    python lmc-init.py --status
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# =============================================================================
# CONFIGURATION (from LMC v1.0)
# =============================================================================

LMC_VERSION = "1.0.0"
CANON_FILE = "master-canon/Labyrinth_Master_Canon_v1.0.md"

EXPECTED_DIRECTORIES = [
    "master-canon",
    "cathedral-os",
    "cathedral-os/medical",
    "v2.3",
    "v2.3/phi-artifacts",
    "proof-of-process",
    "history",
    "tools",
    "governance",
    "evidence",
    "registry",
    "receipts",
    "witness",
    "knowledge-graph",
]

EVIDENCE_LEVELS = {
    0: "Concept",
    1: "Specification",
    2: "Implementation",
    3: "Local Testing",
    4: "Receipt",
    5: "Cross-Environment Reproduction",
    6: "Independent Verification",
    7: "Operational Deployment",
    8: "Institutional Trust",
}

UNIVERSAL_OBJECT_FIELDS = [
    "id", "type", "title", "author", "created", "modified",
    "version", "status", "evidence_level", "governance_state",
    "dependencies", "parents", "children", "claims", "predictions",
    "experiments", "receipts", "hash", "signature", "location"
]


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def compute_sha256(file_path: Path) -> str:
    """Compute SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def atomic_write_json(file_path: Path, data: dict) -> None:
    """Write JSON atomically using temp file + rename."""
    temp_path = file_path.with_suffix(".tmp")
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(temp_path, file_path)


def get_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


# =============================================================================
# CORE FUNCTIONS
# =============================================================================

def validate_directory_structure(base_path: Path) -> Dict[str, bool]:
    """Check that all expected LMC directories exist."""
    results = {}
    for directory in EXPECTED_DIRECTORIES:
        dir_path = base_path / directory
        results[directory] = dir_path.exists() and dir_path.is_dir()
    return results


def load_canon_metadata(base_path: Path) -> Optional[Dict]:
    """Load basic metadata from the Master Canon document."""
    canon_path = base_path / CANON_FILE
    if not canon_path.exists():
        return None

    try:
        content = canon_path.read_text(encoding="utf-8")
        # Simple metadata extraction
        metadata = {
            "file": str(canon_path),
            "size_bytes": canon_path.stat().st_size,
            "sha256": compute_sha256(canon_path),
            "last_modified": datetime.fromtimestamp(
                canon_path.stat().st_mtime, tz=timezone.utc
            ).isoformat(),
            "contains_lmc_header": "LABYRINTH MASTER CANON" in content,
            "contains_core_laws": "Core Laws" in content,
            "contains_evidence_ladder": "Evidence Ladder" in content,
        }
        return metadata
    except Exception as e:
        return {"error": str(e)}


def check_evidence_ladder_compliance(artifacts: List[Path]) -> List[Dict]:
    """
    Basic Evidence Ladder enforcement check on JSON artifacts.
    Prevents claiming evidence_level higher than supported by presence of receipts/verification.
    """
    results = []
    for artifact_path in artifacts:
        if not artifact_path.suffix == ".json":
            continue
        try:
            with open(artifact_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            claimed_level = data.get("evidence_level", 0)
            has_receipts = bool(data.get("receipts"))
            has_hash = bool(data.get("hash"))
            has_signature = bool(data.get("signature"))

            # Simple rule: Level 4+ should have receipts or strong provenance
            is_compliant = True
            issues = []

            if claimed_level >= 4 and not has_receipts:
                is_compliant = False
                issues.append("Claims Level 4+ but missing 'receipts' field")

            if claimed_level >= 6 and not (has_hash and has_signature):
                is_compliant = False
                issues.append("Claims Level 6+ but missing hash/signature")

            results.append({
                "file": str(artifact_path),
                "claimed_evidence_level": claimed_level,
                "claimed_name": EVIDENCE_LEVELS.get(claimed_level, "Unknown"),
                "compliant": is_compliant,
                "issues": issues,
                "has_receipts": has_receipts,
                "has_hash": has_hash,
                "has_signature": has_signature,
            })
        except Exception as e:
            results.append({
                "file": str(artifact_path),
                "error": str(e)
            })
    return results


def generate_init_report(base_path: Path) -> Dict:
    """Generate a comprehensive initialization status report."""
    report = {
        "timestamp": get_timestamp(),
        "lmc_version": LMC_VERSION,
        "base_path": str(base_path),
        "directory_validation": validate_directory_structure(base_path),
        "canon_metadata": load_canon_metadata(base_path),
        "evidence_compliance": [],
        "summary": {}
    }

    # Find JSON artifacts for evidence checking
    json_artifacts = list(base_path.rglob("*.json"))
    if json_artifacts:
        report["evidence_compliance"] = check_evidence_ladder_compliance(json_artifacts)

    # Summary
    dir_ok = all(report["directory_validation"].values())
    canon_ok = report["canon_metadata"] and not report["canon_metadata"].get("error")

    report["summary"] = {
        "directories_ok": dir_ok,
        "canon_loaded": canon_ok,
        "evidence_checks_performed": len(report["evidence_compliance"]),
        "evidence_violations": sum(
            1 for item in report["evidence_compliance"]
            if not item.get("compliant", True)
        ),
        "overall_status": "READY" if (dir_ok and canon_ok) else "NEEDS_ATTENTION"
    }

    return report


# =============================================================================
# MAIN CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="lmc-init — Labyrinth Master Canon Bootstrap Loader"
    )
    parser.add_argument(
        "--init", action="store_true",
        help="Initialize/validate the full LMC directory structure and canon"
    )
    parser.add_argument(
        "--validate", action="store_true",
        help="Run validation checks only (no changes)"
    )
    parser.add_argument(
        "--status", action="store_true",
        help="Print current status report"
    )
    parser.add_argument(
        "--base-path", type=Path, default=Path.cwd(),
        help="Base path of the LMC repository (default: current directory)"
    )
    parser.add_argument(
        "--output-report", type=Path,
        help="Write full JSON report to specified path"
    )

    args = parser.parse_args()

    base_path = args.base_path.resolve()

    if args.init or args.validate or args.status:
        print(f"[lmc-init] Labyrinth Master Canon Bootstrap Loader v{LMC_VERSION}")
        print(f"[lmc-init] Base path: {base_path}\n")

    if args.init:
        print("[lmc-init] Running full initialization and validation...")
        # In a real implementation, we could create missing directories here.
        # For safety, we only validate in this version.

    report = generate_init_report(base_path)

    if args.status or args.init or args.validate:
        print("=== LMC Status Report ===")
        print(f"Overall Status: {report['summary']['overall_status']}")
        print(f"Directories OK: {report['summary']['directories_ok']}")
        print(f"Canon Loaded:   {report['summary']['canon_loaded']}")
        print(f"Evidence Checks: {report['summary']['evidence_checks_performed']}")
        print(f"Evidence Violations: {report['summary']['evidence_violations']}")

        if report["evidence_compliance"]:
            print("\n--- Evidence Ladder Compliance Issues ---")
            for item in report["evidence_compliance"]:
                if not item.get("compliant", True):
                    print(f"  {item['file']}")
                    for issue in item.get("issues", []):
                        print(f"    - {issue}")

    if args.output_report:
        atomic_write_json(args.output_report, report)
        print(f"\n[ lmc-init ] Full report written to: {args.output_report}")

    if report["summary"]["overall_status"] != "READY":
        sys.exit(1)
    else:
        print("\n[lmc-init] Bootstrap complete. Environment is aligned with LMC v1.0.")


if __name__ == "__main__":
    main()