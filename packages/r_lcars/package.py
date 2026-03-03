# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcars(RPackage):
	"""LCARS Aesthetic for Shiny

	Provides Shiny widgets and theme that support a 'Library Computer Access/Retrieval System' (LCARS) aesthetic for Shiny apps. 
    The package also includes functions for adding a minimal LCARS theme to static 'ggplot2' graphs. 
    More details about LCARS can be found at <https://en.wikipedia.org/wiki/LCARS>.
	"""
	
	homepage = "https://github.com/leonawicz/lcars"
	cran = "lcars" 

	version("0.3.8", md5="f800f654f6aba4bd736e4bc9ba32c73b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-trekcolors", type=("build", "run"))
