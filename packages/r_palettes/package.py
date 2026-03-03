# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalettes(RPackage):
	"""Methods for Colour Vectors and Colour Palettes

	Provides a comprehensive library for colour vectors and colour
    palettes using a new family of colour classes (palettes_colour and
    palettes_palette) that always print as hex codes with colour previews.
    Capabilities include: formatting, casting and coercion, extraction and
    updating of components, plotting, colour mixing arithmetic, and colour
    interpolation.
	"""
	
	homepage = "https://mccarthy-m-g.github.io/palettes/"
	cran = "palettes" 

	version("0.2.0", md5="f14dbe76b47a9749be16172d3906c6a2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-prismatic", type=("build", "run"))
	depends_on("r-farver@2.0.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
