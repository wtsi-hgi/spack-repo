# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCit(RPackage):
	"""Causal Inference Test

	A likelihood-based hypothesis testing approach is implemented for
  assessing causal mediation. Described in Millstein, Chen, and Breton (2016),
  <DOI:10.1093/bioinformatics/btw135>, it could be used to test for mediation
  of a known causal association between a DNA variant, the 'instrumental variable',
  and a clinical outcome or phenotype by gene expression or DNA methylation, the
  potential mediator. Another example would be testing mediation of the effect
  of a drug on a clinical outcome by the molecular target. The hypothesis test
  generates a p-value or permutation-based FDR value with confidence intervals
  to quantify uncertainty in the causal inference. The outcome can be represented
  by either a continuous or binary variable, the potential mediator is continuous,
  and the instrumental variable can be continuous or binary and is not limited to
  a single variable but may be a design matrix representing multiple variables.
	"""
	
	homepage = "https://github.com/USCbiostats/cit"
	cran = "cit" 

	version("2.3.1", md5="ebfa35e3b8d4eafe5d0d17f6576f6e17")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
