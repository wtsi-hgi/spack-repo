# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynlm(RPackage):
	"""Dynamic Linear Regression

	Dynamic linear models and time series regression.
	"""
	
	cran = "dynlm" 

	version("0.3-6", md5="6875dcfa6847e5f33ee2c59bbabbe02c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-car@2.0.0:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
