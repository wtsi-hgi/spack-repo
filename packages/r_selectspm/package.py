# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectspm(RPackage):
	"""Select Point Pattern Models Based on Minimum Contrast, AIC and
Goodness of Fit

	Fit and selects point pattern models based on minimum contrast, AIC and and goodness of fit.
	"""
	
	cran = "selectspm" 

	version("0.6", md5="e10ac7665d6010bbcb9beb9e40e1204c")

	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-ecespa", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
