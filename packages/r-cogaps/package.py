# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCogaps(RPackage):
	"""Coordinated Gene Activity in Pattern Sets

	Coordinated Gene Activity in Pattern Sets (CoGAPS) implements a Bayesian MCMC matrix factorization algorithm, GAPS, and links it to gene set statistic methods to infer biological process activity.  It can be used to perform sparse matrix factorization on any data, and when this data represents biomolecules, to do gene set analysis.
	"""
	
	bioc = "CoGAPS"

	version("3.28.0", commit="0a5f395bd62e353b19d57c8ac1dafd9ea0742263")
	version("3.22.0", commit="4118fd66c028954ddddce9455c0aaa25e2e58968")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
