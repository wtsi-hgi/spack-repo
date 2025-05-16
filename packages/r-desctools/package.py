# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesctools(RPackage):
	"""Tools for Descriptive Statistics

	A collection of miscellaneous basic statistic functions and convenience wrappers for efficiently describing data. The author's intention was to create a toolbox, which facilitates the (notoriously time consuming) first descriptive tasks in data analysis, consisting of calculating descriptive statistics, drawing graphical summaries and reporting the results. The package contains furthermore functions to produce documents using MS Word (or PowerPoint) and functions to import data from Excel. Many of the included functions can be found scattered in other packages and other sources written partly by Titans of R. The reason for collecting them here, was primarily to have them consolidated in ONE instead of dozens of packages (which themselves might depend on other packages which are not needed at all), and to provide a common and consistent interface as far as function and arguments naming, NA handling, recycling rules etc. are concerned. Google style guides were used as naming rules (in absence of convincing alternatives). The 'BigCamelCase' style was consequently applied to functions borrowed from contributed R packages as well.
	"""
	
	homepage = "https://andrisignorell.github.io/DescTools/"
	cran = "DescTools" 

	version("0.99.54", md5="3045c3d7b5111ace2e61ac35435d6246")
	version("0.99.48", md5="e21ec4519eac315cefc2ad04a5bd52d7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-exact", type=("build", "run"))
	depends_on("r-gld", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
