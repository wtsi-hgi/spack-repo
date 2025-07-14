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

	version("2.8.0", commit="b9d014258043046c3d8ebf3da081898d9914337f")
	version("2.2.0", commit="bc5503d662768ce5bf9b9ef7970dad0ef8c40a8d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rankprod", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
