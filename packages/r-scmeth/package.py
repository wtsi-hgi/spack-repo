# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScmeth(RPackage):
	"""Functions to conduct quality control analysis in methylation data

	Functions to analyze methylation data can be found here. Some functions are relevant for single cell methylation data but most other functions can be used for any methylation data. Highlight of this workflow is the comprehensive quality control report.
	"""
	
	bioc = "scmeth" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scmeth_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scmeth/scmeth_1.22.0.tar.gz"]

	version("1.22.0", sha256="17d8c5d1c4276be5790d4e7e7f1da5f07c3ca8c239512ec08b74db4d836d610b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-delayedarray@0.5.15:", type=("build", "run"))
	depends_on("r-annotatr", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.5.6:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-hdf5array@1.7.5:", type=("build", "run"))
