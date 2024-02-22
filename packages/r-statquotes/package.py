# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatquotes(RPackage):
	"""Quotes on Statistics, Data Visualization and Science

	Generates a random quotation from a database of quotes on topics
    in statistics, data visualization and science. Other functions allow searching
    the quotes database by key term tags, or authors or creating a word cloud.
    The output is designed to be suitable for use at the console, in Rmarkdown
    and LaTeX.
	"""
	
	homepage = "https://github.com/friendly/statquotes/"
	cran = "statquotes" 

	version("0.3.2", md5="f070a768f3428595fc62d8246ae440d3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
