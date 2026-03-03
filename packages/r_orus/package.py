# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrus(RPackage):
	"""Operational Research User Stories

	A first implementation of automated parsing of user stories, when used 
  to defined functional requirements for operational research mathematical 
  models. It allows reading user stories, splitting them on the who-what-why template,
  and classifying them according to the parts of the mathematical model that 
  they represent. Also provides semantic grouping of stories, 
  for project management purposes.
	"""
	
	homepage = "https://github.com/melvidoni/oRus"
	cran = "oRus" 

	version("1.0.0", md5="62ff5d63478e1cf7e492f33930109811")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
