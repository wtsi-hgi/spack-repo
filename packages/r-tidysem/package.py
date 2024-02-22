# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidysem(RPackage):
	"""Tidy Structural Equation Modeling

	A tidy workflow for generating, estimating, reporting,
    and plotting structural equation models using 'lavaan', 'OpenMx', or
    'Mplus'. Throughout this workflow, elements of syntax, results, and graphs
    are represented as 'tidy' data, making them easy to customize.
    Includes functionality to estimate latent class analyses.
	"""
	
	homepage = "https://cjvanlissa.github.io/tidySEM/"
	cran = "tidySEM" 

	version("0.2.6", md5="384d61803e874353ce4c8f3556b0b528")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-openmx", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-blavaan", type=("build", "run"))
	depends_on("r-mplusautomation", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-bain", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-nonnest2@0.5.6:", type=("build", "run"))
