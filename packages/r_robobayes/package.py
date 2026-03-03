# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobobayes(RPackage):
	"""Robust Online Bayesian Monitoring

	An implementation of Bayesian online changepoint detection (Adams and MacKay (2007) <arXiv:0710.3742>) with an option for probability based outlier detection and removal (Wendelberger et. al. (2021) <arXiv:2112.12899>). Building on the independent multivariate constant mean model implemented in the 'R' package 'ocp', this package models multivariate data as multivariate normal about a linear trend, defined by user input covariates, with an unstructured error covariance. Changepoints are identified based on a probability threshold for windows of points.
	"""
	
	cran = "roboBayes" 

	version("1.2", md5="0a299d232113d6a18ba117ab2d661bfd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
