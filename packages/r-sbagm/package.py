# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbagm(RPackage):
	"""Search Best ARIMA, GARCH, and MS-GARCH Model

	Get the most appropriate autoregressive integrated moving average, generalized auto-regressive conditional heteroscedasticity and Markov switching GARCH model. For method details see Haas M, Mittnik S, Paolella MS (2004). <doi:10.1093/jjfinec/nbh020>, Bollerslev T (1986). <doi:10.1016/0304-4076(86)90063-1>.
	"""
	
	cran = "SBAGM" 

	version("0.1.0", md5="01845109de6fd4c796c76800704858bb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-msgarch", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
