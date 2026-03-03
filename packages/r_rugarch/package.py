# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRugarch(RPackage):
	"""Univariate GARCH Models

	ARFIMA, in-mean, external regressors and various GARCH flavors, with methods for fit, forecast, simulation, inference and plotting.
	"""
	
	homepage = "http://www.unstarched.net"
	cran = "rugarch" 

	version("1.5-1", md5="98d9cb00c50db386ca21f716656df2b6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-spd", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-skewhyperbolic", type=("build", "run"))
	depends_on("r-rcpp@0.10.6:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.2.34:", type=("build", "run"))
