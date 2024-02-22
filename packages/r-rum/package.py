# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRum(RPackage):
	"""R Templates from the University of Miami

	This holds some r markdown and quarto templates and a template to 
    create a research project in "R Studio".
	"""
	
	homepage = "https://raymondbalise.github.io/rUM/"
	cran = "rUM" 

	version("1.0.2", md5="160094c3d61805d704499eb6f438778e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-conflicted", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-table1", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
