# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCenso2017(RPackage):
	"""Base de Datos de Facil Acceso del Censo 2017 de Chile (2017
Chilean Census Easy Access Database)

	Provee un acceso conveniente a mas de 17 millones de registros
    de la base de datos del Censo 2017. Los datos fueron importados desde
    el DVD oficial del INE usando el Convertidor REDATAM creado por Pablo De
    Grande. Esta paquete esta documentado intencionalmente en castellano
    asciificado para que funcione sin problema en diferentes plataformas.
    (Provides convenient access to more than 17 million records from the
    Chilean Census 2017 database. The datasets were imported from the official
    DVD provided by the Chilean National Bureau of Statistics by using the
    REDATAM converter created by Pablo De Grande and in addition it includes the
    maps accompanying these datasets.)
	"""
	
	homepage = "https://docs.ropensci.org/censo2017/"
	cran = "censo2017" 

	version("0.6.2", md5="1dd1eacdd2e3dbc013b0b9ffd0079f6f", url="https://cran.r-project.org/src/contrib/censo2017_0.6.2.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-duckdb", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
