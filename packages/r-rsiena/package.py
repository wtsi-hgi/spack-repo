# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsiena(RPackage):
	"""Siena - Simulation Investigation for Empirical Network Analysis

	The main purpose of this package is to perform simulation-based
   estimation of stochastic actor-oriented models for longitudinal network
   data collected as panel data. Dependent variables can be single or
   multivariate networks, which can be directed, non-directed, or two-mode;
   and associated actor variables.
   There are also functions for testing parameters and checking goodness of fit.
   An overview of these models is given in Snijders (2017),
   <doi:10.1146/annurev-statistics-060116-054035>.
	"""
	
	homepage = "https://www.stats.ox.ac.uk/~snijders/siena/"
	cran = "RSiena" 

	version("1.4.7", md5="910574f5e0f2b852e72fc978ba4f6955")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
