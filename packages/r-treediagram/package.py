# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreediagram(RPackage):
	"""Tree Diagram

	Visualizing cuts for either axis-align or non axis-align tree methods (e.g. decision tree, random tessellation process).
	"""
	
	cran = "TreeDiagram" 

	version("0.1.1", md5="ed51764b9283127121abd0af9d9201e9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tree", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
