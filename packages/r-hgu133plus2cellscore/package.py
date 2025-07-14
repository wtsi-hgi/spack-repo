# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133plus2cellscore(RPackage):
	"""CellScore Standard Cell Types Expression Dataset [hgu133plus2]

	The CellScore Standard Dataset contains expression data from a wide variety of human cells and tissues, which should be used as standard cell types in the calculation of the CellScore. All data was curated from public databases such as Gene Expression Omnibus (https://www.ncbi.nlm.nih.gov/geo/) or ArrayExpress (https://www.ebi.ac.uk/arrayexpress/). This standard dataset only contains data from the Affymetrix GeneChip Human Genome U133 Plus 2.0 microarrays. Samples were manually annotated using the database information or consulting the publications in which the datasets originated. The sample annotations are stored in the phenoData slot of the expressionSet object. Raw data (CEL files) were processed with the affy package to generate present/absent calls (mas5calls) and background-subtracted values, which were then normalized by the R-package yugene to yield the final expression values for the standard expression matrix. The annotation table for the microarray was retrieved from the BioC annotation package hgu133plus2. All data are stored in an expressionSet object.
	"""
	
	bioc = "hgu133plus2CellScore"

	version("1.28.0", commit="e841026d375dc0b238fbaf860db30af882f1a1d0")
	version("1.22.0", commit="8e34b0c98a2a4316523809e8adeac45bfd6d920f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase@2.39.1:", type=("build", "run"))

