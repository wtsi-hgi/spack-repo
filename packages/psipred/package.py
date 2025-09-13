# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class Psipred(Package):
    """"""

    homepage = "https://github.com/psipred/psipred"
    url = "https://github.com/psipred/psipred/archive/refs/tags/v4.0.tar.gz"

    version("4.0", sha256="ce4c901c8f152f6e93e4f70dc8079a5432fc64d02bcc0215893e33fbacb1fed2")

    # Scripts are shell/perl/tcsh; ensure tcsh and BLAST+ present at runtime
    depends_on("perl", type=("run"))
    depends_on("tcsh", type=("run"))
    depends_on("blast-plus~python", type=("run"))

    def patch(self):
        filter_file("../bin", self.prefix.bin, "src/Makefile", string=True)

    def install(self, spec, prefix):
        # Build core binaries
        cd("src")
        make()
        mkdir(prefix.bin)
        make("install")

        # Install data and scripts if present in the source tree
        with working_dir(self.stage.source_path):
            if os.path.isdir("data"):
                install_tree("data", join_path(prefix, "share", "psipred", "data"))
            # Top-level driver scripts
            for script_name in ["runpsipred", "runpsipred_single"]:
                if os.path.exists(script_name):
                    install(script_name, prefix.bin)
            # BLAST+ pipeline script
            blast_script = join_path("BLAST+", "runpsipredplus")
            if os.path.exists(blast_script):
                install(blast_script, prefix.bin)

        # Symlink common driver scripts into bin if available
        # Ensure scripts are executable
        for script_name in ["runpsipred", "runpsipred_single", "runpsipredplus"]:
            script_path = join_path(prefix.bin, script_name)
            if os.path.exists(script_path):
                chmod = which("chmod")
                chmod("+x", script_path)
                # Normalize tcsh shebang to env for portability in Spack envs
                filter_file(r"^#!/bin/tcsh", "#!/usr/bin/env tcsh", script_path)
                # Point execdir/datadir to Spack prefixes and prefer psiblast from PATH
                filter_file(r"^set execdir = .*", f"set execdir = {prefix.bin}", script_path)
                filter_file(r"^set datadir = .*", f"set datadir = {join_path(prefix, 'share', 'psipred', 'data')}", script_path)
                filter_file(r"^set ncbidir = .*", "set ncbidir = ", script_path)
                filter_file(r"\$ncbidir/psiblast", "psiblast", script_path)
                filter_file(r"\$ncbidir/blastpgp", "psiblast", script_path)
                # Allow DB override via env var PSIPRED_DB with fallback
                filter_file(
                    r"^set dbname = .*$",
                    "set dbname = uniref90filt\nif ( $?PSIPRED_DB ) set dbname = \"$PSIPRED_DB\"",
                    script_path,
                )

        # Wrap the raw psipred binary so FASTA inputs are routed via runpsipredplus
        psipred_bin = join_path(prefix.bin, "psipred")
        if os.path.exists(psipred_bin):
            move(psipred_bin, join_path(prefix.bin, "psipred.real"))
            wrapper = join_path(prefix.bin, "psipred")
            with open(wrapper, "w") as f:
                f.write("""#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 1 ]]; then
  exec "$(dirname "$0")/psipred.real" "$@"
fi
in="$1"
ext="${in##*.}"
if [[ -f "$in" && "$ext" != "mtx" ]]; then
  if command -v runpsipredplus >/dev/null 2>&1; then
    exec runpsipredplus "$in"
  elif [[ -x "$(dirname "$0")/runpsipredplus" ]]; then
    exec "$(dirname "$0")/runpsipredplus" "$in"
  elif command -v runpsipred >/dev/null 2>&1; then
    exec runpsipred "$in"
  elif [[ -x "$(dirname "$0")/runpsipred" ]]; then
    exec "$(dirname "$0")/runpsipred" "$in"
  else
    echo "psipred wrapper: runpsipred(plus) not found. Ensure scripts are installed." >&2
    exit 127
  fi
else
  exec "$(dirname "$0")/psipred.real" "$@"
fi
""")
            chmod = which("chmod")
            chmod("+x", wrapper)

    def setup_run_environment(self, env):
        data_dir = join_path(self.prefix, "share", "psipred", "data")
        env.set("PSIPRED", str(self.prefix))
        env.set("PSIPRED_DATA", data_dir)
        if "blast-plus" in self.spec:
            env.prepend_path("PATH", join_path(self.spec["blast-plus"].prefix, "bin"))
