# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExrq(RPackage):
	"""Extreme Regression of Quantiles

	Estimation for high conditional quantiles based on quantile regression.
	"""
	
	cran = "EXRQ" 

	version("1.0", md5="30f6db404b8676478c30cb83cb548cae")

	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
