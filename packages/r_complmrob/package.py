# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComplmrob(RPackage):
	"""Robust Linear Regression with Compositional Data as Covariates

	Robust regression methods for compositional data.
    The distribution of the estimates can be approximated with various bootstrap
    methods. These bootstrap methods are available for the compositional as well
    as for standard robust regression estimates. This allows for direct
    comparison between them.
	"""
	
	homepage = "https://github.com/dakep/complmrob"
	cran = "complmrob" 

	version("0.7.0", md5="581a658126348e9f8d205ab6cbaad700")

	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
