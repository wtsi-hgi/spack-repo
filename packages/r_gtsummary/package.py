# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtsummary(RPackage):
	"""Presentation-Ready Data Summary and Analytic Result Tables

	Creates presentation-ready tables summarizing data
    sets, regression models, and more. The code to create the tables is
    concise and highly customizable. Data frames can be summarized with
    any function, e.g. mean(), median(), even user-written functions.
    Regression models are summarized and include the reference rows for
    categorical variables. Common regression models, such as logistic
    regression and Cox proportional hazards regression, are automatically
    identified and the tables are pre-filled with appropriate column
    headers.
	"""
	
	homepage = "https://github.com/ddsjoberg/gtsummary"
	cran = "gtsummary" 

	version("1.7.2", md5="15b68053b36c3f02939323b6db3d0bb8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-broom@1.0.1:", type=("build", "run"))
	depends_on("r-broom-helpers@1.13:", type=("build", "run"))
	depends_on("r-cli@3.1.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-gt@0.9:", type=("build", "run"))
	depends_on("r-knitr@1.37:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.1:", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-rlang@1.0.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-vctrs@0.5.2:", type=("build", "run"))
