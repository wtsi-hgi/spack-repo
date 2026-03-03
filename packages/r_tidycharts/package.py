# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidycharts(RPackage):
	"""Generate Tidy Charts Inspired by 'IBCS'

	There is a wide range of R packages created for data visualization, but still, there was no simple and easily accessible way to create clean and transparent charts - up to now. The 'tidycharts' package enables the user to generate charts compliant with International Business Communication Standards ('IBCS').
    It means unified bar widths, colors, chart sizes, etc. Creating homogeneous reports has never been that easy! Additionally, users can apply semantic notation to indicate different data scenarios (plan, budget, forecast). What's more, it is possible to customize the charts by creating a personal color pallet with the possibility of switching to default options after the experiments.
    We wanted the package to be helpful in writing reports, so we also made joining charts in a one, clear image possible.
    All charts are generated in SVG format and can be shown in the 'RStudio' viewer pane or exported to HTML output of 'knitr'/'markdown'.
	"""
	
	homepage = "https://mi2datalab.github.io/tidycharts/"
	cran = "tidycharts" 

	version("0.1.3", md5="b9500b3266b0cd7c4d14c60e85e1700f")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
