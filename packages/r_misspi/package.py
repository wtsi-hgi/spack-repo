# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisspi(RPackage):
	"""Missing Value Imputation in Parallel

	A framework that boosts the imputation of 'missForest' by Stekhoven, D.J. and Bühlmann, P. (2012) <doi:10.1093/bioinformatics/btr597> by harnessing parallel processing and through the fast Gradient Boosted Decision Trees (GBDT) implementation 'LightGBM' by Ke, Guolin et al.(2017) <https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision>. 'misspi' has the following main advantages:
             1. Allows embrassingly parallel imputation on large scale data.
             2. Accepts a variety of machine learning models as methods with friendly user portal.
             3. Supports multiple initializations methods.
             4. Supports early stopping that prohibits unnecessary iterations.
	"""
	
	cran = "misspi" 

	version("0.1.0", md5="6acbf485e0eb4dc97b7a11fb89ade18d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lightgbm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-sis", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
