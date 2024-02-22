# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinsegrcpp(RPackage):
	"""Efficient Implementation of Binary Segmentation

	Standard template library 
 containers are used to implement an efficient binary segmentation
 algorithm, which is log-linear on average and quadratic in the
 worst case.
	"""
	
	homepage = "https://github.com/tdhock/binsegRcpp"
	cran = "binsegRcpp" 

	version("2023.8.31", md5="9807932f9cb024985f3e2a2b7d5c8476")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
