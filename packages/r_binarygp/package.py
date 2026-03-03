# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinarygp(RPackage):
	"""Fit and Predict a Gaussian Process Model with (Time-Series)
Binary Response

	Allows the estimation and prediction for binary Gaussian process model. The mean function can be assumed to have time-series structure. The estimation methods for the unknown parameters are based on penalized quasi-likelihood/penalized quasi-partial likelihood and restricted maximum likelihood. The predicted probability and its confidence interval are computed by Metropolis-Hastings algorithm. More details can be seen in Sung et al (2017) <arXiv:1705.02511>.
	"""
	
	cran = "binaryGP" 

	version("0.2", md5="f91ce9224ddd236843f9e1b86cce29b6")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lhs@0.10:", type=("build", "run"))
	depends_on("r-logitnorm@0.8.29:", type=("build", "run"))
	depends_on("r-nloptr@1.0.4:", type=("build", "run"))
	depends_on("r-gpfit@1.0.0:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
