# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinytest2(RPackage):
	"""Testing for Shiny Applications

	Automated unit testing of Shiny applications through a headless 'Chromium' browser.
	"""
	
	homepage = "https://rstudio.github.io/shinytest2/"
	cran = "shinytest2" 

	version("0.3.1", md5="9128a0e94819c88be73ecaa36e4ba83c", url="https://cran.r-project.org/src/contrib/shinytest2_0.3.1.tar.gz")

	depends_on("r-testthat@3.1.2:", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-chromote@0.1.2:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-globals@0.14:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pingr", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
