# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaetrafo(RPackage):
	"""Transformations for Unit-Level Small Area Models

	The aim of this package is to offer new methodology for unit-level 
    small area models under transformations and limited population auxiliary 
    information. In addition to this new methodology, the widely used nested 
    error regression model without transformations (see "An Error-Components 
    Model for Prediction of County Crop Areas Using Survey and Satellite Data" 
    by Battese, Harter and Fuller (1988) <doi:10.1080/01621459.1988.10478561>) 
    and its well-known uncertainty estimate (see "The estimation of the mean 
    squared error of small-area estimators" by Prasad and Rao (1990) 
    <doi:10.1080/01621459.1995.10476570>) are provided. In this package, the 
    log transformation and the data-driven log-shift transformation are 
    provided. If a transformation is selected, an appropriate method is chosen 
    depending on the respective input of the population data: Individual 
    population data (see "Empirical best prediction under a nested error model 
    with log transformation" by Molina and Martín (2018) 
    <doi:10.1214/17-aos1608>) but also aggregated population data (see 
    "Estimating regional income indicators under transformations and access to 
    limited population auxiliary information" by Würz, Schmid and Tzavidis 
    <unpublished>) can be entered. Especially under limited data access, new 
    methodologies are provided in saeTrafo. Several options are available to 
    assess the used model and to judge, present and export its results. For a 
    detailed description of the package and the methods used see the 
    corresponding vignette.
	"""
	
	homepage = "https://github.com/NoraWuerz/saeTrafo"
	cran = "saeTrafo" 

	version("1.0.2", md5="e431276b1532c32ec635b804c939c940")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-emdi", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-parallelmap", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-hlmdiag", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readods", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
