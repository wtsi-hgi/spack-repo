# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMqrcm(RPackage):
	"""M-Quantile Regression Coefficients Modeling

	Parametric modeling of M-quantile regression coefficient functions.
	"""
	
	cran = "Mqrcm" 

	version("1.3", md5="d02db6ce416a353f9080da81ea8a80be")

	depends_on("r-pch@2.1:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
