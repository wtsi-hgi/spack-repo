# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrajectoryutils(RPackage):
    """Single-Cell Trajectory Analysis Utilities

    Implements low-level utilities for single-cell trajectory analysis, primarily intended for re-use inside higher-level packages. Include a function to create a cluster-level minimum spanning tree and data structures to hold pseudotime inference results.
    """

    homepage = "https://bioconductor.org/packages/TrajectoryUtils"
    bioc = "TrajectoryUtils"

    version("1.16.1", commit="a488c624fd20dc775fd12a978779094b2d360efc")
    version("1.10.1", commit="5d8634e9465afe386bb23b5e6b12d383d4035556")

    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
