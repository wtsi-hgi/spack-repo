# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongevity(RPackage):
	"""Statistical Methods for the Analysis of Excess Lifetimes

	A collection of parametric and nonparametric methods for the analysis of survival data. Parametric families implemented include Gompertz-Makeham, exponential and generalized Pareto models and extended models. The package includes an implementation of the nonparametric maximum likelihood estimator for arbitrary truncation and censoring pattern based on Turnbull (1976) <doi:10.1111/j.2517-6161.1976.tb01597.x>, along with graphical goodness-of-fit diagnostics. Parametric models for positive random variables and peaks over threshold models based on extreme value theory are described in Rootzén and Zholud (2017) <doi:10.1007/s10687-017-0305-5>; Belzile et al. (2021) <doi:10.1098/rsos.202097> and Belzile et al. (2022) <doi:10.1146/annurev-statistics-040120-025426>.
	"""
	
	homepage = "https://lbelzile.github.io/longevity/"
	cran = "longevity" 

	version("1.0.0", md5="06ec013bd8cf05f5ffdacfb134f72999")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
