# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfastp(RPackage):
	"""An Ultra-Fast and All-in-One Fastq Preprocessor (Quality Control, Adapter, low quality and polyX trimming) and UMI Sequence Parsing).

	Rfastp is an R wrapper of fastp developed in c++. fastp performs quality control for fastq files. including low quality bases trimming, polyX trimming, adapter auto-detection and trimming, paired-end reads merging, UMI sequence/id handling. Rfastp can concatenate multiple files into one file (like shell command cat) and accept multiple files as input.
	"""
	
	bioc = "Rfastp" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rfastp_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rfastp/Rfastp_1.12.0.tar.gz"]

	version("1.12.0", md5="9f6903cb485151c4d3c368abf5193309")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rhtslib", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
