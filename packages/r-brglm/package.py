# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrglm(RPackage):
	"""Bias Reduction in Binomial-Response Generalized Linear Models

	Fit generalized linear models with binomial responses using either an adjusted-score approach to bias reduction or maximum penalized likelihood where penalization is by Jeffreys invariant prior. These procedures return estimates with improved frequentist properties (bias, mean squared error) that are always finite even in cases where the maximum likelihood estimates are infinite (data separation). Fitting takes place by fitting generalized linear models on iteratively updated pseudo-data. The interface is essentially the same as 'glm'.  More flexibility is provided by the fact that custom pseudo-data representations can be specified and used for model fitting. Functions are provided for the construction of confidence intervals for the reduced-bias estimates.
	"""
	
	homepage = "https://github.com/ikosmidis/brglm"
	cran = "brglm" 

	version("0.7.2", md5="ce9f9e9381b460f9e170ddd1370776cb")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-profilemodel", type=("build", "run"))
