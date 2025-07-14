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

	version("1.26.0", commit="0b9d150ca5f0613176f267a36738ecf6eb050b48")
	version("1.20.0", commit="358c1ad98b3386017503d38bb80de0597ececde9")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
