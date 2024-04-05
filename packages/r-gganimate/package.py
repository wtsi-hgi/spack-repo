# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGganimate(RPackage):
	"""A Grammar of Animated Graphics

	The grammar of graphics as implemented in the 'ggplot2'
    package has been successful in providing a powerful API for creating
    static visualisation. In order to extend the API for animated graphics
    this package provides a completely new set of grammar, fully
    compatible with 'ggplot2' for specifying transitions and animations in
    a flexible and extensible way.
	"""
	
	homepage = "https://gganimate.com"
	cran = "gganimate" 

	version("1.0.9", md5="9be9453ae809aa81f1722f2215681edb")
	version("1.0.8", md5="2ec08a5316dfd4d845238dfb296e2b91")

	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-transformr@0.1.5:", type=("build", "run"))
	depends_on("r-tweenr@2.0.3:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
