# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStevethemes(RPackage):
	"""Steve's 'ggplot2' Themes and Related Theme Elements

	This is a compilation of my preferred themes and
    related theme elements for 'ggplot2'. I believe these themes
    and theme elements are aesthetically pleasing, both for pedagogical 
    instruction and for the presentation of applied statistical research to a wide
    audience. These themes imply routine use of easily obtained/free fonts, simple
    forms of which are included in this package.
	"""
	
	homepage = "http://svmiller.com/stevethemes/"
	cran = "stevethemes" 

	version("0.1.0", md5="958de5bd6a56070500019241d0eb50de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-systemfonts", type=("build", "run"))
