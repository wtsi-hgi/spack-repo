# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRed(RPackage):
	"""IUCN Redlisting Tools

	Includes algorithms to facilitate the assessment of extinction risk of species according to the IUCN (International Union for Conservation of Nature, see <https://www.iucn.org/> for more information) red list criteria.
	"""
	
	cran = "red" 

	version("1.6.1", md5="5a29e5ced1f001ba680d4b80532ab19a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bat", type=("build", "run"))
	depends_on("r-dismo", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-predicts", type=("build", "run"))
