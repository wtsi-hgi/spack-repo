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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ERSSA_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ERSSA/ERSSA_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="965e2091c4d3049bc12947880545da316caece750459369c9bde924236edffc6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-edger@3.23.3:", type=("build", "run"))
	depends_on("r-deseq2@1.21.16:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-biocparallel@1.15.8:", type=("build", "run"))
	depends_on("r-apeglm@1.4.2:", type=("build", "run"))
