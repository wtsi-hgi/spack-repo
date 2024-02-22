# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSolar(RPackage):
	"""Radiation and Photovoltaic Systems

	Calculation methods of solar radiation and performance of photovoltaic systems from daily and intradaily irradiation data sources.
	"""
	
	homepage = "https://oscarperpinan.github.io/solar/"
	cran = "solaR" 

	version("0.46", md5="35a1d2d4b6b5959f0e96c3a61b8cdc2c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
