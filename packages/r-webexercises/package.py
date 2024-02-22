# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebexercises(RPackage):
	"""Create Interactive Web Exercises in 'R Markdown' (Formerly
'webex')

	Functions for easily creating interactive web pages using
    'R Markdown' that students can use in self-guided learning.
	"""
	
	homepage = "https://github.com/psyteachr/webexercises"
	cran = "webexercises" 

	version("1.1.0", md5="c29daf2a531a585166dc3171f473f10d")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rmarkdown@2.2:", type=("build", "run"))
