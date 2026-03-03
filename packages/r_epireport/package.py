# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpireport(RPackage):
	"""Epidemiological Report

	Drafting an epidemiological report in 'Microsoft Word' format for a given disease,
  similar to the Annual Epidemiological Reports published by the European Centre 
  for Disease Prevention and Control. Through standalone functions, it is specifically 
  designed to generate each disease specific output presented in these reports and includes:
  - Table with the distribution of cases by Member State over the last five years;
  - Seasonality plot with the distribution of cases at the European Union / European Economic Area level, 
  by month, over the past five years;
  - Trend plot with the trend and number of cases at the European Union / European Economic Area level, 
  by month, over the past five years;
  - Age and gender bar graph with the distribution of cases at the European Union / European Economic Area level.
  Two types of datasets can be used:
  - The default dataset of dengue 2015-2019 data;
  - Any dataset specified as described in the vignette.
	"""
	
	homepage = "https://www.ecdc.europa.eu/en/all-topics-z/surveillance-and-disease-data/annual-epidemiological-reports-aers"
	cran = "EpiReport" 

	version("1.0.2", md5="5fec92c248a1e45a50b4fdef9cf2806d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
