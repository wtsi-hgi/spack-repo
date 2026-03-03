# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBakr(RPackage):
	"""Analyze and Compare Nucleotide Recoding RNA Sequencing Datasets

	Several implementations of a novel Bayesian hierarchical statistical model of nucleotide
	recoding RNA-seq experiments (NR-seq; TimeLapse-seq, SLAM-seq, TUC-seq, etc.)
	for analyzing and comparing NR-seq datasets (see 'Vock and Simon' (2023) <doi:10.1261/rna.079451.122>).
	NR-seq is a powerful extension of RNA-seq that provides information about the kinetics
	of RNA metabolism (e.g., RNA degradation rate constants), which is notably lacking
	in standard RNA-seq data. The statistical model makes maximal use of these high-throughput
	datasets by sharing information across transcripts to significantly improve
	uncertainty quantification and increase statistical power. 'bakR' includes a maximally
	efficient implementation of this model for conservative initial investigations of datasets. 'bakR'
	also provides more highly powered implementations using the probabilistic programming language
	'Stan' to sample from the full posterior distribution. 'bakR' performs multiple-test
	adjusted statistical inference with the output of these model implementations to
	help biologists separate signal from background. Methods to automatically visualize key
	results and detect batch effects are also provided.
	"""
	
	homepage = "https://simonlabcode.github.io/bakR/"
	cran = "bakR" 

	version("1.0.1", md5="83d0a680bdaff3968def0e7211b7dc97")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
