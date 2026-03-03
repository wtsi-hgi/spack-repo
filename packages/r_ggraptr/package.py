# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgraptr(RPackage):
	"""Allows Interactive Visualization of Data Through a Web Browser
GUI

	Intended for both technical and non-technical users to create
    interactive data visualizations through a web browser GUI without writing any
    code.
	"""
	
	cran = "ggraptR" 

	version("1.3", md5="8ff9925fa841f7eedd0b22d350be900a")

	depends_on("r-dplyr@0.7.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-pacman@0.4.6:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-shiny@0.12.2:", type=("build", "run"))
