# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastqcleaner(RPackage):
	"""A Shiny Application for Quality Control, Filtering and Trimming of FASTQ Files

	An interactive web application for quality control, filtering and trimming of FASTQ files. This user-friendly tool combines a pipeline for data processing based on Biostrings and ShortRead infrastructure, with a cutting-edge visual environment. Single-Read and Paired-End files can be locally processed. Diagnostic interactive plots (CG content, per-base sequence quality, etc.) are provided for both the input and output files.
	"""
	
	bioc = "FastqCleaner" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/FastqCleaner_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/FastqCleaner/FastqCleaner_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="84fe332d6b8a0687a2df0845d8e804ba0bf364b60b878e48e33fa472c016c76c")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
