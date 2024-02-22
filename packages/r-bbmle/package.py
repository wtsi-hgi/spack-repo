# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbmle(RPackage):
	"""Tools for General Maximum Likelihood Estimation

	Methods and functions for fitting maximum likelihood models in R. This package modifies and extends the 'mle' classes in the 'stats4' package.
	"""
	
	homepage = "https://github.com/bbolker/bbmle"
	cran = "bbmle" 

	version("1.0.25.1", md5="73de3800a92640884c5db0e85724cdd3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-bdsmatrix", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
