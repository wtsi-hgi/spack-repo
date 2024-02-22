# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightr(RPackage):
	"""Estimating Weight-Function Models for Publication Bias

	Estimates the Vevea and Hedges (1995)
    weight-function model. By specifying arguments, users can
    also estimate the modified model described in Vevea and Woods (2005), 
    which may be more practical with small datasets. Users 
    can also specify moderators to estimate a linear model. 
    The package functionality allows users to easily extract the 
    results of these analyses as R objects for other uses. In addition, 
    the package includes a function to launch both models as 
    a Shiny application. Although the Shiny application is also available online, 
    this function allows users to launch it locally if they choose.
	"""
	
	homepage = "http://faculty.ucmerced.edu/jvevea/"
	cran = "weightr" 

	version("2.0.2", md5="4df4fd360c5b7919bad6323ae71c4c9b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
