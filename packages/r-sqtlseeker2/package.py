# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqtlseeker2(RPackage):
    """Splicing QTL mapping workflow.

    Provides functions and visualizations used by the sQTLseekeR2 workflow for
    splicing QTL discovery and downstream analyses.
    """

    homepage = "https://github.com/guigolab/sQTLseekeR2"
    git = "https://github.com/guigolab/sQTLseekeR2.git"

    license("GPL-3.0-only", "LICENSE")

    version(
        "1.1.0",
        sha256="f0ad02957796fc177e3aad3543f4d9979ef833724347ba7866671fdb37122da6",
        url="https://github.com/guigolab/sQTLseekeR2/archive/refs/tags/v1.1.0.tar.gz",
    )

    depends_on("r@3.3.2:", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-qvalue", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
    depends_on("r-permute", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-compquadform", type=("build", "run"))
    depends_on("r-fitdistrplus", type=("build", "run"))
    depends_on("r-car", type=("build", "run"))
