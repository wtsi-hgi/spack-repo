# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSofia(RPackage):
	"""Making Sophisticated and Aesthetical Figures in R

	Software that leverages the capabilities of Circos by manipulating data, preparing configuration files, and running the Perl-native Circos directly from the R environment with minimal user intervention. Circos is a novel software that addresses the challenges in visualizing genetic data by creating circular ideograms composed of tracks of heatmaps, scatter plots, line plots, histograms, links between common markers, glyphs, text, and etc. Please see <http://www.circos.ca>. 
	"""
	
	homepage = "http://cggl.horticulture.wisc.edu"
	cran = "SOFIA" 

	version("1.0", md5="af66b3e2636307f7d5a7108c48c1a0ee")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("circos", type=("build", "link", "run"))
