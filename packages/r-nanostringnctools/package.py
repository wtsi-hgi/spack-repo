# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanostringnctools(RPackage):
	"""NanoString nCounter Tools

	Tools for NanoString Technologies nCounter Technology. Provides support for reading RCC files into an ExpressionSet derived object.  Also includes methods for QC and normalizaztion of NanoString data.
	"""
	
	bioc = "NanoStringNCTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NanoStringNCTools_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NanoStringNCTools/NanoStringNCTools_1.10.0.tar.gz"]

    version("1.16.1", tag="RELEASE_3_21")
	version("1.10.0", md5="97985a577c04cc2d7c19d00f2bd8e1d1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-ggiraph", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
