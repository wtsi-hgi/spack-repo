# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMina(RPackage):
	"""Microbial community dIversity and Network Analysis

	An increasing number of microbiome datasets have been generated and analyzed with the help of rapidly developing sequencing technologies. At present, analysis of taxonomic profiling data is mainly conducted using composition-based methods, which ignores interactions between community members. Besides this, a lack of efficient ways to compare microbial interaction networks limited the study of community dynamics. To better understand how community diversity is affected by complex interactions between its members, we developed a framework (Microbial community dIversity and Network Analysis, mina), a comprehensive framework for microbial community diversity analysis and network comparison. By defining and integrating network-derived community features, we greatly reduce noise-to-signal ratio for diversity analyses. A bootstrap and permutation-based method was implemented to assess community network dissimilarities and extract discriminative features in a statistically principled way.
	"""
	
	bioc = "mina"

	version("1.16.0", commit="5640360ff45563b8205a10a8234c6d7e0d8585cb")
	version("1.10.0", commit="f0e35638fb19642e4b04446ba8415bc03766083a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mcl", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-biganalytics", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
