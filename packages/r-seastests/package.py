# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeastests(RPackage):
	"""Seasonality Tests

	An overall test for seasonality of a given time
    series in addition to a set of individual seasonality tests as
    described by Ollech and Webel (forthcoming): An overall seasonality
    test. Bundesbank Discussion Paper.
	"""
	
	cran = "seastests" 

	version("0.15.4", md5="5c8e8949c7433c6ab4bca86ec125e71a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
