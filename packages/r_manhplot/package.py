# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManhplot(RPackage):
	"""The Manhattan++ Plot

	This plot integrates annotation into a manhattan plot. The plot is implemented as a heatmap, which is binned using -log10(p-value) and chromosome position. Annotation currently supported is minor allele frequency and gene function high impact variants.
	"""
	
	homepage = "https://github.com/cgrace1978/manhplot/"
	cran = "manhplot" 

	version("1.1", md5="c157983ad4f85f665c145b9f5451bcbe")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
