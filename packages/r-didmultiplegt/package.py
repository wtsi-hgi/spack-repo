# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDidmultiplegt(RPackage):
	"""Estimation in DID with Multiple Groups and Periods

	
    Estimate the effect of a treatment on an outcome in sharp Difference-in-Difference designs with multiple groups and periods. 
    It computes the DIDM estimator introduced in Section 4 of "Two-Way Fixed Effects Estimators with Heterogeneous
    Treatment Effects" (Chaisemartin, D'Haultfoeuille (2020)  <doi:10.1257/aer.20181169>), which
    generalizes the standard DID estimator with two groups, two periods and a binary treatment to situations
    with many groups,many periods and a potentially non-binary treatment. For each pair of consecutive time
    periods t-1 and t and for each value of the treatment d, the package computes a DID estimator comparing
    the outcome evolution among the switchers, the groups whose treatment changes from d to some other value
    between t-1 and t, to the same evolution among control groups whose treatment is equal to d both in t-1 and t.
    Then the DIDM estimator is equal to the average of those DIDs across all pairs of consecutive time periods and
    across all values of the treatment. Under a parallel trends assumption, DIDM is an unbiased and consistent estimator
    of the average treatment effect among switchers, at the time period when they switch.
    The package can also compute placebo estimators that can be used to test the parallel trends assumption.
    Finally, in staggered adoption designs where each group's treatment is weakly increasing over time,
    it can compute estimators of switchers' dynamic treatment effects, one time period or more after they have
    started receiving the treatment.
	"""
	
	cran = "DIDmultiplegt" 

	version("0.1.2", md5="09646036047968d40f628db2f2fc3e06")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-fixest@0.6:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-wooldridge", type=("build", "run"))
