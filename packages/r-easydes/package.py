# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasydes(RPackage):
	"""An Easy Way to Descriptive Analysis

	
  Descriptive analysis is essential for publishing medical articles.
  This package provides an easy way to conduct the descriptive analysis.
  1. Both numeric and factor variables can be handled. For numeric variables, normality test will be applied to choose the parametric and nonparametric test.
  2. Both two or more groups can be handled. For groups more than two, the post hoc test will be applied, 'Tukey' for the numeric variables and 'FDR' for the factor variables.
  3. T test, ANOVA or Fisher test can be forced to apply.
  4. Mean and standard deviation can be forced to display.
	"""
	
	cran = "easyDes" 

	version("6.0", md5="9e776c3d7a42898ed5427579d11722cf")

	depends_on("r-pmcmrplus", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
