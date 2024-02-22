# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInlajoint(RPackage):
	"""Multivariate Joint Modeling for Longitudinal and Time-to-Event
Outcomes with 'INLA'

	Estimation of joint models for multivariate longitudinal markers (with various distributions available) and survival outcomes (possibly accounting for competing risks) with Integrated Nested Laplace Approximations (INLA). The flexible and user friendly function joint() facilitates the use of the fast and reliable inference technique implemented in the 'INLA' package for joint modeling. More details are given in the help page of the joint() function (accessible via ?joint in the R console) and the vignette associated to the joint() function (accessible via vignette("INLAjoint") in the R console).
	"""
	
	homepage = "https://github.com/DenisRustand/INLAjoint"
	cran = "INLAjoint" 

	version("24.2.4", md5="651f36a990a46f7558afed2d0ccd0bb7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
