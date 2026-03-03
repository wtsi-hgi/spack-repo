# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrimport(RPackage):
	"""Importing Vector Graphics

	Functions for converting, importing, and drawing PostScript 
              pictures in R plots.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/grimport/"
	cran = "grImport" 

	version("0.9-7", md5="15b22fb059f5cc409231f1af50b7316d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("ghostscript", type=("build", "link", "run"))
