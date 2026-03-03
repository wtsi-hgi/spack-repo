# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcfrailphdv(RPackage):
	"""Bivariate Correlated Frailty Models with Varied Variances

	Fit and simulate bivariate correlated frailty models with
    proportional hazard structure. Frailty distributions, such as gamma and
    lognormal models are supported for semiparametric procedures. Frailty variances of the two subjects 
    can be varied or equal. Details on the models are available in book of 
    Wienke (2011,ISBN:978-1-4200-7388-1). Bivariate gamma fit is obtained using the approach given 
    in Iachine (1995) with modifications. Lognormal fit is based on the approach
    by Ripatti and Palmgren (2000) <doi:10.1111/j.0006-341X.2000.01016.x>. Frailty distributions, 
    such as gamma, inverse gaussian and power variance frailty models are supported for parametric approach.
	"""
	
	cran = "bcfrailphdv" 

	version("0.1.1", md5="fe1253c4ced5fe35527d1ffcb6fa1a48")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-bcfrailph@0.1.1:", type=("build", "run"))
