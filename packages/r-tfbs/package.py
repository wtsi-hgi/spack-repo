# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class RTfbs(Package):
    """Workflows, datasets, and helper scripts for transcription-factor motif and
    binding-site analysis published with the TFBS project."""

    homepage = "https://github.com/MariaOsmala/TFBS"
    url = "https://github.com/MariaOsmala/TFBS/archive/refs/tags/v1.0.0.tar.gz"
    git = "https://github.com/MariaOsmala/TFBS.git"

    maintainers("softpack-bot")
    license = "MIT"

    version("1.0.0", sha256="d748376f36016ed8a14d1be2560a40b7de794a2e3ef64467e5e124ad9aa1bb30")

    depends_on("r@4.2:", type=("build", "run"))
    with default_args(type=("build", "run")):
        depends_on("r-biocmanager")
        depends_on("r-data-table")
        depends_on("r-dplyr")
        depends_on("r-ggplot2")
        depends_on("r-ggrepel")
        depends_on("r-igraph")
        depends_on("r-magrittr")
        depends_on("r-openxlsx")
        depends_on("r-pheatmap")
        depends_on("r-readr")
        depends_on("r-stringr")
        depends_on("r-annotationhub")
        depends_on("r-biostrings")
        depends_on("r-genomicranges")
        depends_on("r-tfbstools")

    def install(self, spec, prefix):
        tfbs_dir = join_path(prefix.share, "tfbs")
        install_tree(".", tfbs_dir)

        code_dir = join_path(tfbs_dir, "RProjects", "TFBS", "code")
        mkdirp(prefix.bin)
        wrapper = join_path(prefix.bin, "tfbs-list-workflows")
        with open(wrapper, "w", encoding="utf-8") as fout:
            fout.write("#!/bin/bash\n")
            fout.write("set -euo pipefail\n")
            fout.write(f'CODE_DIR="{code_dir}"\n')
            fout.write('if [ ! -d "$CODE_DIR" ]; then\n')
            fout.write('  echo "TFBS code directory is missing: $CODE_DIR" >&2\n')
            fout.write("  exit 1\n")
            fout.write("fi\n")
            fout.write('ls "$CODE_DIR"\n')
        set_executable(wrapper)

    def setup_run_environment(self, env):
        env.set("R_TFBS_HOME", join_path(self.prefix.share, "tfbs"))

    @run_after("install")
    def install_test(self):
        tfbs_dir = join_path(self.prefix.share, "tfbs")
        list_workflows = join_path(self.prefix.bin, "tfbs-list-workflows")
        if not os.path.exists(list_workflows):
            raise InstallError("tfbs-list-workflows helper missing after install")
        with working_dir("spack-test", create=True):
            wf = Executable(list_workflows)
            wf()
