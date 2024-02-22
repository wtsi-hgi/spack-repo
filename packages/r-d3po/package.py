# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RD3po(RPackage):
	"""Fast and Beautiful Interactive Visualization for 'Markdown' and
'Shiny'

	Apache licensed alternative to 'Highcharter' which provides 
  functions for both fast and beautiful interactive visualization for 'Markdown'
  and 'Shiny'.
	"""
	
	homepage = "https://pacha.dev/d3po/"
	cran = "d3po" 

	version("0.5.5", md5="f02493400fa5eb7bddd58ad923bd8340")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
