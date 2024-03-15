# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene10stprobesetDb(RPackage):
	"""Affymetrix mogene10 annotation data (chip mogene10stprobeset)

	Affymetrix mogene10 annotation data (chip mogene10stprobeset) assembled using data from public repositories
	"""
	
	bioc = "mogene10stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mogene10stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mogene10stprobeset.db/mogene10stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", md5="570d4cf3fcc42d1e9b54237b9e4eb5f7")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation