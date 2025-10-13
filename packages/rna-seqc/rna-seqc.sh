#!/bin/sh

# Wrapper script for RNA-SeQC. The Spack recipe replaces
# the 'java' binary path and the jar placeholder below.

java -jar RNA-SeQC_v{0}.jar "$@"

