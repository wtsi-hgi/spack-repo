# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSherlock(RPackage):
	"""Graphical Displays for Structured Problem Solving and Diagnosis

	Powerful graphical displays and statistical tools for structured problem solving and diagnosis. 
    The functions of the 'sherlock' package are especially useful for applying the process of elimination as a problem diagnosis technique.
    The 'sherlock' package was designed to seamlessly work with the 'tidyverse' set of packages and provides a collection of graphical displays 
    built on top of the 'ggplot' and 'plotly' packages, such as different kinds of small multiple plots as well as helper functions such as 
    adding reference lines, normalizing observations, reading in data or saving analysis results in an Excel file.
    References:
    David Hartshorne (2019, ISBN: 978-1-5272-5139-7).
    Stefan H. Steiner, R. Jock MacKay (2005, ISBN: 0873896467).
	"""
	
	homepage = "https://github.com/gaboraszabo/sherlock"
	cran = "sherlock" 

	version("0.7.0", md5="9c2da93876afee8b36f5dff5101de5ba")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggh4x", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
