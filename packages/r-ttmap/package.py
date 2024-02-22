# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtmap(RPackage):
	"""Two-Tier Mapper: a clustering tool based on topological data analysis

	TTMap is a clustering method that groups together samples with the same deviation in comparison to a control group. It is specially useful when the data is small. It is parameter free.
	"""
	
	bioc = "TTMap" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TTMap_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TTMap/TTMap_1.24.0.tar.gz"]

	version("1.24.0", md5="9fb52b78486eff55cc91ef0f8116633b")

	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
