# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgscatridges(RPackage):
	"""Scatter Plot Combined with Ridgelines in 'ggplot2'

	The function combines a scatter plot with ridgelines to better visualise the distribution between sample groups. The plot is created with 'ggplot2'.
	"""
	
	homepage = "https://github.com/matbou85/ggScatRidges"
	cran = "ggScatRidges" 

	version("0.1.1", md5="db1a7967fe84848249ea3999aa93effb")
	version("0.1.0", md5="bf209eb0a00f57c6a7c59871752fc944")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-hrbrthemes", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
