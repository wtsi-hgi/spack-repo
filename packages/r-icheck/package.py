# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcheck(RPackage):
    """QC Pipeline and Data Analysis Tools for High-Dimensional Illumina mRNA Expression Data

    QC pipeline and data analysis tools for high-dimensional Illumina mRNA expression data.
    """

    bioc = "iCheck"

    version("1.38.0", commit="09ca7e4fde482e5fa660520b4d311fde4460d5d7")
    version("1.32.0", commit="17bf4a8f67b5267555733384b3124c391b7d0638")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-lumi", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-preprocesscore", type=("build", "run"))
    depends_on("r-randomforest", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-geneselectmmd", type=("build", "run"))
    depends_on("r-rgl", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-lmtest", type=("build", "run"))
    depends_on("r-scatterplot3d", type=("build", "run"))
