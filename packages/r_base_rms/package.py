# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaseRms(RPackage):
	"""Convert Regression Between Base Function and 'rms' Package

	
  We perform linear, logistic, and cox regression using the base functions lm(), 
    glm(), and coxph() in the R software and the 'survival' package. Likewise, we 
    can use ols(), lrm() and cph() from the 'rms' package for the same 
    functionality. Each of these two sets of commands has a different focus.
  In many cases, we need to use both sets of commands in the same situation, 
    e.g. we need to filter the full subset model using AIC, and we need to build 
    a visualization graph for the final model. 'base.rms' package can help you to switch 
    between the two sets of commands easily.
	"""
	
	cran = "base.rms" 

	version("1.0", md5="3f4f81b6ba6f400a71fa4330d764f2bd")

	depends_on("r-rms", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-do", type=("build", "run"))
