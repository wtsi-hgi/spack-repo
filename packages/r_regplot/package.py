# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegplot(RPackage):
	"""Enhanced Regression Nomogram Plot

	A function to plot a regression nomogram of regression 
    objects. Covariate distributions are superimposed on nomogram scales and the plot
	can be animated to allow on-the-fly changes to distribution representation and to 
	enable outcome calculation. 
	"""
	
	cran = "regplot" 

	version("1.1", md5="6e4ec74056048f73d1829961bbb37add")

	depends_on("r-vioplot", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
	depends_on("r-beanplot", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
