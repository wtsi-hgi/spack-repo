# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwissair(RPackage):
	"""Air Quality Data of Switzerland for One Year in 30 Min
Resolution

	Ozone, NOx (= Sum of nitrogen monoxide and nitrogen dioxide), nitrogen monoxide, ambient temperature, dew point, wind speed and wind direction at 3 sites around lake of Lucerne in Central Switzerland in 30 min time resolution for year 2004.
	"""
	
	cran = "SwissAir" 

	version("1.1.6", md5="3ca9d1f7230dc6cc53cd2d87598bce19")

	depends_on("r@2.13.1:", type=("build", "run"))
