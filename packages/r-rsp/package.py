# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsp(RPackage):
	"""'shiny' Applications for Statistical and Psychometric Analysis

	Toolbox with 'shiny' applications for widely used psychometric
    methods. Those methods include following analysis: Item analysis, item response theory calibration, principal component analysis,
    confirmatory factor analysis - structural equation modeling, generating simulated data.
    References:
    Chalmers (2012, <doi:10.18637/jss.v048.i06>);
    Revelle (2022, <https://CRAN.R-project.org/package=psych Version = 2.2.9.>);
    Rosseel (2012, <doi:10.18637/jss.v048.i02>);
    Magis & Raiche (2012, <doi:10.18637/jss.v048.i08>);
    Magis & Barrada (2017, <doi:10.18637/jss.v076.c01>).
	"""
	
	cran = "RSP" 

	version("0.4", md5="ba2fc6379ceb532bd8c3fef14644b1a7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-mvn", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-shinyitemanalysis", type=("build", "run"))
	depends_on("r-catr", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-hornpa", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-semplot", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-shinycustomloader", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
