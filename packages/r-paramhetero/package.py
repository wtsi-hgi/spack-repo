# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParamhetero(RPackage):
	"""Numeric and Visual Comparisons of Heterogeneity in Parametric
Models

	Performs statistical tests to compare coefficients and residual 
    variance across models. Also provides graphical methods for 
    assessing heterogeneity in coefficients and residuals. Currently supports 
    linear and generalized linear models.
	"""
	
	cran = "paramhetero" 

	version("1.0.0", md5="1f4eaf166f5cb2caa1341d5b2c563138")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
