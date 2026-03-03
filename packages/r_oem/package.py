# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROem(RPackage):
	"""Orthogonalizing EM: Penalized Regression for Big Tall Data

	Solves penalized least squares problems for big tall data
    using the orthogonalizing EM algorithm of Xiong et al. (2016) 
    <doi:10.1080/00401706.2015.1054436>. The main fitting function is oem() and the
    functions cv.oem() and xval.oem() are for cross validation, the latter being an
    accelerated cross validation function for linear models. The big.oem() function
    allows for out of memory fitting. A description of the underlying methods and 
    code interface is described in Huling and Chien (2022) <doi:10.18637/jss.v104.i06>.
	"""
	
	homepage = "https://arxiv.org/abs/1801.09661"
	cran = "oem" 

	version("2.0.11", md5="e4514d440ed7b3b11efc84488e6d0e96")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
