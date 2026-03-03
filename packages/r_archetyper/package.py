# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchetyper(RPackage):
	"""An Archetype for Data Mining and Data Science Projects

	A project template to support the data science workflow.
	"""
	
	homepage = "https://mkorvink.github.io/archetyper/index.html"
	cran = "archetyper" 

	version("0.1.0", md5="174425a5f93be51c0239da5e51db9b34")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-log4r", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-skimr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("r-bannercommenter", type=("build", "run"))
	depends_on("r-feather", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-ps", type=("build", "run"))
