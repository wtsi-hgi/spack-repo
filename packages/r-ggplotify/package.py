# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgplotify(RPackage):
	"""Convert Plot to 'grob' or 'ggplot' Object.

	Convert plot function call (using expression or formula) to 'grob' or
	'ggplot' object that compatible to the 'grid' and 'ggplot2' ecosystem. With
	this package, we are able to e.g. using 'cowplot' to align plots produced
	by 'base' graphics, 'ComplexHeatmap', 'eulerr', 'grid', 'lattice',
	'magick', 'pheatmap', 'vcd' etc. by converting them to 'ggplot' objects."""

	cran = "ggplotify"

	license("Artistic-2.0")

	version("0.1.2", md5="3bd4a51a0406a4b44f456aa75a8093df")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridgraphics", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
