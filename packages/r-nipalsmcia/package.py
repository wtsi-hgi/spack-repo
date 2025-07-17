# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNipalsmcia(RPackage):
    """Multiple Co-Inertia Analysis via the NIPALS Method

    Computes Multiple Co-Inertia Analysis (MCIA), a dimensionality reduction (jDR) algorithm, for a multi-block dataset using a modification to the Nonlinear Iterative Partial Least Squares method (NIPALS) proposed in (Hanafi et. al, 2010). Allows multiple options for row- and table-level preprocessing, and speeds up computation of variance explained. Vignettes detail application to bulk- and single cell- multi-omics studies.
    """

    homepage = "https://github.com/Muunraker/nipalsMCIA"
    bioc = "nipalsMCIA"

    version("1.6.0", commit="24050e84fee82f4cad648bc09d14b5f8d917a169")
    version("1.0.0", commit="70dd4bf19fec20576906c66de8d1c7ae3f64a01b")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-fgsea", type=("build", "run"))
    depends_on("r-ggplot2@3:", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-pracma", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rspectra", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
