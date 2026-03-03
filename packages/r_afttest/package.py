# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfttest(RPackage):
	"""Model Diagnostics for Accelerated Failure Time Models

	A collection of model checking methods for semiparametric accelerated 
    failure time (AFT) models under the rank-based approach. For the (computational)
    efficiency, Gehan's weight is used. It provides functions to verify whether the 
    observed data fit the specific model assumptions such as a functional form of 
    each covariate, a link function, and an omnibus test. The p-value offered in this 
    package is based on the Kolmogorov-type supremum test and the variance of the 
    proposed test statistics is estimated through the re-sampling method. Furthermore, 
    a graphical technique to compare the shape of the observed residual to a number of 
    the approximated realizations is provided.
	"""
	
	homepage = "https://github.com/WooJungBae/afttest"
	cran = "afttest" 

	version("4.3.2.3", md5="fb06d8978dc4e29058b9c928ce9d056b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-aftgee", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
