# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvydiags(RPackage):
	"""Linear Regression Model Diagnostics for Survey Data

	Diagnostics for fixed effects linear regression models fitted with survey data. Extensions of standard diagnostics to complex survey data are included: standardized residuals, leverages, Cook's D, dfbetas, dffits, condition indexes, and variance inflation factors as found in Li and Valliant (Surv. Meth., 2009, 35(1), pp. 15-24; Jnl. of Off. Stat., 2011, 27(1), pp. 99-119; Jnl. of Off. Stat., 2015, 31(1), pp. 61-75); Liao and Valliant (Surv. Meth., 2012, 38(1), pp. 53-62; Surv. Meth., 2012, 38(2), pp. 189-202).  Variance inflation factors are also computed for some general linear models (logistic and poisson) as described in Liao (U. Maryland thesis, 2010).
	"""
	
	cran = "svydiags" 

	version("0.5", md5="158afab7da4cb1bbbd6036b24134b428")
	version("0.4", md5="2984861f18507247ba871c4c909c7d59")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
