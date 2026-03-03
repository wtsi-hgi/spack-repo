# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdamocca(RPackage):
	"""Model-Based Clustering for Functional Data with Covariates

	Routines for model-based functional cluster analysis for functional data with optional covariates. The idea is to cluster functional subjects (often called functional objects) into homogenous groups by using spline smoothers (for functional data) together with scalar covariates. The spline coefficients and the covariates are modelled as a multivariate Gaussian mixture model, where the number of mixtures corresponds to the number of clusters. The parameters of the model are estimated by maximizing the observed mixture likelihood via an EM algorithm (Arnqvist and Sjöstedt de Luna, 2019) <arXiv:1904.10265>. The clustering method is used to analyze annual lake sediment from lake Kassjön (Northern Sweden) which cover more than 6400 years and can be seen as historical records of weather and climate.
	"""
	
	cran = "fdaMocca" 

	version("0.1-1", md5="aa17dc8b517abd4e9ba0a5096dc7fea7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
