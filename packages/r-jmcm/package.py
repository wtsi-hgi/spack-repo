# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmcm(RPackage):
	"""Joint Mean-Covariance Models using 'Armadillo' and S4

	Fit joint mean-covariance models for longitudinal data. The models
    and their components are represented using S4 classes and methods. The core
    computational algorithms are implemented using the 'Armadillo' C++ library
    for numerical linear algebra and 'RcppArmadillo' glue.
	"""
	
	homepage = "https://github.com/ypan1988/jmcm/"
	cran = "jmcm" 

	version("0.2.4", md5="b47c9aac273b5320b43520405d42a62d")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.900.1:", type=("build", "run"))
	depends_on("r-roptim", type=("build", "run"))
