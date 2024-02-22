# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMost(RPackage):
	"""Multiphase Optimization Strategy

	Provides functions similar to the 'SAS' macros previously provided
              to accompany Collins, Dziak, and Li (2009) <DOI:10.1037/a0015826>
              and Dziak, Nahum-Shani, and Collins (2012) <DOI:10.1037/a0026972>, papers
              which outline practical benefits and challenges of factorial
              and fractional factorial experiments for scientists interested
              in developing biological and/or behavioral interventions, especially
              in the context of the multiphase optimization strategy
              (see Collins, Kugler & Gwadz 2016) <DOI:10.1007/s10461-015-1145-4>.  The package
              currently contains three functions. First, RelativeCosts1() draws a graph
              of the relative cost of complete and reduced factorial designs versus
              other alternatives. Second, RandomAssignmentGenerator() returns a dataframe
              which contains a list of random numbers that can be used to conveniently
              assign participants to conditions in an experiment with
              many conditions. Third, FactorialPowerPlan() estimates the power, detectable effect
              size, or required sample size of a factorial or fractional factorial
              experiment, for main effects or interactions, given several possible choices
              of effect size metric, and allowing pretests and clustering.
	"""
	
	cran = "MOST" 

	version("0.1.2", md5="4b521502ed649eba92eb9512e40a817c")

	depends_on("r@2.15:", type=("build", "run"))
