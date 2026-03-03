# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgnparser(RPackage):
	"""Parse Scientific Names

	Parse scientific names using 'gnparser'
    (<https://github.com/gnames/gnparser>), written in Go. 'gnparser'
    parses scientific names into their component parts; it utilizes
    a Parsing Expression Grammar specifically for scientific names.
	"""
	
	homepage = "https://docs.ropensci.org/rgnparser/"
	cran = "rgnparser" 

	version("0.3.0", md5="37b32ead7316b1a57a246e0f93b14350")

	depends_on("r-sys", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
