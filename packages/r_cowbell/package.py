# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCowbell(RPackage):
	"""Performs Segmented Linear Regression on Two Independent
Variables

	Implements a specific form of segmented linear regression
    with two independent variables. The visualization of that function looks 
    like a quarter segment of a cowbell giving the package its name. 
    The package has been specifically constructed for the case where minimum 
    and maximum value of the dependent and two independent variables 
    are known a prior, which is usually the case
    when those values are derived from Likert scales.
	"""
	
	cran = "cowbell" 

	version("0.1.0", md5="171acea6d12800dccd8bbfc07347e97d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
