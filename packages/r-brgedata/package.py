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

	version("1.30.0", commit="e0902bf1e39a6705b00f2923561e78633a6fe244")
	version("1.24.0", commit="e7038431a31dec263a9252da37f80fd7bef592d6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

