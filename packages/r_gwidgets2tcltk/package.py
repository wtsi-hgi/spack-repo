# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwidgets2tcltk(RPackage):
	"""Toolkit Implementation of gWidgets2 for tcltk

	Port of the 'gWidgets2' API for the 'tcltk' package.
	"""
	
	homepage = "https://github.com/jverzani/gWidgets2tcltk"
	cran = "gWidgets2tcltk" 

	version("1.0-8", md5="3a1a9892839ba7f0248b84edada60335")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-gwidgets2@1.0.7:", type=("build", "run"))
