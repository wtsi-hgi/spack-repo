# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpigraphdb(RPackage):
	"""Interface Package for the 'EpiGraphDB' Platform

	The interface package to access data from the
    'EpiGraphDB' <https://epigraphdb.org> platform.
    It provides easy access to the 'EpiGraphDB' platform with functions that
    query the corresponding REST endpoints on the API <https://api.epigraphdb.org>
    and return the response data in the 'tibble' data frame format.
	"""
	
	homepage = "https://mrcieu.github.io/epigraphdb-r/"
	cran = "epigraphdb" 

	version("0.2.3", md5="98cc3aa671a64b53b06a25315e6506e6")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
