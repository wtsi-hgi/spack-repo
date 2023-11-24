# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDimsum(RPackage):
    """An error model and pipeline for analyzing deep mutational scanning (DMS) data and diagnosing common experimental pathologies."""

    homepage = "https://github.com/lehner-lab/DiMSum"
    git = "https://github.com/lehner-lab/DiMSum"

    version("1.3", tag="v1.3")

    depends_on("fastqc@0.11.9")
    depends_on("vsearch@2.22.1")
    depends_on("starcode@1.4 cppflags='-fcommon'")
    depends_on("zlib")

    depends_on("py-cutadapt@2.4")

    depends_on("r+X", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-shortread", type=("build", "run"))
    depends_on("r-cairo", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggally", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-hexbin", type=("build", "run"))
    depends_on("r-optparse", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-seqinr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
