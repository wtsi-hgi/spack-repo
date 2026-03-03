# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMidasr(RPackage):
	"""Mixed Data Sampling Regression

	Methods and tools for mixed frequency time series data analysis.
    Allows estimation, model selection and forecasting for MIDAS regressions.
	"""
	
	homepage = "http://mpiktas.github.io/midasr/"
	cran = "midasr" 

	version("0.8", md5="30b2d933da41eff5464785eedbd5ec97")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
