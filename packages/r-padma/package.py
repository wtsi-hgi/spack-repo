# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPadma(RPackage):
	"""Individualized Multi-Omic Pathway Deviation Scores Using Multiple Factor Analysis

	Use multiple factor analysis to calculate individualized pathway-centric scores of deviation with respect to the sampled population based on multi-omic assays (e.g., RNA-seq, copy number alterations, methylation, etc). Graphical and numerical outputs are provided to identify highly aberrant individuals for a particular pathway of interest, as well as the gene and omics drivers of aberrant multi-omic profiles.
	"""
	
	homepage = "https://github.com/andreamrau/padma"
	bioc = "padma"

	version("1.18.1", commit="be1bb74a22f483afb3058f734c74496977cd18c8")
	version("1.12.0", commit="d925ab16867c93dde2de9200d47a4c1064c931ce")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
