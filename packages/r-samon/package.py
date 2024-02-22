# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamon(RPackage):
	"""Sensitivity Analysis for Missing Data

	In a clinical trial with repeated measures designs, outcomes are often taken from subjects at fixed time-points.  The focus of the trial may be to compare the mean outcome in two or more groups at some pre-specified time after enrollment. In the presence of missing data auxiliary assumptions are necessary to perform such comparisons.  One commonly employed assumption is the missing at random assumption (MAR).   The 'samon' package allows the user to perform a (parameterized) sensitivity analysis of this assumption.  In particular it can be used to examine the sensitivity of tests in the difference in outcomes to violations of the MAR assumption.  The sensitivity analysis can be performed under two scenarios, a) where the data exhibit a monotone missing data pattern (see the samon() function), and, b) where in addition to a monotone missing data pattern the data exhibit intermittent missing values (see the samonIM() function).
	"""
	
	cran = "samon" 

	version("4.0.2", md5="6ef7de6c0d9a07d0c5c74af19aa5ce8b")

	depends_on("r@2.10:", type=("build", "run"))
