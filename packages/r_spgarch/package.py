# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpgarch(RPackage):
	"""Spatial ARCH and GARCH Models (spGARCH)

	A collection of functions to deal with spatial and spatiotemporal autoregressive conditional heteroscedasticity (spatial ARCH and GARCH models) by Otto, Schmid, Garthoff (2018, Spatial Statistics) <arXiv:1609.00711>: simulation of spatial ARCH-type processes (spARCH, exponential spARCH, complex spARCH); quasi-maximum-likelihood estimation of the parameters of spARCH models and spatial autoregressive models with spARCH disturbances, diagnostic checks, visualizations.
	"""
	
	cran = "spGARCH" 

	version("0.2.2", md5="db72124d2e0eeb5275ce0ff67f8f07bc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
