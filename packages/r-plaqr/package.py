# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlaqr(RPackage):
	"""Partially Linear Additive Quantile Regression

	Estimation, prediction, thresholding, transformation, and plotting for partially linear additive quantile regression.  Intuitive functions for fitting and plotting partially linear additive quantile regression models.  Uses and works with functions from the 'quantreg' package.
	"""
	
	cran = "plaqr" 

	version("2.0", md5="53129f59211b7feff11a8d98d01f77c1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
