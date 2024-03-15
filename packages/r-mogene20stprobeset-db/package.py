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

	version("8.8.0", md5="a64ddbf33e4f2b96301452e808d0e81a")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation