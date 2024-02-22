# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextmininggui(RPackage):
	"""Text Mining GUI Interface

	Graphic interface for text analysis, implement a few methods such as biplots, correspondence analysis, co-occurrence, clustering, topic models, correlations and sentiments.
	"""
	
	homepage = "https://c0reyes.github.io/TextMiningGUI/"
	cran = "TextMiningGUI" 

	version("0.3", md5="1031407bb9629952a67b0b524deb05fe")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-syuzhet", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggwordcloud", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
