# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcd(RPackage):
	"""Global Charcoal Database

	Contains the Global Charcoal database data. Data include charcoal
    series (age, depth, charcoal quantity, associated units and methods) and
    information on sedimentary sites (localisation, depositional environment, biome,
    etc.) as well as publications informations. Since 4.0.0 the GCD mirrors the online SQL database at <http://paleofire.org>.
	"""
	
	homepage = "http://paleofire.org"
	cran = "GCD" 

	version("4.0.7", md5="b9cf30c4594dc0ee359e902170df8f2b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
