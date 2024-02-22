# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegrEasy(RPackage):
	"""Easy Linear, Quadratic and Cubic Regression Models

	Focused on linear, quadratic and cubic regression models, it has a function for calculating the models, obtaining a list with their parameters, and a function for making the graphs for the respective models.
	"""
	
	cran = "regr.easy" 

	version("1.0.2", md5="e2f7208c47e61b348b6363ba18ccad88")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stargazer", type=("build", "run"))
