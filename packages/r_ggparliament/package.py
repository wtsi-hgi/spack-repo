# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgparliament(RPackage):
	"""Parliament Plots

	Simple parliament plots using 'ggplot2'. Visualize election results as points in the architectural layout of the legislative chamber.
	"""
	
	homepage = "https://github.com/robwhickman/ggparliament"
	cran = "ggparliament" 

	version("2.0.0", md5="b7e65526fa61a0eb3473d926a935363b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
