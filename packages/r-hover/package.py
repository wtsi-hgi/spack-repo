# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHover(RPackage):
	"""CSS Animations for 'shiny' Button Elements

	A wrapper around a CSS library called 'Hover.css', intended for use 
  in 'shiny' applications.
	"""
	
	homepage = "https://github.com/r4fun/hover"
	cran = "hover" 

	version("0.1.1", md5="7bb48012bc0b4851a5d6e7a29abf130f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
