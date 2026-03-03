# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsabcv(RPackage):
	"""Estimate Number of Latent Factors and Factor Matrix for Factor
Analysis

	These functions estimate the latent factors of a given matrix, no matter it is high-dimensional or not. It tries to first estimate the number of factors using bi-cross-validation and then estimate the latent factor matrix and the noise variances. For more information about the method, see Art B. Owen and Jingshu Wang 2015 archived article on factor model (<arXiv:1503.03515>). 
	"""
	
	cran = "esaBcv" 

	version("1.2.1.1", md5="07a9cb9fec4dd2d63916e07bee864516")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-svd", type=("build", "run"))
