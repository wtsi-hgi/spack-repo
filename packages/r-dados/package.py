# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDados(RPackage):
	"""Translate Datasets to Portuguese

	Este pacote traduz os seguintes 
    conjuntos de dados: 'airlines', 'airports', 'ames_raw', 'AwardsManagers',
    'babynames', 'Batting', 'diamonds', 'faithful', 'fueleconomy',
    'Fielding', 'flights', 'gapminder', 'gss_cat', 'iris', 'Managers',
    'mpg', 'mtcars', 'atmos', 'penguins', 'People, 'Pitching', 'pixarfilms','planes',
    'presidential', 'table1', 'table2', 'table3', 'table4a', 'table4b',
    'table5', 'vehicles', 'weather', 'who'.  English: It provides a
    Portuguese translated version of the datasets listed above.
	"""
	
	homepage = "https://github.com/cienciadedatos/dados"
	cran = "dados" 

	version("0.1.0", md5="1556f10dc157a81d40aec045cc5a31b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ameshousing", type=("build", "run"))
	depends_on("r-babynames", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-fueleconomy", type=("build", "run"))
	depends_on("r-gapminder", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lahman", type=("build", "run"))
	depends_on("r-palmerpenguins", type=("build", "run"))
	depends_on("r-nasaweather", type=("build", "run"))
	depends_on("r-nycflights13", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-pixarfilms", type=("build", "run"))
