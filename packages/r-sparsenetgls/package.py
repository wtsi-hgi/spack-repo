# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsenetgls(RPackage):
	"""Using Gaussian graphical structue learning estimation in generalized least squared regression for multivariate normal regression

	The package provides methods of combining the graph structure learning and generalized least squares regression to improve the regression estimation. The main function sparsenetgls() provides solutions for multivariate regression with Gaussian distributed dependant variables and explanatory variables utlizing multiple well-known graph structure learning approaches to estimating the precision matrix, and uses a penalized variance covariance matrix with a distance tuning parameter of the graph structure in deriving the sandwich estimators in generalized least squares (gls) regression. This package also provides functions for assessing a Gaussian graphical model which uses the penalized approach. It uses Receiver Operative Characteristics curve as a visualization tool in the assessment.
	"""
	
	bioc = "sparsenetgls" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sparsenetgls_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sparsenetgls/sparsenetgls_1.20.0.tar.gz"]

	version("1.20.0", sha256="b5f0f2fd12c48386213553e55d1bb130cfeb5bcc30d77228787cefd8126090f2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
