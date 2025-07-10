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

	version("1.18.0", sha256="211a464555f33c445beadd2d0a5b0b4db853f70fc89669f50890e96ad1634939")

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
	depends_on("zlib", type=("build", "link", "run"))
