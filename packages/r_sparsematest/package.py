# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsematest(RPackage):
	"""Sparse Matrix Estimation and Inference

	The 'sparseMatEst' package provides functions for estimating sparse 
  covariance and precision matrices with error control. A false positive
  rate is fixed corresponding to the probability of falsely including a matrix 
  entry in the support of the estimator.  It uses the binary search
  method outlined in Kashlak and Kong (2019) <arXiv:1705.02679> and in 
  Kashlak (2019) <arXiv:1903.10988>.
	"""
	
	cran = "sparseMatEst" 

	version("1.0.0", md5="b1b0f85b06fcb86df2bf5d5e6c81f75c")

	depends_on("r-glasso", type=("build", "run"))
