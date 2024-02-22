# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiqr(RPackage):
	"""An R Package for Single-Index Quantile Regression

	Single-Index Quantile Regression is effective in some scenarios. We provides functions that allow users to fit Single-Index Quantile Regression model. It also provides functions to do prediction, estimate standard errors of the single-index coefficients via bootstrap, and visualize the estimated univariate function. Please see W., Y., Y. (2010) <doi:10.1016/j.jmva.2010.02.003> for details.
	"""
	
	cran = "siqr" 

	version("0.8.1", md5="57ed3cfb4570deaf8c548630285a40e8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
