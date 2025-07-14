# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenarise(RPackage):
	"""Microarray Analysis tool

	genArise is an easy to use tool for dual color microarray data. Its GUI-Tk based environment let any non-experienced user performs a basic, but not simple, data analysis just following a wizard. In addition it provides some tools for the developer.
	"""
	
	homepage = "http://www.ifc.unam.mx/genarise"
	bioc = "genArise"

	version("1.84.0", commit="744afb82c202941809bd89e2f4fde175bc8c4640")
	version("1.78.0", commit="acf91f3f3ee322fb348d194a5d55c8078adb3738")

	depends_on("r@1.7.1:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
