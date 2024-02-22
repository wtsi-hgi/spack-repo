# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIar(RPackage):
	"""Irregularly Observed Autoregressive Models

	Data sets, functions and scripts with examples to implement autoregressive models for irregularly observed time series. The models available in this package are the irregular autoregressive model (Eyheramendy et al.(2018) <doi:10.1093/mnras/sty2487>), the complex irregular autoregressive model (Elorrieta et al.(2019) <doi:10.1051/0004-6361/201935560>) and the bivariate irregular autoregressive model (Elorrieta et al.(2021) <doi:10.1093/mnras/stab1216>).
	"""
	
	homepage = "https://github.com/felipeelorrieta"
	cran = "iAR" 

	version("1.2.0", md5="7a4de71f91dda38d903fc310d2f400ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
