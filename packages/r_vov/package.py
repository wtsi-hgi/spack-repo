# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVov(RPackage):
	"""CSS Animations for 'shiny' Elements

	A wrapper around a CSS library called 'vov.css', intended for use 
  in 'shiny' applications. Simply wrap a UI element in one of the animation 
  functions to see it move.
	"""
	
	homepage = "https://github.com/tyluRp/vov"
	cran = "vov" 

	version("0.1.2", md5="d97693b8a35d0d2904064aed238a40c8")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
