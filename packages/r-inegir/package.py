# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInegir(RPackage):
	"""Integrate INEGI’s (Mexican Stats Office) API with R

	Provides functions to download and parse information from INEGI
    (Official Mexican statistics agency). To learn more about the API, see <https://www.inegi.org.mx/servicios/api_indicadores.html>.
	"""
	
	cran = "inegiR" 

	version("3.0.0", md5="6b4564d64ee89eb2fa2193c2fe4ab39b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tibbletime", type=("build", "run"))
