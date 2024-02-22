# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrendyy(RPackage):
	"""A Tidy Wrapper Around 'gtrendsR'

	Access Google Trends information. This package provides a tidy wrapper to the 'gtrendsR' package.
    Use four spaces when indenting paragraphs within the Description.
	"""
	
	homepage = "https://github.com/josiahparry/trendyy"
	cran = "trendyy" 

	version("0.1.1", md5="bc3ecb1c32fabad0372b984074717fa2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-gtrendsr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
