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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ssviz_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ssviz/ssviz_1.36.0.tar.gz"]

	version("1.36.0", sha256="4bcd7117b5bd33b92945e2fbbc66ee62ce66c264745ff5216bc391e4aa79ad0b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
