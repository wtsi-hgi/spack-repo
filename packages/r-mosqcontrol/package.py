# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosqcontrol(RPackage):
	"""Mosquito Control Resource Optimization

	This project aims to make an accessible model for mosquito control resource optimization. The model uses data provided by users to estimate the mosquito populations in the sampling area for the sampling time period, and the optimal time to apply a treatment or multiple treatments.
	"""
	
	cran = "mosqcontrol" 

	version("0.1.0", md5="73b6ded53df5f6bdc968f2a623148907")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-nlcoptim", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
