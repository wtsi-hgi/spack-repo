# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpsp(RPackage):
	"""Selection by Partitioning the Solution Paths

	An implementation of the feature Selection procedure by Partitioning the entire Solution Paths
            (namely SPSP) to identify the relevant features rather than using a single tuning parameter. 
            By utilizing the entire solution paths, this procedure can obtain better selection accuracy than 
            the commonly used approach of selecting only one tuning parameter based on existing criteria, 
            cross-validation (CV), generalized CV, AIC, BIC, and extended BIC (Liu, Y., & Wang, P. (2018) 
            <doi:10.1214/18-EJS1434>). It is more stable and accurate (low false positive and 
            false negative rates) than other variable selection approaches. In addition, it can be flexibly 
            coupled with the solution paths of Lasso, adaptive Lasso, ridge regression, and other penalized 
            estimators.
	"""
	
	homepage = "https://xiaorui.site/SPSP/"
	cran = "SPSP" 

	version("0.2.0", md5="6fb21343e796323a11eeb1e994b1311e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
