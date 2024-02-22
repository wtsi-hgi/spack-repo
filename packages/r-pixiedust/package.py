# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPixiedust(RPackage):
	"""Tables so Beautifully Fine-Tuned You Will Believe It's Magic

	The introduction of the 'broom' package has made converting model
    objects into data frames as simple as a single function. While the 'broom'
    package focuses on providing tidy data frames that can be used in advanced
    analysis, it deliberately stops short of providing functionality for reporting
    models in publication-ready tables. 'pixiedust' provides this functionality with
    a programming interface intended to be similar to 'ggplot2's system of layers
    with fine tuned control over each cell of the table. Options for output include
    printing to the console and to the common markdown formats (markdown, HTML, and
    LaTeX). With a little 'pixiedust' (and happy thoughts) tables can really fly.
	"""
	
	homepage = "https://github.com/nutterb/pixiedust"
	cran = "pixiedust" 

	version("0.9.4", md5="f42db3d8ec3c193f3272ea76898681df")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-checkmate@1.8:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-labelvector", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
