# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcfrailph(RPackage):
	"""Semiparametric Bivariate Correlated Frailty Models Fit

	Fit and simulate a semiparametric bivariate correlated frailty models with proportional 
    hazard structure. Frailty distributions, such as gamma and lognormal models are 
    supported. Bivariate gamma fit is obtained using the approach given in Iachine (1995) and 
    lognormal fit is based on the approach by 
    Ripatti and Palmgren (2000) <doi:10.1111/j.0006-341X.2000.01016.x>.
	"""
	
	cran = "bcfrailph" 

	version("0.1.1", md5="c77e01de4012cf25f1b3bd7cf9a9c97d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
