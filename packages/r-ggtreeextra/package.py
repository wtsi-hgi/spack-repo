# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtreeextra(RPackage):
	"""An R Package To Add Geometric Layers On Circular Or Other Layout Tree Of "ggtree"

	'ggtreeExtra' extends the method for mapping and visualizing associated data on phylogenetic tree using 'ggtree'. These associated data can be presented on the external panels to circular layout, fan layout, or other rectangular layout tree built by 'ggtree' with the grammar of 'ggplot2'.
	"""
	
	homepage = "https://github.com/YuLab-SMU/ggtreeExtra/"
	bioc = "ggtreeExtra"

	version("1.18.0", commit="2be0f5c6d663b2da4ffda70edaab6cfc24c68da4")
	version("1.12.0", commit="8b408a0acb5e4ccf0d43521a7a6675cd41facfba")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-tidytree@0.3.9:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
