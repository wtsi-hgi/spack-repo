# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpathsenser(RPackage):
	"""Process and Analyse Data from m-Path Sense

	Overcomes one of the major challenges in mobile (passive)
    sensing, namely being able to pre-process the raw data that comes from
    a mobile sensing app, specifically 'm-Path Sense' <https://m-path.io>.
    The main task of 'mpathsenser' is therefore to read 'm-Path Sense'
    JSON files into a database and provide several convenience functions
    to aid in data processing.
	"""
	
	homepage = "https://gitlab.kuleuven.be/ppw-okpiv/researchers/u0134047/mpathsenser/"
	cran = "mpathsenser" 

	version("1.2.3", md5="a054a6b49b973d9272997507cfefec9f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
