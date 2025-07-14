# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcc(RPackage):
	"""TCC: Differential expression analysis for tag count data with robust normalization strategies

	This package provides a series of functions for performing differential expression analysis from RNA-seq count data using robust normalization strategy (called DEGES). The basic idea of DEGES is that potential differentially expressed genes or transcripts (DEGs) among compared samples should be removed before data normalization to obtain a well-ranked gene list where true DEGs are top-ranked and non-DEGs are bottom ranked. This can be done by performing a multi-step normalization strategy (called DEGES for DEG elimination strategy). A major characteristic of TCC is to provide the robust normalization methods for several kinds of count data (two-group with or without replicates, multi-group/multi-factor, and so on) by virtue of the use of combinations of functions in depended packages.
	"""
	
	bioc = "TCC"

	version("1.48.0", commit="069745ef4f0fe9881a4e8c84d5826438876074fa")
	version("1.42.0", commit="b2650a46ea70cd24b7a1f867e908a0f62ec20d83")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-bayseq", type=("build", "run"))
	depends_on("r-roc", type=("build", "run"))
