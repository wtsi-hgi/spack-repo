# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStandardize(RPackage):
	"""Tools for Standardizing Variables for Regression in R

	Tools which allow regression variables to be placed on similar
    scales, offering computational benefits as well as easing interpretation of
    regression output.
	"""
	
	homepage = "https://github.com/CDEager/standardize"
	cran = "standardize" 

	version("0.2.2", md5="bd47c4e370e5ad6514db3826f0dd494f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
