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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/IntEREst_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/IntEREst/IntEREst_1.26.0.tar.gz"]

	version("1.26.0", md5="b9b473ea53b89a32487163ef6a664905")

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
