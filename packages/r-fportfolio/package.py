# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFportfolio(RPackage):
	"""Rmetrics - Portfolio Selection and Optimization

	A collection of functions to optimize portfolios and to analyze them from different points of view.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/rmetrics/"
	cran = "fPortfolio" 

	version("4023.84", md5="7a382ac5a4345110975c7243c9c29083")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-fassets", type=("build", "run"))
	depends_on("r-fcopulae", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-rneos", type=("build", "run"))
