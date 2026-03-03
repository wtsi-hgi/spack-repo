# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdmapr(RPackage):
	"""Molecular Detection Mapping and Analysis Platform

	Runs a Shiny web application that merges raw 'qPCR' fluorescence data with related 
    metadata to visualize species presence/absence detection patterns and assess data quality. 
    The application calculates threshold values from raw fluorescence data using a method based 
    on the second derivative method, Luu-The et al (2005) <doi:10.2144/05382RR05>,  and utilizes 
    the ‘chipPCR’ package by Rödiger, Burdukiewicz, & Schierack (2015) <doi:10.1093/bioinformatics/btv205> 
    to calculate Cq values. The application has the ability to connect to a custom developed MySQL 
    database to populate the applications interface. The application allows users to interact with 
    visualizations such as a dynamic map, amplification curves and standard curves, that allow for 
    zooming and/or filtering. It also enables the generation of customized exportable reports based
    on filtered mapping data. 
	"""
	
	homepage = "https://github.com/HannerLab/MDMAPR"
	cran = "MDMAPR" 

	version("0.2.3", md5="079c00ea88378328dade5a737222052c")

	depends_on("r-rmysql", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-leaflet-extras", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-berryfunctions", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
