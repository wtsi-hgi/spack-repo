# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaros(RPackage):
	"""Semi-Automatic Reporting of Ordinary Surveys

	Produces highly customized reports, primarily intended for survey
    research. Building on 'Quarto' (<https://quarto.org>), it generates draft
    chapters of all specified dependent/independent variables, which can be
    further edited by hand, containing figures, tables and analyses (currently
    only uni-/bivariate tests of equivalent means/proportions). The feature
    'mesos'-reports offer tailor-made batch report production where e.g. an
    institution can compare itself to all other participants. Publication tools
    are also included, such as password generation for 'mesos'-report sections
    on a 'Quarto' Website.
	"""
	
	homepage = "https://nifu-no.github.io/saros/"
	cran = "saros" 

	version("1.0.4", md5="6a9c40103a6f11e7d182845081df389a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-bcrypt", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggiraph", type=("build", "run"))
	depends_on("r-mschart", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("quarto-cli", type=("build", "link", "run"))
