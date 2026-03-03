# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimereg(RPackage):
	"""Flexible Regression Models for Survival Data

	Programs for Martinussen and Scheike (2006), `Dynamic Regression
    Models for Survival Data', Springer Verlag.  Plus more recent developments.
    Additive survival model, semiparametric proportional odds model, fast
    cumulative residuals, excess risk models and more. Flexible competing risks
    regression including GOF-tests. Two-stage frailty modelling. PLS for the
    additive risk model. Lasso in the 'ahaz' package.
	"""
	
	homepage = "https://github.com/scheike/timereg"
	cran = "timereg" 

	version("2.0.5", md5="858ff28934de6315828ee526e3c9e3e8")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-lava", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
