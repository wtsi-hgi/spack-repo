# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarwarsdb(RPackage):
	"""Relational Data from the 'Star Wars' API for Learning and
Teaching

	Provides data about the 'Star Wars' movie franchise
    in a set of relational tables or as a complete 'DuckDB' database. All
    data was collected from the open source 'Star Wars' API
    <https://swapi.dev/>.
	"""
	
	homepage = "https://github.com/gadenbuie/starwarsdb"
	cran = "starwarsdb" 

	version("0.1.2", md5="b097b0de077fb3e8200d713c4899f14d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-duckdb", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
