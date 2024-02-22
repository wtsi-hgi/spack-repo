# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountdown(RPackage):
	"""A Countdown Timer for HTML Presentations, Documents, and Web
Apps

	A simple countdown timer for slides and HTML documents
    written in 'R Markdown' or 'Quarto'. Integrates fully into 'Shiny'
    apps. Countdown to something amazing.
	"""
	
	homepage = "https://pkg.garrickadenbuie.com/countdown/"
	cran = "countdown" 

	version("0.4.0", md5="50a125598148429b5143766036da0356")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-prismatic@1.1:", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
