# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExactltre(RPackage):
	"""An Exact Method for Life Table Response Experiment (LTRE)
Analysis

	Life Table Response Experiments (LTREs) are a method of comparative demographic analysis. The purpose is to quantify how the difference or variance in vital rates (stage-specific survival, growth, and fertility) among populations contributes to difference or variance in the population growth rate, "lambda." We provide functions for one-way fixed design and random design LTRE, using either the classical methods that have been in use for several decades, or an fANOVA-based exact method that directly calculates the impact on lambda of changes in matrix elements, for matrix elements and their interactions. The equations and descriptions for the classical methods of LTRE analysis can be found in "Matrix Population Models: Construction, Analysis, and Interpretation (2nd edition)" Caswell (2001, ISBN: 0878930965), and the fANOVA-based exact methods will be published in a forthcoming paper. We also provide some demographic functions, including generation time from Bienvenu and Legendre (2015) <doi:10.1086/681104>. For implementation of exactLTRE where all possible interactions are calculated, we use an operator matrix presented in Poelwijk, Krishna, and Ranganathan (2016) <doi:10.1371/journal.pcbi.1004771>.
	"""
	
	cran = "exactLTRE" 

	version("0.1.0", md5="41507b2a1f4d057ff468d14ab1e05b15")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-popdemo", type=("build", "run"))
