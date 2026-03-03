# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarrietr(RPackage):
	"""Wrangle Phylogenetic Distance Matrices and Other Utilities

	Harriet was Charles Darwin's pet tortoise (possibly). 'harrietr'
    implements some function to manipulate distance matrices and phylogenetic trees
    to make it easier to plot with 'ggplot2' and to manipulate using 'tidyverse'
    tools.
	"""
	
	homepage = "https://github.com/andersgs/harrietr"
	cran = "harrietr" 

	version("0.2.3", md5="f461dacc77149636c5eae934dc82cb48")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ape@4.1:", type=("build", "run"))
	depends_on("r-ggtree@1.8.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-lazyeval@0.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.2:", type=("build", "run"))
	depends_on("r-tidyr@0.7:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
