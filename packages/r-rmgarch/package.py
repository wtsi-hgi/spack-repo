# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmgarch(RPackage):
	"""Multivariate GARCH Models

	Feasible multivariate GARCH models including DCC, GO-GARCH and Copula-GARCH.
	"""
	
	homepage = "http://www.unstarched.net"
	cran = "rmgarch" 

	version("1.3-9", md5="b0c0b987a8555716cbf9bf2c30cb8e45")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rugarch@1.4.7:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-bessel", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-spd", type=("build", "run"))
	depends_on("r-rcpp@0.10.6:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.2.34:", type=("build", "run"))
