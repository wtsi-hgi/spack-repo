# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarschemar(RPackage):
	"""Obtaining Stars from Flat Tables

	Data in multidimensional systems is obtained from operational
    systems and is transformed to adapt it to the new structure.
    Frequently, the operations to be performed aim to transform a flat
    table into a star schema. Transformations can be carried out using
    professional extract, transform and load tools or tools intended for
    data transformation for end users. With the tools mentioned, this
    transformation can be carried out, but it requires a lot of work. The
    main objective of this package is to define transformations that allow
    obtaining stars from flat tables easily. In addition, it includes
    basic data cleaning, dimension enrichment, incremental data refresh
    and query operations, adapted to this context.
	"""
	
	homepage = "https://josesamos.github.io/starschemar/"
	cran = "starschemar" 

	version("1.2.4", md5="8db874f3b6983e27d806dbf23264cfb7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
