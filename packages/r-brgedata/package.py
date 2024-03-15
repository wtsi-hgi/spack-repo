# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrgedata(RPackage):
	"""Exposures, Gene Expression and Methylation data for ilustration purpouses

	This package contains several sets of omics data including Gene Expression (ExpressionSet), Methylation (GenomicRatioSet), Proteome and Exposome (ExposomeSet). This data is used in vignettes and exaples at MEAL, MultiDataSet and omicRexposome.
	"""
	
	bioc = "brgedata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/brgedata_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/brgedata/brgedata_1.24.0.tar.gz"]

	version("1.24.0", md5="b8d26c8dfa756e9eb556e4662e3b3302")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

	# experiment