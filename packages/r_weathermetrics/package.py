# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeathermetrics(RPackage):
	"""Functions to Convert Between Weather Metrics

	Functions to convert between weather metrics, including conversions
    for metrics of temperature, air moisture, wind speed, and precipitation.
    This package also includes functions to calculate the heat index from
    air temperature and air moisture.
	"""
	
	homepage = "https://github.com/geanders/weathermetrics/"
	cran = "weathermetrics" 

	version("1.2.2", md5="7999d354971aa93edc029c43f1af022b")

	depends_on("r@2.10:", type=("build", "run"))
