# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowerly(RPackage):
	"""Sample Size Analysis for Psychological Networks and More

	An implementation of the sample size computation method for network
    models proposed by Constantin et al. (2021) <doi:10.31234/osf.io/j5v7u>.
    The implementation takes the form of a three-step recursive algorithm
    designed to find an optimal sample size given a model specification and a
    performance measure of interest. It starts with a Monte Carlo simulation
    step for computing the performance measure and a statistic at various sample
    sizes selected from an initial sample size range. It continues with a
    monotone curve-fitting step for interpolating the statistic across the entire
    sample size range. The final step employs stratified bootstrapping to quantify
    the uncertainty around the fitted curve.
	"""
	
	homepage = "https://powerly.dev"
	cran = "powerly" 

	version("1.8.6", md5="42ee55e07053f4ea9dc3df35fcf81ad1")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-bootnet", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
