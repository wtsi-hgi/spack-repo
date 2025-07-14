# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErssa(RPackage):
	"""Empirical RNA-seq Sample Size Analysis

	The ERSSA package takes user supplied RNA-seq differential expression dataset and calculates the number of differentially expressed genes at varying biological replicate levels. This allows the user to determine, without relying on any a priori assumptions, whether sufficient differential detection has been acheived with their RNA-seq dataset.
	"""
	
	homepage = "https://github.com/zshao1/ERSSA"
	bioc = "ERSSA"

	version("1.26.0", commit="b78a59a2e7028aa03730a0eb237b7afb555cc396")
	version("1.20.0", commit="c2aa6e199c897d4c03bb0d0714f3c3aeaeb4a146")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-edger@3.23.3:", type=("build", "run"))
	depends_on("r-deseq2@1.21.16:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-biocparallel@1.15.8:", type=("build", "run"))
	depends_on("r-apeglm@1.4.2:", type=("build", "run"))
