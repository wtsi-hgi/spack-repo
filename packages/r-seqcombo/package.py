# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqcombo(RPackage):
	"""Visualization Tool for Genetic Reassortment

	Provides useful functions for visualizing virus reassortment events.
	"""
	
	bioc = "seqcombo"

	version("1.30.0", commit="6e872ecd8530e3b1a5024ec11757a4aaaa301ea0")
	version("1.24.0", commit="701d045f838d0267b363e8537492d487a2c8ae6c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
