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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/padma_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/padma/padma_1.12.0.tar.gz"]

	version("1.12.0", md5="126a8aec3057f8ccc5a435c5435adfc0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
