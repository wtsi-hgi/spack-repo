# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCount(RPackage):
	"""Functions, Data and Code for Count Data

	Functions, data and code for Hilbe, J.M. 2011. Negative Binomial Regression, 2nd Edition (Cambridge University Press) and Hilbe, J.M. 2014. Modeling Count Data (Cambridge University Press).
	"""
	
	cran = "COUNT" 

	version("1.3.4", md5="2c4c60614c9fd7dfd2db54b28fbfe75e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-msme", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
