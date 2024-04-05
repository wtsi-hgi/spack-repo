# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlnmodels(RPackage):
	"""Poisson Lognormal Models

	The Poisson-lognormal model and variants (Chiquet, Mariadassou and Robin, 
    2021 <doi:10.3389/fevo.2021.588292>) can be used for 
    a variety of multivariate problems when count data are at play, including 
    principal component analysis for count data, discriminant analysis, model-based clustering and 
    network inference. Implements variational algorithms to fit such models accompanied with a set of 
    functions for visualization and diagnostic. 
	"""
	
	homepage = "https://pln-team.github.io/PLNmodels/"
	cran = "PLNmodels" 

	version("1.2.0", md5="aafbc099db10212c0b79703856568d33")
	version("1.1.0", md5="2a2232c3c46e9614e1e5a9546517f190")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-glassofast", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
