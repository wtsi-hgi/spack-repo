# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIregression(RPackage):
	"""Regression Methods for Interval-Valued Variables

	Contains some important regression methods for interval-valued variables. For each method, it is available the fitted values, residuals and some goodness-of-fit measures.
	"""
	
	cran = "iRegression" 

	version("1.2.1", md5="325bc7fe396cbfbaaa73ab27050a59b2")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
