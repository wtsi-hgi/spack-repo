# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorhcplot(RPackage):
	"""Colorful Hierarchical Clustering Dendrograms

	Build dendrograms with sample groups highlighted by different colors. Visualize results of hierarchical clustering analyses as dendrograms whose leaves and labels are colored according to sample grouping. Assess whether data point grouping aligns to naturally occurring clusters. 
	"""
	
	cran = "colorhcplot" 

	version("1.3.1", md5="c209b6afeabb749cabe8b822bc28bdaa")

	depends_on("r@3:", type=("build", "run"))
