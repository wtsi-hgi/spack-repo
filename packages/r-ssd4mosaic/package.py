# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsd4mosaic(RPackage):
	"""Web Application for the SSD Module of the MOSAIC Platform

	Web application using 'shiny' for the SSD (Species
    Sensitivity Distribution) module of the MOSAIC (MOdeling and
    StAtistical tools for ecotoxICology) platform. It estimates the
    Hazardous Concentration for x% of the species (HCx) from toxicity
    values that can be censored and provides various plotting options for
    a better understanding of the results. See our companion paper
    Kon Kam King et al. (2014) <doi:10.48550/arXiv.1311.5772>.
	"""
	
	homepage = "https://gitlab.in2p3.fr/mosaic-software/mosaic-ssd"
	cran = "ssd4mosaic" 

	version("1.0.1", md5="5b2297d231acf6107ea4721736712faa")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-fitdistrplus@1.1.11:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem@0.3.5:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny@1.7.4:", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
