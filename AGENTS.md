## Failure Reason Summariser

This guide instructs the AI to perform one simple task per package.

### Task
- Read the provided install log for the specified Python package (built via Spack).
- the install log will always mention another log file in /tmp under `See build log for details:`, make sure you read that file to find the actual reason. A reason such as `uv pip install failure` is not a good reason, you should find the actual reason from the other log file.
- Produce a concise, one-sentence summary of the root cause of the installation failure.

### Input
- Package name (string)
- Install log text (string)

### Output
- Return only strict JSON with the following keys:
  - `package`: the package name
  - `failure_reason`: a short sentence (≤ 25 words) describing the primary cause of failure
  - `lowest_r_version`: the lowest R version that can be used to install the package (optional, only fill in if the error is related to R version)

### Requirements
- Be specific: missing system library, version conflict, network/SSL, compiler error, incompatible wheel, wrong import name, checksum mismatch, etc.
- Do not include build steps or long stack traces in the summary.
- If there is clearly no failure in the log, set `failure_reason` to `No failure detected in log`.
- Output must be JSON only. No extra commentary or formatting.
