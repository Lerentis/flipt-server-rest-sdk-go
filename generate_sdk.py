#!/usr/bin/env python3
"""
Script to download Flipt OpenAPI specification and generate Go SDK.
"""

import os
import sys
import subprocess
import urllib.request
from pathlib import Path

# Configuration
OPENAPI_SPEC_URL = "https://raw.githubusercontent.com/flipt-io/flipt/main/openapi.yaml"
OPENAPI_SPEC_FILE = "openapi.yaml"
OUTPUT_DIR = "generated"
PACKAGE_NAME = "flipt"

def download_openapi_spec():
    """Download the OpenAPI specification from GitHub."""
    print(f"Downloading OpenAPI spec from {OPENAPI_SPEC_URL}...")
    try:
        urllib.request.urlretrieve(OPENAPI_SPEC_URL, OPENAPI_SPEC_FILE)
        print(f"✓ Downloaded to {OPENAPI_SPEC_FILE}")
        return True
    except Exception as e:
        print(f"✗ Error downloading OpenAPI spec: {e}", file=sys.stderr)
        return False

def check_openapi_generator():
    """Check if openapi-generator is available."""
    try:
        result = subprocess.run(
            ["openapi-generator", "version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print(f"✓ openapi-generator is available")
            return True
        else:
            print("✗ openapi-generator returned an error", file=sys.stderr)
            return False
    except FileNotFoundError:
        print("✗ openapi-generator not found", file=sys.stderr)
        print("\nPlease install openapi-generator:", file=sys.stderr)
        print("  npm install -g @openapitools/openapi-generator", file=sys.stderr)
        print("  or")
        print("  brew install openapi-generator", file=sys.stderr)
        return False
    except Exception as e:
        print(f"✗ Error checking openapi-generator: {e}", file=sys.stderr)
        return False

def generate_go_sdk():
    """Generate Go SDK using openapi-generator."""
    print(f"\nGenerating Go SDK...")
    print(f"  Input: {OPENAPI_SPEC_FILE}")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"  Package: {PACKAGE_NAME}")
    
    # Create output directory if it doesn't exist
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    
    try:
        cmd = [
            "openapi-generator",
            "generate",
            "-i", OPENAPI_SPEC_FILE,
            "-g", "go",
            "-o", OUTPUT_DIR,
            "--package-name", PACKAGE_NAME,
            "--git-user-id", "lerentis",
            "--git-repo-id", "flipt-server-rest-sdk-go",
        ]
        
        print(f"\nRunning: {' '.join(cmd)}")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✓ SDK generated successfully!")
            print(f"\nGenerated files are in: {OUTPUT_DIR}/")
            return True
        else:
            print("✗ SDK generation failed", file=sys.stderr)
            print(result.stdout)
            print(result.stderr, file=sys.stderr)
            return False
    except Exception as e:
        print(f"✗ Error generating SDK: {e}", file=sys.stderr)
        return False

def main():
    """Main execution flow."""
    print("=" * 60)
    print("Flipt Go SDK Generator")
    print("=" * 60)
    print()
    
    # Step 1: Check if openapi-generator is available
    if not check_openapi_generator():
        sys.exit(1)
    
    # Step 2: Download OpenAPI spec
    if not download_openapi_spec():
        sys.exit(1)
    
    # Step 3: Generate Go SDK
    if not generate_go_sdk():
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ All steps completed successfully!")
    print("=" * 60)
    print(f"\nNext steps:")
    print(f"  cd {OUTPUT_DIR}")
    print(f"  go mod init github.com/lerentis/flipt-server-rest-sdk-go/generated")
    print(f"  go mod tidy")

if __name__ == "__main__":
    main()
