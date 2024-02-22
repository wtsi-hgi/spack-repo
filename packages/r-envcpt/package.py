# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvcpt(RPackage):
	"""Detection of Structural Changes in Climate and Environment Time
Series

	Tools for automatic model selection and diagnostics for Climate and Environmental data.  In particular the envcpt() function does automatic model selection between a variety of trend, changepoint and autocorrelation models.  The envcpt() function should be your first port of call.
	"""
	
	homepage = "https://github.com/rkillick/EnvCpt/"
	cran = "EnvCpt" 

	version("1.1.3", md5="5d1a13e001ad5884735da189ea8ed111")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-changepoint@2.2.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
