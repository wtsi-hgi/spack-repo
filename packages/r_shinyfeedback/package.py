# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyfeedback(RPackage):
	"""Display User Feedback in Shiny Apps

	Easily display user feedback in Shiny apps.
	"""
	
	homepage = "https://github.com/merlinoa/shinyFeedback"
	cran = "shinyFeedback" 

	version("0.4.0", md5="13250ebdd6e4b2ed4594fb4ce1dae39d")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-fontawesome", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
