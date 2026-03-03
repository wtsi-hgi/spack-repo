# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWpa(RPackage):
	"""Tools for Analysing and Visualising Viva Insights Data

	Opinionated functions that enable easier and faster
    analysis of Viva Insights data. There are three main types of functions in 'wpa':
    (i) Standard functions create a 'ggplot' visual or a summary table based on a specific
    Viva Insights metric; (2) Report Generation functions generate HTML reports on
    a specific analysis area, e.g. Collaboration; (3) Other miscellaneous functions cover
    more specific applications (e.g. Subject Line text mining) of Viva Insights data.
    This package adheres to 'tidyverse' principles and works well with the pipe syntax.
    'wpa' is built with the beginner-to-intermediate R users in mind, and is optimised for
    simplicity. 
	"""
	
	homepage = "https://github.com/microsoft/wpa/"
	cran = "wpa" 

	version("1.9.0", md5="4f90dc95d42e92a086fe27f23f78ebb7")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-ggwordcloud", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
