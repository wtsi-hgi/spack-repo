# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFccac(RPackage):
    """functional Canonical Correlation Analysis to evaluate Covariance between nucleic acid sequencing datasets

    Computational evaluation of variability across DNA or RNA sequencing datasets is a crucial step in genomics, as it allows both to evaluate reproducibility of replicates, and to compare different datasets to identify potential correlations. fCCAC applies functional Canonical Correlation Analysis to allow the assessment of: (i) reproducibility of biological or technical replicates, analyzing their shared covariance in higher order components; and (ii) the associations between different datasets. fCCAC represents a more sophisticated approach that complements Pearson correlation of genomic coverage.
    """

    bioc = "fCCAC"

    version("1.34.0", commit="009c87b8ca140a09b3aefd47d858f257b6ac867e")
    version("1.28.0", commit="36ffa7199fc04b1cc21fec174efa63df6b4c6a5a")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-fda", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-genomation", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
