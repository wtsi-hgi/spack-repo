# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpwcoxcsv(RPackage):
	"""Inverse Probability Weighted Cox Model with Corrected Sandwich
Variance

	An implementation of corrected sandwich variance (CSV) estimation method for making inference of marginal hazard ratios (HR) in inverse probability weighted (IPW) Cox model without and with clustered data, proposed by Shu, Young, Toh, and Wang (2019) in their paper under revision for Biometrics. Both conventional inverse probability weights and stabilized weights are implemented. Logistic regression model is assumed for propensity score model.
	"""
	
	cran = "ipwCoxCSV" 

	version("1.0", md5="ffb607975fb9604c803b77413ffa7b36")

	depends_on("r-survival", type=("build", "run"))
