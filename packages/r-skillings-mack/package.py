# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkillingsMack(RPackage):
	"""The Skillings-Mack Test Statistic for Block Designs with Missing
Observations

	A generalization of the statistic used in Friedman's ANOVA method and in Durbin's rank test. This nonparametric statistical test is useful for the data obtained from block designs with missing observations occurring randomly. A resulting p-value is based on the chi-squared distribution and Monte Carlo method.
	"""
	
	cran = "Skillings.Mack" 

	version("1.10", md5="d2ebc63f566523def49ef2223d9572e7")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
