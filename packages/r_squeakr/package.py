# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqueakr(RPackage):
	"""An Experiment Interface for 'DeepSqueak' Bioacoustics Research

	Data processing and visualizations for rodent vocalizations exported from
    'DeepSqueak'. These functions are compatible with the 'SqueakR' Shiny Dashboard,
    which can be used to visualize experimental results and analyses.
	"""
	
	homepage = "https://osimon81.github.io/SqueakR/"
	cran = "SqueakR" 

	version("1.3.0", md5="259f2fd5ba955d39c19939fae7f16f9a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-ggeasy", type=("build", "run"))
	depends_on("r-gghighlight", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-googlesheets4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-report", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
