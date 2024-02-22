# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNasaweather(RPackage):
	"""Collection of datasets from the ASA 2006 data expo

	This package contains tidied data from the ASA 2006 data expo,
    as well as a number of useful other related data sets.
	"""
	
	homepage = "http://github.com/hadley/nasaweather"
	cran = "nasaweather" 

	version("0.1", md5="c5d51d11e1efa31b9d3b78d499adfaf2")

	depends_on("r@3.1:", type=("build", "run"))
