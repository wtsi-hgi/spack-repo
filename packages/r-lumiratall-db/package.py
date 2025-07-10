# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLumiratallDb(RPackage):
	"""Illumina Rat Illumina expression annotation data (chip lumiRatAll)

	Illumina Rat Illumina expression annotation data (chip lumiRatAll) assembled using data from public repositories
	"""
	
	bioc = "lumiRatAll.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/lumiRatAll.db_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/lumiRatAll.db/lumiRatAll.db_1.22.0.tar.gz"]

	version("1.22.0", sha256="86bff00b4a2c7c9ca2f3e76569c01fb0232b61059b00092fb1ba8fc115c200fa")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@2.10.1:", type=("build", "run"))

