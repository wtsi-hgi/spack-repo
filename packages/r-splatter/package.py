# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplatter(RPackage):
	"""Simple Simulation of Single-cell RNA Sequencing Data

	Splatter is a package for the simulation of single-cell RNA sequencing count data. It provides a simple interface for creating complex simulations that are reproducible and well-documented. Parameters can be estimated from real data and functions are provided for comparing real and simulated datasets.
	"""
	
	homepage = "https://github.com/Oshlack/splatter"
	bioc = "splatter"

	version("1.32.0", commit="0097e05a80918714edd2e92837c82378e56bc6ba")
	version("1.26.0", commit="07e5c7deddb2fc1eb9c3d55befa19b2e650492bd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
