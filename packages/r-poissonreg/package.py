# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoissonreg(RPackage):
	"""Model Wrappers for Poisson Regression

	Bindings for Poisson regression models for use with the
    'parsnip' package. Models include simple generalized linear models,
    Bayesian models, and zero-inflated Poisson models (Zeileis, Kleiber,
    and Jackman (2008) <doi:10.18637/jss.v027.i08>).
	"""
	
	homepage = "https://github.com/tidymodels/poissonreg"
	cran = "poissonreg" 

	version("1.0.1", md5="d9a1c0e4b16c40b7f5281d7449333e41")

	depends_on("r-parsnip@0.2:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
