# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStory(RPackage):
	"""Download, Explore, and Analyze Literary Theme Ontology Data

	Download, explore, and analyze Literary Theme Ontology themes
    and thematically annotated story data. To learn more about the project
    visit <https://github.com/theme-ontology/theming> and
    <https://www.themeontology.org>.
	"""
	
	homepage = "https://github.com/theme-ontology/stoRy"
	cran = "stoRy" 

	version("0.2.2", md5="242d1dc0fa21733fb60c685a1a75fef1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fansi", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyjson", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
