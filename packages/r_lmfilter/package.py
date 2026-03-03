# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmfilter(RPackage):
	"""Filter Methods for Parameter Estimation in Linear and Non Linear
Regression Models

	We present a method based on filtering algorithms to estimate the parameters of linear, i.e. the coefficients and the variance of the error term. The proposed algorithms make use of Particle Filters following Ristic, B., Arulampalam, S., Gordon, N. (2004, ISBN: 158053631X) resampling methods. Parameters of logistic regression models are also estimated using an evolutionary particle filter method.
	"""
	
	cran = "LMfilteR" 

	version("0.1.3.1", md5="2ef26fcc1838dbc3dd1da4b3765639a3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass@7.3.50:", type=("build", "run"))
