# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdspecest(RPackage):
	"""An Analysis Toolbox for Hermitian Positive Definite Matrices

	An implementation of data analysis tools for samples of symmetric or 
  Hermitian positive definite matrices, such as collections of covariance matrices 
  or spectral density matrices. The tools in this package can be used to perform: (i) 
  intrinsic wavelet transforms for curves (1D) or surfaces (2D) of Hermitian positive 
  definite matrices with applications to dimension reduction, denoising and clustering in the 
  space of Hermitian positive definite matrices; and (ii) exploratory data analysis and inference 
  for samples of positive definite matrices by means of intrinsic data depth functions and 
  rank-based hypothesis tests in the space of Hermitian positive definite matrices.
	"""
	
	homepage = "https://github.com/JorisChau/pdSpecEst"
	cran = "pdSpecEst" 

	version("1.2.4", md5="bd7c6e5a2cd4bbbd6b13f1a57d3c3b46")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-multitaper", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ddalpha", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.500:", type=("build", "run"))
