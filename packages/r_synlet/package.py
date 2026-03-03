# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynlet(RPackage):
	"""Hits Selection for Synthetic Lethal RNAi Screen Data

	Select hits from synthetic lethal RNAi screen data. For example, there are two identical celllines except one gene is knocked-down in one cellline. The interest is to find genes that lead to stronger lethal effect when they are knocked-down further by siRNA. Quality control and various visualisation tools are implemented. Four different algorithms could be used to pick up the interesting hits. This package is designed based on 384 wells plates, but may apply to other platforms with proper configuration.
	"""
	
	bioc = "synlet" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/synlet_2.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/synlet/synlet_2.2.0.tar.gz"]

	version("2.2.0", md5="f56c634faaae3a0de5e46d18e6617d11")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rankprod", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
