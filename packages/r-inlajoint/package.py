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

	version("24.3.25", md5="2232e2b8e21b476b7b58b398d733ad0a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
