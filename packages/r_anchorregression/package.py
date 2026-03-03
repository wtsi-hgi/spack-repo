# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnchorregression(RPackage):
	"""Perform AnchorRegression

	Performs AnchorRegression proposed by Rothenhäusler et al. 2020. 
    The code is adapted from the original paper repository. (<https://github.com/rothenhaeusler/anchor-regression>)
    The code was developed independently from the authors of the paper. 
	"""
	
	homepage = "https://github.com/simzim96/AnchorRegression"
	cran = "AnchorRegression" 

	version("0.1.3", md5="75eac0615df7270cb25bdc394eaf3594")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-glmnet@1.4:", type=("build", "run"))
	depends_on("r-selectiveinference@1:", type=("build", "run"))
	depends_on("r-mgcv@1:", type=("build", "run"))
