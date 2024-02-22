# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsviz(RPackage):
	"""A small RNA-seq visualizer and analysis toolkit

	Small RNA sequencing viewer
	"""
	
	bioc = "ssviz" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ssviz_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ssviz/ssviz_1.36.0.tar.gz"]

	version("1.36.0", md5="00bd4a7d6a57af51b74187993bdf84c4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
