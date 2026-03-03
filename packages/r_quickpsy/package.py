# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuickpsy(RPackage):
	"""Fits Psychometric Functions for Multiple Groups

	Quickly fits and plots psychometric functions (normal, logistic,
    Weibull or any or any function defined by the user) for multiple groups.
	"""
	
	homepage = "http://dlinares.org/quickpsy.html"
	cran = "quickpsy" 

	version("0.1.5.1", md5="d0a0e644ea3fded6cf0909c8d6957aaa")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mpdir", type=("build", "run"))
