# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRead(RPackage):
	"""Powerful Replicability Analysis of Genome-Wide Association
Studies

	A robust and powerful approach is developed for replicability analysis of two Genome-wide association studies (GWASs) accounting for the linkage disequilibrium (LD) among genetic variants. The LD structure in two GWASs is captured by a four-state hidden Markov model (HMM). The unknowns involved in the HMM are estimated by an efficient expectation-maximization (EM) algorithm in combination with a non-parametric estimation of functions. By incorporating information from adjacent locations via the HMM, this approach identifies the entire clusters of genotype-phenotype associated signals, improving the power of replicability analysis while effectively controlling the false discovery rate.
	"""
	
	cran = "ReAD" 

	version("1.0.1", md5="55250c643731203f581bd6c573454aed")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
