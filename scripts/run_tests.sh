#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "${ROOT}/reference/python"
PYTHONPATH=. python3 -m pytest tests/ -q