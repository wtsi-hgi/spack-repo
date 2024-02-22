# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZoltr(RPackage):
	"""Interface to the 'Zoltar' Forecast Repository API

	'Zoltar' <https://www.zoltardata.com/> is a website that provides a repository of model forecast results
    in a standardized format and a central location. It supports storing, retrieving, comparing, and analyzing time
    series forecasts for prediction challenges of interest to the modeling community. This package provides functions
    for working with the 'Zoltar' API, including connecting and authenticating, getting information about projects,
    models, and forecasts, deleting and uploading forecast data, and downloading scores.
	"""
	
	homepage = "https://github.com/reichlab/zoltr"
	cran = "zoltr" 

	version("0.5.1", md5="5ded4085dcfd841cfbe383d828d0d6d8")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-mockery", type=("build", "run"))
	depends_on("r-webmockr", type=("build", "run"))
	depends_on("r-base64url", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mmwrweek", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
