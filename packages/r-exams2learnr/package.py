# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExams2learnr(RPackage):
	"""Interface for 'exams' Exercises in 'learnr' Tutorials

	Automatic generation of quizzes or individual questions for 'learnr' tutorials based on 'R/exams' exercises.
	"""
	
	homepage = "https://www.R-exams.org/"
	cran = "exams2learnr" 

	version("0.1-0", md5="7cedcb02a5cfef647ae6f3263ab35c51")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-exams@2.4.0:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-learnr@0.11:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
