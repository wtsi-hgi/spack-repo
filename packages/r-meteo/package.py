# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeteo(RPackage):
	"""RFSI and Spatio-Temporal Geostatistical Interpolation for
Meteorological and Other Environmental Variables

	RFSI and spatio-temporal geostatistical interpolation for meteorological and other environmental variables. Global spatio-temporal models calculated using publicly available data are stored in package.
	"""
	
	homepage = "https://www.r-pkg.org/pkg/meteo"
	cran = "meteo" 

	version("2.0-2", md5="578d74a25c9a5d2edaebb4d5bae9c9b0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spacetime", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-cast", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sftime", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
