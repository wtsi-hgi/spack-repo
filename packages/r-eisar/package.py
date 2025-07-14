# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REisar(RPackage):
	"""Exon-Intron Split Analysis (EISA) in R

	Exon-intron split analysis (EISA) uses ordinary RNA-seq data to measure changes in mature RNA and pre-mRNA reads across different experimental conditions to quantify transcriptional and post-transcriptional regulation of gene expression. For details see Gaidatzis et al., Nat Biotechnol 2015. doi: 10.1038/nbt.3269. eisaR implements the major steps of EISA in R.
	"""
	
	homepage = "https://github.com/fmicompbio/eisaR"
	bioc = "eisaR"

	version("1.20.0", commit="8a219411a15275d0254700ed4d691223b70fa9da")
	version("1.14.1", commit="e4a470a6d61f55fafbf152dd1fd6ec29514186b4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
