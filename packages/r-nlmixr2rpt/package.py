# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmixr2rpt(RPackage):
	"""Templated Word and PowerPoint Reporting of 'nlmixr2' Fitting
Results

	This allows you to generate reporting workflows around 'nlmixr2' analyses with outputs in Word and PowerPoint. You can specify figures, tables and report structure in a user-definable 'YAML' file. Also you can use the internal functions to access the figures and tables to allow their including in other outputs (e.g. R Markdown).
	"""
	
	homepage = "https://nlmixr2.github.io/nlmixr2rpt/"
	cran = "nlmixr2rpt" 

	version("0.2.0", md5="fbb746eb47e8997cff398c994810805a")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-nlmixr2", type=("build", "run"))
	depends_on("r-nlmixr2extra@2.0.7:", type=("build", "run"))
	depends_on("r-onbrand", type=("build", "run"))
	depends_on("r-rxode2", type=("build", "run"))
	depends_on("r-xpose", type=("build", "run"))
	depends_on("r-xpose-nlmixr2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
