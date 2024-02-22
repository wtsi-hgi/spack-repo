# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXrf(RPackage):
	"""eXtreme RuleFit

	An implementation of the RuleFit algorithm as described in Friedman & Popescu 
  (2008) <doi:10.1214/07-AOAS148>. eXtreme Gradient Boosting ('XGBoost') is used 
  to build rules, and 'glmnet' is used to fit a sparse linear model on the raw and rule features. The result
  is a model that learns similarly to a tree ensemble, while often offering improved interpretability
  and achieving improved scoring runtime in live applications. Several algorithms for
  reducing rule complexity are provided, most notably hyperrectangle de-overlapping. All algorithms scale to 
  several million rows and support sparse representations to handle tens of thousands of dimensions.
	"""
	
	homepage = "https://github.com/holub008/xrf"
	cran = "xrf" 

	version("0.2.2", md5="b0cfc72f00c987f3b07ae7913ddfa95a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet@3:", type=("build", "run"))
	depends_on("r-xgboost@0.71.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fuzzyjoin", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
