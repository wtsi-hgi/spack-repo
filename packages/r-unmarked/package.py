# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnmarked(RPackage):
	"""Models for Data from Unmarked Animals

	Fits hierarchical models of animal abundance and occurrence to data collected using survey methods such as point counts, site occupancy sampling, distance sampling, removal sampling, and double observer sampling. Parameters governing the state and observation processes can be modeled as functions of covariates. References: Kellner et al. (2023) <doi:10.1111/2041-210X.14123>, Fiske and Chandler (2011) <doi:10.18637/jss.v043.i10>.
	"""
	
	homepage = "https://groups.google.com/d/forum/unmarked"
	cran = "unmarked" 

	version("1.4.1", md5="343693936f09376153abcf8e71036f6c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
