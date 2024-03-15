# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqpen(RPackage):
	"""Penalized Quantile Regression

	Performs penalized quantile regression with LASSO, elastic net, SCAD and MCP penalty functions including group penalties. Provides a function that automatically generates lambdas and evaluates different models with cross validation or BIC, including a large p version of BIC. Below URL provides a link to a work in progress vignette. 
	"""
	
	homepage = "https://github.com/bssherwood/rqpen/blob/master/ignore/rqPenArticle.pdf"
	cran = "rqPen" 

	version("3.2.2", md5="b4bcd4813968c38d4d77b113f1ce180d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-hqreg", type=("build", "run"))
	depends_on("r-hrqglas", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
