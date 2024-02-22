# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntomics(RPackage):
	"""Integrative analysis of multi-omics data to infer regulatory networks

	IntOMICS is an efficient integrative framework based on Bayesian networks. IntOMICS systematically analyses gene expression (GE), DNA methylation (METH), copy number variation (CNV) and biological prior knowledge (B) to infer regulatory networks. IntOMICS complements the missing biological prior knowledge by so-called empirical biological knowledge (empB), estimated from the available experimental data. An automatically tuned MCMC algorithm (Yang and Rosenthal, 2017) estimates model parameters and the empirical biological knowledge. Conventional MCMC algorithm with additional Markov blanket resampling (MBR) step (Su and Borsuk, 2016) infers resulting regulatory network structure consisting of three types of nodes: GE nodes refer to gene expression levels, CNV nodes refer to associated copy number variations, and METH nodes refer to associated DNA methylation probe(s).
	"""
	
	homepage = "https://github.com/anna-pacinkova/IntOMICS"
	bioc = "IntOMICS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/IntOMICS_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/IntOMICS/IntOMICS_1.2.0.tar.gz"]

	version("1.2.0", md5="61628ea37535123f71455b77b194b08c")

	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-bnstruct", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-bestnormalize", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
