# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtl(RPackage):
	"""Extract-Transform-Load Framework for Medium Data

	A predictable and pipeable framework for performing ETL 
    (extract-transform-load) operations on publicly-accessible medium-sized data 
    set. This package sets up the method structure and implements generic 
    functions. Packages that depend on this package download specific data sets 
    from the Internet, clean them up, and import them into a local or remote 
    relational database management system.
	"""
	
	homepage = "https://github.com/beanumber/etl"
	cran = "etl" 

	version("0.4.1", md5="b2e13d75b3ae55325f12f460fded5e95")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
