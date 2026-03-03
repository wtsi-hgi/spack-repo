# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDriver(RPackage):
	"""Prioritizing Cancer Driver Genes Using Genomics Data

	Cancer genomes contain large numbers of somatic alterations but few
    genes drive tumor development. Identifying cancer driver genes is critical 
    for precision oncology. Most of current approaches either identify driver 
    genes based on mutational recurrence or using estimated scores predicting 
    the functional consequences of mutations. 'driveR' is a tool for 
    personalized or batch analysis of genomic data for driver gene prioritization 
    by combining genomic information and prior biological knowledge. As features, 
    'driveR' uses coding impact metaprediction scores, non-coding impact scores, 
    somatic copy number alteration scores, hotspot gene/double-hit gene 
    condition, 'phenolyzer' gene scores and memberships to cancer-related KEGG 
    pathways. It uses these features to estimate cancer-type-specific 
    probability for each gene of being a cancer driver using the related task of 
    a multi-task learning classification model. The method is described in detail 
    in Ulgen E, Sezerman OU. 2021. driveR: driveR: a novel method for 
    prioritizing cancer driver genes using somatic genomics data. BMC 
    Bioinformatics <doi:10.1186/s12859-021-04203-7>.
	"""
	
	homepage = "https://egeulgen.github.io/driveR/"
	cran = "driveR" 

	version("0.4.1", md5="9ffe643bde0abb3dcd994fdbb1e6ce05")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
