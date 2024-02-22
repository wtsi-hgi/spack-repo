# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeatmaps(RPackage):
	"""Flexible Heatmaps for Functional Genomics and Sequence Features

	This package provides functions for plotting heatmaps of genome-wide data across genomic intervals, such as ChIP-seq signals at peaks or across promoters. Many functions are also provided for investigating sequence features.
	"""
	
	bioc = "heatmaps" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/heatmaps_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/heatmaps/heatmaps_1.26.0.tar.gz"]

	version("1.26.0", md5="68b0a507dd5b2bcdfef2106195429dc2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
