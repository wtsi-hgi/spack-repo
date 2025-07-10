# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene20stprobesetDb(RPackage):
	"""Affymetrix mogene20 annotation data (chip mogene20stprobeset)

	Affymetrix mogene20 annotation data (chip mogene20stprobeset) assembled using data from public repositories
	"""
	
	bioc = "mogene20stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mogene20stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mogene20stprobeset.db/mogene20stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="cf3e58f52c86d41a58e65aabaf77fccdc22c5c0b8687e2f533350d0b84a2266c")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

