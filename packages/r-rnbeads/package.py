# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeads(RPackage):
    """RnBeads

    RnBeads facilitates comprehensive analysis of various types of DNA methylation data at the genome scale.
    """

    bioc = "RnBeads"

    version("2.26.0", commit="9d24193bbcad0395d51b28db38395f439849d2d4")
    version("2.20.0", commit="26222aa384e0ff18b60ca10e85ee35bb62d2e9d5")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-ff", type=("build", "run"))
    depends_on("r-fields", type=("build", "run"))
    depends_on("r-ggplot2@0.9.2:", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-illuminaio", type=("build", "run"))
    depends_on("r-methylumi", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
