# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMind(RPackage):
	"""Multivariate Model Based Inference for Domains

	Allows users to produce estimates and MSE for multivariate variables using Linear Mixed Model. The package follows the approach of Datta, Day and Basawa (1999) <doi:10.1016/S0378-3758(98)00147-5>.
	"""
	
	cran = "mind" 

	version("1.1.0", md5="f02fc2ce39bd9f1994ccb6678aea0435")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jwileymisc", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
