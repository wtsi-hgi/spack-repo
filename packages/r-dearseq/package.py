# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDearseq(RPackage):
	"""Differential Expression Analysis for RNA-seq data through a robust variance component test

	Differential Expression Analysis RNA-seq data with variance component score test accounting for data heteroscedasticity through precision weights. Perform both gene-wise and gene set analyses, and can deal with repeated or longitudinal data. Methods are detailed in: i) Agniel D & Hejblum BP (2017) Variance component score test for time-course gene set analysis of longitudinal RNA-seq data, Biostatistics, 18(4):589-604 ; and ii) Gauthier M, Agniel D, Thiébaut R & Hejblum BP (2020) dearseq: a variance component score test for RNA-Seq differential analysis that effectively controls the false discovery rate, NAR Genomics and Bioinformatics, 2(4):lqaa093.
	"""
	
	bioc = "dearseq" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/dearseq_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/dearseq/dearseq_1.14.0.tar.gz"]

	version("1.14.0", md5="40f5669b310e7d2142836e3b1592bdd6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scattermore", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
