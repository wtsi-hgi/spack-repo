# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDagirlite(RPackage):
	"""Spatial Vector Data for Danmarks Administrative Geografiske
Inddeling DAGI

	Compressed spatial vector data originally from <https://dawadocs.dataforsyningen.dk/> saved as Simple 
    Features, SF, objects with data on population, age and gender from Statistics Denmark <https://www.dst.dk/da/>.
	"""
	
	cran = "dagirlite" 

	version("0.1.0", md5="198217e31b490253e03491ce299c4f73")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
