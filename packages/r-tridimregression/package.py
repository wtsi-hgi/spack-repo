# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTridimregression(RPackage):
	"""Bayesian Statistics for 2D/3D Transformations

	Fits 2D and 3D geometric transformations via 'Stan' probabilistic programming engine ( 
    Stan Development Team (2021) <https://mc-stan.org>). Returns posterior distribution for individual
    parameters of the fitted distribution. Allows for computation of LOO and WAIC information criteria 
    (Vehtari A, Gelman A, Gabry J (2017) <doi:10.1007/s11222-016-9696-4>) as well as Bayesian R-squared
    (Gelman A, Goodrich B, Gabry J, and Vehtari A (2018) <doi:10.1080/00031305.2018.1549100>).
	"""
	
	homepage = "https://github.com/alexander-pastukhov/tridim-regression"
	cran = "TriDimRegression" 

	version("1.0.2", md5="cbe2af051f4d9928d044383131a9ae2b")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-rstantool", type=("build", "link", "run"))
