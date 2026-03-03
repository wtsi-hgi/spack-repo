# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlumshiny(RPackage):
	"""'Shiny' Applications for the R Package 'Luminescence'

	A collection of 'shiny' applications for the R package
    'Luminescence'. These mainly, but not exclusively, include applications for
    plotting chronometric data from e.g. luminescence or radiocarbon dating. It
    further provides access to bootstraps tooltip and popover functionality and
    contains the 'jscolor.js' library with a custom 'shiny' output binding.
	"""
	
	homepage = "https://tzerk.github.io/RLumShiny/"
	cran = "RLumShiny" 

	version("0.2.3", md5="0117a380df293c7f2c5940dae868c1a9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-luminescence@0.9.17:", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-rhandsontable@0.3.8:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-googlevis@0.6.11:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7.2:", type=("build", "run"))
	depends_on("r-rcarb@0.1.4:", type=("build", "run"))
	depends_on("r-markdown@1.1:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-dt@0.20:", type=("build", "run"))
	depends_on("r-knitr@1.37:", type=("build", "run"))
