# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtrafrail(RPackage):
	"""Estimation and Additional Tools for Alternative Shared Frailty
Models

	Provide estimation and data generation tools for some new multivariate frailty models.
             This version includes the gamma, inverse Gaussian, weighted Lindley, Birnbaum-Saunders,
	     truncated normal and mixture of inverse Gaussian as the distribution for the frailty terms. 
             For the basal model, it is considered a parametric approach based on the exponential, 
             Weibull and the piecewise exponential distributions as well as a semiparametric approach. 
             For details, see Gallardo and Bourguignon (2022) <arXiv:2206.12973>.
	"""
	
	cran = "extrafrail" 

	version("1.9", md5="ebe70599e66cbb6b2b21af019cd6af0a")
	version("1.8", md5="d60164c8f02c11036f12fbd4f099318f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-expint", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
