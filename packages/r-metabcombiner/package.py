# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabcombiner(RPackage):
    """Method for Combining LC-MS Metabolomics Feature Measurements

    This package aligns LC-HRMS metabolomics datasets acquired from biologically similar specimens analyzed under similar, but not necessarily identical, conditions. Peak-picked and simply aligned metabolomics feature tables (consisting of m/z, rt, and per-sample abundance measurements, plus optional identifiers & adduct annotations) are accepted as input. The package outputs a combined table of feature pair alignments, organized into groups of similar m/z, and ranked by a similarity score. Input tables are assumed to be acquired using similar (but not necessarily identical) analytical methods.
    """

    bioc = "metabCombiner"

    version("1.18.0", commit="46cac36ca0d54b931f5ed3366d799d30360ac029")
    version("1.12.0", commit="f842d785d353dfa7e0157fe6e6a38fbcc23ef9e6")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-dplyr@1:", type=("build", "run"))
    depends_on("r-mgcv", type=("build", "run"))
    depends_on("r-caret", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
