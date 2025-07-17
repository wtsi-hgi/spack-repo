# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchot(RPackage):
    """single-cell higher order testing

    Single cell Higher Order Testing (scHOT) is an R package that facilitates testing changes in higher order structure of gene expression along either a developmental trajectory or across space. scHOT is general and modular in nature, can be run in multiple data contexts such as along a continuous trajectory, between discrete groups, and over spatial orientations; as well as accommodate any higher order measurement such as variability or correlation. scHOT meaningfully adds to first order effect testing, such as differential expression, and provides a framework for interrogating higher order interactions from single cell data.
    """

    bioc = "scHOT"

    version("1.20.1", commit="37387ece147b3e54bdde4e5a26c9e742e1f29237")
    version("1.14.0", commit="7445339eb1637d9cf90524bb68032aa0c4f24fc4")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-s4vectors@0.24.3:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-ggforce", type=("build", "run"))
