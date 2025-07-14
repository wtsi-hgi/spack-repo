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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/eisaR_1.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/eisaR/eisaR_1.14.1.tar.gz"]

	version("1.20.0", tag="RELEASE_3_21")
	version("1.14.1", sha256="315bd11e65d3fd65aa2acfcc929242872d9376050cfb9d06877f6f2c8a40e22d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
