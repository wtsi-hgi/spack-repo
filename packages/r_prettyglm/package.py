# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrettyglm(RPackage):
	"""Pretty Summaries of Generalized Linear Model Coefficients

	One of the main advantages of using Generalised Linear Models
    is their interpretability.  The goal of 'prettyglm' is to provide a
    set of functions which easily create beautiful coefficient summaries
    which can readily be shared and explained. 'prettyglm' helps users
    create coefficient summaries which include categorical base levels,
    variable importance and type III p.values. 'prettyglm' also creates
    beautiful relativity plots for categorical, continuous and splined
    coefficients.
	"""
	
	homepage = "https://jared-fowler.github.io/prettyglm/"
	cran = "prettyglm" 

	version("1.0.1", md5="5326d16e233871b5562a61788f5adf18")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidycat", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vip", type=("build", "run"))
