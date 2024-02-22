# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStopes(RPackage):
	"""Selection Threshold Optimized Empirically via Splitting

	Implements variable selection procedures for low to moderate size generalized linear regressions models. It includes the STOPES functions for linear regression (Capanu M, Giurcanu M, Begg C, Gonen M, Optimized variable selection via repeated data splitting, Statistics in Medicine, 2020, 19(6):2167-2184) as well as subsampling based optimization methods for generalized linear regression models (Marinela Capanu, Mihai Giurcanu, Colin B Begg, Mithat Gonen, Subsampling based variable selection for generalized linear models).
	"""
	
	cran = "STOPES" 

	version("0.2", md5="70ad442aafa79d65480536370d59d19b")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
