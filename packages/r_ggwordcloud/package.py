# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgwordcloud(RPackage):
	"""A Word Cloud Geom for 'ggplot2'

	Provides a word cloud text geom for 'ggplot2'. Texts
    are placed so that they do not overlap as in 'ggrepel'.  The algorithm
    used is a variation around the one of 'wordcloud2.js'.
	"""
	
	homepage = "https://github.com/lepennec/ggwordcloud"
	cran = "ggwordcloud" 

	version("0.6.1", md5="7ba9894b559065f9141fac1dc964eceb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-gridtext", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
