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

	version("1.22.0", md5="65027624574d5e33f18b0a54a54f4be9")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@2.10.1:", type=("build", "run"))

