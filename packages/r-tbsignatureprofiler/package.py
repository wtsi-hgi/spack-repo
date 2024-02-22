# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbsignatureprofiler(RPackage):
	"""Profile RNA-Seq Data Using TB Pathway Signatures

	Gene signatures of TB progression, TB disease, and other TB disease states have been validated and published previously. This package aggregates known signatures and provides computational tools to enlist their usage on other datasets. The TBSignatureProfiler makes it easy to profile RNA-Seq data using these signatures and includes common signature profiling tools including ASSIGN, GSVA, and ssGSEA. Original models for some gene signatures are also available.  A shiny app provides some functionality alongside for detailed command line accessibility.
	"""
	
	homepage = "https://github.com/compbiomed/TBSignatureProfiler"
	bioc = "TBSignatureProfiler" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TBSignatureProfiler_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TBSignatureProfiler/TBSignatureProfiler_1.14.0.tar.gz"]

	version("1.14.0", md5="1cd38948c20b0f43904a8ff204f2940d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-assign@1.23.1:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rocit", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singscore", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
