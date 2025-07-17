# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerfect(RPackage):
    """Permutation filtration for microbiome data

    PERFect is a novel permutation filtering approach designed to address two unsolved problems in microbiome data processing: (i) define and quantify loss due to filtering by implementing thresholds, and (ii) introduce and evaluate a permutation test for filtering loss to provide a measure of excessive filtering.
    """

    homepage = "https://github.com/cxquy91/PERFect"
    bioc = "PERFect"

    version("1.16.0", commit="c173a08766677c9e79f43c8fbffbaa653278d19c")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-sn@1.5.2:", type=("build", "run"))
    depends_on("r-ggplot2@3:", type=("build", "run"))
    depends_on("r-phyloseq@1.28:", type=("build", "run"))
    depends_on("r-zoo@1.8.3:", type=("build", "run"))
    depends_on("r-psych@1.8.4:", type=("build", "run"))
    depends_on("r-matrix@1.2.14:", type=("build", "run"))
    depends_on("r-fitdistrplus@1.0.12:", type=("build", "run"))
