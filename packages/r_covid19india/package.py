# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19india(RPackage):
	"""Pulling Clean Data from Covid19india.org

	Pull raw and pre-cleaned versions of national and state-level 
    COVID-19 time-series data from covid19india.org <https://www.covid19india.org>. 
    Easily obtain and merge case count data, testing data, and vaccine data. 
    Also assists in calculating the time-varying effective reproduction number 
    with sensible parameters for COVID-19.
	"""
	
	homepage = "https://github.com/maxsal/covid19india"
	cran = "covid19india" 

	version("0.1.4", md5="cd06ce32fecdf7107b29c0cd40a8cfe1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table@1.14.1:", type=("build", "run"))
	depends_on("r-epiestim", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
