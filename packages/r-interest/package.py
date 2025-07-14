# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterest(RPackage):
	"""Intron-Exon Retention Estimator

	This package performs Intron-Exon Retention analysis on RNA-seq data (.bam files).
	"""
	
	bioc = "IntEREst"

	version("1.32.0", commit="c32f5ba2b56f88c5b873df093a6af829e87a0bdc")
	version("1.26.0", commit="759bac6d413e727ba518e7a33f2e136a3dfae2fb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicfiles", type=("build", "run"))
	depends_on("r-seqlogo", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicfeatures@1.39.4:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-dexseq", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
