# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustcov(RPackage):
	"""Collection of Robust Covariance and (Sparse) Precision Matrix
Estimators

	Collection of methods for robust covariance and (sparse) precision matrix estimation based on Loh and Tan (2018) <doi:10.1214/18-EJS1427>. 
	"""
	
	cran = "robustcov" 

	version("0.1", md5="e6360a34a0f79978aecef4527b5488cf")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
