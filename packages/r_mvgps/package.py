# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvgps(RPackage):
	"""Causal Inference using Multivariate Generalized Propensity Score

	
    Methods for estimating and utilizing the multivariate generalized
    propensity score (mvGPS) for multiple continuous exposures described in
    Williams, J.R, and Crespi, C.M. (2020) <arxiv:2008.13767>. The methods allow
    estimation of a dose-response surface relating the joint distribution of multiple
    continuous exposure variables to an outcome. Weights are constructed assuming a
    multivariate normal density for the marginal and conditional distribution of
    exposures given a set of confounders. Confounders can be different for different
    exposure variables. The weights are designed to achieve balance across all
    exposure dimensions and can be used to estimate dose-response surfaces.
	"""
	
	homepage = "https://github.com/williazo/mvGPS"
	cran = "mvGPS" 

	version("1.2.2", md5="c217b832f03d86a2e6009c07f018e7d2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-weightit", type=("build", "run"))
	depends_on("r-cobalt", type=("build", "run"))
	depends_on("r-matrixnormal", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-cbps", type=("build", "run"))
