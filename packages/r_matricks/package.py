# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatricks(RPackage):
	"""Useful Tricks for Matrix Manipulation

	Provides functions, which make matrix creation conciser 
             (such as the core package's function m() for rowwise matrix definition or 
             runifm() for random value matrices).
             Allows to set multiple matrix values at once, by using list of formulae. 
             Provides additional matrix operators and dedicated plotting function.
	"""
	
	homepage = "https://github.com/krzjoa/matricks"
	cran = "matricks" 

	version("0.8.2", md5="ff57d9009dd31fbacd775e69b7da0961")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
