# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustermi(RPackage):
	"""Cluster Analysis with Missing Values by Multiple Imputation

	Allows clustering of incomplete observations by addressing missing values using multiple imputation. For achieving this goal, the methodology consists in three steps. 
    I) Missing data imputation using dedicated models. Four multiple imputation methods are proposed, two are based on joint modelling and two are fully sequential methods.
    II) cluster analysis of imputed data sets. Six clustering methods are available (distances-based or model-based), but custom methods can also be easily used.
    III) Partition pooling, The set of partitions is aggregated using Non-negative Matrix Factorization based method. An associated instability measure is computed by bootstrap. Among applications, this instability measure can be used to choose a number of clusters with missing values.
    The package also proposes several diagnostic tools to tune the number of imputed data sets, to tune the number of iterations in fully sequential imputation, to check the fit of imputation models, etc.
	"""
	
	cran = "clusterMI" 

	version("1.0.0", md5="ecc64eb36e73597a4b6702a8aea1be2a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-micemd", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mix", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-usedist", type=("build", "run"))
	depends_on("r-knockoff", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-dicer", type=("build", "run"))
	depends_on("r-npbayesimputecat", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-cat", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
