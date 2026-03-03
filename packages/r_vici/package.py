# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVici(RPackage):
	"""Vaccine Induced Cellular Immunogenicity with Bivariate Modeling

	A shiny app for accurate estimation of vaccine induced immunogenicity 
    with bivariate linear modeling. Method is detailed in: Lhomme, Hejblum, Lacabaratz, 
    Wiedemann, Lelievre, Levy, Thiebaut & Richert (2020). Journal of Immunological Methods, 
    477:112711. <doi:10.1016/j.jim.2019.112711>.
	"""
	
	cran = "vici" 

	version("0.7.3", md5="959a4b1e9106ff427fad6cb069fb027f")

	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
