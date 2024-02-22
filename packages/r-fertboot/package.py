# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFertboot(RPackage):
	"""Fertilizer Response Curve Analysis by Bootstrapping Residuals

	Quantify variability (such as confidence interval) of fertilizer response curves and optimum fertilizer rates using bootstrapping residuals with several popular non-linear and linear models.
	"""
	
	cran = "FertBoot" 

	version("0.5.0", md5="501d480d3bdd7e335fe3829c0cf9358a")

	depends_on("r-nls-multstart", type=("build", "run"))
	depends_on("r-simpleboot", type=("build", "run"))
