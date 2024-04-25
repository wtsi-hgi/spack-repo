# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsankey(RPackage):
	"""The goal of ggsankey is to make beautiful sankey, alluvial and sankey bump plots in ggplot2."""
	
	homepage = "https://github.com/davidsjoberg/ggsankey"
	git = "https://github.com/davidsjoberg/ggsankey.git"

	version("2024-04-04", commit="b675d0d5144b1b5758d3b2b41e86ceee66a1e071")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
