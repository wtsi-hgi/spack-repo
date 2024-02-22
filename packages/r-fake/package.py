# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFake(RPackage):
	"""Flexible Data Simulation Using the Multivariate Normal
Distribution

	This R package can be used to generate artificial data conditionally on pre-specified (simulated or user-defined) relationships between the variables and/or observations. Each observation is drawn from a multivariate Normal distribution where the mean vector and covariance matrix reflect the desired relationships. Outputs can be used to evaluate the performances of variable selection, graphical modelling, or clustering approaches by comparing the true and estimated structures (B Bodinier et al (2021) <arXiv:2106.02521>).
	"""
	
	cran = "fake" 

	version("1.4.0", md5="f5072985304b79134ceec0f5e9f2c448")

	depends_on("r-huge", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-withr@2.4:", type=("build", "run"))
