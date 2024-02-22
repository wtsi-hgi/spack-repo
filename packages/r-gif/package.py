# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGif(RPackage):
	"""Graphical Independence Filtering

	Provides a method of recovering the precision matrix for Gaussian graphical models efficiently. Our approach could be divided into three categories. First of all, we use Hard Graphical Thresholding for best subset selection problem of Gaussian graphical model, and the core concept of this method was proposed by Luo et al. (2014) <arXiv:1407.7819>. Secondly, a closed form solution for graphical lasso under acyclic graph structure is implemented in our package (Fattahi and Sojoudi (2019) <https://jmlr.org/papers/v20/17-501.html>). Furthermore, we implement block coordinate descent algorithm to efficiently solve the covariance selection problem (Dempster (1972) <doi:10.2307/2528966>). Our package is computationally efficient and can solve ultra-high-dimensional problems, e.g. p > 10,000, in a few minutes.
	"""
	
	cran = "gif" 

	version("0.1.1", md5="47cf13a3affec3df48e0b0877dc0fc33")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
