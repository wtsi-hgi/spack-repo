# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRexer(RPackage):
	"""Random Exercises and Exams Generator

	The main purpose of this package is to streamline the
    generation of exams that include random elements in exercises.
    Exercises can be defined in a table, based on text and figures, and
    may contain gaps to be filled with provided options. Exam documents
    can be generated in various formats. It allows us to generate a
    version for conducting the assessment and another version that
    facilitates correction, linked through a code.
	"""
	
	homepage = "https://josesamos.github.io/rexer/"
	cran = "rexer" 

	version("1.0.0", md5="fcb5ea4615885445866f95f653b69c84")

	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
