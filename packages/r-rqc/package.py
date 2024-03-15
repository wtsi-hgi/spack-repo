# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqc(RPackage):
	"""Quality Control Tool for High-Throughput Sequencing Data

	Rqc is an optimised tool designed for quality control and assessment of high-throughput sequencing data. It performs parallel processing of entire files and produces a report which contains a set of high-resolution graphics.
	"""
	
	homepage = "https://github.com/labbcb/Rqc"
	bioc = "Rqc" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rqc_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rqc/Rqc_1.36.0.tar.gz"]

	version("1.36.0", md5="425dbc839b22b6af4d19ca20174c24c1")

	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocgenerics@0.25.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-knitr@1.7:", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biovizbase", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfiles", type=("build", "run"))
