# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevticulate(RPackage):
	"""Interaction with "RevBayes" in R

	Interaction with "RevBayes" via R. Objects created in "RevBayes" can be passed into the R environment, and many types can be converted into similar R objects. To download "RevBayes", go to <https://revbayes.github.io/download>.
	"""
	
	cran = "Revticulate" 

	version("1.0.0", md5="607abd22ae7f3f61b76539d285814a17")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-comprehenr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
