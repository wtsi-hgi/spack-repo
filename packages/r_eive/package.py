# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REive(RPackage):
	"""An Algorithm for Reducing Errors-in-Variable Bias in Simple and
Multiple Linear Regressions

	Performs a compact genetic algorithm search to reduce errors-in-variables bias in linear regression. The algorithm estimates the regression parameters with lower biases and higher variances but mean-square errors (MSEs) are reduced.  
	"""
	
	cran = "eive" 

	version("3.1.3", md5="92e8ce505f7b69201d8a58b4e6d6084c")

	depends_on("r-rcpp", type=("build", "run"))
