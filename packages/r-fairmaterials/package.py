# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFairmaterials(RPackage):
	"""Make Materials Data FAIR

	We provide here tools used by the Solar Durability and Lifetime Extension Center (SDLE)
    for FAIRifying data from materials science projects. Functions have been created for numerous tools common
    in the field in order to make the metadata more Findable, Accessible, Interoperable, and Reproducible. 
	"""
	
	cran = "FAIRmaterials" 

	version("0.4.1", md5="f180e26ad171af1f4aa5787a812adb82")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-svdialogs", type=("build", "run"))
	depends_on("r-tidyjson", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonld", type=("build", "run"))
