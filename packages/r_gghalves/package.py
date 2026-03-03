# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGghalves(RPackage):
	"""Compose Half-Half Plots Using Your Favourite Geoms

	A 'ggplot2' extension for easy plotting of half-half geom combinations. Think half boxplot and half jitterplot, or half violinplot and half dotplot.
	"""
	
	homepage = "https://github.com/erocoar/gghalves"
	cran = "gghalves" 

	version("0.1.4", md5="586f523fa8444322bca0000809538374")

	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
