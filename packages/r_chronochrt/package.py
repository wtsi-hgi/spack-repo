# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChronochrt(RPackage):
	"""Creating Chronological Charts

	Easy way to draw chronological charts from tables, aiming to include an intuitive environment for anyone new to R. Includes 'ggplot2' geoms and theme for chronological charts. 
	"""
	
	homepage = "https://gitlab.com/archaeothommy/chronochrt"
	cran = "chronochrt" 

	version("0.1.3", md5="20c573ac992bfcde2fc84d3a98f3c61e")

	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
