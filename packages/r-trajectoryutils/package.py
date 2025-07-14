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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TrajectoryUtils_1.10.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TrajectoryUtils/TrajectoryUtils_1.10.1.tar.gz"]

    version("1.16.1", tag="RELEASE_3_21")
	version("1.10.1", sha256="a7d184ed827ae8f32de6e830ff0dfe65f6f04f1749c2338ba6314d66412e1b9d")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
