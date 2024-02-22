# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenalizedcdf(RPackage):
	"""Estimate a Penalized Linear Model using the CDF Penalty Function

	Utilize the CDF penalty function to estimate a penalized linear model. 
  It enables you to display some graphical representations and determine whether the Karush-Kuhn-Tucker conditions are met. 
  For more details about the theory, please refer to Cuntrera, D., Augugliaro, L., & Muggeo, V. M. (2022) <arXiv:2212.08582>.
	"""
	
	cran = "penalizedcdf" 

	version("0.1.0", md5="a7f21a5c3eda16b83492c0454dcd0b61")

	depends_on("r-plot-matrix", type=("build", "run"))
