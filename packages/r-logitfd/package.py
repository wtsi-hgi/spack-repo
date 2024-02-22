# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogitfd(RPackage):
	"""Functional Principal Components Logistic Regression

	Functions for fitting a functional principal components logit regression model
	in four different situations: ordinary and filtered functional principal components
	of functional predictors, included in the model according to their variability
	explanation power, and according to their prediction ability by stepwise methods. The
	proposed methods were developed in Escabias et al (2004) 
	<doi:10.1080/10485250310001624738> and Escabias et al (2005)
	<doi:10.1016/j.csda.2005.03.011>.
	"""
	
	cran = "logitFD" 

	version("1.0", md5="67585256c4eb3ffba6758984db3086d5")

	depends_on("r@3.4.3:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
