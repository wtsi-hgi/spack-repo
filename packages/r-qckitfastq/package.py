# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQckitfastq(RPackage):
	"""FASTQ Quality Control

	Assessment of FASTQ file format with multiple metrics including quality score, sequence content, overrepresented sequence and Kmers.
	"""
	
	bioc = "qckitfastq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/qckitfastq_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/qckitfastq/qckitfastq_1.18.0.tar.gz"]

	version("1.18.0", md5="60955b37d9eb0868da1c5ecd262334e8")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-seqtools", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rseqan", type=("build", "run"))
