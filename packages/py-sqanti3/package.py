# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PySqanti3(Package):
    """SQANTI3 performs quality control, filtering, and rescue analyses for
    long-read transcriptomes."""

    homepage = "https://github.com/ConesaLab/SQANTI3"
    url = "https://github.com/ConesaLab/SQANTI3/archive/refs/tags/v6.0.tar.gz"

    license("GPL-3.0-only")

    version("6.0", sha256="7703da9acca51150d4e1ab9def8bf1cd37e507a760a9a5259b9cd9b8be1fd3fa")

    # Python runtime stack
    depends_on("python@3.11:3.11", type=("build", "run"))
    depends_on("py-argcomplete@3:", type=("build", "run"))
    depends_on("py-argh@0.26.2:", type=("build", "run"))
    depends_on("py-bcbio-gff@0.7:", type=("build", "run"))
    depends_on("py-biopython@1.81:", type=("build", "run"))
    depends_on("py-bx-python@0.10:", type=("build", "run"))
    depends_on("py-cython@3:", type="build")
    depends_on("py-dill@0.3.6:", type=("build", "run"))
    depends_on("py-edlib@1.3.9:", type=("build", "run"))
    depends_on("py-gffutils@0.10:", type=("build", "run"))
    depends_on("py-gtfparse@2.5:", type=("build", "run"))
    depends_on("py-gtftools@0.9.0", type=("build", "run"))
    depends_on("py-importlib-metadata@6:", type=("build", "run"))
    depends_on("py-intervaltree@3.1:", type=("build", "run"))
    depends_on("py-jinja2@3.1:", type=("build", "run"))
    depends_on("py-numpy@1.26:1", type=("build", "run"))
    depends_on("py-pandas@2.2:", type=("build", "run"))
    depends_on("py-parasail@1.3:", type=("build", "run"))
    depends_on("py-pdf2image@1.16:", type=("build", "run"))
    depends_on("py-polars@0.20.31", type=("build", "run"))
    depends_on("py-pyarrow@10.0.1:", type=("build", "run"))
    depends_on("py-pybedtools@0.10:", type=("build", "run"))
    depends_on("py-pyfaidx@0.8:", type=("build", "run"))
    depends_on("py-pysam@0.22:", type=("build", "run"))
    depends_on("py-psutil@6:", type=("build", "run"))
    depends_on("py-pyyaml@6:", type=("build", "run"))
    depends_on("py-scikit-learn@1.5:", type=("build", "run"))
    depends_on("py-scipy@1.11:1.11", type=("build", "run"))
    depends_on("py-seaborn@0.13:", type=("build", "run"))
    depends_on("py-simplejson@3.19:", type=("build", "run"))
    depends_on("py-sortedcontainers@2.4:", type=("build", "run"))
    depends_on("py-td2@1.0:", type=("build", "run"))
    depends_on("py-ultra-bioinformatics@0.1:", type=("build", "run"))
    depends_on("py-zipp@3.17:", type=("build", "run"))

    # External tools and libraries
    depends_on("bedtools2@2.31:", type="run")
    depends_on("desalt@1.5:", type="run")
    depends_on("gffread@0.12:", type="run")
    depends_on("gmap-gsnap", type="run")
    depends_on("kallisto@0.48:", type="run")
    depends_on("minimap2@2.26:", type="run")
    depends_on("namfinder@0.1.3:", type="run")
    depends_on("openssl@3:", type="run")
    depends_on("pandoc@3:", type="run")
    depends_on("perl@5.32:", type="run")
    depends_on("samtools@1.21:", type="run")
    depends_on("seqtk@1.4:", type="run")
    depends_on("star@2.7.11b:", type="run")

    # R stack for reporting
    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-biocmanager@1.30:", type=("build", "run"))
    depends_on("r-busparse@1.16:", type=("build", "run"))
    depends_on("r-caret@6.0:", type=("build", "run"))
    depends_on("r-devtools@2.4:", type=("build", "run"))
    depends_on("r-dplyr@1.1:", type=("build", "run"))
    depends_on("r-dt@0.32:", type=("build", "run"))
    depends_on("r-e1071@1.7:", type=("build", "run"))
    depends_on("r-forcats@1.0:", type=("build", "run"))
    depends_on("r-ggplot2@3.4:", type=("build", "run"))
    depends_on("r-ggplotify@0.1:", type=("build", "run"))
    depends_on("r-gridbase@0.4:", type=("build", "run"))
    depends_on("r-gridextra@2.3:", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-htmltools@0.5:", type=("build", "run"))
    depends_on("r-jsonlite@1.8:", type=("build", "run"))
    depends_on("r-noiseq@2.46:", type=("build", "run"))
    depends_on("r-optparse@1.7:", type=("build", "run"))
    depends_on("r-plotly@4.10:", type=("build", "run"))
    depends_on("r-plyr@1.8:", type=("build", "run"))
    depends_on("r-purrr@1.0:", type=("build", "run"))
    depends_on("r-randomforest@4.7:", type=("build", "run"))
    depends_on("r-rmarkdown@2.26:", type=("build", "run"))
    depends_on("r-readr@2.1:", type=("build", "run"))
    depends_on("r-reshape@0.8:", type=("build", "run"))
    depends_on("r-scales@1.3:", type=("build", "run"))
    depends_on("r-stringi@1.8:", type=("build", "run"))
    depends_on("r-stringr@1.5:", type=("build", "run"))
    depends_on("r-tibble@3.2:", type=("build", "run"))
    depends_on("r-tidyr@1.3:", type=("build", "run"))

    def install(self, spec, prefix):
        install_tree(".", prefix.libexec)

        scripts = [
            "sqanti3",
            "sqanti3_qc.py",
            "sqanti3_filter.py",
            "sqanti3_rescue.py",
            "sqanti3_reads.py",
        ]

        python_exe = spec["python"].command.path
        mkdirp(prefix.bin)

        for script in scripts:
            script_src = join_path(prefix.libexec, script)
            if not os.path.exists(script_src):
                continue

            wrapper_path = join_path(prefix.bin, script)
            with open(wrapper_path, "w", encoding="utf-8") as wrapper:
                wrapper.write("#!/bin/bash\n")
                wrapper.write("set -euo pipefail\n")
                wrapper.write(f'export SQANTI3_HOME="{prefix.libexec}"\n')
                wrapper.write(f'export PYTHONPATH="{prefix.libexec}:${{PYTHONPATH:-}}"\n')
                wrapper.write(f'exec {python_exe} "{script_src}" "$@"\n')
            os.chmod(wrapper_path, 0o755)

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", self.prefix.libexec)
        env.set("SQANTI3_HOME", self.prefix.libexec)

    @run_after("install")
    def install_test(self):
        python = self.spec["python"].command
        env = os.environ.copy()
        env["SQANTI3_HOME"] = str(self.prefix.libexec)
        existing = env.get("PYTHONPATH", "")
        env["PYTHONPATH"] = (
            f"{self.prefix.libexec}:{existing}" if existing else str(self.prefix.libexec)
        )
        python("-c", "import sqanti3_qc", env=env)
