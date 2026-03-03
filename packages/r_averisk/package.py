# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAverisk(RPackage):
	"""Calculation of Average Population Attributable Fractions and
Confidence Intervals

	Average population attributable fractions are calculated for a set
    of risk factors (either binary or ordinal valued) for both prospective and case-
    control designs. Confidence intervals are found by Monte Carlo simulation. The
    method can be applied to either prospective or case control designs, provided an
    estimate of disease prevalence is provided. In addition to an exact calculation
    of AF, an approximate calculation, based on randomly sampling permutations has
    been implemented to ensure the calculation is computationally tractable when the
    number of risk factors is large.
	"""
	
	cran = "averisk" 

	version("1.0.3", md5="5ad8975bd9dc778ab7f29ad579c86b5f")

	depends_on("r-mass@7.3:", type=("build", "run"))
