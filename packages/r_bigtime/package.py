# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigtime(RPackage):
	"""Sparse Estimation of Large Time Series Models

	Estimation of large Vector AutoRegressive (VAR), Vector AutoRegressive with Exogenous Variables X (VARX) and Vector AutoRegressive Moving Average (VARMA) Models with Structured Lasso Penalties, see Nicholson, Wilms, Bien and Matteson (2020) <https://jmlr.org/papers/v21/19-777.html> and Wilms, Basu, Bien and Matteson (2021) <doi:10.1080/01621459.2021.1942013>.
	"""
	
	homepage = "https://github.com/ineswilms/bigtime"
	cran = "bigtime" 

	version("0.2.3", md5="2109d31bfd709950be81915af63d180a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
