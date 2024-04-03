# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoonGgplot(RPackage):
	"""A Grammar of Interactive Graphics

	Provides a bridge between the 'loon' and  'ggplot2' packages.  Extends the grammar of ggplot to add clauses to create interactive 'loon' plots. Existing ggplot(s) can be turned into interactive 'loon' plots and 'loon' plots into static ggplot(s); the function 'loon.ggplot()' is the bridge from one plot structure to the other.
	"""
	
	cran = "loon.ggplot" 

	version("1.3.4", md5="5ba3d374f6b4cd57a5bc401598b72a6e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-loon@1.3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggmulti", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
