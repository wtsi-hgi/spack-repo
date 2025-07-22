# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtaccogaps(RPackage):
	"""Analysis Tools for scATACseq Data with CoGAPS

	Provides tools for running the CoGAPS algorithm (Fertig et al, 2010) on single-cell ATAC sequencing data and analysis of the results. Can be used to perform analyses at the level of genes, motifs, TFs, or pathways. Additionally provides tools for transfer learning and data integration with single-cell RNA sequencing data.
	"""
	
	bioc = "ATACCoGAPS"

	version("1.4.0", commit="1e974804aac600ddc1bd8497be154da244d1d9eb")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-cogaps@3.5.13:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-projectr", type=("build", "run"))
	depends_on("r-tfbstools", type=("build", "run"))
	depends_on("r-geneoverlap", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-motifmatchr", type=("build", "run"))
	depends_on("r-chromvar", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-rgreat", type=("build", "run"))
	depends_on("r-jaspar2016", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-mus-musculus", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-bsgenome-mmusculus-ucsc-mm10", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
