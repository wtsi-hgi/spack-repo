# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlot3logit(RPackage):
	"""Ternary Plots for Trinomial Regression Models

	An implementation of the ternary plot for interpreting regression
    coefficients of trinomial regression models, as proposed in Santi, Dickson
    and Espa (2019) <doi:10.1080/00031305.2018.1442368>. Ternary plots can be
    drawn using either 'ggtern' package (based on 'ggplot2') or 'Ternary'
    package (based on standard graphics). The package and its features are
    illustrated in Santi, Dickson, Espa and Giuliani (2022)
    <doi:10.18637/jss.v103.c01>.
	"""
	
	homepage = "https://www.flaviosanti.it/software/plot3logit/"
	cran = "plot3logit" 

	version("3.1.4", md5="b34883337639b7db2c063830c861010f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggtern@3.4:", type=("build", "run"))
	depends_on("r-ternary@1.0.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
