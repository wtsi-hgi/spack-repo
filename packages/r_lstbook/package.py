# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLstbook(RPackage):
	"""Data and Software for "Lessons in Statistical Thinking"

	"Lessons in Statistical Thinking" D.T. Kaplan (2014) 
    <https://dtkaplan.github.io/Lessons-in-statistical-thinking/> 
    is a textbook for a first or second course in statistics that embraces 
    data wrangling, causal reasoning, modeling, statistical adjustment, 
    and simulation. 'LSTbook' supports the student-centered, tidy, 
    pipeline-oriented computing style featured in the book.
	"""
	
	homepage = "https://dtkaplan.github.io/LSTbook/"
	cran = "LSTbook" 

	version("0.5.0", md5="b3f0f0cfcdc3b4bf29359730e4751339")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
