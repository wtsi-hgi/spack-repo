# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmaqshiny(RPackage):
	"""Explore Air-Quality Mobile-Monitoring Data

	Mobile-monitoring or "sensors on a mobile platform", is an increasingly 
    popular approach to measure high-resolution pollution data at the street level. 
    Coupled with location data, spatial visualisation of air-quality parameters 
    helps detect localized areas of high air-pollution, also called hotspots. 
    In this approach, portable sensors are mounted on a vehicle and driven on 
    predetermined routes to collect high frequency data (1 Hz). 
    'mmaqshiny' is for analysing, visualising and spatial mapping of 
    high-resolution air-quality data collected by specific devices installed on 
    a moving platform. 1 Hz data of PM2.5 (mass concentrations of particulate  
    matter with size less than 2.5 microns), Black carbon mass concentrations 
    (BC), ultra-fine particle number concentrations, carbon dioxide along with 
    GPS coordinates and relative humidity (RH) data collected by popular 
    portable instruments (TSI DustTrak-8530, Aethlabs microAeth-AE51, TSI CPC3007, 
    LICOR Li-830, Garmin GPSMAP 64s, Omega USB RH probe respectively). It 
    incorporates device specific cleaning and correction algorithms. RH correction 
    is applied to DustTrak PM2.5 following the Chakrabarti et al., (2004) 
    <doi:10.1016/j.atmosenv.2004.03.007>. Provision is given to add linear 
    regression coefficients for correcting the PM2.5 data (if required). BC data
    will be cleaned for the vibration generated noise, by adopting the statistical 
    procedure as explained in Apte et al., (2011) <doi:10.1016/j.atmosenv.2011.05.028>, 
    followed by a loading correction as suggested by Ban-Weiss et al., (2009)  
    <doi:10.1021/es8021039>. For the number concentration data, provision is 
    given for dilution correction factor (if a diluter is used with CPC3007; 
    default value is 1). The package joins the raw, cleaned and corrected data 
    from the above said instruments and outputs as a downloadable csv file. 
	"""
	
	homepage = "https://github.com/meenakshi-kushwaha/mmaqshiny"
	cran = "mmaqshiny" 

	version("1.0.0", md5="9e31dd4d278ceb309af096e22fb36ca1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
