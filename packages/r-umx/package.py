# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUmx(RPackage):
	"""Structural Equation Modeling and Twin Modeling in R

	Quickly create, run, and report structural equation models, and twin models.
    See '?umx' for help, and umx_open_CRAN_page("umx") for NEWS.
    Timothy C. Bates, Michael C. Neale, Hermine H. Maes, (2019). umx: A library for Structural Equation and Twin Modelling in R.
    Twin Research and Human Genetics, 22, 27-41. <doi:10.1017/thg.2019.2>.
	"""
	
	homepage = "https://github.com/tbates/umx#readme"
	cran = "umx" 

	version("4.19.0", md5="871163a000af25c481746e7867809b97")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-openmx@2.19:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-gert", type=("build", "run"))
	depends_on("r-hrbrthemes", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-paran", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-psychtools", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
