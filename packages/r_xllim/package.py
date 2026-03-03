# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXllim(RPackage):
	"""High Dimensional Locally-Linear Mapping

	Provides a tool for non linear mapping (non linear regression) using a mixture of regression model and an inverse regression strategy. The methods include the GLLiM model (see Deleforge et al (2015) <DOI:10.1007/s11222-014-9461-5>) based on Gaussian mixtures and a robust version of GLLiM, named SLLiM (see Perthame et al (2016) <DOI:10.1016/j.jmva.2017.09.009>) based on a mixture of Generalized Student distributions. The methods also include BLLiM (see Devijver et al (2017) <arXiv:1701.07899>) which is an extension of GLLiM with a sparse block diagonal structure for large covariance matrices (particularly interesting for transcriptomic data).
	"""
	
	cran = "xLLiM" 

	version("2.3", md5="b6a6ed5c55ecf78d1e55587884c6f756")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-capushe", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mda", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
