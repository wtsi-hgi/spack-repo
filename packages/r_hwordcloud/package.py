# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHwordcloud(RPackage):
	"""Rendering Word Clouds

	Provides a way to display word clouds in R. The word cloud is a html widget, so you can use it in interactive documents and 'shiny' applications.
	"""
	
	homepage = "https://github.com/czxa/hwordcloud"
	cran = "hwordcloud" 

	version("0.1.0", md5="e5dd6a5261eb3e65987337e70229cf15")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-wordcloud2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
