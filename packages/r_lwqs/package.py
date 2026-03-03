# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLwqs(RPackage):
	"""Lagged Weighted Quantile Sum Regression

	Wrapper functions for the implementation of lagged weighted quantile sum regression, as per 'Gennings et al' (2020) <doi:10.1016/j.envres.2020.109529>. 
	"""
	
	cran = "lwqs" 

	version("0.5.0", md5="44a1720fe10593ed0ce186ef9883b3b1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gwqs", type=("build", "run"))
	depends_on("r-gamm4", type=("build", "run"))
