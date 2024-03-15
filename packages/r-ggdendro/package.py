# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgdendro(RPackage):
	"""Create Dendrograms and Tree Diagrams Using 'ggplot2'.

	This is a set of tools for dendrograms and tree plots using 'ggplot2'. The
	'ggplot2' philosophy is to clearly separate data from the presentation.
	Unfortunately the plot method for dendrograms plots directly to a plot
	device without exposing the data. The 'ggdendro' package resolves this by
	making available functions that extract the dendrogram plot data.  The
	package provides implementations for tree, rpart, as well as diana and
	agnes cluster diagrams."""

	cran = "ggdendro"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("0.2.0", md5="9df2367d1c26c8b1f1adc376fb1ac3c4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2@0.9.2:", type=("build", "run"))
