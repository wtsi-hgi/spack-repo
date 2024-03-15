# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmanh(RPackage):
	"""Visualization Tool for GWAS Result

	Manhattan plot and QQ Plot are commonly used to visualize the end result of Genome Wide Association Study. The "ggmanh" package aims to keep the generation of these plots simple while maintaining customizability. Main functions include manhattan_plot, qqunif, and thinPoints.
	"""
	
	bioc = "ggmanh" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ggmanh_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ggmanh/ggmanh_1.6.0.tar.gz"]

	version("1.6.0", md5="dbbd8130e9ef70cb69c7e305af0c37d7")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-seqarray@1.32:", type=("build", "run"))
