# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDifferentialregulation(RPackage):
	"""Differentially regulated genes from scRNA-seq data

	DifferentialRegulation is a method for detecting differentially regulated genes between two groups of samples (e.g., healthy vs. disease, or treated vs. untreated samples), by targeting differences in the balance of spliced and unspliced mRNA abundances, obtained from single-cell RNA-sequencing (scRNA-seq) data. From a mathematical point of view, DifferentialRegulation accounts for the sample-to-sample variability, and embeds multiple samples in a Bayesian hierarchical model. Furthermore, our method also deals with two major sources of mapping uncertainty: i) 'ambiguous' reads, compatible with both spliced and unspliced versions of a gene, and ii) reads mapping to multiple genes. In particular, ambiguous reads are treated separately from spliced and unsplced reads, while reads that are compatible with multiple genes are allocated to the gene of origin. Parameters are inferred via Markov chain Monte Carlo (MCMC) techniques (Metropolis-within-Gibbs).
	"""
	
	homepage = "https://github.com/SimoneTiberi/DifferentialRegulation"
	bioc = "DifferentialRegulation"

	version("2.6.0", commit="ed32ae005eea317fa7b4cf98590fd1fd4ad32a02")
	version("2.0.3", commit="5880e44652e16dc9fc496f756a7c65c1145df841")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-bandits", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tximport", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
