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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/padma_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/padma/padma_1.12.0.tar.gz"]

    version("1.18.1", tag="RELEASE_3_21")
	version("1.12.0", sha256="ad1f233509d53b24af8344f0ec0f196633b0b5d9b0dd4cb9572986a095fa660d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
