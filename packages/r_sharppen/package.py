# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharppen(RPackage):
	"""Penalized Data Sharpening for Local Polynomial Regression

	Functions and data sets for data sharpening.
    Nonparametric regressions are computed subject to smoothness
    and other kinds of penalties. 
	"""
	
	cran = "sharpPen" 

	version("1.9", md5="6fdac4656dfabdcd4bbc8db3dffc78df")

	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
