# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcotoxr(RPackage):
	"""Download and Extract Data from US EPA's ECOTOX Database

	The US EPA ECOTOX database is a freely available database
    with a treasure of aquatic and terrestrial ecotoxicological data.
    As the online search interface doesn't come with an API, this
    package provides the means to easily access and search the database
    in R. To this end, all raw tables are downloaded from the EPA website
    and stored in a local SQLite database.
	"""
	
	homepage = "https://github.com/pepijn-devries/ECOTOXr"
	cran = "ECOTOXr" 

	version("1.0.9", md5="df0b687b53ece92035f07b629e79d2a5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rsqlite@2.3.4:", type=("build", "run"))
	depends_on("r-crayon@1.5.2:", type=("build", "run"))
	depends_on("r-dbplyr@2.4:", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-httr2@1:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.8:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.4:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.3:", type=("build", "run"))
	depends_on("r-readr@2.1.4:", type=("build", "run"))
	depends_on("r-readxl@1.4.3:", type=("build", "run"))
	depends_on("r-rlang@1.1.2:", type=("build", "run"))
	depends_on("r-rvest@1.0.3:", type=("build", "run"))
	depends_on("r-stringr@1.5.1:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
