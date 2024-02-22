# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrna(RPackage):
	"""Analyzing tRNA sequences and structures

	The tRNA package allows tRNA sequences and structures to be accessed and used for subsetting. In addition, it provides visualization tools to compare feature parameters of multiple tRNA sets and correlate them to additional data. The tRNA package uses GRanges objects as inputs requiring only few additional column data sets.
	"""
	
	bioc = "tRNA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/tRNA_1.20.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/tRNA/tRNA_1.20.1.tar.gz"]

	version("1.20.1", md5="e44e072f320f35d6cf6210074fbdf665")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-structstrings", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-modstrings", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
