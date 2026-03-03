# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkomics(RPackage):
	"""Minicircle Sequence Classes (MSC) Analyses

	This is a analysis toolkit to streamline the analyses of minicircle sequence diversity in population-scale genome projects. rKOMICS is a user-friendly R package that has simple installation requirements and that is applicable to all 27 trypanosomatid genera. Once minicircle sequence alignments are generated, rKOMICS allows to examine, summarize and visualize minicircle sequence diversity within and between samples through the analyses of minicircle sequence clusters. We showcase the functionalities of the (r)KOMICS tool suite using a whole-genome sequencing dataset from a recently published study on the history of diversification of the Leishmania braziliensis species complex in Peru. Analyses of population diversity and structure highlighted differences in minicircle sequence richness and composition between Leishmania subspecies, and between subpopulations within subspecies. The rKOMICS package establishes a critical framework to manipulate, explore and extract biologically relevant information from mitochondrial minicircle assemblies in tens to hundreds of samples simultaneously and efficiently. This should facilitate research that aims to develop new molecular markers for identifying species-specific minicircles, or to study the ancestry of parasites for complementary insights into their evolutionary history. ***** !! WARNING: this package relies on dependencies from Bioconductor. For Mac users, this can generate errors when installing rKOMICS. Install Bioconductor and ComplexHeatmap at advance: install.packages("BiocManager"); BiocManager::install("ComplexHeatmap") *****.
	"""
	
	cran = "rKOMICS" 

	version("1.3", md5="2b4c64fef001de5a8bf4d4c3b8019b34")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
