# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnamodr(RPackage):
	"""Detection of post-transcriptional modifications in high throughput sequencing data

	RNAmodR provides classes and workflows for loading/aggregation data from high througput sequencing aimed at detecting post-transcriptional modifications through analysis of specific patterns. In addition, utilities are provided to validate and visualize the results. The RNAmodR package provides a core functionality from which specific analysis strategies can be easily implemented as a seperate package.
	"""
	
	homepage = "https://github.com/FelixErnst/RNAmodR"
	bioc = "RNAmodR"

	version("1.22.0", commit="6bb601d6f393a0f02e6bcb6423feeaa45e6e1022")
	version("1.16.0", commit="721aa3d96d3a1bf74a7167fa6d39f49663a1cf32")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors@0.27.12:", type=("build", "run"))
	depends_on("r-iranges@2.23.9:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-modstrings", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings@2.57.2:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gviz@1.31:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
