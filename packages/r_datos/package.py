# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatos(RPackage):
	"""Traduce al Español Varios Conjuntos de Datos de Práctica

	Provee una versión traducida de los siguientes
    conjuntos de datos: 'airlines', 'airports', 'AwardsManagers',
    'babynames', 'Batting', 'credit_data', 'diamonds', 'faithful', 'fueleconomy',
    'Fielding', 'flights', 'gapminder', 'gss_cat', 'iris', 'Managers',
    'mpg', 'mtcars', 'atmos', 'palmerpenguins', 'People, 'Pitching', 'planes',
    'presidential', 'table1', 'table2', 'table3', 'table4a', 'table4b',
    'table5', 'vehicles', 'weather', 'who'.  English: It provides a
    Spanish translated version of the datasets listed above.
	"""
	
	homepage = "https://github.com/cienciadedatos/datos"
	cran = "datos" 

	version("0.5.1", md5="c652f5ba0dcf1f27203f7e802cba4a61")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-babynames", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-fueleconomy", type=("build", "run"))
	depends_on("r-gapminder", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lahman", type=("build", "run"))
	depends_on("r-nasaweather", type=("build", "run"))
	depends_on("r-nycflights13", type=("build", "run"))
	depends_on("r-palmerpenguins", type=("build", "run"))
	depends_on("r-modeldata@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
