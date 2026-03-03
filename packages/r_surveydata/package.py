# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveydata(RPackage):
	"""Tools to Work with Survey Data

	Data obtained from surveys contains information not only about the
    survey responses, but also the survey metadata, e.g. the original survey
    questions and the answer options. The 'surveydata' package makes it easy to
    keep track of this metadata, and to easily extract columns with
    specific questions.
	"""
	
	homepage = "https://github.com/andrie/surveydata"
	cran = "surveydata" 

	version("0.2.7", md5="3039f14d16985ed83026c496db4596c8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
