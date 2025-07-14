# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagpie(RPackage):
	"""MeRIP-Seq data Analysis for Genomic Power Investigation and Evaluation

	This package aims to perform power analysis for the MeRIP-seq study. It calculates FDR, FDC, power, and precision under various study design parameters, including but not limited to sample size, sequencing depth, and testing method. It can also output results into .xlsx files or produce corresponding figures of choice.
	"""
	
	homepage = "https://github.com/dxd429/magpie"
	bioc = "magpie"

	version("1.8.0", commit="501452172e592b1d7356a6aa948ab1478e3102df")
	version("1.2.0", commit="ae6eb0eb4758447fbcf20ffde0ca11baa534aaf9")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tress", type=("build", "run"))
