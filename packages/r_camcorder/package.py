# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCamcorder(RPackage):
	"""Record Your Plot History

	Record and generate a 'gif' of your 'R' sessions plots. When creating 
    a visualization, there is inevitably iteration and refinement that occurs. 
    Automatically save the plots made to a specified directory, previewing them 
    as they would be saved. Then combine all plots generated into a 'gif'
    to show the plot refinement over time.
	"""
	
	cran = "camcorder" 

	version("0.1.0", md5="4f806975a9a03d7f15bcf6caef3a25c8")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gifski", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
