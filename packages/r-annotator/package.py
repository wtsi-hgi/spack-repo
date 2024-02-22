# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotator(RPackage):
	"""Image Annotation and Polygon Outlining using Free Drawing

	Provides functions to create image annotations through polygon outlining. Annotator has the same function as 'graphics::locator()' but achieves its purpose through drawing, rather than multiple mouse clicks. It is based on the 'htmlwidgets' package and 'fabric.js' JavaScript library <http://fabricjs.com/>. 
	"""
	
	homepage = "https://github.com/valcu/annotator"
	cran = "annotator" 

	version("0.0.3.1", md5="01c37b3a2956db168a6b154cb5dd5112")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
