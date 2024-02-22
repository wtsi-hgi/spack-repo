# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPnar(RPackage):
	"""Poisson Network Autoregressive Models

	Quasi likelihood-based methods for estimating linear and log-linear Poisson Network Autoregression models with p lags and covariates. Tools for testing the linearity versus several non-linear alternatives. Tools for simulation of multivariate count distributions, from linear and non-linear PNAR models, by using a specific copula construction. References include: Armillotta, M. and K. Fokianos (2022a). Poisson network autoregression. <arXiv:2104.06296>. Armillotta, M. and K. Fokianos (2022b). Testing linearity for network autoregressive models. <arXiv:2202.03852>. Armillotta, M., Tsagris, M. and Fokianos, K. (2022c). The R-package PNAR for modelling count network time series. <arXiv:2211.02582>.
	"""
	
	cran = "PNAR" 

	version("1.6", md5="8fe1489999c4b06d2ec1f40fc0682d9d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
