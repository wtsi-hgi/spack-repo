# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgscidca(RPackage):
	"""Plotting Decision Curve Analysis with Coloured Bars

	Decision curve analysis is a method for evaluating and comparing prediction models that incorporates clinical consequences, requires only the data set on which the models are tested, and can be applied to models that have either continuous or dichotomous results. The 'ggscidca' package adds coloured bars of discriminant relevance to the traditional decision curve. Improved practicality and aesthetics. This method was described by Balachandran VP (2015) <doi:10.1016/S1470-2045(14)71116-7>.
	"""
	
	cran = "ggscidca" 

	version("0.1.9", md5="fd55cc8936916dcb825f9dd3eeb955b5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
