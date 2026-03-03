# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvalues(RPackage):
	"""R-Values for Ranking in High-Dimensional Settings

	A collection of functions for computing "r-values" from various
    kinds of user input such as MCMC output or a list of effect size estimates
    and associated standard errors. Given a large collection of measurement units,
    the r-value, r, of a particular unit is a reported percentile that may be
    interpreted as the smallest percentile at which the unit should be placed in the
    top r-fraction of units.
	"""
	
	homepage = "https://doi.org/10.1111/rssb.12131"
	cran = "rvalues" 

	version("0.7.1", md5="88715116e6a8da0db0d97bd97bb0ba8f")

