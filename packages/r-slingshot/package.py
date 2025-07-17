# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlingshot(RPackage):
    """Tools for ordering single-cell sequencing

    Provides functions for inferring continuous, branching lineage structures in low-dimensional data. Slingshot was designed to model developmental trajectories in single-cell RNA sequencing data and serve as a component in an analysis pipeline after dimensionality reduction and clustering. It is flexible enough to handle arbitrarily many branching events and allows for the incorporation of prior knowledge through supervised graph construction.
    """

    bioc = "slingshot"

    version("2.16.0", commit="79e32b097a569f95a39de689b22b6acb4c06eee0")
    version("2.10.0", commit="9166218b81ee53237b209e9185eafd13fb0bcaf4")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-princurve@2.0.4:", type=("build", "run"))
    depends_on("r-trajectoryutils", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
