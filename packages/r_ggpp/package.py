# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpp(RPackage):
	"""Grammar Extensions to 'ggplot2'

	Extensions to 'ggplot2' respecting the grammar of graphics 
    paradigm. Geometries: geom_table(), geom_plot() and geom_grob() add insets to 
    plots using native data coordinates, while geom_table_npc(), geom_plot_npc()
    and geom_grob_npc() do the same using "npc" coordinates through new 
    aesthetics "npcx" and "npcy". Statistics: select observations based on 2D 
    density. Positions: radial nudging away from a center point and nudging away
    from a line or curve; combined stacking and nudging; combined dodging and
    nudging.
	"""
	
	homepage = "https://docs.r4photobiology.info/ggpp/"
	cran = "ggpp" 

	version("0.5.6", md5="d6462ac4fd009ba1618795068ddb20c2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-glue@1.6:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-tibble@3.1.8:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-xts@0.13:", type=("build", "run"))
	depends_on("r-zoo@1.8.11:", type=("build", "run"))
	depends_on("r-mass@7.3.58:", type=("build", "run"))
	depends_on("r-polynom@1.4.0:", type=("build", "run"))
	depends_on("r-lubridate@1.9:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
