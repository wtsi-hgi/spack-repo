# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdci(RPackage):
	"""High Dimensional Confidence Interval Based on Lasso and
Bootstrap

	Fits regression models on high dimensional data to estimate coefficients and use bootstrap method to obtain confidence intervals. Choices for regression models are Lasso, Lasso+OLS, Lasso partial ridge, Lasso+OLS partial ridge. 
	"""
	
	cran = "HDCI" 

	version("1.0-2", md5="806dea67dc386f8782b82ad5172fb234")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
