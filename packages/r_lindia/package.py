# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLindia(RPackage):
	"""Automated Linear Regression Diagnostic

	Provides a set of streamlined functions that allow
    easy generation of linear regression diagnostic plots necessarily 
    for checking linear model assumptions.
    This package is meant for easy scheming of linear 
    regression diagnostics, while preserving merits of 
    "The Grammar of Graphics" as implemented in 'ggplot2'.
    See the 'ggplot2' website for more information regarding the
    specific capability of graphics.
	"""
	
	homepage = "https://github.com/yeukyul/lindia"
	cran = "lindia" 

	version("0.10", md5="b7aec215000880701e6f2ea69d818fc2")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
