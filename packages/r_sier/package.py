# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSier(RPackage):
	"""Signal Extraction Approach for Sparse Multivariate Response
Regression

	Methods for regression with high-dimensional predictors and  univariate or maltivariate response variables. It considers the decomposition of the coefficient matrix that leads to the best approximation to the signal part in the response given any rank, and estimates the decomposition by solving a penalized generalized eigenvalue problem followed by a least squares procedure. Ruiyan Luo and Xin Qi (2017) <doi:10.1016/j.jmva.2016.09.005>.
	"""
	
	cran = "SiER" 

	version("0.1.0", md5="a2908a934b39cb64a2ad50acbe964b1d")

