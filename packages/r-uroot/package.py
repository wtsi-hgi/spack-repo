# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUroot(RPackage):
	"""Unit Root Tests for Seasonal Time Series

	Seasonal unit roots and seasonal stability tests.
    P-values based on response surface regressions are available for both tests.
    P-values based on bootstrap are available for seasonal unit root tests.
	"""
	
	homepage = "https://geobosh.github.io/uroot/"
	cran = "uroot" 

	version("2.1-3", md5="d73809f5d89fd86024c110f51ba96415")

	depends_on("r@3:", type=("build", "run"))
