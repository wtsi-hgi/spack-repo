# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgr(RPackage):
	"""Analyse Text Files Created by Emacs' Org mode

	Provides functionality to process text files created by Emacs' Org mode, and decompose the content to the smallest components (headlines, body, tag, clock entries etc).  Emacs is an extensible, customizable text editor and Org mode is for keeping notes, maintaining TODO lists, planning projects.  Allows users to analyze org files as data frames in R, e.g., to convieniently group tasks by tag into project and calculate total working hours.  Also provides some help functions like search.parent, gg.pie (visualise working hours in ggplot2) and tree.headlines (visualise headline stricture in tree format) to help user managing their complex org files. 
	"""
	
	cran = "orgR" 

	version("0.9.0", md5="3e5be742de28c1a805595fbfcf21d389")

	depends_on("r-ggthemes@1.7:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-lubridate@1.3.3:", type=("build", "run"))
	depends_on("r-data-table@1.9.4:", type=("build", "run"))
	depends_on("r-stringr@0.6.2:", type=("build", "run"))
