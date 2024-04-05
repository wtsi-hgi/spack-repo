# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrf(RPackage):
	"""Generalized Random Forests

	Forest-based statistical estimation and inference.
  GRF provides non-parametric methods for heterogeneous treatment effects estimation
  (optionally using right-censored outcomes, multiple treatment arms or outcomes, or instrumental variables),
  as well as least-squares regression, quantile regression, and survival regression,
  all with support for missing covariates.
	"""
	
	homepage = "https://github.com/grf-labs/grf"
	cran = "grf" 

	version("2.3.2", md5="68c8c5700737c57df558c2f4e960fbc1")
	version("2.3.1", md5="e4ac89ddb34c3c5795415eebc8057ad8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sandwich@2.4.0:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
