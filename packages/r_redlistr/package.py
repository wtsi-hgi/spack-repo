# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedlistr(RPackage):
	"""Tools for the IUCN Red List of Ecosystems and Species

	A toolbox created by members of the International Union for
    Conservation of Nature (IUCN) Red List of Ecosystems Committee for
    Scientific Standards. Primarily, it is a set of tools suitable for
    calculating the metrics required for making assessments of species and
    ecosystems against the IUCN Red List of Threatened Species and the
    IUCN Red List of Ecosystems categories and criteria. See the IUCN
    website for detailed guidelines, the criteria, publications and other
    information.
	"""
	
	homepage = "https://github.com/red-list-ecosystem/redlistr"
	cran = "redlistr" 

	version("1.0.4", md5="25b11a6206be777cfffa7842cf925687")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-raster@2.5.8:", type=("build", "run"))
	depends_on("r-sp@1.2.4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
