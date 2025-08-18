# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeal(RPackage):
    """Perform methylation analysis

    Package to integrate methylation and expression data. It can also perform methylation or expression analysis alone. Several plotting functionalities are included as well as a new region analysis based on redundancy analysis. Effect of SNPs on a region can also be estimated.
    """

    bioc = "MEAL"

    version("1.38.0", commit="e7b1934033bf4d95e284903f2019766379da49e0")
    version("1.32.0", commit="4d6f89b3cf4cee339137cbe9c5ef163b8ae63c8f")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-multidataset", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-minfi", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-ggplot2@2:", type=("build", "run"))
    depends_on("r-permute", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-missmethyl", type=("build", "run"))
    depends_on("r-isva", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-smartsva", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))

    def install_args(self, spec, prefix):
        """Speed up installation by skipping vignettes, manual, and test-load."""
        return [
            "--no-build-vignettes",
            "--no-manual",
            "--no-test-load",
        ]
