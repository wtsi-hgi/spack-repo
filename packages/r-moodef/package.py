# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoodef(RPackage):
	"""Defining 'Moodle' Elements from R

	The main objective of this package is to support the
    definition of 'Moodle' elements taking advantage of the power that R
    offers. In this first version, it allows the definition of questions
    to be included in the question bank.
	"""
	
	homepage = "https://josesamos.github.io/moodef/"
	cran = "moodef" 

	version("1.1.0", md5="1115f51934ed0d59b1543f855bc73400")

	depends_on("r-blastula", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
