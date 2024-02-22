# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPromr(RPackage):
	"""Prometheus 'PromQL' Query Client for 'R'

	A native 'R' client library for querying the 'Prometheus' 
    time-series database, using the 'PromQL' query language.
	"""
	
	homepage = "https://github.com/domodwyer/promr"
	cran = "promr" 

	version("0.1.3", md5="3dd8f88859cdc9e3810c99d65a63b002")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
