# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROddsNEnds(RPackage):
	"""Odds Ratios, Contingency Table, and Model Significance from a
Generalized Linear Model Object

	Computes odds ratios and 95% confidence intervals from a generalized linear model object. It also computes model significance with the chi-squared statistic and p-value and it computes model fit using a contingency table to determine the percent of observations for which the model correctly predicts the value of the outcome. Calculates model sensitivity and specificity.
	"""
	
	cran = "odds.n.ends" 

	version("0.1.4", md5="4b61ec5f46ec4944fe7d013f1f999282")

	depends_on("r-mass", type=("build", "run"))
