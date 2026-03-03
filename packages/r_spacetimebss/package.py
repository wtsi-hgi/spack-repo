# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacetimebss(RPackage):
	"""Blind Source Separation for Multivariate Spatio-Temporal Data

	Simultaneous/joint diagonalization of local autocovariance matrices to estimate spatio-temporally uncorrelated random fields. 
	"""
	
	cran = "SpaceTimeBSS" 

	version("0.3-0", md5="5a75afd07cfc90a4a8fe82fde1063515")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jade", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
