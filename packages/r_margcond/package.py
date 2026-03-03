# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMargcond(RPackage):
	"""Joint Marginal-Conditional Model

	Fits joint marginal conditional models for multivariate longitudinal data, as in Proudfoot, Faig, Natarajan, and Xu (2018) <doi:10.1002/sim.7552>. Development of this package was supported by the UCSD Altman Translational Research Institute, NIH grant UL1TR001442. The content is solely the responsibility of the authors and does not necessarily represent the official views of the NIH.
	"""
	
	cran = "MargCond" 

	version("1.0.0", md5="4e942d55fd9eaf2899fd61700e11ff2e")

	depends_on("r-gee", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
