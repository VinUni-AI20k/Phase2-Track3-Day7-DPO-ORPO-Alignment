#!/usr/bin/env bash
set -euo pipefail
pref-lab validate data/sample_preferences.jsonl
pref-lab evaluate --config configs/local.yaml
cat outputs/metrics.json
