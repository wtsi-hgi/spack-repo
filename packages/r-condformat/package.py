# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondformat(RPackage):
	"""Conditional Formatting in Data Frames

	Apply and visualize conditional formatting to data frames in R.
    It renders a data frame with cells formatted according to
    criteria defined by rules, using a tidy evaluation syntax. The table is
    printed either opening a web browser or within the 'RStudio' viewer if
    available. The conditional formatting rules allow to highlight cells
    matching a condition or add a gradient background to a given column. This
    package supports both 'HTML' and 'LaTeX' outputs in 'knitr' reports, and
    exporting to an 'xlsx' file.
	"""
	
	homepage = "https://zeehio.github.io/condformat/"
	cran = "condformat" 

	version("0.10.1", md5="674c1b24aafc451988d8cdb229048ae3")

	depends_on("r-dplyr@0.7.7:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-gtable@0.2:", type=("build", "run"))
	depends_on("r-htmltable@1.9:", type=("build", "run"))
	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-knitr@1.20:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-openxlsx@4.1.5:", type=("build", "run"))
	depends_on("r-rmarkdown@1.10:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-tibble@1.3.4:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
