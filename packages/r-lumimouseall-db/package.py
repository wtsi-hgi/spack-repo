# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLumimouseallDb(RPackage):
	"""Illumina Mouse Illumina expression annotation data (chip lumiMouseAll)

	Illumina Mouse Illumina expression annotation data (chip lumiMouseAll) assembled using data from public repositories
	"""
	
	bioc = "lumiMouseAll.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/lumiMouseAll.db_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/lumiMouseAll.db/lumiMouseAll.db_1.22.0.tar.gz"]

	version("1.22.0", md5="6f12330377aaddc83bfa9c37477b999e")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@2.10.1:", type=("build", "run"))

