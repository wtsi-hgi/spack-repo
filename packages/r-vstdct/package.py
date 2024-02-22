# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVstdct(RPackage):
	"""Nonparametric Estimation of Toeplitz Covariance Matrices

	A nonparametric method to estimate Toeplitz covariance matrices from a sample of n independently and identically distributed p-dimensional vectors with mean zero. The data is preprocessed with the discrete cosine matrix and a variance stabilization transformation to obtain an approximate Gaussian regression setting for the log-spectral density function. Estimates of the spectral density function and the inverse of the covariance matrix are provided as well. Functions for simulating data and a protein data example are included. For details see (Klockmann, Krivobokova; 2023), <arXiv:2303.10018>.
	"""
	
	cran = "vstdct" 

	version("0.2", md5="0ce5d1660bb119b9c907bd021f21d4d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dtt", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
