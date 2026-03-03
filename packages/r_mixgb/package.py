# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixgb(RPackage):
	"""Multiple Imputation Through 'XGBoost'

	Multiple imputation using 'XGBoost', subsampling, and predictive mean 
    matching as described in Deng and Lumley (2023) <arXiv:2106.01574>. Our
    method utilizes the capabilities of XGBoost, a highly efficient implementation
    of gradient boosted trees, to capture interactions and non-linear relations
    automatically. Moreover, we have integrated subsampling and predictive mean
    matching to minimize bias and reflect appropriate imputation variability. This
    package supports various types of variables and offers flexible settings for
    subsampling and predictive mean matching. Additionally, it includes diagnostic
    tools for evaluating the quality of the imputed values.
	"""
	
	homepage = "https://github.com/agnesdeng/mixgb"
	cran = "mixgb" 

	version("1.0.2", md5="ab30abfcce075b9f95ffcaadf59e9cd2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
