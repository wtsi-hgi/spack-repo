# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClariomdhumanprobesetDb(RPackage):
	"""Affymetrix clariomdhuman annotation data (chip clariomdhumanprobeset)

	Affymetrix clariomdhuman annotation data (chip clariomdhumanprobeset) assembled using data from public repositories
	"""
	
	bioc = "clariomdhumanprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/clariomdhumanprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/clariomdhumanprobeset.db/clariomdhumanprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", md5="01cb1a5cc4674750b6ce5988cd62fad3")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

