# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene11stprobesetDb(RPackage):
	"""Affymetrix mogene11 annotation data (chip mogene11stprobeset)

	Affymetrix mogene11 annotation data (chip mogene11stprobeset) assembled using data from public repositories
	"""
	
	bioc = "mogene11stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mogene11stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mogene11stprobeset.db/mogene11stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="7a4317ded07b7cd4924df710c0ea338301ed4fab8061b8d99e6ab5c8c589b473")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

