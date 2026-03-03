# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatarium(RPackage):
	"""Data Bank for Statistical Analysis and Visualization

	Contains data organized by topics: categorical data, regression model, 
            means comparisons, independent and repeated measures ANOVA, mixed ANOVA and ANCOVA.
	"""
	
	cran = "datarium" 

	version("0.1.0", md5="6c29493b2a45381721bdb37ab8d9b0d2")

	depends_on("r@3.1:", type=("build", "run"))
