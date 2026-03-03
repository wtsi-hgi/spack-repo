# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigvar(RPackage):
	"""Dimension Reduction Methods for Multivariate Time Series

	Estimates VAR and VARX models with Structured Penalties using the methods developed by Nicholson et al (2017)<doi:10.1016/j.ijforecast.2017.01.003> and Nicholson et al (2020) <doi:10.48550/arXiv.1412.5250>.
	"""
	
	homepage = "https://github.com/wbnicholson/BigVAR"
	cran = "BigVAR" 

	version("1.1.2", md5="00d47eeff4a4b88820604cb1b682c5c9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
