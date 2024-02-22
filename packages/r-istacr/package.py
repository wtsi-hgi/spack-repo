# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIstacr(RPackage):
	"""Obtaining Open Data from Instituto Canario De Estadistica
(ISTAC) API

	You can access to open data published in Instituto Canario De Estadistica (ISTAC) APIs at <https://datos.canarias.es/api/estadisticas/>.
	"""
	
	cran = "istacr" 

	version("0.2.2", md5="d0118d87e3f0c600daee80e63e9777bc")

	depends_on("r-jsonlite", type=("build", "run"))
