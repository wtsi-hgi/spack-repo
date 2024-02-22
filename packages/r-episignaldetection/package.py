# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpisignaldetection(RPackage):
	"""Signal Detection Analysis

	Exploring time series for signal detection. It is specifically designed
    to detect possible outbreaks using infectious disease surveillance data
    at the European Union / European Economic Area or country level.
    Automatic detection tools used are presented in the paper
    "Monitoring count time series in R: aberration detection in public health surveillance",
    by Salmon (2016) <doi:10.18637/jss.v070.i10>.
    The package includes:
    - Signal Detection tool, an interactive 'shiny' application
      in which the user can import external data and perform basic signal detection analyses;
    - An automated report in HTML format, presenting the results of the time series analysis in tables and graphs.
      This report can also be stratified by population characteristics (see 'Population' variable).
    This project was funded by the European Centre for Disease Prevention and Control.
	"""
	
	homepage = "https://github.com/EU-ECDC/EpiSignalDetection"
	cran = "EpiSignalDetection" 

	version("0.1.2", md5="6bd70c1b5429c782136067d4e3b84ebb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-isoweek", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-surveillance", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
