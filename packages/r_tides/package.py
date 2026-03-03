# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTides(RPackage):
	"""Quasi-Periodic Time Series Characteristics

	Calculate Characteristics of Quasi-Periodic Time Series, e.g. Estuarine Water Levels.
	"""
	
	cran = "Tides" 

	version("2.1", md5="954d493292e7c3d1e1084a8e7fe7f59c")

	depends_on("r@2.10:", type=("build", "run"))
