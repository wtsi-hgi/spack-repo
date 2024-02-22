# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRockchalk(RPackage):
	"""Regression Estimation and Presentation

	A collection of functions for interpretation and presentation
    of regression analysis.  These functions are used
    to produce the statistics lectures in
    <https://pj.freefaculty.org/guides/>. Includes regression
    diagnostics, regression tables, and plots of interactions and
    "moderator" variables. The emphasis is on "mean-centered" and
    "residual-centered" predictors. The vignette 'rockchalk' offers a
    fairly comprehensive overview.  The vignette 'Rstyle' has advice
    about coding in R.  The package title 'rockchalk' refers to our
    school motto, 'Rock Chalk Jayhawk, Go K.U.'.
	"""
	
	cran = "rockchalk" 

	version("1.8.157", md5="232fc6d92a779b539c84f0b894ec9a72")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-cardata", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-kutils", type=("build", "run"))
