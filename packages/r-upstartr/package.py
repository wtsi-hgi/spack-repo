# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpstartr(RPackage):
	"""Utilities Powering the Globe and Mail's Data Journalism Template

	Core functions necessary for using The Globe and Mail's R data journalism template, 'startr', along with utilities for day-to-day data journalism tasks, such as reading and writing files, producing graphics and cleaning up datasets.
	"""
	
	homepage = "https://github.com/globeandmail/upstartr"
	cran = "upstartr" 

	version("0.1.2", md5="97eb0732ca78d02dcb7660df6027412e")

	depends_on("r@3.6.3:", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-librarian", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-textclean", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tgamtheme", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
