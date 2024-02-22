# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexrsurv(RPackage):
	"""Flexible Relative Survival Analysis

	Package for parametric relative survival analyses. It allows to model non-linear and 
        non-proportional effects and both non proportional and non linear effects, using splines (B-spline and truncated power basis), Weighted Cumulative Index of Exposure effect, with correction model for 
        the life table. Both non proportional and non linear effects are described in 
			Remontet, L. et al. (2007) <doi:10.1002/sim.2656> and 
			Mahboubi, A. et al. (2011) <doi:10.1002/sim.4208>. 
	"""
	
	cran = "flexrsurv" 

	version("2.0.18", md5="38e2a1c6df51a1e97cdf43dc51cc64fe")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-orthogonalsplinebasis", type=("build", "run"))
	depends_on("r-epi", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
