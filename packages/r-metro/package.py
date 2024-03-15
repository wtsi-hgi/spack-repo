# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetro(RPackage):
	"""Washington Metropolitan Area Transit Authority API

	The Washington Metropolitan Area Transit Authority is a
    government agency operating light rail and passenger buses in the
    Washington D.C. area. With a free developer account, access their
    'Metro Transparent Data Sets API' <https://developer.wmata.com/> to
    return data frames of transit data for easy analysis.
	"""
	
	homepage = "https://k5cents.github.io/metro/"
	cran = "metro" 

	version("0.9.3", md5="2f77190aca10a28ee15d288ee08f4006")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-geodist@0.0.6:", type=("build", "run"))
	depends_on("r-hms@1:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.1:", type=("build", "run"))
	depends_on("r-tibble@3.0.4:", type=("build", "run"))
