# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnlinepca(RPackage):
	"""Online Principal Component Analysis

	Online PCA for multivariate and functional data using perturbation methods, low-rank incremental methods, and stochastic optimization methods. 
	"""
	
	homepage = "https://cran.r-project.org/package=onlinePCA"
	cran = "onlinePCA" 

	version("1.3.2", md5="083ff354912f9925e026e04997ad27ea")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
