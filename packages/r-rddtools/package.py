# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRddtools(RPackage):
	"""Toolbox for Regression Discontinuity Design ('RDD')

	Set of functions for Regression Discontinuity Design ('RDD'), for
    data visualisation, estimation and testing.
	"""
	
	homepage = "https://qua.st/rddtools/"
	cran = "rddtools" 

	version("1.6.0", md5="4ad01a72fc5f25af6c0f272c1738395c")

	depends_on("r-aer", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdd", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
	depends_on("r-rdrobust", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
