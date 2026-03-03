# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapechange(RPackage):
	"""Change-Point Estimation using Shape-Restricted Splines

	In a scatterplot where the response variable is Gaussian, Poisson or binomial, we consider the case in which the mean function is smooth with a change-point, which is a mode, an inflection point or a jump point. The main routine estimates the mean curve and the change-point as well using shape-restricted B-splines. An optional subroutine delivering a bootstrap confidence interval for the change-point is incorporated in the main routine. 
	"""
	
	cran = "ShapeChange" 

	version("1.5", md5="667257c4eca5ef08dd5dd43e72d6e7ac")

	depends_on("r-coneproj@1.11:", type=("build", "run"))
	depends_on("r-quadprog@1.5.5:", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
