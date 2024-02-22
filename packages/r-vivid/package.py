# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVivid(RPackage):
	"""Variable Importance and Variable Interaction Displays

	A suite of plots for displaying variable importance and two-way variable interaction jointly. Can also display partial dependence plots laid out in a pairs plot or 'zenplots' style.
	"""
	
	homepage = "https://alaninglis.github.io/vivid/"
	cran = "vivid" 

	version("0.2.8", md5="5df2a8043f1e4678d5662a4fd8c03516")

	depends_on("r-condvis2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dendser", type=("build", "run"))
	depends_on("r-ggalt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-flashlight", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
