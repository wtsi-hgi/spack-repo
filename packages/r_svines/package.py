# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvines(RPackage):
	"""Stationary Vine Copula Models

	Provides functionality to fit and simulate from stationary vine 
  copula models for time series, see Nagler et al. (2022) 
  <doi:10.1016/j.jeconom.2021.11.015>.
	"""
	
	homepage = "https://github.com/tnagler/svines"
	cran = "svines" 

	version("0.2.3", md5="c92b3c5afa1bcb674f6de5d389010ea3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rvinecopulib", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-univariateml", type=("build", "run"))
	depends_on("r-wdm", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
