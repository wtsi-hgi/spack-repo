# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircrnaprofiler(RPackage):
	"""circRNAprofiler: An R-Based Computational Framework for the Downstream Analysis of Circular RNAs

	R-based computational framework for a comprehensive in silico analysis of circRNAs. This computational framework allows to combine and analyze circRNAs previously detected by multiple publicly available annotation-based circRNA detection tools. It covers different aspects of circRNAs analysis from differential expression analysis, evolutionary conservation, biogenesis to functional analysis.
	"""
	
	homepage = "https://github.com/Aufiero/circRNAprofiler"
	bioc = "circRNAprofiler" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/circRNAprofiler_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/circRNAprofiler/circRNAprofiler_1.16.0.tar.gz"]

	version("1.16.0", md5="5cd7f621f355f9d816938675dd550e2f")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-universalmotif", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-gwascat", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
