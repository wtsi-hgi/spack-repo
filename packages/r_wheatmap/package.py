# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWheatmap(RPackage):
	"""Incrementally Build Complex Plots using Natural Semantics

	Builds complex plots, heatmaps in particular, using natural semantics. Bigger plots can be assembled using directives such as 'LeftOf', 'RightOf', 'TopOf', and 'Beneath' and more. Other features include clustering, dendrograms and integration with 'ggplot2' generated grid objects. This package is particularly designed for bioinformaticians to assemble complex plots for publication.
	"""
	
	homepage = "https://github.com/zwdzwd/wheatmap"
	cran = "wheatmap" 

	version("0.2.0", md5="93f820bace140900b65cb8c128eb4b6e")

	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
