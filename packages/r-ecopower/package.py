# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcopower(RPackage):
	"""Power Estimates and Equivalence Testing for Multivariate Data

	Estimates power by simulation for multivariate
    abundance data to be used for sample size estimates. Multivariate
    equivalence testing by simulation from a Gaussian copula model.
    The package also provides functions for parameterising multivariate effect
    sizes and simulating multivariate abundance data jointly. The discrete
    Gaussian copula approach is described in
    Popovic et al. (2018) <doi:10.1016/j.jmva.2017.12.002>.
	"""
	
	cran = "ecopower" 

	version("0.2.0", md5="68194ba2ca563c6d8e57e2eb6989f6d6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvabund", type=("build", "run"))
	depends_on("r-ecocopula", type=("build", "run"))
