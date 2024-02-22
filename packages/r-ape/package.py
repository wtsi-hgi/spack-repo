# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApe(RPackage):
	"""Analyses of Phylogenetics and Evolution.

	Functions for reading, writing, plotting, and manipulating phylogenetic
	trees, analyses of comparative data in a phylogenetic framework, ancestral
	character analyses, analyses of diversification and macroevolution,
	computing distances from DNA sequences, reading and writing nucleotide
	sequences as well as importing from BioConductor, and several tools such as
	Mantel's test, generalized skyline plots, graphical exploration of
	phylogenetic data (alex, trex, kronoviz), estimation of absolute
	evolutionary rates and clock-like trees using mean path lengths and
	penalized likelihood, dating trees with non-contemporaneous sequences,
	translating DNA into AA sequences, and assessing sequence alignments.
	Phylogeny estimation can be done with the NJ, BIONJ, ME, MVR, SDM, and
	triangle methods, and several methods handling incomplete distance matrices
	(NJ*, BIONJ*, MVR*, and the corresponding triangle method). Some functions
	call external applications (PhyML, Clustal, T-Coffee, Muscle) whose results
	are returned into R."""

	cran = "ape"

	version("5.7-1", md5="04d75a639533b2d91dfbb034e9b6b9ff")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
