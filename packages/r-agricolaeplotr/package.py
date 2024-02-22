# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgricolaeplotr(RPackage):
	"""Visualization of Design of Experiments from the 'agricolae'
Package

	Visualization of Design of Experiments from the 'agricolae' package with 'ggplot2' framework
    The user provides an experiment design from the 'agricolae' package, calls the corresponding function and will receive a 
    visualization with 'ggplot2' based functions that are specific for each design. As there are many different designs, each design is tested on its type.
    The output can be modified with standard 'ggplot2' commands or with other packages with 'ggplot2' function extensions.
	"""
	
	homepage = "https://github.com/jensharbers/agricolaeplotr"
	cran = "agricolaeplotr" 

	version("0.5.0", md5="4b5f55e5e84fb11b86695b3239449cac")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp@2:", type=("build", "run"))
	depends_on("r-fieldhub", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stplanr", type=("build", "run"))
	depends_on("r-ggspatial", type=("build", "run"))
