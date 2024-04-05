# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVars(RPackage):
	"""VAR Modelling

	Estimation, lag selection, diagnostic testing, forecasting, causality analysis, forecast error variance decomposition and impulse response functions of VAR models and estimation of SVAR and SVEC models.
	"""
	
	homepage = "https://www.pfaffikus.de"
	cran = "vars" 

	version("1.6-1", md5="70ca3ea1e66aad07f561358439f0e471")
	version("1.6-0", md5="90863e2458c69f74b8a8bef5c9f75905")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-urca@1.1.6:", type=("build", "run"))
	depends_on("r-lmtest@0.9.26:", type=("build", "run"))
	depends_on("r-sandwich@2.2.4:", type=("build", "run"))
