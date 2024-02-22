# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrailler(RPackage):
	"""Improved Access for Blind Users

	Blind users do not have access to the graphical output from R
    without printing the content of graphics windows to an embosser of
    some kind. This is not as immediate as is required for efficient
    access to statistical output.  The functions here are created so that
    blind people can make even better use of R. This includes the text
    descriptions of graphs, convenience functions to replace the
    functionality offered in many GUI front ends, and experimental
    functionality for optimising graphical content to prepare it for
    embossing as tactile images.
	"""
	
	homepage = "https://github.com/ajrgodfrey/BrailleR"
	cran = "BrailleR" 

	version("1.0.2", md5="7ece107d0ee614125427f28271c8a2d9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-gridgraphics", type=("build", "run"))
	depends_on("r-gridsvg", type=("build", "run"))
	depends_on("r-hunspell", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-quarto", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-roloc", type=("build", "run"))
	depends_on("r-rolocisccnbs", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
