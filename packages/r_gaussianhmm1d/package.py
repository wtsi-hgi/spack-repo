# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaussianhmm1d(RPackage):
	"""Inference, Goodness-of-Fit and Forecast for Univariate Gaussian
Hidden Markov Models

	Inference, goodness-of-fit test, and prediction densities and intervals for univariate Gaussian Hidden Markov Models (HMM). The goodness-of-fit is based on a Cramer-von Mises statistic and uses parametric bootstrap to estimate the p-value. The description of the methodology is taken from Chapter 10.2 of Remillard (2013) <doi:10.1201/b14285>.
	"""
	
	cran = "GaussianHMM1d" 

	version("1.1.1", md5="a8c72f6e58fbfcd73caa492db9076ac5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
