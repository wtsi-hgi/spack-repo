# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromstar(RPackage):
	"""Combinatorial and Differential Chromatin State Analysis for ChIP-Seq Data

	This package implements functions for combinatorial and differential analysis of ChIP-seq data. It includes uni- and multivariate peak-calling, export to genome browser viewable files, and functions for enrichment analyses.
	"""
	
	homepage = "https://github.com/ataudt/chromstaR"
	bioc = "chromstaR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/chromstaR_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/chromstaR/chromstaR_1.28.0.tar.gz"]

	version("1.28.0", md5="4288983863e4523b5c7e7750691e8987")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-chromstardata", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-biocgenerics@0.31.6:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-bamsignals", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
