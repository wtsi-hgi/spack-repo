# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcebayes(RPackage):
	"""Optimal Bayesian Experimental Design using the ACE Algorithm

	Optimal Bayesian experimental design using the approximate coordinate exchange (ACE) algorithm. See <doi:10.18637/jss.v095.i13>.
	"""
	
	cran = "acebayes" 

	version("1.10", md5="3c0bc4f2709e54ac4c1813fc3cf5143f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-compare", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.100.5:", type=("build", "run"))
