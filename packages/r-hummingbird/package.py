# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHummingbird(RPackage):
	"""Bayesian Hidden Markov Model for the detection of differentially methylated regions

	A package for detecting differential methylation. It exploits a Bayesian hidden Markov model that incorporates location dependence among genomic loci, unlike most existing methods that assume independence among observations. Bayesian priors are applied to permit information sharing across an entire chromosome for improved power of detection. The direct output of our software package is the best sequence of methylation states, eliminating the use of a subjective, and most of the time an arbitrary, threshold of p-value for determining significance. At last, our methodology does not require replication in either or both of the two comparison groups.
	"""
	
	bioc = "hummingbird" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hummingbird_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hummingbird/hummingbird_1.12.0.tar.gz"]

	version("1.12.0", sha256="108e6b1ac9a742a941e15d1894d2706f1312138fc40f7c2d6ed7d2ea5b6debc2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
