# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRa4bayesmeta(RPackage):
	"""Reference Analysis for Bayesian Meta-Analysis

	Functionality for performing a principled reference analysis in the Bayesian normal-normal hierarchical model used for Bayesian meta-analysis, as described in Ott, Plummer and Roos (2021) <doi:10.1002/sim.9076>. Computes a reference posterior, induced by a minimally informative improper reference prior for the between-study (heterogeneity) standard deviation. Determines additional proper anti-conservative (and conservative) prior benchmarks. Includes functions for reference analyses at both the posterior and the prior level, which, given the data, quantify the informativeness of a heterogeneity prior of interest relative to the minimally informative reference prior and the proper prior benchmarks. The functions operate on data sets which are compatible with the 'bayesmeta' package.
	"""
	
	cran = "ra4bayesmeta" 

	version("1.0-8", md5="e3973cbabf553fda3840084419d7ac47")

	depends_on("r-bayesmeta", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
